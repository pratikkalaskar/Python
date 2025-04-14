ingredients = {
    "milk": 500,
    "water": 300,
    "tea_leaves": 80,
    "coffee_powder": 100,
    "sugar": 200,
    "honey": 50
}

# Selling prices for beverages
prices = {"tea": 15, "coffee": 20}

# Cost per unit of each ingredient
ingredient_costs = {
    "milk": 2,
    "water": 0.5,
    "tea_leaves": 1.5,
    "coffee_powder": 3,
    "sugar": 0.5,
    "honey": 4
}

# Store order history for billing
orders = []

def check_availability(required):
    """Check if all required ingredients are available."""
    for ingredient, qty in required.items():
        if ingredients[ingredient] < qty:
            print(f"Not enough {ingredient}. Please refill.")
            return False
    return True

def deduct_ingredients(required):
    """Deduct used ingredients from stock."""
    for ingredient, qty in required.items():
        ingredients[ingredient] -= qty

def calculate_cost(required):
    """Calculate the total cost of ingredients used."""
    cost = sum(ingredient_costs[ingredient] * qty for ingredient, qty in required.items())
    return cost

def serve_beverage():
    """Serve tea or coffee based on user input."""
    print("\nSelect Beverage:")
    print("1. Tea")
    print("2. Coffee")
    beverage_choice = input("Enter choice: ")

    if beverage_choice == "1":
        beverage_type = "tea"
        print("\nFor Tea, select:")
        print("1. Light Tea")
        print("2. Strong Tea")
        strength = "light" if input("Enter choice: ") == "1" else "strong"
        
        print("\nSweetener:")
        print("1. Without Sugar")
        print("2. With Sugar")
        print("3. Honey")
        sweetener_choice = input("Enter choice: ")
        sweetener = "none" if sweetener_choice == "1" else "sugar" if sweetener_choice == "2" else "honey"

        base = {"milk": 20, "water": 30, "tea_leaves": 10}
        if strength == "strong":
            base["tea_leaves"] *= 2
        
    elif beverage_choice == "2":
        beverage_type = "coffee"
        print("\nFor Coffee, select:")
        print("1. Light Coffee")
        print("2. Strong Coffee")
        strength = "light" if input("Enter choice: ") == "1" else "strong"

        print("\nSweetener:")
        print("1. Without Sugar")
        print("2. With Sugar")
        sweetener_choice = input("Enter choice: ")
        sweetener = "none" if sweetener_choice == "1" else "sugar"

        base = {"milk": 30, "water": 20, "coffee_powder": 10}
        if strength == "strong":
            base["coffee_powder"] *= 2
        
    else:
        print("Invalid choice!")
        return

    # Add sweetener
    if sweetener == "sugar":
        base["sugar"] = 5
    elif sweetener == "honey":
        base["honey"] = 5

    # Check availability and serve if possible
    if check_availability(base):
        deduct_ingredients(base)
        cost = calculate_cost(base)
        profit = prices[beverage_type] - cost
        orders.append({"beverage": beverage_type, "strength": strength, "sweetener": sweetener, "price": prices[beverage_type], "cost": cost, "profit": profit})
        print(f"\n{strength.capitalize()} {beverage_type.capitalize()} with {sweetener} served!")
        print(f"Cost: ₹{cost:.2f}, Profit: ₹{profit:.2f}")
    else:
        print(f"Cannot serve {beverage_type.capitalize()}.")

def refill_ingredients():
    """Refill ingredients as per user input."""
    print("\nEnter refill quantities (or 0 to skip):")
    for ingredient in ingredients:
        refill_qty = int(input(f"{ingredient.capitalize()}: "))
        ingredients[ingredient] += refill_qty
    print("Ingredients refilled successfully.")

def display_bill():
    """Display bill details with total cost and profit."""
    if not orders:
        print("\nNo beverages served yet.")
        return

    print("\nTotal Beverages Served:")
    total_cost = total_profit = 0
    for order in orders:
        print(f"{order['strength'].capitalize()} {order['beverage'].capitalize()} ({order['sweetener']}): ₹{order['price']}")
        total_cost += order['cost']
        total_profit += order['profit']
    
    print(f"\nTotal Cost: ₹{total_cost:.2f}")
    print(f"Profit: ₹{total_profit:.2f}")

def main():
    """Main function to display the vending machine menu."""
    while True:
        print("\nVending Machine Menu:")
        print("1. Serve Beverage")
        print("2. Refill Containers")
        print("3. Bill")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            serve_beverage()
        elif choice == "2":
            refill_ingredients()
        elif choice == "3":
            display_bill()
        elif choice == "4":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()







# # CREATING A VENDING MACHINE

# # fiirst I have created a dictionary to store the capacity of ingredients
# ingredients = {
#     "milk":400,
#     "sugar":200,
#     "coffee powder":200,
#     "tea leaves":200,
#     "water":500,
#     "honey":200,
# } 

# ingredient_prices = {
#     "milk":400,
#     "sugar":200,
#     "coffee powder":200,
#     "tea leaves":200,
#     "water":500,
#     "honey":200,
# }

# def check_availability():
#     for ingredient,qty in ingredients.items():
#         if ingredients[ingredient]<qty:
#             print(f"Not Enough {ingredient}. Refill ingredient")
#             return False
#         return True
# def deduct_ingredients():
#     for ingredient,qty in ingredients.items():
#         ingredients[ingredient] -=qty

# def refill_ingredients():
#     for ingredient,qty in ingredients.items():
#         if ingredient < qty:
#             return f"Refill the {ingredient} in machine."  
        