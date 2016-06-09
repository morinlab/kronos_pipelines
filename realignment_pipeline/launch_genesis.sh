VERSION="6.1"
COMPONENT_VERSION="9.0"
/extscratch/morinlab/software/anaconda/2.3.0/envs/kronos-2.1.0_beta/bin/kronos run \
-y /extscratch/morinlab/software/pipelines_morinlab/$VERSION/realignment_pipeline/realignment_pipeline_linear.yaml \
-w ./ \
-i samples.tsv \
-s /extscratch/morinlab/software/pipelines_morinlab/$VERSION/realignment_pipeline/setup.GRCh38_no_alt.genesis.tsv \
-c /extscratch/morinlab/software/pipeline_components_morinlab/$COMPONENT_VERSION/ \
-b sge \
--num_pipelines 10 \
-j 20 \
-p /extscratch/morinlab/software/anaconda/2.3.0/envs/kronos-2.0.4/bin/python2.7 \
--qsub_options ' -pe ncpus {num_cpus} -l mem_free={mem} -l mem_token={mem} -l h_vmem={mem} -w n -S /bin/sh' \
--no_prefix
