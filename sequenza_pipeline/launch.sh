NAME="sequenza_pipeline"
VERSION="5.0"
/extscratch/morinlab/software/anaconda/2.3.0/envs/kronos-2.0.4/bin/kronos \
    run \
        --working_dir . \
        --pipeline_name "$NAME" \
        --config_file "/extscratch/morinlab/software/pipelines_morinlab/$VERSION/$NAME/tasks.yaml" \
        --setup_file "/extscratch/morinlab/software/pipelines_morinlab/$VERSION/$NAME/setup.GRCh37-lite.genesis.tsv" \
        --input_samples "samples.tsv" \
        --job_scheduler "sge" \
        --components_dir "/extscratch/morinlab/software/pipeline_components_morinlab/6.3" \
        --python_installation "/extscratch/morinlab/software/anaconda/2.3.0/envs/kronos-2.0.4/bin/python" \
        --num_pipelines "10" \
        --num_jobs "200" \
        --qsub_options ' -pe ncpus {num_cpus} -l mem_free={mem} -l mem_token={mem} -l h_vmem={mem} -w n -S /bin/sh'
