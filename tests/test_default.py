from wake.testing import *

from pytypes.contracts.IERC20 import IERC20
from pytypes.contracts.IPriceFeed import IPriceFeed

@default_chain.connect(fork="https://ethereum-rpc.publicnode.com")
def test_default():
    # Forked addresses
    test_address = Address("0x40B38765696e3d5d8d9d834D8AaD4bB6e418E489")
    feed_registry = IPriceFeed("0x47Fb2585D2C56Fe188D0E6ec628a38b74fCeeeDf")

    # ISO 4217 currency code for USD
    usd = Address("0x0000000000000000000000000000000000000348")

    # Tokens to check
    tokens = [
        IERC20("0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"), # SHIB
        IERC20("0x514910771AF9Ca656af840dff83E8264EcF986CA"), # LINK
        IERC20("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"), # USDC
    ]

    total_value = 0
    for t in tokens:
        # Skip tokens that are not supported by the price feed
        with may_revert():
            response = feed_registry.latestRoundData(t, usd)
            price = response[1]
            amount = t.balanceOf(test_address)
            total_value += price * amount
            print(f"- Token: {t}, Price: {price}, Amount: {amount}, Value: {price * amount}")
            continue
        print(f"- Token: {t} price calculation failed")

    print(f"Total value: {total_value} USD")