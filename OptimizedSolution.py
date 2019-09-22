import pandas as pd
import numpy as np
import time

t = time.time() #this time is used to calculate the overall program runtime

loci = pd.read_csv('csv_files/loci.csv')
reads = np.asarray(pd.read_csv('csv_files/reads.csv'))

res=[]
locinp = np.asarray(loci["position"])
for i in range(len(locinp)):
    c=0
    for j in range(len(reads)):
        if reads[j][0] <= locinp[i] < reads[j][0]+reads[j][1]:
            c+=1
    res.append(c)
    print(res)
loci["coverage"] = res
print(loci)
loci.to_csv('csv_files/loci.csv') #writing to CSV

print (time.time()-t)


# The time complexity of the program is O(M*N) as the M is the loci.csv inputs and N is reads.csv inputs
# The improvization has been done by reducing the number of File I/O operations using other packages to read the csv files only once.
# I tried to find better solution than O(M*N) but couldn't get the other solutions.