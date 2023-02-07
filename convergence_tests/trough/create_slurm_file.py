
def create_slurm(fname, nproc, outdir, time="00:10:00", nodes=1):
    # prefix is the prefix used for custom files e.g. mesh files
    # SL_prefix is used for SL/Ice/Material List...probs constant between different sims.
    # Fname is the psem filename
    f = open(f"{outdir}/{fname}.slurm", "w")

    f.write( "#!/bin/bash\n")
    f.write(f"#SBATCH -N {nodes}   # node count\n")
    f.write( "#SBATCH --ntasks-per-node=40\n")
    f.write(f"#SBATCH -t {time}\n\n")

    f.write(f"# THIS SLURM FILE WAS AUTOWRITTEN USING create_slurm_file.py - WE\n\n")

    f.write("source ~/.login\n\n")
    f.write("cd $SLURM_SUBMIT_DIR\n")


    f.write(f"mpiexec -n {nproc} ./bin/pspecfemx ./input/{fname}/{fname}.psem  -ksp_monitor -ksp_type fgmres -pc_type asm -ksp_gmres_restart 300")

    f.close()
