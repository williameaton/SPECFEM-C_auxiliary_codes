#!/bin/bash

# This takes the .e file and runs the Exodus2SEMGEOTEC binary on it, then moves
# it to the inputs/input_files folder

FNAME="trough_trim"
exodus_path="./inputs/meshes/exodus"
inp_files_path="./inputs/input_files/unique_files/$FNAME"

# Run binary
~/Documents/Software/MeshAssist/MeshAssist/bin/exodus2semgeotech $exodus_path/$FNAME.e -bin=1 -fac=1
# Move everything to other dir.
mkdir $inp_files_path

mv $exodus_path/*.txt $inp_files_path
mv $exodus_path/${FNAME}_* $inp_files_path

