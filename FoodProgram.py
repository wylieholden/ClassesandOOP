import FoodClass as fc

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

# customer 1
customerid = 570
name = "Danni Sellyar"
address = "97 Mitchell Way Hewitt Texas 76712"
email = "dsellyarft@gmpg.org"
phone = "254-555-9362"
member_status = False
customer = fc.Customer(customerid, name, address, email, phone, member_status)

# # customer2
# customerid = 569
# name = "Aubree Himsworth"
# address = "1172 Moulton Hill Waco Texas 76710"
# email = "ahimsworthfs@list-manage.com"
# phone = "254-555-2273"
# member_status = True
# customer = fc.Customer(customerid, name, address, email, phone, member_status)

# transactions
transactions = []
for key in dict:
    date = dict[key][0]
    item_name = dict[key][1]
    cost = dict[key][2]
    customerid = dict[key][3]
    transaction = fc.Transaction(date, item_name, cost, customerid)
    transactions.append(transaction)

# Statement:
print("Customer Name:", customer.get_name())
print("Phone:", customer.get_phone())


order_total = 0
for trans in transactions:
    if trans.get_customerid() == customer.get_customerid():
        print(f"Order Item: {trans.get_item_name()}  Price: ${trans.get_cost():.2f}")


for trans in transactions:
    if trans.get_customerid() == customer.get_customerid():
        order_total += trans.get_cost()
print(f"Total Cost: ${order_total:.2f}")


if customer.get_member_status() == True:
    print(f"Member Discount: ${(order_total * 0.2):.2f}")
    print(f"Total Cost after discount: ${(order_total * 0.8):.2f}")
