import os
#Step 1 Start hardhat, compile and deploy contracts. #Done
#stream = os.system('npm install')
stream = os.system('npx hardhat clean')
stream = os.system('npx hardhat compile')
stream = os.popen('npx hardhat run --network localhost scripts/deploy.js')
output = stream.read()
print(output)

#Prints the TXID for cidstorage to a file #Done
import subprocess
cidoutput = open('scripts/cidstorageTXID.txt', 'w')
cid = output.split()
print(cid[-1], file = cidoutput)
cidoutput.close()

#Prints the TXID for hashstorage to a file #Done
hashoutput = open('scripts/hashstorageTXID.txt', 'w')
hash = output.split()
print(hash[-5], file = hashoutput)
hashoutput.close()


#STEP 2: COMPLETE
#Generate MD5 hash of a file and store hash in uploadhash.txt #Done

import hashlib
filename = input("Enter the file name for md5 hash generation: ")
with open(filename,"rb") as f:
    bytes = f.read() # read file as bytes
    readable_hash = hashlib.md5(bytes).hexdigest()
    print(readable_hash)
    hashobject = open('uploadhash.txt', 'w')
    hashobject.write(readable_hash)
    hashobject.close()

# Updates sethashstorage.js by running edithashstorage.
import editHashstorage

#Step 3: Upload file hash to eth blockchain. #Done
stream = os.system('npx hardhat run --network localhost scripts/SetHashstorage.js')
print('File Hash Successfully uploaded to ethereum blockchain.')


#STEP 4: COMEPLETE
#upload file to ipfs using web3.storage.

file_name = input('Enter filename to upload to IPFS: ')
stream = os.popen('node web3-storage/put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDVmZDU2OUFCNzlGNjI5ZjQzMzg2RGEzOTI5MzIxYzM5MzE5NjMyMGEiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NTIyODY3NDYwMTMsIm5hbWUiOiJpbnRlZ3JpdHktY2hlY2sifQ.YU7Idir5PE5dB5C7OWlT6Udec0NJCu3VJybpvThBaUw '+file_name)
output = stream.read()

print(output)

import subprocess
myoutput = open('cidstorage.txt', 'w')
cid = output.split()
print(cid[-1], file = myoutput)
myoutput.close()


#STEP 5: 

# Updates sethashstorage.js by running edithashstorage.
import editHashstorage
print('Updates SetHashstorage') #For debugging


#STEP 5.5: NEEDS WORK.
#write the file's hash and ipfs cid to pre deployed contracts
#write the blockchain transaction/smart contract ID to txt file.



#STEP 6: COMPLETE
#download file from ipfs/web3.storage

with open('cidstorage.txt', 'r') as file:
    cid_read = file.read().rstrip()
    download_file_name = input('Enter filename to download from IPFS: ')
    stream = os.system('ipfs get '+ cid_read + '/' + download_file_name)
print(download_file_name + ' successfully downloaded.')

#STEP 7: COMPLETED
#generate hash from downloaded file.

import hashlib
with open(download_file_name,"rb") as f:
    bytes = f.read() # read file as bytes
    readable_hash = hashlib.md5(bytes).hexdigest()
    print(readable_hash)
    hashobject = open('downloadhash.txt', 'w')
    hashobject.write(readable_hash)
    hashobject.close()


#Step 8: Get the "immutable" version of uploadhash from the blockchain by running GetHashStorage.js to query Blockchain.

#Reads the output from 'GetHashStorage' into uploadhash.txt
stream = os.popen('npx hardhat run --network localhost scripts/GetHashStorage.js')
output = stream.read()
print(output)

lasthash = open('uploadhash.txt', 'w')
hashput = output.split()
print(hashput[-1], file = lasthash)
lasthash.close()
print('Updating uploadhash.txt with value downloaded from Ethereum Blockchain')


#STEP 9: Sort of Completed (need to update uploadhash from BC DB.)
#compare downloaded file's hash to uploaded file's hash.
# output 'yes' or 'no' indicating if it is a match.

import filecmp
  
f1 = "uploadhash.txt"
f2 = "downloadhash.txt"

with open("uploadhash.txt", 'r') as f:
    key_hash = set(f.read().splitlines())

with open("downloadhash.txt", 'r') as f:
    download_hash = f.read().splitlines()
    for line in download_hash:
        if any(kw in line for kw in key_hash): # if any of the word in key words is in line print it
            print('Data Ingegrity Check Success! Both hashes are: ' + line)
