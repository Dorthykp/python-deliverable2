print("Welcome to the GC Fruit Market!")
name = "Grant Chirpus"
print("What is your name?")
print(f">{name}\n")
fruit_prices = {"Apple": 2, "Grape": 1, "Orange": 3}
fruit_count = {"Apple": 0, "Grape": 0, "Orange": 0}
print(f"Welcome {name}. Which fruit would you like to buy?")
for i, (fruit, price) in enumerate(fruit_prices.items(), 1):
    print(f"{i}. {fruit} ${price}")
inputs = (["1", "y", "2", "n"])
input_index = 0
while True:
    choice = inputs[input_index]
    print(f">{choice}")
    input_index += 1
    if choice == "1":
        fruit = "Apple"
    elif choice == "2":
        fruit = "Orange"
    elif choice == "3":
        fruit = "Grape"
    else:
        print("Invalid choice, please select again.")
        continue
    fruit_count[fruit] += 1
    print(f"You bought 1 {fruit.lower()} at ${fruit_prices[fruit]}")
    another = inputs[input_index]
    print(f"Would you like to buy another piece of fruit? y/n\n> {another}")
    input_index += 1
    if another == "n":
        break
    print(f"\nWelcome {name}. Which fruit would you like to buy?")
    for i, (fruit, price) in enumerate(fruit_prices.items(), 1):
        print(f"{i}. {fruit} ${price}")
print(f"\nOrder for {name}")
for fruit, count in fruit_count.items():
    print(f"{count} {fruit.lower()}(s) at ${fruit_prices[fruit]} apiece")
subtotal = sum(fruit_count[fruit] * price for fruit, price in fruit_prices.items())
tax = subtotal * 0.05
total = subtotal + tax
print(f"Sub Total: ${subtotal}")
print(f"5% Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
