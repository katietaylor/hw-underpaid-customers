melon_cost = 1.00


def find_underpaid_customers(customer_data_file):
    customer_data = open(customer_data_file)
    for line in customer_data:
        customer_tokens = line.split("|")

        customer_name = customer_tokens[1]
        customer_first = customer_name.split(" ")[0]
        customer_melons = float(customer_tokens[2])
        customer_paid = float(customer_tokens[3])
        customer_expected = customer_melons * melon_cost

        if customer_expected > customer_paid:
            print customer_first + " has underrpaid - Paid: %s, Expected %s" % (customer_paid, customer_expected)
        elif customer_expected < customer_paid:
            print customer_first + " has overpaid - Paid: %s, Expected %s" % (customer_paid, customer_expected)



find_underpaid_customers("customer-orders.txt")
