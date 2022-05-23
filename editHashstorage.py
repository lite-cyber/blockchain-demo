import os
#Part 1: Updates TXID field in sethashstorage.js

#Reads hashstorageTXID.txt and stores the TXID as a string variable.
with open('scripts/hashstorageTXID.txt', 'r') as file:
    TXID = file.read().rstrip()

#Reads Sethashstorage.js
with open('scripts/SetHashstorage.js','r') as f:
   lines = f.readlines()

#Updates Hashstorage Contract TXID from HashstorageTXID variable above.

with open('scripts/SetHashstorage.js','w') as f:
   new_value = "const address = '" +TXID + "';\n"
   for line in lines:
       if line.startswith('const address'):
           line = '{}'.format(new_value)
       f.write(line)
f.close()
file.close()    

#-------------------------------------------------------------------------
#PART 2: Updates SetFileHash field in SetHashstorage.js to that of uploadhash.txt


with open('uploadhash.txt', 'r') as file:
    uploadhashvalue = file.read().rstrip()

with open('scripts/SetHashstorage.js','r') as f:
   lines = f.readlines()

# Replaces the line in 'SetHashstorage.js' which contains
# the transaction id of the deployed hashstorage contract.
with open('scripts/SetHashstorage.js','w') as f:
   new_upload_value = "await hashstorage.setfilehash('" +uploadhashvalue + "');\n"
   for line in lines:
       if line.startswith('await hashstorage.setfilehash'):
           line = '{}'.format(new_upload_value)
       f.write(line)
f.close()
file.close()

#-------------------------------------------------------------------------
#Part 3: Updates TXID field in 'GetHashstorage.js'

#Reads hashstorageTXID.txt and stores the TXID as a string variable.

with open('scripts/hashstorageTXID.txt', 'r') as file:
    TXID = file.read().rstrip()

#Reads Sethashstorage.js
with open('scripts/GetHashStorage.js','r') as f:
   lines = f.readlines()

#Updates Hashstorage Contract TXID from HashstorageTXID variable above.

with open('scripts/GetHashStorage.js','w') as f:
   hash_new_value = "const address = '" +TXID + "';\n"
   for line in lines:
       if line.startswith('const address'):
           line = '{}'.format(hash_new_value)
       f.write(line)
f.close()
file.close()       