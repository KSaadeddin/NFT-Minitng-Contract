from brownie import AdvancedCollectible, accounts, config, network

STATIC_SEED = 123

# Run second: brownie run scripts/advanced_collectible/mint_collectible.py --network polygon-main (or other network)
def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(dev)
    print(network.show_active())

    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    print(advanced_collectible)

    transaction = advanced_collectible.safeMint(
        dev,
        "NONE",
        {"from": dev},
    )

    transaction.wait(1)
