

def order_total(orders):

    tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

    orders = open("orders-by-type.txt")


    for order in orders:
        # these lines have an id, melontype, and melon count
        # we need to split this and to get type and melon count
        data = order.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        tallies[melon_type] = tallies[melon_type] + melon_count

    orders.close()
    return tallies

def revenue_total(tallies):

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0

    print('TOTAL REVENUE')

    for melon_type in tallies:
        price = melon_prices[melon_type]
        melon_revenue = price * tallies[melon_type]
        total_revenue = total_revenue + melon_revenue
         # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
        print(f"We sold {tallies[melon_type]:,} {melon_type} melons at {price:.2f} each for a total of {melon_revenue:.2f}")
    return total_revenue


def sales_comparison (sales):

    sales = open('orders-with-sales.txt')
    online_rev = 0
    sales_rev = 0


    for sale in sales:
        # we know the third line gives sales credit we will fine that and apply credit accordingly
        data = sale.split("|")
        if data[2] == "ONLINE":
            online_rev = online_rev + float(data[3])
        else:
            sales_rev = sales_rev + float(data[3])

    print("Sale Data")
    print(f"Salespeople generated ${sales_rev:,.2f} in revenue.")
    print(f"Internet sales generated ${online_rev:,.2f} in revenue.")

    if sales_rev > online_rev:
        print("Guess there's some value to those salespeople after all.")
    else:
        print("Time to fire the sales team! Online sales rule all!")

    sales.close()

# Get Melon tallies
melon_tallies = order_total('orders-by-type.txt')

# print revenue
revenue_total(melon_tallies)

print()

# print sales report

sales_comparison('orders-with-sales.txt')

print()

