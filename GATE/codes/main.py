import random

def toss_three_coins():
    # Simulate tossing three unbiased coins
    outcomes = ['H', 'T']  # 'H' for heads, 'T' for tails
    return [random.choice(outcomes) for _ in range(3)]

num_trials = 100000  # You can adjust the number of trials

outcomes = [toss_three_coins() for _ in range(num_trials)]

count_all_tails = sum(1 for outcome in outcomes if outcome.count('T') == 3)
count_at_least_two_tails = sum(1 for outcome in outcomes if outcome.count('T') >= 2)

probability = count_all_tails / count_at_least_two_tails

print(f"Simulated Probability: {probability:.4f}")
print(f"Theoretical Probability: 1/4 = 0.25")

import random

def toss_three_coins():
    # Simulate tossing three unbiased coins
    outcomes = ['H', 'T']  # 'H' for heads, 'T' for tails
    result = [random.choice(outcomes) for _ in range(3)]
    return result

def experiment(num_trials):
    count_all_tails = 0
    count_at_least_two_tails = 0

    for _ in range(num_trials):
        outcome = toss_three_coins()
        if outcome.count('T') == 3:
            count_all_tails += 1
        if outcome.count('T') >= 2:
            count_at_least_two_tails += 1

    probability = count_all_tails / count_at_least_two_tails

    return probability

num_trials = 100000  # You can adjust the number of trials
probability = experiment(num_trials)

print(f"Simulated Probability: {probability:.4f}")
print(f"Theoretical Probability: 1/4 = 0.25")
