from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import get_pic, OPENSEA_FORMAT, MAINNET_OPENSEA_FORMAT

# Uncomment and use your metadata file name (.json) and its IPFS url. You can get it after uploading your file to a pinning service such as pinata.
pic_metadata_dic = {
    # "FILE NAME": "FILE NAME URL ON IPFS WITH ITS CORRECT CID",
}

# Run forth: brownie run scripts/advanced_collectible/set_token_uri.py --network polygon-main (or other network)
def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    # number_of_advanced_collectibles = 1
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(
        "The number of tokens you have deployed is: "
        + str(number_of_advanced_collectibles)
    )

    for token_id in range(number_of_advanced_collectibles):
        pic = get_pic(token_id)
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}.".format(token_id))
            set_tokenURI(token_id, advanced_collectible, pic_metadata_dic[pic])
        else:
            print("Skipping {}. That tokenURI is already set.".format(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "You can now view your NFT at {}.".format(
            # For testnet:
            # OPENSEA_FORMAT.format(nft_contract.address, token_id)
            # For mainnet:
            MAINNET_OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )

    print("Please give up to 20 minutes and hit 'refresh metadata' button")
