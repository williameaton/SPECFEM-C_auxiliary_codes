# THIS SLURM FILE WAS AUTOWRITTEN USING create_slurm_file.py - WE

# !/bin/bash
# SBATCH -N 1   # node count
# SBATCH --ntasks-per-node=40
# SBATCH -t 00:10:00

source ~/.login

cd $SLURM_SUBMIT_DIR
mpiexec -n 2 ./bin/pspecfemx ./input/singlecube/singlecube.psem  -ksp_monitor -ksp_type fgmres -pc_type asm -ksp_gmres_restart 300