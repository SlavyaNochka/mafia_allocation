from random import shuffle
from os import path, mkdir

separator = "=" * 10


def get_allocation(players: list, game_count: int) -> str:
    allocation = ""
    for i in range(game_count):
        shuffle(players)
        allocation += f'{separator} Game {i + 1} {separator}\n'
        for j in range(len(players)):
            allocation += f'{j + 1}.\t{players[j]}\n'
        allocation += '\n'
    return allocation


def main(players: list, tournament_name: str, game_count: int):
    try:
        with open(path.join('result', f'allocation_{tournament_name}.txt'), 'w') as f:
            f.write(get_allocation(players, game_count))
    except FileNotFoundError:
        mkdir('result')
        main(players=players, tournament_name=tournament_name, game_count=game_count)
