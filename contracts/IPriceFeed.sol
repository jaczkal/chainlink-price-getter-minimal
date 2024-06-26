// SPDX-License-Identifier: None

pragma solidity 0.8.20;

interface IPriceFeed {
  function latestRoundData(address base, address quote)
    external
    view
    returns (uint80 roundId, int256 answer, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound);
}