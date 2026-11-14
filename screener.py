# Known issue for docs: Using Yahoo data sometimes will give you mis formated ratios for payout which code accounts for by skipping 
import yfinance as yf # import finance API

TICKERS = [ "KO", "PEP", "JNJ", "PG", "MMM", "T", "VZ", "XOM", "CVX", "IBM","MCD", "WMT", "HD", "ABBV", "PFE", "MRK", "O", "MO", "PM", "CL",] # hard coding tickers for MVP 
THRESHOLD = 0.60  # payout ratio <= 60% is Safe


def fetch_payout_ratio(ticker):
    """Return payout ratio as a fraction, or None if unavailable."""
    try: # Used try to ensure that the whole program does not get stoped from one wrong ticker
        return yf.Ticker(ticker).info.get("payoutRatio") # from given ticker, get its company data and then its payout ratio 
    except Exception as error:  # network/API failure will treat ticker as missing
        print(f"warn: {ticker} fetch failed: {error}")
        return None


def classify(ratio): # using ratios given, classify each as 'safe' 'risky' or just skipped
    if ratio is None:
        return "skipped"
    return "safe" if ratio <= THRESHOLD else "risky"


def main(): # main func! here is where the pizzaz happens :) (we need some fun in coding comments!)
    groups = {"safe": [], "risky": [], "skipped": []} # init dict that will be used for classify tickers into their groups
    for ticker in TICKERS: # iterate through hard coded ticker list and get the payout ratio and group it into its respective types ('safe', 'risky', and 'skipped')
        ratio = fetch_payout_ratio(ticker)
        groups[classify(ratio)].append((ticker, ratio))

    for name, rows in groups.items(): # iterate the groups dict to print each type of stock to the user
        print(f"\n== {name.upper()} ({len(rows)}) ==")
        for ticker, ratio in rows:
            shown = "n/a" if ratio is None else f"{ratio:.0%}"
            print(f"{ticker:<6}{shown:>6}")


if __name__ == "__main__":
    main()

