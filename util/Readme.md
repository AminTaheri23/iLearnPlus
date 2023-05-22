# How to use

This creates a directory names cleaned_data.
/home/amintg/df1x_new.fasta is the path to your special fasta file. Your special fasta file should have a header in this format. ">name|0|testing" the 0 is the label. testing or training doesn't matter. also it shouldn't have any spaces and illegal genomic characters other than ATCG. 

50000 is the batch size for parallel 

8 is the number of the cores.

You can find the main in the FileProcessing.py file and comment or uncomment the features you want. also the strings above the huge dictionary is the features per featuresets. Meaning that you can change that too. 

```python FileProcessing.py /home/amintg/df1x_new.fasta 50000 8 cleaned_data ```



For merging batch files you can use this bash script. Which merges all ps3 files into one. (the order of the instances will change)
```head -n 1 PS3_0.csv > Merged_PS3.csv && tail -n+2 -q PS3_*.csv >> Merged_PS3.csv``