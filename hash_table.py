stock_prices = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])
stock_prices
[['march 6', 310.0],
 ['march 7', 340.0],
 ['march 8', 380.0],
 ['march 9', 302.0],
 ['march 10', 297.0],
 ['march 11', 323.0]]
stock_prices[0]