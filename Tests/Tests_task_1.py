import pytest

from Task_1.work_1 import solution
from Task_1.work_2 import vote
from Task_1.work_3 import get_name, get_directory


@pytest.mark.parametrize(
    "a, b ,c ,expected",
    (
        [1, 8, 15, (-3.0, -5.0)],
        [1, -13, 12, (12.0, 1.0)],
        [-4, 28, -49, 3.5],
        [1, 1, 1, 'корней нет'],
        [0, 0, 0, 0]  # ошибка
    )
)
@pytest.mark.xfail
def test_solution_work_1(a, b, c, expected):
    assert solution(a, b, c) == expected


@pytest.mark.parametrize(
    "votes, expected",
    (
        [[1, 1, 1, 2, 3], 1],
        [[1, 2, 3, 2, 2], 2],
        [[1, 3, 3, 2, 2], 2],  # Maксимальное число голосов всегда уникально
        [[], '']  # ошибка
    )
)
@pytest.mark.xfail
def test_vote_work_2(votes, expected):
    assert vote(votes) == expected


@pytest.mark.parametrize(
    "doc_number, expected",
    (
        ["10006", "Аристарх Павлов"],
        ["", "Документ не найден"],
        ["g5kg5m", "Документ не найден"],
    )
)
@pytest.mark.xfail
def test_get_name_work_3(doc_number, expected):
    assert get_name(doc_number) == expected


@pytest.mark.parametrize(
    "doc_number, expected",
    (
        ["11-2", '1'],
        ["", "Полки с таким документом не найдено"],
        ["g5kg5m", "Полки с таким документом не найдено"],
    )
)
@pytest.mark.xfail
def test_get_directory_work_3(doc_number, expected):
    assert get_directory(doc_number) == expected
