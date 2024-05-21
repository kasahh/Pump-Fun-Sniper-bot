from solana.rpc.api import Client
from solders.keypair import Keypair

PUB_KEY = ""
PRIV_KEY = ""
BUY_AMOUNT = 0.02
SELL_TIMEOUT = 30
CHECK_TELEGRAM = True
CHECK_WEBSITE = False
CHECK_TWITTER = False

RPC = "https://api.mainnet-beta.solana.com"

client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)
