from src.functions import get_allocation, main
from os.path import exists, join
import pytest

players = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'f', 'i', 'j']


def test_get_allocation_unique():
    assert get_allocation(players, 3) != get_allocation(players, 3)


def test_get_allocation_games_count():
    assert get_allocation(players, 3).count('Game') == 3


def test_main_creates_folder():
    main(players=players, tournament_name='magistratik', game_count=2)
    assert exists('result')


def test_main_creates_file():
    main(players=players, tournament_name='magistratik', game_count=2)
    assert exists(join('result', 'allocation_magistratik.txt'))
