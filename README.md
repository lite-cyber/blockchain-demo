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

# Step 5: This step runs "editHashstorage.py", which updates the variables in the file "sethashstorage.js . 