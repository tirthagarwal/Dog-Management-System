dogs = {
    "buddy": {
        "breed": "Golden Retriever",
        "age": 3,
        "owner": "Rahul"
    },
    "max": {
        "breed": "German Shepherd",
        "age": 5,
        "owner": "Amit"
    },
    "rocky": {
        "breed": "Labrador",
        "age": 2,
        "owner": "Priya"
    }
}

print("🐕 DOG MANAGEMENT SYSTEM")
print("Available dogs: Buddy, Max, Rocky")

name = input("\nEnter dog's name: ").strip().lower()

if name in dogs:
    dog = dogs[name]

    print("\n--- DOG DETAILS ---")
    print("Name:", name.title())
    print("Breed:", dog["breed"])
    print("Age:", dog["age"], "years")
    print("Owner:", dog["owner"])
else:
    print("\nDog not found in the system.")

