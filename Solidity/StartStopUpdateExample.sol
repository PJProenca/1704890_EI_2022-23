// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.1;
contract StartStopUpdateExample {
 function sendMoney() public payable {
 }
 function withdrawAllMoney(address payable _to) public {
 _to.transfer(address(this).balance);
 }
}