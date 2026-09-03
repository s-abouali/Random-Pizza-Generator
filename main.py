import random

sauce = [
    "Tomato sauce",
    "BBQ sauce",
    "Pesto",
    "Garlic sauce",
    "Spicy tomato sauce",
    "Alfredo sauce"
]

cheese = [
    "Mozzarella",
    "Cheddar",
    "Parmesan",
    "Gouda",
    "Feta",
    "Four cheese"
]

meat = [
    "Pepperoni",
    "Chicken",
    "Beef",
    "Sausage",
    "Ham",
    "Bacon",
    "Tuna",
    "No meat"
]

vegetables = [
    "Mushrooms",
    "Onions",
    "Bell peppers",
    "Olives",
    "Jalapeños",
    "Tomatoes",
    "Spinach",
    "Corn"
]

extra = [
    "Pineapple",
    "Garlic",
    "Extra cheese",
    "Caramelized onions",
    "Chili flakes",
    "Fresh basil",
    "Pickles",
    "Nothing extra"
]

crust = [
    "Classic crust",
    "Thin crust",
    "Thick crust",
    "Garlic crust",
    "Cheese-stuffed crust",
    "Pretzel crust"
]

seasoning = [
    "Oregano",
    "Basil",
    "Chili flakes",
    "Garlic powder",
    "Italian herbs",
    "No seasoning"
]

print("🍕 YOUR RANDOM PIZZA 🍕")
print("======================")

print("🍅 Sauce:", random.choice(sauce))
print("🧀 Cheese:", random.choice(cheese))
print("🥩 Meat:", random.choice(meat))
print("🥬 Vegetable:", random.choice(vegetables))
print("✨ Extra:", random.choice(extra))
print("🥖 Crust:", random.choice(crust))
print("🌿 Seasoning:", random.choice(seasoning))
