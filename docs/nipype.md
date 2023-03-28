# Nipype

## Why Nipype?
1. Most neuroimaging software packages all-together. Choose and combine functions from different packages.
2. Free and open-source.
3. Caches past runs of workflow, and re-runs accordingly.
4. Easy parallelization.


## Installation
Let's create a virtual environment (pop quiz!) in which to install nipype and friends.

```python
# 1. set-up and activate virtual env
module load miniconda3/py39_4.11.0-ncf
python -m venv nipype39_venv
source nipype39_venv/bin/activate

# 2. install nipype and friends
pip install nipype pytest sphinx networkx==3.0 nibabel==2.0.4

# 3. test install
python -c "import nipype; print(nipype.__version__)"
python -c "import nipype; nipype.test()"
#You might get warnings, but make sure you don't have any errors or fails.
```

## Interface, Node, Workflow
Let's start with the 3 levels of "stuff" we use in Nipype:
1. Interfaces,
2. Nodes, and
3. Workflows

<insert image here>

### Interfaces == Modules
[_Interfaces_](https://nipype.readthedocs.io/en/latest/interfaces.html) are Python functions that wrap the magical (mostly neuroimaging) tools from other software packages (e.g., fslmaths from FSL or recon-all from Freesurfer)

Like modules, interfaces aren't Python built-ins, so they must be imported in your Python script:
```python
from nipype.interfaces import fsl, spm
```
Then, we can call things that we imported as, for example: `spm.EstimateContrast()`


### Nodes: Happy package for an interface
Nodes contain the wrapped interfaces, but also:
1. inputs (including input files, or any specified paramaters), and
2. outputs.

Let's choose a simple example: [_Freesurfer's mri_convert_](https://nipype.readthedocs.io/en/latest/api/generated/nipype.interfaces.freesurfer.preprocess.html#mriconvert).

To create a simple mriconvert node:
```python
convert = pe.Node(freesurfer.MRIConvert(), name="convert")
  # first convert is the variable name of the node
  # second "convert" is naming the output directory

#now set the inputs
convert.inputs.in_file = 'structural.nii.gz'
convert.inputs.out_type = 'nii'
```

#### MapNode
This was a simple version, but in reality, you might have a bunch of images that need to be converted, but then reconverge as a single set when it's passed on to another node. Then you'll need a *MapNode*.

<insert image>

```python
convert = pe.MapNode(freesurfer.MRIConvert(), name="convert", iterfield=['in_file'])
convert.inputs.in_file = funcFiles #this is an object this all my files I made earlier
convert.inputs.out_type = 'nii'
```

**Note**
The `iterfield` entry is not limited to files. You could use it for any input. For instance, if you're doing smoothing and want to try a bunch of different kernels, this input parameter could go in the iterfield. Or if you're doing a second level analysis over many contrasts, this could also go in the iterfield.

### Workflow: Series of nodes passing data
Workflows are the biggest "thing" in nipype, and can contain a series of nodes.

To make a workflow:

```python
l1analysis = pe.Workflow(name='nipype_1stlevel')
l1analysis.base_dir = os.path.join(baseDir, outDir)
```

The important property of workflows is that it links the nodes. In the above Node and MapNode examples, I gave the node its input, but if we really want to use Nipype, one node is going to pass its *output* to another node's *input*.

##Structure of a nipype script


## BIDSLayout and datasync


## Accessing interface software packages
Nipype is providing functions which Python-ize **access** to tools that may be written in another language, but not the tools themselves. You still need to `module load` (if on FASSE) or install the software packages.

The tricky thing is that we can't load the modules in any permanent way from **within** Python. If you're on FASSE, I suggest having a separate (batch?) script that loads the necessary modules and then calls the Python script.

```
#!/bin/bash
# if running on SLURM, could put all your #SBATCH lines here...

module load ncf
module load matlab/R2020b-fasrc01
module load spm/12.7487-fasrc01
module load freesurfer/6.0.0-ncf
module load fsl/6.0.4-ncf

python nipype_spm1stlevel.py
```

Then you would run this as:
```
sh run_spm1stlevel.sh
```

or if you're running on SLURM
```
sbatch run_spm1stlevel.sh
```
