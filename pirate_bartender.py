import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def get_drink():
    preferences = {}
    response = False
    for question in questions:
        answer = input(questions[question] + ": Please type y for YES or n for NO, for each choice.")
        
        if answer == "y":
            response = True
        else:
            response = False
            
        preferences.update({question: response})
    return preferences

def make_drink(preferences):
    drink = []
    for preference in preferences:
        if preferences[preference] == True:
            drink.append(random.choice(ingredients[preference]))
    return drink
    
if __name__ == '__main__':
   preferences = get_drink()
   print(make_drink(preferences))
