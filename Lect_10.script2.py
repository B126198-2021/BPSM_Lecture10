#!/usr/local/bin/python3

#input dnaseq
dnaseq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print("The original dnaseq is\n" + dnaseq)

# complementing dnaseq
dna1 = dnaseq.replace("A","t")
dna2 = dna1.replace("T","a")
dna3 = dna2.replace("C","g")
dna4 = dna3.replace("G","c")
dnacomplement = dna4.upper()

#output
print("\nThe corresponding complementary dna sequence is\n" +dnacomplement)
 
