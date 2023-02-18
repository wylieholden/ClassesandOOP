# Customer Class - that has the following attributes - customerid, name, address, email, phone, member_status (True or False).
# The Customer class’s __init__ method should accept an argument for each attribute.
# The Customer class should have accessor methods only for each attribute.

# Transaction Class - that has the following attributes - date, item name,cost and customerid.
# The Procedure class’s __init__ method should accept an argument for each attribute.
# The Transaction class should have accessor methods only for each attribute.


class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.__customerid = customerid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_member_status(self):
        return self.__member_status


class Transaction:
    def __init__(self, date, item_name, cost, customerid):
        self.__date = date
        self.__item_name = item_name
        self.__cost = cost
        self.__customerid = customerid

    # def trans_statement(self):
    # for key in dict:
    # if dict[key][3] == self.__customerid:
    # print(f"Order Item: {dict[key][1]} Price: {dict[key][2]}")

    # def calc_cost(self):
    # self.__cost = 0
    # for key in dict:
    # if dict[key][4] == self.__customerid:
    # self.__cost = +dict[key][3]

    # def get_cost(self):
    # return self.__cost
