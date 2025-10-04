class Lion:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
#yyy
class Tiger:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
#j
class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
#ff
class Keeper:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
class Caretaker:
    def __init__(self,name,age,salary):
        self.name = name 
        self.age = age
        self.salary = salary
    def __repr__(self):
        return f"Name:{self.name}, Age:{self.age}, Salary{self.salary}"
class Vet:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Zoo:
    def __init__(self, name: str, budget: float, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy."

    def tend_animals(self):
        total_cost = sum(a.get_needs() for a in self.animals)
        if self.__budget >= total_cost:
            self.__budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = [f"You have {len(self.animals)} animals"]
        result.append(f"----- {len(lions)} Lions:")
        result.extend([repr(l) for l in lions])
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend([repr(t) for t in tigers])
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend([repr(c) for c in cheetahs])
        return "\n".join(result)

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result = [f"You have {len(self.workers)} workers"]
        result.append(f"----- {len(keepers)} Keepers:")
        result.extend([repr(k) for k in keepers])
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend([repr(c) for c in caretakers])
        result.append(f"----- {len(vets)} Vets:")
        result.extend([repr(v) for v in vets])
        return "\n".join(result)
zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [
    Cheetah("Cheeta", "Male", 2),
    Cheetah("Cheetia", "Female", 1),
    Lion("Simba", "Male", 4),
    Tiger("Zuba", "Male", 3),
    Tiger("Tigeria", "Female", 1),
    Lion("Nala", "Female", 4)
]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [
    Keeper("John", 26, 100),
    Keeper("Adam", 29, 80),
    Keeper("Anna", 31, 95),
    Caretaker("Bill", 21, 68),
    Caretaker("Marie", 32, 105),
    Caretaker("Stacy", 35, 140),
    Vet("Peter", 40, 300),
    Vet("Kasey", 37, 280),
    Vet("Sam", 29, 220)
]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Firing a worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
