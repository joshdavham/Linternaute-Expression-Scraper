# Linternaute-Expression-Scraper
A web scraper that can be used to scrape French expressions from www.linternaute.fr.


## Required Python Packages:

1. `urllib`
2. `bs4` (BeautifulSoup)
3. `re`
5. `string`

## Quick Explanation:

There are three principal functions in this code:

1. `scrape_site()`
2. `scrape_letter()`
3. `scrape_page()`

Each of them will return a list of French expressions scraped from the site.

`scrape_site()` takes no arguments and will scrape the entirety of the site.

`scrape_letter()` takes one letter as an argument (e.g., 'a', 'k', 'x', etc.) and scrapes every French expression that begins with that letter.

`scrape_page()` takes two arguments: a letter and a positive integer (e.g., 1, 3, 101, etc.). The letter and the integer correspond to a page on the website (e.g., scrape_page('q', 2) would scrape all of the expressions found on [this page](https://www.linternaute.fr/expression/recherche/q/2/)).
