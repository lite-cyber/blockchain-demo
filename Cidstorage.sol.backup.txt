// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "hardhat/console.sol";

contract Cidstorage {
    string private cid;

    constructor(string memory _cid) {
        console.log("", _cid);
        cid = _cid;

    }

    function getcid() public view returns (string memory) {
        return cid;
    }

    function setCid(string memory _cid) public {
        console.log("Setting CID value from '%s' to '%s'", cid, _cid);
        cid = _cid;
    }
}