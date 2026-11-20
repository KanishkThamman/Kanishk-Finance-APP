# Kanishk-Finance-APP
A Python cmd tool that checks dividend stocks and tells the user if each one is safe, risky, or has no record of a dividend payout. All based on how likely it is to cut its dividend.
 
## The Problem (Project Goal)
 
One of the issues I have had is understanding which stocks to pick for long-term investment and income. This is a common problem amongst college students who are trying to save money for the future.  A popular strategy is to buy high-dividend stocks, since they pay dividends on top of price growth. But many of these stocks cannot afford their high dividends over the long run and end up cutting them.
 
**Goal:** give a college investor a quick way to look at which dividend stocks they should invest in. 
 
**Hypothesis:** a lower payout ratio = more sustainable dividend.
 
## MVP Scope

**In scope**
 
- Find and code in a list of 20 stock tickers (later replaced by user-entered tickers, see "What Changed From the Plan")
- Pull the data for each ticker from a free api
- Do data cleaning and skip tickers with missing data rather than assuming
- Print the cleaned data so there is output we can verify (built as grouped text output instead of a DataFrame)
- Test factors like a payout ratio between 0% and 60% is safe. Negative or above 60% is risky. Exactly 0%  is no record of dividend payout (not 'risky', since the stock itself may still be an ok investment). 

**Out of scope**
 
- ML forecasting from historical data, a mobile app, etc
## How It Works

**Future Plans**
- Add more safety factors beyond payout ratio and debt-to-equity (for example interest coverage)
- Make the thresholds sector-aware, since utilities and telecoms normally carry more debt
- Allow Export
 
This is a Python script that takes the tickers the user types in and pulls each one's payout ratio and debt-to-equity from a free public API (yfinance), so the data stays up to date. Each ticker is then sorted into one of four groups:

- **Safe:** payout ratio above 0% and up to 60%, and debt-to-equity at or below 1.7x.
- **Risky:** payout ratio negative or above 60%, or debt-to-equity above 1.7x (or negative). The output says which check failed.
- **No record of dividend payout:** a payout ratio of exactly 0%. This is not 'risky', since the stock itself may still be an ok investment.
- **Skipped:** the ticker was not found or has no payout ratio data, and the user is notified.

If debt-to-equity is missing (some companies do not report it), that check is ignored and the ticker is judged on payout ratio alone. The 1.7x debt limit is a rule of thumb: sources commonly treat above 1.0 as elevated and above 2.0 as heavily leveraged, and it does not account for sector differences.

![System diagram](System%20Diagram.png)
 
## Tech Stack
 
- **Language:** Python 3.9 or newer
- **Libraries:** `yfinance` (live payout ratio and debt-to-equity data), `logging` (Python standard library, used to silence yfinance's raw error output)
- **External tools:** Yahoo Finance data through `yfinance` (free, no API key needed)
- **Data storage:** none. Data is fetched live on every run and nothing is saved to disk.

## Roadmap

- [x] Classify tickers by payout ratio
- [x] Do not allow negative payout ratios (Issue #6)
- [x] Separate 0% payout as "no record of dividend payout" (Issue #8)
- [x] Catch yfinance errors so one error does not stop the run (Issue #4)
- [x] Let the user enter their own tickers (Schedule feature, Issue #11)
- [x] Add debt-to-equity as a second safety check and show user why a ticker is classified as risky (Schedule feature: use multiple factors, Issue #13)

## What Changed From the Plan

- **Tickers:** the plan was a hardcoded list of 20. The final tool asks the user to type any tickers.
- **Output:** the plan was a pandas DataFrame, sorted and formatted as a table. The final tool prints grouped rows with no pandas, and shows why a ticker is risky.
- **Factors:** the plan used yield and payout ratio. The final tool uses payout ratio and debt-to-equity.
- **Labels:** the plan had safe and risky. The final tool also has "no record of dividend payout" and "skipped".
- **Errors:** the plan had an internet check that exits. The final tool catches errors per ticker and skips only the bad one.

## Setup
 
Requires Python 3.9+, Git, and an internet connection.

1. Clone the repo and move into it:
   ```
   git clone https://github.com/KanishkThamman/Kanishk-Finance-APP.git
   cd Kanishk-Finance-APP
   ```
2. Install the dependency:
   ```
   pip install -r requirements.txt
   ```
3. Run the screener (use `python3` instead of `python` on macOS/Linux if needed):
   ```
   python screener.py
   ```
4. When prompted, type any stock tickers separated by spaces or commas, then press Enter.

### Example run

Input: `AAPL, KO, MMM, LMT, FAKEXYZ`

```
Enter tickers separated by spaces or commas: AAPL, KO, MMM, LMT, FAKEXYZ

== SAFE (1) ==
AAPL     12%  D/E  0.8x

== RISKY (3) ==
KO       62%  D/E  1.1x  fails: payout ratio
MMM      46%  D/E  3.0x  fails: debt-to-equity
LMT      49%  D/E  2.0x  fails: debt-to-equity

== NO RECORD OF DIVIDEND PAYOUT (0) ==

== SKIPPED (1) ==
FAKEXYZ   n/a  D/E   n/a
```

Each row shows the ticker, its payout ratio, and its debt-to-equity (D/E). Numbers come from live data, so they change over time. Entering nothing exits with an error message, and a ticker that cannot be found is skipped instead of stopping the run.
 
## Demo

TODO: add video walkthrough link here before submitting.

## Author
 
Kanishk Thamman
 
