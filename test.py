import csv
with open('../Calculating-genomic-coverage-from-next-generation-sequencing-data/csv_files/loci.csv') as csvfile:
    readLociCSV = csv.reader(csvfile, delimiter=',')
    loci = 0
    dict=[]
    c = 0
    next(readLociCSV)
    for row in readLociCSV:
        loci = row[0]
        print(c)
        # if c == 3:
        #     break
        with open('../Calculating-genomic-coverage-from-next-generation-sequencing-data/csv_files/reads.csv') as readsCsvfile:
            readsCSV = csv.reader(readsCsvfile, delimiter=',')
            count = 0
            # n = 101844980
            for r in readsCSV:
                try:
                    if int(loci) in range(int(r[0]), int(r[0]) + int(r[1])):
                        count = count + 1
                except ValueError:
                        pass
        dict.append({'position' : loci, 'coverage' : count})
        c = c + 1
print(dict)
with open('../Calculating-genomic-coverage-from-next-generation-sequencing-data/csv_files/result_file.csv', mode ='w') as csv_file:
    fieldnames = ['position', 'coverage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # writer.writerow(dict)
    for data in dict:
        writer.writerow(data)
        # print(key, value)
