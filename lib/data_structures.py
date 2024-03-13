spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5] 

def print_spicy_foods(spicy_foods):
    for spicy_foods_dict in spicy_foods:
        peppers = spicy_foods_dict ['heat_level'] * "🌶"
        print(f"{spicy_foods_dict['name']} ({spicy_foods_dict['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food ["cuisine"] == cuisine:
            return food
    # return [cuisine for cuisine in spicy_foods_dict["cuisine"] for 

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total = 0
    for spicy_foods_dict in spicy_foods:
        total += spicy_foods_dict['heat_level']
    return total / len(spicy_foods)



def create_spicy_food(spicy_foods, spicy_food):
    # spicy_food =  {
    #     'name': 'Griot',
    #     'cuisine': 'Haitian',
    #     'heat_level': 10,
    # }
    spicy_foods.append(spicy_food)
    return spicy_foods

#testing only below / not included in  assignment 
spicy_jerry = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
 }
print(create_spicy_food(spicy_foods, spicy_jerry))




