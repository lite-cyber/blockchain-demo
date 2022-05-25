# Basic Sample Hardhat Commands

```shell
npx hardhat accounts
npx hardhat compile
npx hardhat clean
npx hardhat test
npx hardhat node
node scripts/sample-script.js
npx hardhat help
```

# Refer to the Project Report for instructions on how to run this program.











# This project demonstrates how file integrity checks can be aided by storing file hashes on a immutable blockchain.

# The python program 'main,py' achieves this in its 9 steps, as outlined below.

# Step 1: 
# Cleans the hardhat environment, then compiles the smart contracts and deploy them onto the locally hosted test ethereum blockchain network. It also stores the blockchain Transaction ID for each contract in respective txt files for later access.

# Step 2: 
# Asks the operator for a filename, and generates a MD5 hash of the file. The hash is then written into uploadhash.txt for later access. It then runs 'editHashstorage.py' which takes the Transaction ID's from 'hashstorageTXID.txt' and the file hash from 'uploadhash.txt' and writes these values into two javascript files: 'Sethashstorage.js' and 'GetHashStorage.js'. These two .js files will be used later in order to write the file hash to the smart contract on the blockchain.

# Step 3: 
# This step runs a hardhat command with the SetHashStorage.js file in order to interact with the smart contract and write the file hash to the smart contract 'Hashstorage'. Once the hash is stored in the smart contract's storage variable, it's integrity is maintained by the blockchain network, and we'll query the smart contract to retrieve the unchanged hash later.

# Step 4: 
# Uploads the file to the IPFS (Interplanetary File System) using web3.storage module. This generates a 'CID' value which is written into 'cidstorage.txt' for later access. The 'CID' is needed later in order to download the file from the 'IPFS' network.

# Step 5: 
# This step runs "editHashstorage.py", which updates the variables in the file "sethashstorage.js . 

# Step 6: 
# Downloads the file from the IPFS network, using ipfs/web3.storage integration. Reads the CID value from cidstorage.txt and runs a command "ipfs get <cid-value> / <file-name> which downloads the file related to the CID value from IPFS.

# Step 7: 
# This step generates a md5 hash from the downloaded file, and writes the hash into "downloadhash.txt".

# Step 8: 
# This step runs the hardhat command npx hardhat run --network localhost with the GetHashStorage.js script prefix which calls the HashStorage smart contract and reads the hash value from the blockchain. The hash value read from the blockchain is then written into "uploadhash.txt".

# Step 9: 
# This last step takes the hash value from "uploadhash.txt" (which was just read from the smart contract on the blockchain) and compares it to the hash value which was generated from the file downloaded through IPFS. It checks if the two hashes match, and outputs "Data Integrity Check Success" if they are a match, letting the user know that the file is unchanged from when it was uploaded until it was downloaded. 
