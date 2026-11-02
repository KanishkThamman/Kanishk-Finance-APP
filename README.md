# Kanishk-Finance-APP
A Python cmd tool that checks dividend stocks and tells the user if each one as safe or risky. All based on how likely it is to cut its dividend.
 
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
- Test factors like 60% payout ratio > safe. 

**Out of scope**
 
- Anything in the Future Plans list
- ML forecasting from historical data, a mobile app, etc
## How It Works

**Future Plans**
- Let users type in whatever stocks they want instead of only the 20 built in.
- Judge safety with more than payout ratio alone.
- Allow Export
 
 I plan to build a Python script that, using 20 predefined stocks, checks their factors, such as each ticker's payout ratio, from an external public API. This is then used to evaluate the ticker as safe or risky for investment. The API used pulls live data from a free API (yfinance) to keep it up to date. This evaluation of safety or risk is based on classifying a payout ratio of 60% or higher as 'safe.' 

![System diagram](docs/system_diagram.png)
 
## Tech Stack
 
- **Language:** Python 3.9 or newer
- **Libraries:** `yfinance` (data), `pandas` (table handling and cleaning)
- **External tools:** Yahoo Finance data through `yfinance` (free, no API key needed)
- **Data storage:** none. Data is fetched live on every run and nothing is saved to disk.

## Setup
 
Requires Python 3.9+ and an internet connection.

_More to be added as we develop_
 
## Author
 
Kanishk Thamman, [GitHub](https://github.com/<your-username>)
 
