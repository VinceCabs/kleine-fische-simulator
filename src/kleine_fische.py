# -*-coding:utf8;-*-
# TODO plot # of turns distribution
# TODO DocStrings

import random

# Param: Number of games to simulate
games_simul_num = 10000


def main():
    s = Stats()
    for _ in range(games_simul_num):
        p = Partie()
        p.play_game(s)
    s.print_won_games()


class Partie:
    def __init__(self, board_size: int = 11, fish_position: int = 6):
        self.board_size = board_size
        self.fish_position = fish_position
        self.turn = 0
        self.slice = 0
        self.fishermen = {"red", "green"}
        self.fish = {
            "blue": fish_position,
            "rose": fish_position,
            "orange": fish_position,
            "yellow": fish_position,
        }

        self.sea = []
        self.boat = []

    def roll_dice(self) -> str:
        """rolls dice, returns a color

        Returns : 
            color (str): color shown on dice
        """

        colors = list(self.fishermen) + list(self.fish.keys())
        color = random.choice(colors)
        return color

    def move_fish(self, color: str):
        """the fish of the color set in the parameter goes forward

        If it reaches sea, it goes to the 'sea' list
        If it is already in sea, another fish goes forward (other function call)
        If it is in the boat fishermen goes forward

        Parameters :
            color (str): color of the fish to go forward

        Returns : 
            null
        """

        self.turn += 1
        if color in self.sea:
            # self.move_fish_rand()
            self.move_fish_opt()
        elif color in self.boat:
            self.move_fishermen()
        else:
            pos = self.fish[color]
            if pos < self.board_size:
                self.fish[color] = pos + 1
            else:
                self.sea.append(color)
                self.fish.pop(color)

    def move_fish_rand(self):
        # fait avancer un poisson de manière aléatoire
        fish = random.choice(list(self.fish))
        self.move_fish(fish)

    def move_fish_opt(self):
        # fait avancer le poisson le plus avancé (=le plus proche de la mer)
        max = 0
        for fish in list(self.fish.keys()):
            if self.fish[fish] > max:
                fish_max = fish

        self.move_fish(fish_max)

    def print_game(self):
        print(
            "{0}:     fishes:{1}    fishermen:{2}    sea:{3}     boat:{4}".format(
                self.turn, self.fish, self.slice, self.sea, self.boat
            )
        )

    def is_game_ended(self, stats: 'Stats') -> bool:
        if len(self.sea) > 2:
            # Fishes win!
            stats.won_turns_fish.append(self.turn)
            return True
        elif len(self.boat) > 2:
            # Fishermen win!
            stats.won_turns_fishermen.append(self.turn)
            return True
        elif len(self.boat) == 2 and len(self.sea) == 2:
            # Draw!
            stats.draw_turns.append(self.turn)
            return True
        else:
            return False

    def move_fishermen(self):
        self.turn += 1
        self.slice += 1
        # les poissons peches sont mis dans le bateau
        for fish in list(self.fish.keys()):
            if self.fish[fish] == self.slice:
                self.boat.append(fish)
                del self.fish[fish]

    def play_turn(self):
        c = self.roll_dice()
        if c in ["green", "red"]:
            self.move_fishermen()
        else:
            self.move_fish(c)

    def play_game(self, stats: 'Stats'):
        while True:
            self.play_turn()
            if self.is_game_ended(stats):
                break


class Stats:
    def __init__(self):
        self.won_turns_fish = []
        self.won_turns_fishermen = []
        self.draw_turns = []

    def print_won_games(self):

        wins_fish = len(self.won_turns_fish)
        wins_fishermen = len(self.won_turns_fishermen)
        draws = len(self.draw_turns)
        print(
            "Fishes win: {0}    Fishermen win: {1}  Draws: {2}    Fishes/Fishermen chances: {3:.1f}%/{4:.1f}%".format(
                wins_fish,
                wins_fishermen,
                draws,
                100 * wins_fish / (wins_fish + wins_fishermen + draws),
                100 * wins_fishermen / (wins_fish + wins_fishermen + draws),
            )
        )

    def print_avg_turns(self):
        wins_fish = len(self.won_turns_fish)
        wins_fishermen = len(self.won_turns_fishermen)
        draws = len(self.draw_turns)
        try:
            print(
                "avg turns number: {0:.1f}    (fishes win): {1:.1f}  (fishermen win): {2:.1f} (draw): {3:.1f}".format(
                    (sum(self.won_turns_fish) + sum(self.won_turns_fishermen))
                    / (wins_fish + wins_fishermen),
                    sum(self.won_turns_fish) / wins_fish,
                    sum(self.won_turns_fishermen) / wins_fishermen,
                    sum(self.draw_turns) / draws,
                )
            )
        except ZeroDivisionError:
            pass


if __name__ == "__main__":
    main()
