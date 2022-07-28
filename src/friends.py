from concurrent.futures.process import _sendback_result


def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    likes = False
    favouritesnacks = person["favourites"]["snacks"]
    for snack in favouritesnacks:
        if food == snack:
            likes = True
    return likes
    # return person["favourites"]["snacks"]

def add_friend(person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, removed_friend):
    person["friends"].remove(removed_friend)

def total_money(people):
    total_money = 0
    for person in people:
        cash = person["monies"]
        total_money += cash
    return total_money

def lend_money(person1, person2, loan):
    person1["monies"] -= loan
    person2["monies"] += loan

def all_favourite_foods(people):
    favourite_foods = []
    for person in people:
        foods = person["favourites"]["snacks"]
        favourite_foods += foods
    return favourite_foods

def find_no_friends(people):
    no_friend = []
    for person in people:
        if len(person["friends"])==0:
            no_friend+=[person]
    return no_friend

# create master list
# loop through people and add fave show
# def favourite_tv_inc_duplicates(people):
#     favourite_shows = []
#     for person in people:
#         favourite_shows += person["favourites"]["tv_show"]

def unique_favourite_tv_shows(people):
    nonunique_list=[]
    unique_list=[]
    for person in people:
        show = person["favourites"]["tv_show"]
        nonunique_list += show
    in_list = False
    for list_show in nonunique_list:
        if show == list_show:
            in_list = True
    if in_list == False:
        unique_list += show
    return unique_list

            
    

            

    

