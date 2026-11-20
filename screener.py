import logging
import yfinance as yf # import finance API

logging.getLogger("yfinance").setLevel(logging.CRITICAL) # silence yfinance's raw 404 output (Look at Issue#4 for more info)

THRESHOLD = 0.60  # payout ratio <= 60% is Safe
NO_DIVIDEND = "no record of dividend payout"


def fetch_factors(ticker): # Return payout_ratio and debt_to_equity, any value not found is reported is None."""
    try: # Used try to ensure that the whole program does not get stoped from one wrong ticker
        info = yf.Ticker(ticker).info # one call per ticker so adding a factor does not add another network request (Issue#13)
        return {"payout_ratio": info.get("payoutRatio"), "debt_to_equity": info.get("debtToEquity")}

    except Exception:  # network/API failure and 404s will treat ticker as missing. Fixes issue#4
        print(f"warn: {ticker} skipped (not found or data unavailable)")
        return {"payout_ratio": None, "debt_to_equity": None}


def get_tickers(): # ask user for tickers, exit with an error if they enter nothing (see more info in Issue#11)
    
    raw = input("Enter tickers separated by spaces or commas: ")
    tickers = raw.replace(",", " ").upper().split() # input sanitazation to ensure random spaces and commas = multiple tickers at once
    
    if not tickers:
        raise SystemExit("Error: no tickers entered. Please enter at least one ticker.")
    
    return list(dict.fromkeys(tickers)) # drops duplicates but keeps order


def classify(ratio): # using ratios given, classify each as 'safe' 'risky' or just skipped
    
    if ratio is None:
        return "skipped"
    
    if ratio == 0:
        return NO_DIVIDEND # fixes Issue#8: 0% payout means no dividend, and is not an indication of the stock being 'safe' or 'unsafe' (also has a risk of confusing user since no divident does not mean that the stock is 'unsafe')
    
    return "safe" if 0 < ratio <= THRESHOLD else "risky" # fixes Issue#6 and checks for negetive numbers to prevent incorrect classifiation


def main(): # main func! here is where the pizzaz happens :) (we need some fun in coding comments!)
    
    groups = {"safe": [], "risky": [], NO_DIVIDEND: [], "skipped": []} # init dict that will be used for classify tickers into their groups (added new classification to fix issue#8)
    
    for ticker in get_tickers(): # iterate through user's tickers and get the payout ratio and group it into 'safe', 'risky', or 'skipped'
        ratio = fetch_factors(ticker)["payout_ratio"] # debt_to_equity is fetched until classification (Issue#13)
        groups[classify(ratio)].append((ticker, ratio))

    for name, rows in groups.items(): # iterate the groups dict to print each type of stock to the user
        print(f"\n== {name.upper()} ({len(rows)}) ==")
        for ticker, ratio in rows:
            shown = "n/a" if ratio is None else f"{ratio:.0%}"
            print(f"{ticker:<6}{shown:>6}")


if __name__ == "__main__":
    main()

