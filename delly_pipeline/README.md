# DELLY Pipeline

## Notes

* Keep an eye on memory usage. It can vary quite a bit with DELLY.
* The number of DELLY threads is set to two because it mainly parallelizes by BAM file, which is two in this case (tumour and normal). 