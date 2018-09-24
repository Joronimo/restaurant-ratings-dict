"""Restaurant rating lister."""


# put your code here
def restaurants_ratings_dict(file):
    """prints the restuarant and its ratings"""


    with open(file) as full_list:
        fl = full_list.readlines()

    dict_restaurants = {}

    for line in fl:
        line = line.rstrip()
        row = line.split(":")  # list of words in a line ( => list)
        dict_restaurants[row[0]] = row[1]

    new_restaurant = input("What's the restaurant name? ").title()
    new_rating = int(input("What's the rating? "))

    while new_rating > 5 or new_rating < 1:
        new_rating = int(input("Please enter a number between 1 and 5: "))

    dict_restaurants[new_restaurant] = new_rating


    for restaurant, rating in sorted(dict_restaurants.items()):
        print(f"{restaurant} is rated at {rating}")



restaurants_ratings_dict('scores.txt')
