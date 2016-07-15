# Kronos Pipelines

This repository contains Kronos pipelines used by the Morin lab. 

## Launch a Pipeline

Here's a quick guide on how to launch your own pipeline. 

1. Create a new empty directory for the Kronos pipeline. 

2. Copy the `launch.sh`, `tasks.yaml`, `samples.tsv` and setup files in the new directory. You should also copy any additional pipeline-specific files. See the notes for each individual pipeline for more details. 
	
3. Complete the `samples.tsv` file. Each line corresponds to a different sample and will be run in parallel up to the maximum number of pipelines specified in `launch.sh` (via the `--num_pipelines` parameter). Use tabs to separate your columns, and don't delete or change the header line. 

4. Update the `launch.sh` file accordingly:

    1. Update your Python/Kronos paths. Use absolute paths. 
    2. Update your components directory path. Use absolute path. 
    3. Update the setup file name. You don't need to use the absolute path.
    4. Update the qsub options. For instance, add the appropriate qsub flags to submit to a specific SGE queue. 

5. Run `sh launch.sh` from within the directory you created above to launch your pipeline. If you run the script from another directory, make sure to update the paths in your `launch.sh` file accordingly. **Hint:** Use `screen` or `tmux` to make sure the pipeline continues running in case your shell connection dies. 

6. If your pipeline fails at any point, you may perform any required fixes and relaunch it so that it resumes where it left off. All you need to do is add the run ID to the Kronos command in `launch.sh` using the `--run_id` parameter. The run ID is the name of the directory that was created by Kronos (usually a date and time) to contain your output files, such as `2016-01-14_17-07-35`. 
