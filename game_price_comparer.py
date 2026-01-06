import os
import requests
import re
import sys


def main():

    type_of, name_of = get_input() # USE _OF FOR MINOR NAME CONFLICT PROBLEMS
    api = os.environ.get('API_KEY') # ENVIRONMENT VARIABLE
    site = get_url(type_of, name_of, api)
    req = request(site)
    confirm_req = confirm_request(req)
    confirm_results = confirm_result(confirm_req)
    correct_file = correct_game_dlc(confirm_results, type_of)
    print(correct_file[1])
    print(get_exact_price(get_price(correct_file[0])))

class Search:
    def __init__(self, type, name):
        self.name = name
        self.type = type


    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 0 or len(new_name) > 176:
            raise ValueError("Invalid name!")
        else:
            self._name = new_name

    @type.setter
    def type(self, new_type):
        new_type = new_type.lower().strip()
        if re.search(r"^(dlc$|^game)$", new_type, re.IGNORECASE):
            self._type = new_type
        else:
            raise ValueError("Invalid type!")


def get_input():
    know = Search(input("What is? (DLC) or (GAME): "), input("What's the game name? "))
    return know.type, know.name


def get_url(type_of, name_of, key):
    ### NEVER PUT THE API KEY IN THIS CODE, USE AN ENVIRONMENT VARIABLE FOR MORE SECURITY ###
    if len(name_of) <= 0 or len(type_of) <=0:
        sys.exit("Error. Please, Try again!")
    if len(type_of) > 4:
        sys.exit("Error. Please, Try again!")
    return f"https://api.isthereanydeal.com/games/search/v1?key={key}&id=018d937f&title={name_of}&type={type_of}"


def request(url):
    return requests.get(url)


def confirm_request(right_url):
    if right_url.status_code == 200:
        return right_url.json()
    else:
        return sys.exit("Something wrong happened :(") # THERE's 300+ STATUS CODE, THIS IS MORE SIMPLE!


def confirm_result(game_dlc):
    if type(game_dlc) == float or type(game_dlc) == int:
        return sys.exit("Error with the results. Please, Try again")
    else:
        if len(game_dlc) <= 0: # MAX OF 176 CHAR
            return sys.exit("No results :(")
        return game_dlc


def correct_game_dlc(game_image, typ):
    game_i = [] # LIST FOR THE "TRUE FILES" OF THE REQUEST
    type_list = [] # LIST FOR THE "TEMPORARY FILES" OF THE REQUEST

    ### IN CASE OF BE A GAME ###
       ### ACCESS THE REQUEST -> VIEW THE TYPE -> SAVE ONLY THE TITLE AND IMAGE -> SHOW TO THE USER ###
    if typ == "game":
        for this_dict in game_image:
            if this_dict['type'] == "game":
                type_list.append(this_dict)
            else:
                continue

        for item in type_list:
            game_i.append(item['id'])
            game_i.append(item['title'])


    ### IN CASE OF BE A DLC ###
    if typ == "dlc":
        for this_dict in game_image:
            if this_dict['type'] == "dlc":
                type_list.append(this_dict)
            else:
                continue

        for item in type_list:
            game_i.append(item['id'])
            game_i.append(item['title'])

    return game_i


### USE POST, NEVER GET
def get_price(gdi):
    url_prices = f"https://api.isthereanydeal.com/games/overview/v2?key={os.environ.get('API_KEY')}"
    body = [
        gdi
    ]
    prices = requests.post(url_prices, json=body)
    return prices.json()


### EXTRACT THE LOWEST PRICE WITH THE SHOP-GAME LINK
def get_exact_price(prices):
    price = prices["prices"][0]["current"]["price"]["amount"]
    shop = prices["prices"][0]["current"]["shop"]["name"]
    regular = prices["prices"][0]["current"]["regular"]["amount"]
    regular_price = f"Regular price: ${regular}"
    site_game = prices["prices"][0]["current"]["url"]
    if shop == "GameBillet":
        price_now = f"Price now: ${price} on {shop}"
    else:
        price_now = f"Price now: ${price} on {shop} ({site_game})"
    return f"{price_now}\n{regular_price}"


if __name__ == "__main__":
    main()