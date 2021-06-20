from datetime import datetime, timezone, timedelta

import numpy as np
from pandas import DataFrame
from Historic_Crypto import HistoricalData

################################################################################
VALID_GRANULARITIES = (60, 300, 900, 3600, 21600, 86400)
DEFAULT_GRANULARITY = 300
DEFAULT_CURRENCY = "USD"
################################################################################

def get_ticker(coin_str: str, currency: str = DEFAULT_CURRENCY) -> str:
    ticker = f"{coin_str}-{currency}"
    return ticker


def get_hist_crypto_dt_fmt(dt: datetime) -> str:
    dt_str = dt.strftime("%Y-%m-%d-%H-%M")
    return dt_str


def get_valid_granularity(granularity: int = DEFAULT_GRANULARITY) -> int:
    
    if granularity not in VALID_GRANULARITIES:
        closest_gran_ind = np.argmin(np.abs(granularity - np.array(VALID_GRANULARITIES) ))
        closest_gran = VALID_GRANULARITIES[closest_gran_ind]
        granularity = closest_gran

    return granularity


def retrieve_data(
    coin_str: str, 
    start_date: datetime, end_date: datetime = None, 
    granularity: int = DEFAULT_GRANULARITY
) -> DataFrame:
    coin_ticker = get_ticker(coin_str=coin_str)

    start_date = get_hist_crypto_dt_fmt(dt=start_date)
    if end_date is not None:
        end_date = get_hist_crypto_dt_fmt(dt=end_date)
    
    granularity = get_valid_granularity(granularity=granularity)

    df = HistoricalData(
        ticker=coin_ticker, 
        granularity=granularity, 
        start_date=start_date,
        end_date=end_date
    ).retrieve_data()

    return df


################################################################################


def main(
    coin_str: str, 
    start_date: datetime, end_date: datetime = None, 
    granularity: int = DEFAULT_GRANULARITY
) -> None:
    df = retrieve_data(
        coin_str=coin_str, 
        start_date=start_date, end_date=end_date, 
        granularity=granularity
    )
    breakpoint()


################################################################################
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("coin")
    parser.add_argument("granularity")
    args = parser.parse_args()
    main(
        coin_str=args.coin, 
        granularity=int(args.granularity),
        start_date=datetime(year=2021, month=6, day=17, tzinfo=timezone.utc)
    )