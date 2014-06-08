import csv, datetime, urllib

#User defined variables
ticker = 'T'
print ticker
data_file = 'http://ichart.finance.yahoo.com/table.csv?s='+ticker+'&d=5&e=6&f=2014&g=d&a=0&b=2&c=1980&ignore=.csv'
investment_period = 30.44
investment_count = 60
investment_amount = 3213
investment_target = 192782

#derived variables
adjusted_investment_count = investment_count - 1 #not buying more on the final sale day
investments = range(adjusted_investment_count)

def convert_date_string_to_date(date):
	year, month, day = map(int, date.split('-'))
	return datetime.date(year, month, day)

def add_days_to_date(change):
	return datetime.timedelta(days=change)

def find_closest_trading_date(date):
	if date in historical_dates:
		return date
	elif date + datetime.timedelta(days=1) in historical_dates:
		return date + datetime.timedelta(days=1)
	elif date + datetime.timedelta(days=2) in historical_dates:
		return date + datetime.timedelta(days=2)
	elif date + datetime.timedelta(days=-1) in historical_dates:
		return date + datetime.timedelta(days=-1)
	elif date + datetime.timedelta(days=-2) in historical_dates:
		return date + datetime.timedelta(days=-2)
	elif date > datetime.date(2001,9,10) and date < datetime.date(2001,9,17):
		return datetime.date(2001,9,17)
	else:
		raise Exception("DateNotFound", date)
	#### this function needs testing
	#print find_closest_trading_date(min_trading_date + datetime.timedelta(days=3))

def run_simulation(date):
	shares_held = 0
	for investment in investments:
		trade_date = find_closest_trading_date(date + datetime.timedelta(days=investment * investment_period))
		share_price = int(historical_data[trade_date].replace('.',''))
		#using integer math for accuracy
		share_purchase_quantity = investment_amount * 10000/share_price * 100
		shares_held += share_purchase_quantity

	final_sell_date = find_closest_trading_date(date + datetime.timedelta(days=investment_period*investment_count))
	final_sell_price = int(historical_data[final_sell_date].replace('.',''))
	final_shares_value = final_sell_price * shares_held / 10000
	#showing a final investment that returns 0% on the final day
	final_price = final_shares_value + investment_amount * 100

	return [date, final_sell_date, final_sell_price/100.0, final_shares_value/100.0, final_price/100.0, final_price/100.0 - investment_target]
	
historical_data = {}
f = urllib.urlopen(data_file)
reader = csv.DictReader(f)
for row in reader:
	trading_date = convert_date_string_to_date(row['Date'])
	historical_data[trading_date] = row['Open']

historical_dates = list(historical_data.keys())

max_trading_date = max(historical_dates)
min_trading_date = min(historical_dates)
historical_dates.sort()
last_sim_start_date = find_closest_trading_date(max_trading_date - datetime.timedelta(days=investment_period * investment_count))

simulation = []
for day in historical_dates:
	if day > last_sim_start_date: break
	simulation.append(run_simulation(day))

print len(simulation)
	
with open('sim_'+ticker+'_URL.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(simulation)
