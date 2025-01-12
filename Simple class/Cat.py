class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def find_the_oldest(self, lst):
        return max(lst, key=lambda x: x.age)

        


cat1 = Cat('Whiskers', 3)
cat2 = Cat('Fluffy', 5)
cat3 = Cat('Mittens', 2)
lst_of_cats = [cat1, cat2, cat3]
print(f"The oldest cat is {cat1.find_the_oldest(lst_of_cats).name} years old.")
