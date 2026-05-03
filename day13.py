class Parent:
    a = 100
    b = 45

    def add(self):
        return self.a + self.b
    
class Child(Parent):
    c = "Hari Sharma"
    d = 10

    def display(self):
        return self.add()
    

obj = Child()
print (obj.a) #100
print (obj.b) # 45
# print (obj.display()) #145



# class TestParent():
#     def __init__(self):
#         print("I am from Test Parent")

# class TestChild(TestParent):

#     def __init__(self):
#         print("I am from TestChild")
#         TestParent.__init__(self)
#         super().__init__()

# obj= TestChild()


class TestParent():
    def __init__(self,a):
        print("I am from Test Parent")

class TestChild(TestParent):

    def __init__(self,a,b,c,d):
        print("I am from TestChild")
        self.b = b
        TestParent.__init__(self,a)
        super().__init__(a)

    def test(self,amount):
        return self.b
    
class Child(TestChild):
    pass

obj= Child(1,2,3,4)




#TEst


class Account():
    # account_number = input("Enter your account number: ")
    # balance = float(input("Enter your balance: "))


    def deposit(self, amount):
        self.balance += amount
        return f"Your new balance is: {self.balance}"
    
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Your new balance is: {self.balance}"
        
class SavingsAccount(Account):
    interest_rate = 0.05

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        return f"Your interest is: {interest}"
    
class PremiumSavingsAccount(SavingsAccount):
    reward_points = 0
    def redeem_points(self):
        if self.reward_points >= 100:
            self.balance += 50
            self.reward_points -= 100
            return "You have redeemed your points for a reward!"
        else:
            return "You do not have enough reward points to redeem."    
        
acc = PremiumSavingsAccount()
acc.account_number = "123456789"
acc.balance = 1000.0
acc.reward_points = 150 
print("account number:", acc.account_number)
print("balance:", acc.balance)
print("reward points:", acc.reward_points)
print(acc.deposit(500.0))
print(acc.withdraw(200.0))
print(acc.redeem_points())
print(acc.calculate_interest())
print("balance after redeeming points:", acc.balance)