asset_costs = [122.5, 345.56, 367.8, 200.56, 1200.00, 100.2]

asset_costs.sort(reverse=True)
print("Top 3 priciest assets:")

for price in asset_costs[:3]:
    print(price)