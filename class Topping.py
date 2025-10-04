class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    
    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        if not value:
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = value

   
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value


class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    
    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value):
        if not value:
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = value

    
    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if not value:
            raise ValueError("The baking technique cannot be an empty string")
        self.__baking_technique = value
 

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}  

    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    
    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    
    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    
    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.toppings_capacity and topping.topping_type not in self.toppings:
            raise ValueError("Not enough space for another topping")

        
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    
    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())



if __name__ == "__main__":
    dough = Dough("Whole Wheat", "Crispy", 200)
    pizza = Pizza("Margarita", dough, 2)

    topping1 = Topping("Cheese", 50)
    topping2 = Topping("Tomato", 30)

    pizza.add_topping(topping1)
    pizza.add_topping(topping2)

    print(pizza.calculate_total_weight())  
Enter pizza name: Margarita
Enter flour type: Whole Wheat
Enter baking technique: Crispy
Enter dough weight: 200
Enter toppings capacity: 2
Add topping (type weight) or 'END' to stop: Cheese 50
Add topping (type weight) or 'END' to stop: Tomato 30
Add topping (type weight) or 'END' to stop: END

