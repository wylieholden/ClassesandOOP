import FoodClass as fc

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}
order_total = 0


# customer obejct 1
customerid = "570"
name = "Danni Sellyar"
address = "97 Mitchell Way Hewitt Texas 76712"
email = "dsellyarft@gmpg.org"
phone = "254-555-9362"
member_status = "False"
customer = fc.Customer(customerid, name, address, email, phone, member_status)

# transaction 1
date = "2/15/2023"
item_name = "The Lone Patty"
cost = "16"
cusomterid = 569
transaction1 = fc.Transaction(date, item_name, cost, customerid)
