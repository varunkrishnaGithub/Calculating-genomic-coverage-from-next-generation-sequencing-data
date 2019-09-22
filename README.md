# Calculating-genomic-coverage-from-next-generation-sequencing-data

* There are two solutions provided in this project
    *   BruteForce Solution
    *   Optimized Solution

1. BruteForce solution
   *    For each loci position we are opening the reads.csv and iterating through
        each entry and checking if the given postion falls under the range of start and start + length
        . If it falls we increment the count and move to the next start and length in reads.
        
   *    Finally, after all the count is completed for the loci we store the position and coverage in a dict
        . This provides the key value store for the calculated values.
        
   *    After the both loop ends we iterate on the dict and open the loci.csv in the write mode and write the values to it.

2. Optimized Solution
    *   In this approach is same but File I/O operations has been reduced to only once.
    *   That means we are reading all the values from files once and storing it in a appropriate datatype.
    *   This will reduce the running time of the program in half when compared to the BruteForce solution.

Note : Both solution Run time complexity is O(M * N) where M is loci and N is reads