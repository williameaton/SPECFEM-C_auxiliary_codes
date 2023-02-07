#!/bin/bash

# Accumulates and compresses the relevant files to be uploaded to cluster

FNAME="trough_trim"
inp_files_path="./inputs/input_files"
stc_dir="$inp_files_path/send_to_cluster"

mkdir $stc_dir/$FNAME

# Copy common files:
cp $inp_files_path/common_files/*  $stc_dir/$FNAME/

# Copy other files:
cp $inp_files_path/unique_files/$FNAME/* $stc_dir/$FNAME

# Copy slurm file:
cp $inp_files_path/slurms/$FNAME.slurm $stc_dir/$FNAME

# Zip the files:
cd $stc_dir && zip -r $FNAME.zip $FNAME

echo ""
echo "++++++++++++++++++++++++++++++++++++++++++"
echo "UPLOADING TO TIGER"
scp trough_trim.zip tgpu://scratch/gpfs/we3822/specfemsea/SPECFEMX/input

