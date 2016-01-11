NAME="titan_pipeline"
/extscratch/morinlab/software/anaconda/2.3.0/envs/kronos-2.0.4/bin/kronos \
    run \
        --working_dir . \
        --pipeline_name "$NAME" \
        --config_file "/extscratch/morinlab/software/pipelines_morinlab/3.0/$NAME/tasks.yaml" \
        --setup_file "/extscratch/morinlab/software/pipelines_morinlab/3.0/$NAME/setup.grch37.genesis.tsv" \
        --input_samples "samples.tsv" \
        --job_scheduler "sge" \
        --components_dir "/extscratch/morinlab/software/pipeline_components_shahlab/cycle008.3" \
        --python_installation "/extscratch/morinlab/software/anaconda/2.3.0/envs/kronos-2.0.4/bin/python" \
        --num_pipelines "50" \
        --num_jobs "2500" \
        --no_prefix \
        --qsub_options ' -pe ncpus {num_cpus} -l mem_free={mem} -l mem_token={mem} -l h_vmem={mem} -w n'
