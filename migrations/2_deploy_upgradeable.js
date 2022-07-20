// migrations/deploy_upgradeable.js
const { deployProxy } = require('@openzeppelin/truffle-upgrades');

const AdvancedCollectible = artifacts.require('AdvancedCollectible');

module.exports = async function (deployer) {
  dev = accounts.add(config["wallets"]["from_key"]);
  const instance = await deployProxy(AdvancedCollectible, [dev], { deployer });
  console.log('Deployed', instance.address);
};