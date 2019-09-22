import csv,time

t=time.time()

with open('../Calculating-genomic-coverage-from-next-generation-sequencing-data/csv_files/loci.csv') as lociCsvfile:
    LociCSV = csv.reader(lociCsvfile, delimiter=',')
    dict=[]
    next(LociCSV) #skipping the header line in csv
    for row in LociCSV:
        loci = row[0]
        with open('../Calculating-genomic-coverage-from-next-generation-sequencing-data/csv_files/reads.csv') as readsCsvfile:
            readsCSV = csv.reader(readsCsvfile, delimiter=',')
            count = 0
            for r in readsCSV:
                try:
                    if int(r[0])<=int(loci) and (int(r[0]) + int(r[1]))>int(loci):
                        count = count + 1
                except ValueError:
                        pass
        dict.append({'position' : loci, 'coverage' : count})


# the below code will write the results in the dict to the loci.csv
with open('../Calculating-genomic-coverage-from-next-generation-sequencing-data/csv_files/loci.csv', mode ='w') as csv_file:
    fieldnames = ['position', 'coverage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in dict:
        writer.writerow(data)

print (time.time()-t) #calculates the runtime of the program

# The time complexity of the program is O(M*N) as the M is the loci.csv inputs and N is reads.csv inputs
# The improvization can be done by reducing the number of File I/O operations using other packages to read the csv files only once.
# I tried to find better solution than O(M*N) but couldn't get the other solutions.