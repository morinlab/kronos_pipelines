# TITAN Pipeline

## Launch the TITAN pipeline

Read the [general instructions](../README.md) in the main README for launching a Kronos pipeline. Below are notes specific to the TITAN pipeline that you should also read. 

## Notes about the TITAN pipeline

1. In the setup file, you need to update the values of `mutationseq_intervals` and `titan_intervals` to the absolute paths to the files included in the repository. Also, make sure you select the appropriate version of `mutationseq_intervals` (_e.g._ GRCh37 versus GRCh38). 

2. There's currently a bug that forces us to place the `chromosomes` shared attribute in the `tasks.yaml` file instead of the setup file. You need to update this once again according to the human reference you're using. For instance, change the default value to the following if you are using GRCh37.

    ```
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X,Y]
    ```

3. By default, this pipeline is meant for whole genome sequencing data. If you wish to run TITAN on exomes, you need to update the `target_list` shared attribute in the setup file from `NULL` to a BED file of exons. For instance, the BED files for the target regions in the Agilent exom capture kit is located here:

    ```
    /projects/rmorin/reference/igenomes/Homo_sapiens/GSC/GRCh37-lite/Annotation/Exons/agilent_sureselect_all_exons_v5_and_utr.sort.merge.bed
    ```

4. If you want to run the pipeline on a cluster, change the value of the `use_cluster` shared attribute in the setup file to `True` and make sure you launch the pipeline on a SGE submission host. 
