import random
import requests


def create_list_of_pokemon_numbers(computer_pokemon):
    """
    creates a list of 3 unique random pokemon and ensures the list doesn't contain the same pokemon as computer
    :param computer_pokemon: - random integer used to choose computers pokemon
    :return: - a dictionary of 3 pokemon's name, id, height and weight
    """
    your_pokemon = []
    number_of_pokemon = 0
    while number_of_pokemon < 3:
        pokemon_number = random.randint(1, 151)
        if pokemon_number in your_pokemon:
            continue
        else:
            your_pokemon.append(pokemon_number)
            number_of_pokemon = number_of_pokemon + 1
    return your_pokemon


def random_pokemon(pokemon_number):
    """
    creates a dict of pokemon from the pokemon API
    :param pokemon_number: a random integer
    :return: a dict of pokemon from API
    """
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


if __name__ == "__main__":

    # count the score up to 5
    player_score = 0
    computer_score = 0
    while player_score or computer_score < 5:

        print(f'The score is: You {player_score}, Computer {computer_score}')

        # create the computer's pokemon
        computer_pokemon = random_pokemon(random.randint(1, 151))

        pokemon_numbers = create_list_of_pokemon_numbers(computer_pokemon)

        pokemon_dict = {}
        for pokemon_number in pokemon_numbers:
            pokemon = random_pokemon(pokemon_number)
            pokemon_dict[pokemon['name']] = {
                "id": pokemon['id'],
                "height": pokemon['height'],
                "weight": pokemon['weight']
            }
        # user selects from 3 pokemon
        print("Select your pokemon:")
        for pokemon in pokemon_dict:
            print(f"Name: {pokemon}, ID: {pokemon_dict[pokemon]['id']}, Height: {pokemon_dict[pokemon]['height']}, Weight: {pokemon_dict[pokemon]['weight']}")

        #  user inputs their choice with data validation
        chosen_pokemon = input('Your choice: ')
        chosen_pokemon = chosen_pokemon.lower()
        try:
            pokemon_dict[chosen_pokemon]
        except:
            input('Please choose one of above options ')
            continue

        print(f'Your opponent chose {computer_pokemon["name"]}')

        # user chooses their stat
        stat_choice = input('Which stat do you choose? ID, height, or weight: ')
        stat_choice = stat_choice.lower()

        # used hardcoding to check comparisons work
        # stat_choice = 'height'

        # converts stats to integers so they can be compared
        my_stat = pokemon_dict[chosen_pokemon][stat_choice]
        my_stat = int(my_stat)
        opponent_stat = computer_pokemon[stat_choice]
        opponent_stat = int(opponent_stat)

        print(f"Your stats: Name: {pokemon}, ID: {pokemon_dict[pokemon]['id']}, Height: {pokemon_dict[pokemon]['height']}, Weight: {pokemon_dict[pokemon]['weight']}")
        print(f"Your opponent's stats: Name: {computer_pokemon['name']}, ID: {pokemon_dict[pokemon]['id']}, Height: {computer_pokemon['height']}, Weight: {computer_pokemon['weight']}")

        # decision on the winner and adds to the score
        if my_stat > opponent_stat:
            player_score = player_score + 1
            print('You Win!')
        elif my_stat < opponent_stat:
            computer_score = computer_score + 1
            print('You Lose!')
        else:
            print('Draw!')

    # determines who the champion is
    if computer_score < player_score:
        print('Congratulations! You are the Champion!')
    elif computer_score == player_score:
        print("It's a tie!")
    else:
        print("Computer wins this time! Try again")


# if name == main