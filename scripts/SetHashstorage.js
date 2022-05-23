async function main () {

//make variable hashstorageTXID and read it from a txt file.

// Set up an ethers contract, representing our deployed Hashstorage instance
const address = '0xeF31027350Be2c7439C1b0BE022d49421488b72C';
const Hashstorage = await ethers.getContractFactory('Hashstorage');
const hashstorage = await Hashstorage.attach(address);

// Send a transaction to set a new value in Hashstorage
await hashstorage.setfilehash('1f8659f1623b78642b127c2972132dfe');

// Call the getfilehash() function of the deployed Hashstorage contract
const value = await hashstorage.getfilehash();
console.log('Hashstorage value is', value.toString());
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });