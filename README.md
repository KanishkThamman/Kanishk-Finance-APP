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
- Judge safety with more than payout ratio alone.
- Allow Export
 
 I plan to build a Python script that, using stocks the user types in, checks their factors, such as each ticker's payout ratio, from an external public API. This is then used to evaluate the ticker as safe, risky for investment, or not having a divident record. The API used pulls live data from a free API (yfinance) to keep it up to date. This evaluation of safety or risk is based on classifying a payout ratio of 60% or higher as 'safe,' negetive numbers mean unsafe, and 0% is classified as having no record of dividend distrebution. Additionaly, stocks with missing data is skipped and the user is notified.

![System diagram](System%20Diagram.png)
 
## Tech Stack
 
- **Language:** Python 3.9 or newer
- **Libraries:** `yfinance` (data), `pandas` (table handling and cleaning), `logging` (Python standard library, used for error handling)
- **External tools:** Yahoo Finance data through `yfinance` (free, no API key needed)
- **Data storage:** none. Data is fetched live on every run and nothing is saved to disk.

## Setup
 
Requires Python 3.9+ and an internet connection.

_More to be added as we develop_
 
## Author
 
Kanishk Thamman
 
