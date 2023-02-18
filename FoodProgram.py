import FoodClass as fc

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

# # customer 1
# customerid = 570
# name = "Danni Sellyar"
# address = "97 Mitchell Way Hewitt Texas 76712"
# email = "dsellyarft@gmpg.org"
# phone = "254-555-9362"
# member_status = False
# customer = fc.Customer(customerid, name, address, email, phone, member_status)

##customer 2
customerid = 569
name = "Aubree Himsworth"
address = "1172 Moulton Hill Waco Texas 76710"
email = "ahimsworthfs@list-manage.com"
phone = "254-555-2273"
member_status = True
customer = fc.Customer(customerid, name, address, email, phone, member_status)

# transactions
transaction1 = fc.Transaction("2/15/2023", "The Lone Patty", 17, 569)
transaction2 = fc.Transaction("2/15/2023", "The Octobreakfast", 18, 569)
transaction3 = fc.Transaction("2/15/2023", "The Octoveg", 16, 570)
transaction4 = fc.Transaction("2/15/2023", "The Octoburger", 20, 570)

# Statement
print("Customer Name:", customer.get_name())
print("Phone:", customer.get_phone())

order_total = 0
for key in dict:
    if dict[key][3] == customer.get_customerid():
        print(f"Order Item: {dict[key][1]}  Price: ${dict[key][2]:.2f}")

for key in dict:
    if dict[key][3] == customer.get_customerid():
        order_total += dict[key][2]
print(f"Total Cost: ${order_total:.2f}")

if customer.get_member_status() == True:
    print(f"Member Discount: ${(order_total * 0.2):.2f}")
    print(f"Total Cost after discount: ${(order_total * 0.8):.2f}")
