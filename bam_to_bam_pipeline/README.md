# bam_to_bam_pipeline

```
Development Information
=======================

Date Created : Mar 31 2015
Last Update  : Apr 16 2015
Developer    : Jasleen Grewal (jkg21@sfu.ca)
Input Params : samples (input_bam), output reference (YAML FORMAT)
Output       : out_dir/outputs/realigned_bam/TASK_CLIPOVERLAP_REALND_SAMPLE_ID.clipped.markdup.realigned.ba
Output stats : All checksums for I/O of each task are output to 
                        out_dir/outputs/results/in_IN_TASK_1_out_OUT_TASK_1_sum{in,out}.txt
               To verify your output bam matches the input bam in number of reads, simply cat the following .txts:
               out_dir/outputs/results/in_SAMPLE_out_TASK_CLIPOVERLAP_REALND_SAMPLE_ID_sumin.txt
               out_dir/outputs/results/in_SAMPLE_out_TASK_CLIPOVERLAP_REALND_SAMPLE_ID_sumin.txt
```
### Known Issues

- Currently while running either pipeline on the cluster, sentinel files are not being created. 
  The issue can be tracked at: https://www.bcgsc.ca/jira/browse/PFD-472
- As a result of sentinel files not being created, some intermediate tasks might be relaunched 
  after the pipeline reaches a breakpoint (in the case of interval dependent realignment pipeline).
  From what I've seen however, the cleanup tasks are also instantiated during the rerun, preventing
  a pile-up of input files

### Last Updates

- No new updates

### Description of scripts
cluster_bam_to_bam_interval.yaml - Full pipeline with split_fastq and dependent cleanup tasks. Interval based parallelization of bam alignment step.

cluster_bam_to_bam_nointerval.yaml - Full pipeline without split_fastq. No interval based parallelization

run.py - Script used while running the pipeline with the interval option. Do not run the pipeline independentely.

### Running the pipeline
```
Please prepare a draft of your .yaml with the samples listed.
Make a copy of this .yaml. You will pass the copy to the run.py script.
Run.py regenerates the input yaml and replaces it with additional paramters for interval file locations added for 
each sample. Hence, it is recommended you don't use your actual .yaml directly to instantiate a Realignment Pipeline.

Command to run pipeline (sets up dummy interval files, initiate pipeline, restart it after breakpoint is encountered)
python run.py -c copy_of_interval_based_realignment.yaml --components_dir /home/jgrewal/projects/lab_pipeline/pipeline-components/ --num_jobs 5 --num_pipelines 4 --drmaa lib/lx24-amd64/libdrmaa.so --outdir /extscratch/morinlab/projects/MCL_realignment/results/exomes_realn/
```
