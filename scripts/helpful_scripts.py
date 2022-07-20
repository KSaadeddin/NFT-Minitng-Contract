OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"
MAINNET_OPENSEA_FORMAT = "https://opensea.io/assets/matic/{}/{}"


def get_pic(pic_number):
    # Uncomment and list your NFT names.
    switch = {
        # 0: "ARRAY",
        # 1: "OF",
        # 2: "YOUR",
        # 3: "NFT",
        # 4: "PICTURES"
        # 5: "NAMES",
    }
    return switch[pic_number]


# This an array of your NFT titles (names) as you like them to appear in the metadata (on the marketplace).
def get_name(name_number):
    switch = {
        # 0: "ARRAY",
        # 1: "OF",
        # 2: "YOUR",
        # 3: "NFT",
        # 4: "PICTURES"
        # 5: "NAMES",
    }
    return switch[name_number]


# This an array of your NFT attributes as you like them to appear in the metadata (on the marketplace).
def get_type(type_number):
    switch = {
        # 0: [{"trait-type": "...", "value": "..."}],
        # 1: [{"trait-type": "...", "value": "..."}],
        # 2: [{"trait-type": "...", "value": "..."}],
        # 3: [{"trait-type": "...", "value": "..."}],
        # 4: [{"trait-type": "...", "value": "..."}],
        # 5: [{"trait-type": "...", "value": "..."}],
    }
    return switch[type_number]
