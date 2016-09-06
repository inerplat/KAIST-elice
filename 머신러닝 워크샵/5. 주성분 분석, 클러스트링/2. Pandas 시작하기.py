import numpy as np
import pandas as pd

def main():
    do_exercise()

def do_exercise():
    # 1

    aapl_bars = pd.read_csv("./AAPL.csv")
    date_index=aapl_bars.pop('Date')
    aapl_bars.index=pd.to_datetime(date_index)
    df = aapl_bars[['Open', 'Close', 'Volume']]
    df = df[:]['1989' : '2003-04']
    print(df)
    return df

if __name__ == "__main__":
    main()
