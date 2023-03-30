#--------------------------------------------------
#----------INTERFACE (MODULE) IMPORTS--------------
#--------------------------------------------------

from nipype.interfaces import fsl, freesurfer, matlab, spm
from nipype.interfaces import io as nio
from nipype.interfaces.base import Bunch
from nipype.algorithms import modelgen
from nipype.pipeline import engine as pe

import os, pandas
from bids import BIDSLayout

#--------------------------------------------------
#--------------PIPELINE SPECIFICS------------------
#--------------------------------------------------

subName= '01'
sesName = '01'
task = 'MOTOR'
space = 'MNI152NLin2009cAsym'
TR = 1

condList = ["right_hand","left_hand","right_foot","left_foot"]
contrasts = [
                [ "1: Right - Left", "T", ["right_hand","left_hand","right_foot","left_foot"], [ 0.5, -0.5, 0.5, -0.5 ] ],
                [ "2: Hand - Foot", "T", ["right_hand","left_hand","right_foot","left_foot"], [ 0.5, 0.5, -0.5, -0.5 ] ]
            ]

baseDir='/ncf/nrg/users/jsegawa/pythonWorkshop'
BIDSDir = os.path.abspath(os.path.join(baseDir,'bids'))

outDir = 'nipype-sub-01-ses-01-MOTOR-pythonWorkshop'
resultsDir = os.path.abspath(os.path.join(baseDir,outDir))
eventsDir = os.path.abspath(os.path.join(baseDir,'events'))

print(f'BIDS directory: {BIDSDir}')
print(f'Output directory: {resultsDir}')
print(f'Events tsv files directory: {eventsDir}')

# ---------------------------------------------------
# ------------------ RANDOM BUSINESS ----------------
# ---------------------------------------------------

if not os.path.exists(resultsDir):
    os.mkdir(resultsDir)

matlab.MatlabCommand.set_default_matlab_cmd("matlab -nodesktop -nosplash")

fsl.FSLCommand.set_default_output_type('NIFTI')


# ---------------------------------------------------
# -------------- COLLECT ALL THE THINGS -------------
# ---------------------------------------------------

print('--- Getting structural and functional files ---')

# -------- GET FUNCTIONAL FILES USING BIDSLAYOUT ------

layout = BIDSLayout(BIDSDir, derivatives=True, validate = False)
funcFiles = layout.get(datatype='func', subject = subName, task=task, session=sesName,
                       space = space, suffix = 'bold', extension='nii.gz', return_type='filename')

numFound = len(funcFiles)

print(f'Found: {str(numFound)} functional runs')

# -------- GET STRUCTURAL FILE ------

anatFile = os.path.join(os.path.join(BIDSDir, 'derivatives',
                                    f'sub-{subName}',f'ses-{sesName}','anat',
                                    f'sub-{subName}_ses-{sesName}_run-1_space-{space}_desc-preproc_T1w.nii.gz'))



print('--- Reading confound files from fmriprep output and event files ---')

info = [] # object for all items adding to design matrix
for iRun in range(1,numFound+1):

# -------- GET ONSETS & DURATIONS FROM EVENTS TSV FILES --------

    events = pandas.read_csv(os.path.join(eventsDir, task+'_run'+str(iRun)+'_events.tsv'), sep="\t")

    onsets = []
    durations = []
    for thisCond in condList:
        #print(f'{thisCond=}')
        onsets.append(list(events[events.trial_type == thisCond].onset-(TR/2)))
        durations.append(list(events[events.trial_type == thisCond].duration))


# -------- GET COVARIATES FROM FMRIPREP OUTPUT -------

    confounds = pandas.read_csv(os.path.join(BIDSDir, 'derivatives',
                                        f'sub-{subName}', f'ses-{sesName}', 'func',
                                        f'sub-{subName}_ses-{sesName}_task-{task}_run-{str(iRun)}_desc-confounds_timeseries.tsv'),
                                        sep='\t', na_values='n/a',header=0)

    frameDis = confounds.framewise_displacement[:]
    frameDis_replace_na = frameDis.fillna(0) #n/a on first entry b/c no comp


