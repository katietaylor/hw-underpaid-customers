melon_cost = 1.00


def find_underpaid_customers(customer_data_file):
    """This function opens a file with customer data.
    Checks to see if customer has overpaid or underrpaid
    """

    customer_data = open(customer_data_file)  # open file

    # iterate over each line and split into list
    for line in customer_data:
        customer_tokens = line.split("|")

        # assign values in list to a variable
        customer_name = customer_tokens[1]
        customer_first = customer_name.split(" ")[0]
        customer_melons = float(customer_tokens[2])
        customer_paid = float(customer_tokens[3])

        # calculate amount customer should have paid
        customer_expected = customer_melons * melon_cost

        #check if customer underpaid
        if customer_expected > customer_paid:
            print customer_first + " has underrpaid - Paid: %s, Expected %s" % (customer_paid, customer_expected)

        # check if customer overpaid
        elif customer_expected < customer_paid:
            print customer_first + " has overpaid - Paid: %s, Expected %s" % (customer_paid, customer_expected)


#call the function
find_underpaid_customers("customer-orders.txt")
