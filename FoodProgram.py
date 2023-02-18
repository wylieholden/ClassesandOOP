import FoodClass as fc

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}
order_total = 0

# customer obejct 1
customerid = 570
name = "Danni Sellyar"
address = "97 Mitchell Way Hewitt Texas 76712"
email = "dsellyarft@gmpg.org"
phone = "254-555-9362"
member_status = True
customer = fc.Customer(customerid, name, address, email, phone, member_status)

# transaction 1
date = "2/15/2023"
item_name = "The Lone Patty"
cost = 16
customerid = 569
transaction1 = fc.Transaction(date, item_name, cost, customerid)

# Statement

print("Customer Name:", customer.get_name())
print("Phone:", customer.get_phone())

for key in dict:
    if dict[key][3] == customerid:
        print(f"Order Item: {dict[key][1]}   Price: ${dict[key][2]}")

for key in dict:
    if dict[key][3] == customerid:
        order_total += dict[key][2]
print("Total Cost:", order_total)

if customer.get_member_status() == True:
    print("Member Discount:", (order_total * 0.2))

print("Total Cost after discount:", (order_total * 0.8))
