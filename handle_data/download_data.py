from Historic_Crypto import HistoricalData
from Historic_Crypto import Cryptocurrencies
from Historic_Crypto import LiveCryptoData

if __name == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("coin")
    args = parser.parse_args()
    print(args.coin)