#!/bin/bash
#SBATCH -N 1   # node count
#SBATCH --ntasks-per-node=40
#SBATCH -t 00:10:00

# THIS SLURM FILE WAS AUTOWRITTEN USING create_slurm_file.py - WE

source ~/.login

cd $SLURM_SUBMIT_DIR
mpiexec -n 40 ./bin/pspecfemx ./input/trough_trim/trough_trim.psem  -ksp_monitor -ksp_type fgmres -pc_type asm -ksp_gmres_restart 300