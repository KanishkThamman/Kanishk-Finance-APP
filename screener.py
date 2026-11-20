import logging
import yfinance as yf # import finance API

logging.getLogger("yfinance").setLevel(logging.CRITICAL) # silence yfinance's raw 404 output (Look at Issue#4 for more info)

THRESHOLD = 0.60  # payout ratio <= 60% is Safe
MAX_DEBT_TO_EQUITY = 170  # 1.7x. yfinance reports debtToEquity as a percentage, so 170 not 1.7. Rule of thumb that ignores sector differences (Issue#13)
NO_DIVIDEND = "no record of dividend payout"


def fetch_factors(ticker): # Return payout_ratio and debt_to_equity, any value not found is reported is None.
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


def failed_checks(ratio, debt_to_equity): # names every safety check the ticker fails (Issue#13)
    failed = []
    if not 0 < ratio <= THRESHOLD: # fixes Issue#6 and checks for negetive numbers to prevent incorrect classifiation
        failed.append("payout ratio")

    # missing debt data is ignored and amke sure the values is not negetive 
    if debt_to_equity is not None and not 0 <= debt_to_equity <= MAX_DEBT_TO_EQUITY:
        failed.append("debt-to-equity")

    return failed


def classify(ratio, debt_to_equity): # using the factors given, classify each as 'safe' 'risky' or just skipped

    if ratio is None:
        return "skipped"

    if ratio == 0:
        return NO_DIVIDEND # fixes Issue#8: 0% payout means no dividend, and is not an indication of the stock being 'safe' or 'unsafe' (also has a risk of confusing user since no divident does not mean that the stock is 'unsafe')

    if failed_checks(ratio, debt_to_equity):
        return "risky"
    else:
        return "safe"


def format_row(ticker, factors, label): # Create one line per ticker and also tell user why it as risky (Issue #13)
    ratio, debt = factors["payout_ratio"], factors["debt_to_equity"]
    payout_text = "n/a" if ratio is None else f"{ratio:.0%}"
    debt_text = "n/a" if debt is None else f"{debt / 100:.1f}x" # yfinance gives percentage so it is changed to a multiple to be consistant with how it is described
    row = f"{ticker:<6}{payout_text:>6}  D/E {debt_text:>5}"

    if label == "risky":
        row += "  fails: " + ", ".join(failed_checks(ratio, debt))

    return row


def main(): # main func! here is where the pizzaz happens :) (we need some fun in coding comments!)
    
    groups = {"safe": [], "risky": [], NO_DIVIDEND: [], "skipped": []} # init dict that will be used for classify tickers into their groups (added new classification to fix issue#8)
    
    for ticker in get_tickers(): # iterate through user's tickers and get the payout ratio and group it into 'safe', 'risky', or 'skipped'
        factors = fetch_factors(ticker)
        groups[classify(factors["payout_ratio"], factors["debt_to_equity"])].append((ticker, factors))

    for name, rows in groups.items(): # iterate the groups dict to print each type of stock to the user
        print(f"\n== {name.upper()} ({len(rows)}) ==")
        for ticker, factors in rows:
            print(format_row(ticker, factors, name))


if __name__ == "__main__":
    main()

