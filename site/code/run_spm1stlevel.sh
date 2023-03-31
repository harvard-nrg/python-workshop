#!/bin/bash
# if running on SLURM, could put all your #SBATCH lines here...

module load ncf
module load matlab/R2020b-fasrc01
module load spm/12.7487-fasrc01
module load freesurfer/6.0.0-ncf
module load fsl/6.0.4-ncf

python nipype_spm1stlevel.py