# -------- PUT IT ALL TOGETHER --------

    info.insert(iRun,
                  Bunch(
                    conditions=condList,
                    onsets=onsets,
                    durations=durations,
                    regressors=[list(frameDis_replace_na),
                                 list(confounds.a_comp_cor_00[:]),
                                 list(confounds.a_comp_cor_01[:]),
                                 list(confounds.a_comp_cor_02[:]),
                                 list(confounds.a_comp_cor_03[:]),
                                 list(confounds.a_comp_cor_04[:]),
                                 list(confounds.a_comp_cor_05[:]),
                                ],
                    regressor_names=['framewise_displacement',
                                     'aCompCor0',
                                     'aCompCor1',
                                     'aCompCor2',
                                     'aCompCor3',
                                     'aCompCor4',
                                     'aCompCor5'],
                      amplitudes=None,
                      tmod=None,
                      pmod=None))


# ---------------------------------------------------
# ----------------SET UP WORKFLOW--------------------
# ---------------------------------------------------

print('--- Setting up workflow ---')

### ---------- CREATE NODES ----------

convert = pe.MapNode(freesurfer.MRIConvert(), name="convert", iterfield=['in_file'])
convert.inputs.out_type = 'nii'
convert.inputs.in_file = funcFiles

modelspec = pe.Node(modelgen.SpecifySPMModel(), name="modelspec")
modelspec.inputs.input_units = 'secs' #timing_units
modelspec.inputs.time_repetition = TR
modelspec.inputs.high_pass_filter_cutoff = 128.
modelspec.inputs.concatenate_runs = False
modelspec.inputs.subject_info = info

level1design = pe.Node(spm.Level1Design(), name="level1design")
level1design.inputs.bases = {'hrf': {'derivs': [0, 0]}}
level1design.inputs.interscan_interval = TR
level1design.inputs.model_serial_correlations='AR(1)'
level1design.inputs.timing_units = 'secs'

level1estimate = pe.Node(spm.EstimateModel(), name="level1estimate")
level1estimate.inputs.estimation_method = {'Classical': 1}

contrastestimate = pe.Node(spm.EstimateContrast(), name="contrastestimate")
contrastestimate.inputs.contrasts = contrasts


### ---------- CREATE WORKFLOW ----------

l1analysis = pe.Workflow(name='nipype_1stlevel')
l1analysis.base_dir = os.path.join(baseDir, outDir)


### ---------- CONNECT NODES ----------

l1analysis.connect([(convert, modelspec, [('out_file', 'functional_runs')]),
                    (modelspec, level1design, [('session_info', 'session_info')]),
                    (level1design, level1estimate, [('spm_mat_file', 'spm_mat_file')]),
                    (level1estimate, contrastestimate, [('spm_mat_file', 'spm_mat_file'),
                                                        ('beta_images', 'beta_images'),
                                                        ('residual_image','residual_image')])])


# ---------------------------------------------------
# --------------- SET UP DATASINK -------------------
# ---------------------------------------------------
datasink = pe.Node(nio.DataSink(), name="datasink")
datasink.inputs.base_directory = os.path.join(baseDir,outDir)


# store relevant outputs from various stages of the 1st level analysis
l1analysis.connect([(contrastestimate, datasink,[('con_images', 'contrasts.@con'),
                                                 ('spmT_images', 'contrasts.@T')]),
                    (level1estimate, datasink,[('spm_mat_file', 'spm_mat')])])


# ---------------------------------------------------
# ----------------- GO GO GO!! ----------------------
# ---------------------------------------------------

print('--- Running pipeline ---')
l1analysis.run(plugin='MultiProc',plugin_args={'n_procs':2})
l1analysis.write_graph()
