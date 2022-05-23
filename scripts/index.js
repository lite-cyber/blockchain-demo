// scripts/index.js
async function main () {

// Retrieve accounts from the local node
const accounts = await ethers.provider.listAccounts();
console.log(accounts);

// Set up an ethers contract, representing our deployed Hashstorage instance
const address = '0x0DCd1Bf9A1b36cE34237eEaFef220932846BCD82';
const Hashstorage = await ethers.getContractFactory('Hashstorage');
const hashstorage = await Hashstorage.attach(address);

// Call the getfilehash() function of the deployed Hashstorage contract
const value = await hashstorage.getfilehash();
console.log('Hashstorage value is', value.toString());

// Send a transaction to set a new value in Hashstorage
await hashstorage.setfilehash('test3');





}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });

  // This file is redundant and can be removed/deleted. 