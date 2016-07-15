#!/bin/bash

# Edit the following variables accordingly
PYTHON_BIN_DIR="/projects/rmorin/software/centos-6/anaconda/4.1.0/envs/kronos-2.1.0/bin"
COMPONENTS_DIR="/projects/rmorin/software/centos-6/pipeline_components_shahlab/cycle008.6"
SETUP_FILE="setup.GRCh37_on_gphost.tsv"
QSUB_OPTIONS=" -pe ncpus {num_cpus} -l mem_free={mem} -l mem_token={mem} -l h_vmem={mem} -w n -S /bin/sh -P arc.prj -q arc.q"

# You shouldn't need to edit anything below
${PYTHON_BIN_DIR}/kronos run \
    --working_dir . \
    --pipeline_name "titan_pipeline" \
    --config_file "tasks.yaml" \
    --setup_file "${SETUP_FILE}" \
    --input_samples "samples.tsv" \
    --job_scheduler "sge" \
    --components_dir "${COMPONENTS_DIR}" \
    --python_installation "${PYTHON_BIN_DIR}/python" \
    --num_pipelines "20" \
    --num_jobs "30" \
    --qsub_options '${QSUB_OPTIONS}'
