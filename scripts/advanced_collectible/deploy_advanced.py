from brownie import AdvancedCollectible, accounts, network, config

# Run first: brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby (or other network)
# This deploys the smart contract that acts as a factory for the NFTs that are meant to be minted.
def main():
    pass
    dev = accounts.add(config["wallets"]["from_key"])
    print(dev)
    print(network.show_active())
    # To change the network to rinkeby, write (in the terminal): brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby.
    # To show networks list, write (in the terminal): brownie networks list.
    # publish_source publishes to etherscan or polygonscan.
    publish_source = False
    advanced_collectible = AdvancedCollectible.deploy(
        {"from": dev},
        publish_source=publish_source,
    )

    return advanced_collectible
