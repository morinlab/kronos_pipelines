# TITAN Pipeline

## Notes

1. Select the `setup.tsv` file that matches the human genome build used in the 
input BAM files. 

2. You might have to update the `mutationseq_intervals` and `titan_intervals` 
variables in the setup.tsv file to point to the appropriate locations. 
These are included in the repository. 

3. Currently, there is a bug in Kronos that causes all values in the setup 
file to be parsed as strings. 
This causes problems when components such as `run_titan` expect a list but 
receive a string. For now, the list is hard-coded in the `tasks.yaml` file. 
See: https://www.bcgsc.ca/jira/browse/PFD-552. 

4. By default, this pipeline is meant for exomes. If you wish to run 
it on genomes, you have to set `target_list` in the setup file to `NULL`. 
