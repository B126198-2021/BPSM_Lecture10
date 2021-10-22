#!/usr/local/bin/python3
#script1

#input
dnaseq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#variables setting
A_count =dnaseq.count("A")
T_count = dnaseq.count("T")
lenseq = len(dnaseq)

#output
print("The number of A nucleotides is" + str(A_count)+".\nThe number of T nucleotides is "+str(T_count)+".\nThe total DNAseq length is "+str(lenseq)+".\nThe total AT% is "+str((A_count+T_count)/lenseq)+".")
