#!/usr/local/bin/python3

#input dnaseq
dnaseq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#EcoRI recognition
motif = "GAATTC"
motif_loc = dnaseq.find(motif)
fra_1 = motif_loc+1
dnalen = len(dnaseq)
fra_2 = dnalen - fra_1

# output
print("The origin dnaseq is\n" + dnaseq)
print("\nThe total dnaseq length is " + str(dnalen))
print("\nTwo fragment length are "+str(fra_1)+" and "+str(fra_2))
