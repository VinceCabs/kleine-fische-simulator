import pytest
import src.kleine_fische as kf


def test_fish_goes_to_sea():
    # Fish goes to sea
    p = kf.Partie()
    for _ in range(p.board_size - p.fish_position + 1):
        p.move_fish("blue")
    assert "blue" in p.sea


def test_fish_moves():
    p = kf.Partie()
    p.move_fish("blue")
    assert p.fish["blue"] == p.fish_position + 1


def test_fishermen_move():
    p = kf.Partie()
    p.move_fishermen()
    assert p.slice == 1


def test_roll_dice():
    p = kf.Partie()
    for _ in range(36):
        color = p.roll_dice()
        assert (color in ["blue", "rose", "orange", "yellow"]) or (color in p.fishermen)


def test_fishermen_win():
    s = kf.Stats()
    p = kf.Partie()
    fish_nb = len(p.fish.keys())
    for _ in range(p.fish_position):
        p.move_fishermen()
    assert len(list(p.boat)) == fish_nb
    assert p.is_game_ended(s) == True
    assert s.won_turns_fishermen == [p.fish_position]


def test_draw_game():
    s = kf.Stats()
    p = kf.Partie()
    for _ in range(p.board_size - p.fish_position + 1):
        p.move_fish("blue")
        p.move_fish("yellow")
    for _ in range(p.fish_position):
        p.move_fishermen()
    assert (len(p.boat) == 2) and (len(p.sea) == 2)
    assert p.is_game_ended(s) == True
    assert s.draw_turns == [(p.board_size - p.fish_position + 1) * 2 + p.fish_position]


def test_fihes_win():
    s = kf.Stats()
    p = kf.Partie()
    for _ in range(p.board_size - p.fish_position + 1):
        p.move_fish("blue")
        p.move_fish("yellow")
        p.move_fish("orange")
    assert len(p.sea) == 3
    assert p.is_game_ended(s) == True
    assert s.won_turns_fish == [(p.board_size - p.fish_position + 1) * 3]


def test_play_turn():
    p = kf.Partie()
    p.play_turn()
    assert p.turn == 1
