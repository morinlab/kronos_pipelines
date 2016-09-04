/projects/rmorin/software/centos-6/anaconda/4.1.0/envs/kronos-2.1.0/bin/kronos \
    run \
        --input_samples "samples.tsv" \
        --working_dir "working_dir/" \
        --config_file "tasks.yaml" \
        --setup_file "setup.GRCh38_no_alt.exomes.login-apollo.tsv" \
        --components_dir "~/repos/pipeline-components/" \
        --job_scheduler "sge" \
        --num_pipelines "1" \
        --num_jobs "5" \
        --python_installation "/projects/rmorin/software/centos-6/anaconda/4.1.0/envs/kronos-2.1.0/bin/python" \
        --no_prefix \
        --qsub_options ' -pe ncpus {num_cpus} -l mem_free={mem} -l mem_token={mem} -l h_vmem={mem} -w n -S /bin/sh -P arc.prj -q arc.q'
