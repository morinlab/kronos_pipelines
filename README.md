# Kronos Pipelines

This repository contains Kronos pipelines used by the Morin lab. 

## Launch a Pipeline

Here's a quick guide on how to launch your own pipeline. 

1. Create a new directory named after the pipeline you're interested in running, _e.g._ `titan_pipeline`. 

	```bash
	mkdir titan_pipeline
	cd titan_pipeline
	```

2. Copy the `samples.tsv` and `launch.sh` files for the pipeline you're interested in running in the directory you just created. 
	
	```bash
	cp /extscratch/morinlab/software/pipelines_morinlab/3.0/titan_pipeline/{samples.tsv,launch.sh} .
	```
	
3. Add your sample information to the `samples.tsv` file. 

	1. Don't forget to use tabs to separate your columns.
	2. Add all of your samples to your `samples.tsv` file. 
	3. Include the header line. 

4. Update the `launch.sh` file, if need be. 

	1. If you need to use a later version of the pipeline components, update `--components_dir` accordingly. 
	2. Update the version number at the top of `launch.sh` to whatever version you are currently using to ensure you are using the latest config and setup files. 
	3. If you are using an environment other than Genesis, you need to update `--setup_file` accordingly. There might be another setup file in the repository that you could use. Otherwise, you'll have to create one. Consider adding it to the repository so that others can benefit from it. If you want help, open an issue on GitHub. 

5. Launch your pipeline! **Hint:** use `screen` so that the pipeline continues running after you close your terminal. If you disconnect from `screen`, you can reconnect by running `screen -r`. 

	```bash
	screen
	# You might have to click Enter after running screen.
	sh launch.sh
	```
