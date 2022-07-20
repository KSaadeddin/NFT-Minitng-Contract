from tkinter import N
from brownie import AdvancedCollectible, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_name, get_pic, get_type
from pathlib import Path
import os
import requests
import json

# Uncomment and use your image name and its IPFS url. You can get it after uploading your image to a pinning service such as pinata.
pic_to_image_uri = {
    # "IMAGE NAME": "IMAGE URL ON IPFS WITH ITS CORRECT CID",
}

# Run: [System.Environment]::SetEnvironmentVariable('PATH',$Env:PATH+';;C:\Users\...PATH TO YOUR GO-IPFS\go-ipfs_v0.12.0\go-ipfs')
# Run: ipfs daemon
# Run third: brownie run scripts/advanced_collectible/create_metadata.py --network polygon-main (or other network)
def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_tokens = advanced_collectible.tokenCounter()
    print("The number of tokens deployed is {}.".format(number_of_tokens))
    write_metadata(number_of_tokens, advanced_collectible)


def write_metadata(number_of_tokens, nft_contract):
    for token_id in range(number_of_tokens):
        collectible_metadata = sample_metadata.metadata_template
        pic = get_pic(token_id)
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            # + str(token_id)
            # + "-"
            + pic
            + ".json"
        )

        if Path(metadata_file_name).exists():
            print("{} was already found!".format(metadata_file_name))
        else:
            collectible_metadata["name"] = get_name(token_id)
            # collectible_metadata["description"] = "Your NFT Description"

        print(collectible_metadata)
        image_to_upload = None
        if os.getenv("UPLOAD_IPFS") == "true":
            image_path = "./img/{}.jpg".format(pic.lower().replace("_", "-"))
            image_to_upload = pic_to_image_uri[pic]
            print(image_to_upload)
        collectible_metadata["image"] = image_to_upload
        collectible_metadata["attributes"] = get_type(token_id)

        with open(metadata_file_name, "w") as file:
            json.dump(collectible_metadata, file)

        if os.getenv("UPLOAD_IPFS") == "true":
            upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://localhost:5001"
        response = requests.post(ipfs_url + "/api/v0/add", files={"file": image_binary})
        print(response.json())
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, filename)
        print(uri)
        return uri
    return None
