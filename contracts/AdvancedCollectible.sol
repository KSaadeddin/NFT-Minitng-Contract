// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract AdvancedCollectible is
    ERC721,
    ERC721Enumerable,
    ERC721URIStorage,
    ERC721Burnable,
    Ownable
{
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    uint256 public tokenCounter;

    constructor() ERC721("YOURToken", "YTK") {}

    function safeMint(address to, string memory uri) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        tokenCounter = tokenId + 1;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: Transfer caller is neither owner nor approved."
        );

        _setTokenURI(tokenId, _tokenURI);
    }

    // Function to withdraw balance from the contract
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
