class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


p1 = Person("XuanTruong", 19)
print(p1.get_name())  
print(p1.get_age())   
##
class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, emails):
        email = emails.partition("@")
        name = email[0]
        b = email[2].partition(".")
        mail = b[0]
        do = b[2]

        return self.__validate_name(name) == self.__validate_mail(mail) == self.__validate_domain(do)
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))    
print(email_validator.validate("georgios@gmail.net")) 
print(email_validator.validate("stamatito@abv.net"))  
print(email_validator.validate("abv@softuni.bg"))     

####
class Mammal:
    __kingdom = "animals"  

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"

mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
##
class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"
account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
    
