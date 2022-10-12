from functions import *

if __name__ == "__main__":
    players = []

    tournament_name: str = input('Tournament: ')
    game_count: int = int(input('Games count: '))

    for i in range(10):
        players.append(input(f'Player #{i + 1}: '))

    main(players=players, tournament_name=tournament_name, game_count=game_count)
