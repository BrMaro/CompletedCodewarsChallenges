from itertools import groupby

def score(dice):
    score_dictionary = {
        1: 1000,
        6: 600,
        5: 500,
        4: 400,
        3: 300,
        2: 200,
    }
    single_scores = {
        1: 100,
        5: 50
    }

    total_score = 0
    dice_copy = sorted(dice)

    for key, group in groupby(dice_copy):
        group_list = list(group)
        count = len(group_list)
        if count >= 3:
            total_score += score_dictionary[key]
            count -= 3
        if key in single_scores:
            total_score += single_scores[key] * count

    return total_score

# Example usage
print(score([5, 1, 3, 4, 1, 1]))  # Should output the correct score based on the dice rolled
