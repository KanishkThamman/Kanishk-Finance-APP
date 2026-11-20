# Kanishk-Finance-APP
A Python cmd tool that checks dividend stocks and tells the user if each one is safe, risky, or has no record of a dividend payout. All based on how likely it is to cut its dividend.
 
## The Problem (Project Goal)
 
One of the issues I have had is understanding which stocks to pick for long-term investment and income. This is a common problem amongst college students who are trying to save money for the future.  A popular strategy is to buy high-dividend stocks, since they pay dividends on top of price growth. But many of these stocks cannot afford their high dividends over the long run and end up cutting them.
 
**Goal:** give a college investor a quick way to look at which dividend stocks they should invest in. 
 
**Hypothesis:** a lower payout ratio = more sustainable dividend.
 
## MVP Scope

**In scope**
 
- Find and code in the list of 20 stock tickers for stocks 
- Pull the data for each ticker from a free api
- Do data cleaning and skip tickers with missing data rather than assuming
- Printing Raw Dataframe post data cleaning step to have some output that we can verify
- Test factors like a payout ratio between 0% and 60% is safe. Negative or above 60% is risky. Exactly 0%  is no record of dividend payout (not 'risky', since the stock itself may still be an ok investment). 

**Out of scope**
 
- Anything in the Future Plans list
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
- [x] Let the user enter their own tickers (Issue #11)
- [x] Add debt-to-equity as a second safety check and show user why a ticker is classified as risky (Issue #13)

## Setup
 
Requires Python 3.9+ and an internet connection.

_More to be added as we develop_
 
## Author
 
Kanishk Thamman
 
