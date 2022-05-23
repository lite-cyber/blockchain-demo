const hre = require("hardhat");
const ethers = hre.ethers;
async function main() {
  // Hardhat always runs the compile task when running scripts with its command
  // line interface.
  //
  // If this script is run directly using `node` you may want to call compile
  // manually to make sure everything is compiled
  // await hre.run('compile');

  // Deploys the Hashstorage Contract
  const Hashstorage = await hre.ethers.getContractFactory("Hashstorage");
  const hashstorage = await Hashstorage.deploy("Erlend: No hash stored yet.");

  await hashstorage.deployed();

  console.log("Hashstorage deployed to:", hashstorage.address);

  // Deploys the Cidstorage Contract
  const Cidstorage = await hre.ethers.getContractFactory("Cidstorage");
  const cidstorage = await Cidstorage.deploy("Erlend: No CID stored yet.");

  await cidstorage.deployed();

  console.log("Cidstorage deployed to:", cidstorage.address);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });