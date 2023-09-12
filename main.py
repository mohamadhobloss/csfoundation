# # import unittest

# # # Write a Python program to get the largest number from a list.

# # l = [1, 5, 18, 1, 4, 55]
# # s = max(l)
# # print(s)

# # # Write a Python function that takes two lists and returns True if they have at least one common member.


# # def twolist(l1, l2):
# #     for i in l1:
# #         for x in l2:
# #             if i == x:
# #                 return True
# #             return False

# # # print(twolist([1, 2, 3], [1, 5, 8]))


# # # class TestSolution(unittest.TestCase):
# # #     def test_func(self):
# # #         self.assertEqual(twolist([6, 5, 3], [1, 8, 4]), True)


# # # if __name__ == '__main__':
# # #     unittest.main()


# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age

# # #     def fun(self):
# # #         print(f"hi my name is {self.name} and I am {self.age} years old")


# # # p1 = Person("Mohamad", 23)
# # # p2 = Person("Ahmad", 27)

# # # p1.fun()
# # # p2.fun()


# # def large(l):

# #     la = l(1)
# #     for i in l:
# #         if i > la:
# #             la = i
# #     return la


# # print(large([5, 4, 8, 9, 8, 88]))

# # 3rd session
# # def create_bank_account(account_number, balance=0):
# #     return {'account_number': account_number, 'balance': balance}


# # # my_account = (create_bank_account(13, 1000))
# # # print(my_account)
# # account1 = create_bank_account("92af", 1000)
# # account2 = create_bank_account("54ff", 500)


# # def transfer_money(sender, recipient, amount):
# #     if sender['balance'] < amount:
# #         raise ValueError("insufficient balance")

# #     sender['balance'] -= amount
# #     recipient["balance"] += amount

# # (transfer_money(account1, account2, 100))

# # def deposite (account,amount):
# #     return amount


# # class BankAccount:
# #     # abstraction
# #     def __init__(self, ownername, account_number, balance=0):  # constractor to create the class
# #         self.account_number = ownername
# #         self.account_number = account_number
# #         self.balance = balance  # properties

# # # instance or object

# #     def withdraw_money(self, amount):
# #         if self.balance < amount:
# #             raise ValueError('Insufficient funds')
# #         self.balance -= amount


# # account = BankAccount('mohamad', 123, 1000)

# # account.withdraw_money(700)


# class Book:
#     def __init__(self,title: str, author: str):
#         self.title = title
#         self.author = author
#         self.available = True

#     def borrow(self):
#         if self.available:
#             self.available = False
#         else: raise ValueError("not available")

#     def return_book(self):
#         if not self.available:
#             self.available=True
#         else:
#             raise ValueError()


# class Library:
#     def __init__(self,books=[]):
#         self.books=books

#     def add_book(self,book):
#         self.books(book)

#     def borrow_book(self,title):
#         for title in self.books:
#             if title== self.title:
#                 Book.borrow_book()

#     def return_book(self,title):
#         for title in self.books:

#             if self.available == False:
#                 Book.return_book()
#                 return


#     def available_book(self,list[]):
#         if self.available ==True:
#             list.append(self.book)


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if self.quantity < 0:
            raise ValueError()
        if self.price <= 0:
            raise ValueError()
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_details(self):
        self.name
        self.price
        self.quantity


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        for product in self.products:
            if product == product:
                self.cart.remove(product)
            else:
                raise ValueError()

    def view_cart(self):
        for product in self.cart:
            self.products.display_details()


class User:
    def __init__(self, username: str, email: str, products):
        super().__init__(products)
        self.username = username
        self.email = email

    def view_cart(self):
        ShoppingCart.view_cart()

    def checkout(self):
        order = Order(self.shopping_cart.products)
        order.display_order()
        self.shopping_cart.products = []


class Order:
    def __init__(self):
        order_list = []

    def display_order(self):
        for product in self.order_list:
            self.order_list.display()


class DiscountProduct:
    def __init__(self, name, price, quantity, discount_percentage: float):
        if discount_percentage < 0 or discount_percentage >= 100:
            raise ValueError()

        super().__init__(name, price, quantity)
        self.discount_percentage = discount_percentage

    def display_details(self):
        super().display_details()
