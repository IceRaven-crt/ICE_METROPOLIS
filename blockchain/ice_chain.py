# ICE BLOCKCHAIN MODULE
class ICE_Blockchain:
    def __init__(self):
        self.chain_name = "ICE_NETWORK_TERMUX"
        self.blocks = []
    
    def create_genesis_block(self):
        return "🧊 Genesis Block: ICE METROPOLIS TERMUX"
    
    def mine_block(self, data):
        return f"⛏️ Mined: {data}"

blockchain = ICE_Blockchain()
print(blockchain.create_genesis_block())
