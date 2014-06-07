past-performance-prediction
===========================

###Simulate past performance of periodic investments using Yahoo historical securities prices.

Past performance does not guarantee future results, but it's the best data set available.

The script uses CSV historical data provided by Yahoo. See an example at:

[http://ichart.finance.yahoo.com/table.csv?s=VWINX&d=5&e=6&f=2014&g=d&a=0&b=2&c=1980&ignore=.csv](http://ichart.finance.yahoo.com/table.csv?s=VWINX&d=5&e=6&f=2014&g=d&a=0&b=2&c=1980&ignore=.csv)

###Current behavior:

1. Investments are made with constant frequency
> If the frequency leads to trading on day when the market is closed, the closest day will be chosen by:
	1. Adding 1 day
	2. Adding 2 days
	3. Subtracting 1 day
	4. Subtracting 2 days
	5. Accounting for the September 11th, 2001 shutdown

2. Investments are made with a constant investment amount

3. Simulations are run for each date, starting with the earliest date available in the data until the farthest date available to include the full duration of a simulation

4. All shares are sold at the final date 

5. The sale date will include a single periodic investment that returns 0%
> For example, 3 investments made at a weekly interval would:
	1. Invest the constant amount on week 1
	2. Invest the constant amount on week 2
	3. Sell all shares owned on week 3 and then add the constant amount for week 3 to the proceeds
	
###TODO

* Support for dividends
* Retrieve the data directly from Yahoo's web service
* Support for trading cost accounting
* Support for mutal fund fee accounting: 12b-1, expense ratio, load
* Support for multiple securities
* Support for periodic rebalancing
