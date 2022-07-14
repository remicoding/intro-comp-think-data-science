########################
# Remi Coding
# Problem Set 1
# Introduction to Computational Thinking and Data Science
# MITOPENCOURSEWARE

#================================
# Part B: Golden Eggs
#================================

# Problem 1

def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    # base case for no solution found
    min_num_eggs = float("inf")

    # base case for solution found
    if target_weight == 0:
        return 0
    # base case for solution already found and memo
    elif target_weight in memo:
        return memo[target_weight]
    elif target_weight > 0:
        # iteratively pick each weights
        for weight in egg_weights:
            # recursively pick eggs until target weight is reached
            sub_result = dp_make_weight(egg_weights, target_weight - weight)
            # keep track of minimum number of eggs taken to reach target weight
            min_num_eggs = min(min_num_eggs, sub_result)
    # memo the number of eggs taken to reach the target weight
    memo[target_weight] = min_num_eggs + 1
    return min_num_eggs + 1


# EXAMPLE TESTING CODE, feel free to add more if you'd like
def main():
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()


if __name__ == '__main__':
    main()