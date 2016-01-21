# Realignment Pipeline

## Running the Pipeline

This pipeline performs dynamic parallelization. In other words, the Kronos intervals are created dynamically during the pipeline run based on the number of reads in the input BAM files. Unfortunately, Kronos requires that the interval file exists before launching the pipeline. 

To get around this, we launch the pipeline without specifying an interval file for the `BWA_MEM` and `SAMTOOLS_SORT` tasks. During this first run, the `BAM2FQ` task will dynamically create an interval file and a breakpoint will cause the pipeline to stop after this task. Then, the user adds an I/O connection to the `BWA_MEM` and `SAMTOOLS_SORT` tasks that points to the `interval_file `output from the `BAM2FQ` task and relaunches the pipeline. 
