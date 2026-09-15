def ordinary_annuity(p, cf, r, start, end): #p is the principal amount, cf is the cash flow in the respective year, r is the interest rate
    yearly_balances = []
    all_years = list(range(start, end+1))
    for year in all_years:
        balance = p*(1+r)**year + cf*(((1+r)**(year-1))/r)
        yearly_balances.append(balance)
    return yearly_balances
