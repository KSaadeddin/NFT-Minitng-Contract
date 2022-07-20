from msilib.schema import PublishComponent
from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_advanced_collectible

# token_Id = Uncomment and mention token id that you want to be burnt.

# Run first: brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby (or other network)
# This is for burning an NFT that was already minted.
def main():
    pass
    dev = accounts.add(config["wallets"]["from_key"])
    print(dev)
    print(network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    burn(token_Id, advanced_collectible)


def burn(token_id, nft_contract):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.burn(token_id, {"from": dev})
    print("Token no. {} burnt.".format(token_id))
