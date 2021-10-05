def interest(principal, years, rate):
    balance = principal
    for x in range(years):
        balance = balance + (rate*balance)
    print(balance)

    
interest(10000, 10, .02)