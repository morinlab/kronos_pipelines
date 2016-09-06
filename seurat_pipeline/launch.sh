NAME="seurat_pipeline"
VERSION="5.0"
/extscratch/morinlab/software/anaconda/2.3.0/envs/kronos-2.0.4/bin/kronos \
    run \
        --working_dir "working_dir/" \
        --pipeline_name "$NAME" \
        --config_file "tasks.yaml" \
        --setup_file "setup.GRCh38_no_alt.exome.login-apollo.tsv" \
        --input_samples "samples_test.tsv" \
        --job_scheduler "sge" \
        --components_dir "~/repos/pipeline-components/" \
        --python_installation "/projects/rmorin/software/centos-6/anaconda/4.1.0/envs/kronos-2.1.0/bin/python" \
        --num_pipelines "1" \
        --num_jobs "5" \
        --no_prefix \
        --qsub_options ' -pe ncpus {num_cpus} -l mem_free={mem} -l mem_token={mem} -l h_vmem={mem} -w n -S /bin/sh -P arc.prj -q arc.q'
