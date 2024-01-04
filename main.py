from random import choice

# Importez les données du fichier data_game.py
from data_game import data

def compare_followers(person1, person2):
    """Compare le nombre de followers de deux personnalités."""
    return person1['follower_count'] > person2['follower_count']

def display_personality_info(person):
    """Affiche les informations d'une personnalité."""
    print(f"Nom: {person['name']}")
    print(f"Description: {person['description']}")
    print(f"Pays: {person['country']}")

def game():
    score = 0
    game_over = False
    weakest_personality = None

    while not game_over:
        # Sélectionnez une personnalité au hasard pour person1
        if weakest_personality is None:
            person1 = choice(data)
        else:
            person1 = weakest_personality

        # Sélectionnez une personnalité différente pour person2
        person2 = choice(data)
        while person2 == person1:
            person2 = choice(data)

        print("\nComparez les informations des deux personnalités:")
        print("Personnalité A:")
        display_personality_info(person1)
        print("\nPersonnalité B:")
        display_personality_info(person2)

        user_choice = input("Qui a plus de followers ? 'A' ou 'B': ").lower()

        if user_choice == 'a':
            if compare_followers(person1, person2):
                score += 1
                print("Correct ! Vous avez gagné un point.")
                weakest_personality = person2
            else:
                game_over = True
                print(f"Désolé, incorrect. Votre score final est de {score} points.")
        elif user_choice == 'b':
            if compare_followers(person2, person1):
                score += 1
                print("Correct ! Vous avez gagné un point.")
                weakest_personality = person1
            else:
                game_over = True
                print(f"Désolé, incorrect. Votre score final est de {score} points.")
        else:
            print("Choix invalide. Veuillez entrer 'A' ou 'B'.")

if __name__ == "__main__":
    game()
