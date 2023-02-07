from create_psem_file import create_psem
from create_slurm_file import create_slurm
# Dirs:
fname         = "trough_trim"
inp_files_dir = f"./inputs/input_files/unique_files/{fname}"

# Simulation parameters:
ngll  = 3
nproc = 40

# Prepend the boundary conditions:
BC_label = '2'
BC_val   = '0.0'
for coord in ['x','y','z']:
    with open(f'{inp_files_dir}/{fname}_ssbcu{coord}', 'r') as original: data = original.read()
    with open(f'{inp_files_dir}/{fname}_ssbcu{coord}', 'w') as modified: modified.write(f"{BC_label} {BC_val}\n" + data)


# Create PSEM file:
create_psem(prefix=fname,
            SL_prefix="trough",
            fname=fname,
            nproc=nproc,
            ngll=ngll,
            dir=inp_files_dir)

# Create slurm file:

create_slurm(fname=fname,
             nproc=nproc,
             outdir='./inputs/input_files/slurms',
             time="00:10:00",
             nodes=1)

print(f"REMEMBER TO MAKE THE OUTPUT DIRECTORY CALLED: output_{fname}")