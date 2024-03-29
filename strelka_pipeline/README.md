# Strelka Pipeline

## Notes

1. This pipeline includes the bamUtil clipOverlap processing step by default. 
Edit it accordingly if you do not need this step. See also 3.

2. Note that you should update the `strelka_config` option in the setup file 
according to whether your samples are genomes or not. 
This is because Strelka uses special filtering that is only applicable when
you expect uniform coverage, which isn't the case with exome or targeted
sequencing. 
Here are handy configs on Genesis:
	```
	# For genomes
	/extscratch/morinlab/software/strelka_workflow/1.0.14/etc/strelka_config_bwa_default.ini
	# For anything else (exomes, targeted) 
	/extscratch/morinlab/software/strelka_workflow/1.0.14/etc/strelka_config_bwa_exome.ini
	```

3. If you are running this pipeline on BAM files generated from the Morin Lab realignment pipeline, they have already been processed with clipOverlap and indexed. You should update the `--config-file` in `launch.sh` to use the `tasks_post_realignment_pipeline.yaml` file which omits these steps.