class Dog:
    def __init__(self, name, breed, age, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def display_details(self):
        print("\n--- DOG DETAILS ---")
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Age:", self.age, "years")
        print("Owner:", self.owner)