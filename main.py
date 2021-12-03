from numpy import random
import numpy as np
import matplotlib.pyplot as plt


def sim_toss(size=1):
    """
    :return: np.array of length size, with
     0 if head
     1 if cross
    """
    return random.randint(0, 2, size=size)


def get_payoff(sequence_length):
    """
    :param sequence_length: represents the number of consecutive tosses without 'cross'
    :return: the total payoff considering the formula 2^n-1 where n is the length of the sequence
    """
    if sequence_length == 0:
        return 0
    return 2 ** (sequence_length - 1)


def plot_simulation(all_payoffs, label=''):
    all_avgs = []
    for i in range(1, len(all_payoffs)+1):
        all_avgs.append(np.average(all_payoffs[-i:]))
    plt.plot(range(1, len(all_payoffs)+1), all_avgs, label=label)
    plt.grid(True)
    plt.xlabel("n")
    plt.ylabel("Average Payoff")
    plt.legend()
    plt.title("Average Payoff over the last n games as a function of n")


def exercise_one():
    max_payout = 1e7
    max_rounds = int(np.log2(max_payout) + 1)
    N_GAMES = int(1e4)
    N_SIMS = 5
    for id_sim in range(N_SIMS):
        all_games_payoff = []
        for _ in range(N_GAMES):
            seq_length = 0
            for _ in range(max_rounds):
                if sim_toss() == 1:
                    seq_length += 1
                else:
                    all_games_payoff.append(get_payoff(seq_length))
                    break
        plot_simulation(all_games_payoff, label=f"Sim: {id_sim}")
    plt.savefig("sim.png")


def exercise_two(n_days):
    laambda = 300
    visitors_per_day = []
    for day in range(n_days):
        n_visitors = np.round(random.poisson(lam=laambda))
        visitors_per_day.append(n_visitors)
    plt.bar(range(n_days), visitors_per_day, alpha=.5)
    plt.grid(True)
    plt.xlabel("Day")
    plt.ylabel("n visitors")
    plt.title("Number of visitors per day")
    plt.show()
    n_visitors = np.round(random.poisson(lam=laambda, size=100000))
    plt.hist(n_visitors, alpha=.5)
    plt.title("Distribution of Number of Visitors")
    plt.xlabel("n visitors")
    plt.ylabel("occurrences")
    plt.grid(True)
    breakpoint()


if __name__=='__main__':
    exercise_two(14)