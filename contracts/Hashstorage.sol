// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "hardhat/console.sol";

contract Hashstorage {
    string private filehash;

   constructor(string memory _filehash) {
       console.log("", _filehash);
        filehash = _filehash;

    }

    function getfilehash() public view returns (string memory) {
        return filehash;
    }

    function setfilehash(string memory _filehash) public {
        console.log("Setting filehash value from '%s' to '%s'", filehash, _filehash);
        filehash = _filehash;
    }
}