import numpy as np


def create_psem(prefix, SL_prefix, fname, nproc, ngll, dir='./'):
    # prefix is the prefix used for custom files e.g. mesh files
    # SL_prefix is used for SL/Ice/Material List...probs constant between different sims.
    # Fname is the psem filename
    f = open(f"{dir}/{fname}.psem", "w")

    f.write(f"# THIS FILE WAS AUTOWRITTEN USING write_psem_file.py - WE\n\n")

    f.write(f"preinfo: nproc={nproc}, method='sem', &\n")
    f.write(f"         ngllx={ngll}, nglly={ngll},  &\n")
    f.write(f"         ngllz={ngll}, nenode=8,      &\n")
    f.write(f"         ngnode=8, inp_path='./input/{prefix}/', &\n")
    f.write(f"         out_path='./output_{prefix}/', pot_type='gravity',&\n")
    f.write("          pot_dof=1, disp_dof=1, grav0=1          \n\n")

    # Write the mesh files:
    f.write(f"mesh: xfile='{prefix}_coord_x', &\n")
    f.write(f"      yfile='{prefix}_coord_y', &\n")
    f.write(f"      zfile='{prefix}_coord_z', &\n")
    f.write(f"      confile='{prefix}_connectivity', &\n")
    f.write(f"      fsfile='{prefix}_free_surface', &\n")
    f.write(f"      idfile='{prefix}_material_id', &\n")
    f.write(f"      gfile='{prefix}_ghost'\n\n")

    # Boundary conditions
    f.write(f"bc: ubc=1,                &\n")
    f.write(f"    uxfile='{prefix}_ssbcux', &\n")
    f.write(f"    uyfile='{prefix}_ssbcuy', &\n")
    f.write(f"    uzfile='{prefix}_ssbcuz' \n\n")

    # Material list
    f.write(f"material: matfile='{SL_prefix}_material_list',density=1 \n\n")

    # Sea level and Ice
    f.write(f"sealevel: slfile='{SL_prefix}_SL', savesl0=1, saveOF=1, solvesl=1 \n\n")
    f.write(f"ice: icefile='{SL_prefix}_ice', iceratefile='{SL_prefix}_icerate', saveiceload=1,  saveice0=1, saveicerate=1 \n\n")

    #control parameters
    f.write(f"control: ksp_tol=1e-6, ksp_maxiter=1000, nl_tol=1e-4, nl_maxiter=1 \n\n")

    #save data
    f.write(f"save: disp=1,  strain=1, fsplot=1, gpot=1, agrav=1 \n\n")

    #devel
    f.write("devel: nondim=0")

    f.close()
