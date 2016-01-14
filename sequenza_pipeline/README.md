# Sequenza Pipeline

## Notes

1. A GC content file is needed for every reference genome that exists. By default, we're using 50-base windows. As you generate these, please include them in the Annotation/GC_Content of your reference build in `igenomes`. Include the window size in the file name, _e.g._ `GRCh37-lite.gc50Base.txt.gz`. Here's an example command on how to generate such a GC content file.

```bash
python /extscratch/morinlab/software/sequenza/7cca15e/exec/sequenza-utils.py GC-windows -w 50 ../../Sequence/WholeGenomeFasta/genome.fa | gzip > genome.gc50Base.txt.gz
```
