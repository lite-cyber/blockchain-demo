async function main () {

    //make variable hashstorageTXID and read it from a txt file.
    
    // Set up an ethers contract, representing our deployed Hashstorage instance
    const address = '0x3155755b79aA083bd953911C92705B7aA82a18F9';
    const Hashstorage = await ethers.getContractFactory('Hashstorage');
    const hashstorage = await Hashstorage.attach(address);
    
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