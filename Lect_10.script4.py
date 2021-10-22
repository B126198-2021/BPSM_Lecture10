#!/usr/local/bin/python3

#input dnaseq
dnaseq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# Splicing out introns

#The first exon runs from the start of the sequence to the sixty-third real character
#So 0-63
exon1 =dnaseq[0:63]
print("Exon1 should be\n"+exon1+"\nThe length of exon1 is " +str(len(exon1)))


#The second exon runs from the ninety-first real character to the end of the sequence.
exon2 = dnaseq[90:]
print("\nExon2 should be\n"+exon2+"\nThe length of exon2 is " +str(len(exon2)))

#Coding seq
codeseq =exon1+exon2
lencode = len(codeseq)
print("\nCoding seq should be\n"+codeseq+"\nThe length of coding seq is " +str(lencode)+"\nThe percentage of coding seq is " + str(lencode/len(dnaseq)))

#intron
intron=dnaseq[63:90]
print("\nIntron should be\n"+intron+"\nThe length of intron is " +str(len(intron)))
mod_intron = intron.lower()
mod_dnaseq = exon1+mod_intron+exon2
print("The dnaseq with non-coding bases in lowercase should be\n"+mod_dnaseq)


