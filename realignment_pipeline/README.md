# Realignment pipeline

This pipeline can be used for *realignment* of BAM files or *alignment* of FASTQ files.


## Running the pipeline for realignment of BAM files

1. Create a new working directory.

	```bash
	mkdir realignment_pipeline
	cd realignment_pipeline
	```

2. Copy the pipeline's `samples.tsv` and `launch_genesis.sh` files into the directory you just created. Update the version number to ensure you're using the latest version.
	
	```bash
	cp /extscratch/morinlab/software/pipelines_morinlab/6.1/realignment_pipeline/{samples.tsv,launch_genesis.sh} .
	```
	
3. Add your sample information to the `samples.tsv` file. 

	1. Don't forget to use tabs to separate your columns.
	2. Include the header line.
	3. Leave the `interval_file` column empty for now

4. Create empty interval files for your samples in a new directory.

  ```mkdir interval_files; grep -v ^# samples.tsv | cut -f1 | parallel touch interval_files/{}.intervals.txt```
  
  Add the paths to these newly-created files to the `interval_file` column in `samples.tsv`.

5. Update the `launch_genesis.sh` file, if need be. 

	1. Update the version numbers at the top of the file to whatever version you are currently using to ensure you are using the latest config and setup files. 
	2. If you are using an environment other than Genesis, you need to update `--setup_file` accordingly. There might be another setup file in the repository that you could use. Otherwise, you'll have to create one. Consider adding it to the repository so that others can benefit from it. If you want help, open an issue on GitHub. 

6. Launch your pipeline! **Hint:** use `screen` so that the pipeline continues running after you close your terminal. If you disconnect from `screen`, you can reconnect by running `screen -r`. 

	```bash
	screen
	# You might have to hit Enter after running screen.
	sh launch_genesis.sh
	```

7. Relaunch after the `BAM2FQ` task.
 
  The pipeline will halt due to a breakpoint after the `BAM2FQ` task. Check that the interval files have been populated, and then relaunch that instance of the pipeline (which will resume after the breakpoint) by adding your run ID to the Kronos command in `launch_genesis.sh`. Don't forget the trailing backslash on the previous line.

	```bash
	[...]
	--qsub_options ' -pe ncpus {num_cpus} -l mem_free={mem} -l mem_token={mem} -l h_vmem={mem} -w n -S /bin/sh' \
  	--no_prefix \
  	--run_id "2016-05-20_11-57-05"
	```

## Running the pipeline for alignment of FASTQ files

Usage is similar to the above, with some main differences:
- Use the `alignment_samples.tsv` template instead of `samples.tsv` and include paths for both your `read1.fastq.gz` and `read2.fastq.gz` files for each sample
- In `launch_genesis.sh`, update the `-y` YAML tasks file to use `alignment_pipeline.yaml`
- There is no need for interval files, and there are no forced breakpoints during the pipeline