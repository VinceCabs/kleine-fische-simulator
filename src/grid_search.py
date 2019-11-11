import src.kleine_fische as kf
import itertools
import numpy as np
import matplotlib.pyplot as plt

games_simul_num = 10000
max_board_size = 13


def main():
    grid_search()
    plot_results()


def grid_search():
    # we compute fish and fishermen probability to win depending on board size and fish first position
    board_sizes = range(1, max_board_size + 1)
    fish_positions = range(1, max_board_size + 1)
    fish_proba = np.zeros((max_board_size, max_board_size))
    fishermen_proba = np.zeros((max_board_size, max_board_size))

    for (board, fish) in itertools.product(board_sizes, fish_positions):
        if board >= fish:
            print("computing {0}:{1}".format(board, fish))
            s = kf.Stats()
            for _ in range(games_simul_num):
                p = kf.Partie(board, fish)
                p.play_game(s)
            fish_proba[board - 1][fish - 1] = s.get_proba_fish()
            fishermen_proba[board - 1][fish - 1] = s.get_proba_fishermen()
        else:
            pass

    # saving results on files (.NPY for future plotting, .CSV to import somewhere else)
    np.save("./artefacts/fish", fish_proba)
    np.save("./artefacts/fishermen", fishermen_proba)

    np.savetxt("./artefacts/fish.csv", fish_proba, delimiter=";")
    np.savetxt("./artefacts/fishermen.csv", fishermen_proba, delimiter=";")


def plot_results():

    # loading results from grid search
    fish = np.load("./artefacts/fish.npy")
    fishermen = np.load("./artefacts/fishermen.npy")

    # probab. delta between fish and fishermen (we look for near 0 delta)
    delta = fish - fishermen

    # printing to have nice figures
    np.set_printoptions(precision=2, suppress=True)
    print("fish: \n", fish)
    print("delta: \n", delta)

    # graphical display
    # TODO : better display : https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py
    fig = plt.figure()
    fig.add_subplot(1, 2, 1).title.set_text("fish win probability")
    fig.add_subplot(1, 2, 1)

    plt.imshow(fish)
    fig.add_subplot(1, 2, 2).title.set_text("delta (fish vs fishermen)")
    plt.imshow(delta)
    plt.show()
    plt.legend()


if __name__ == "__main__":
    main()
