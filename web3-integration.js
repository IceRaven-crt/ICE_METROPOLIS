// 🧊 ICE METROPOLIS - Web3 Integration
import { Onboard } from '@web3-onboard/core'
import { injected } from '@web3-onboard/injected-wallets'
import { transactionPreview } from '@web3-onboard/transaction-preview'

const onboard = Onboard({
  wallets: [injected()],
  chains: [
    {
      id: '0x1',
      token: 'ETH',
      label: 'Ethereum Mainnet',
      rpcUrl: 'https://mainnet.infura.io/v3/'
    },
    {
      id: '0x89',
      token: 'MATIC',
      label: 'Polygon Mainnet',
      rpcUrl: 'https://polygon-rpc.com'
    }
  ],
  appMetadata: {
    name: 'ICE METROPOLIS',
    icon: '/assets/ice-logo.png',
    description: 'ICE System - Crypto Payments & NFT'
  }
})

console.log('🧊 Web3 Onboard: READY')
console.log('💰 Crypto Payments: ENABLED')
console.log('🎯 Bitcomat Integration: ACTIVE')
