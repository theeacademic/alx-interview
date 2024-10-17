#!/usr/bin/python3
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    # Determine the maximum value in nums to compute primes up to that limit.
    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)
    
    # Game results cache for each value of n
    game_results = {}

    def game_result(n):
        if n in game_results:
            return game_results[n]
        
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        turn = 0  # 0 for Maria, 1 for Ben
        available_numbers = set(range(1, n + 1))

        while primes:
            chosen_prime = primes[0]
            multiples = set(range(chosen_prime, n + 1, chosen_prime))
            available_numbers -= multiples

            primes = [p for p in primes if p in available_numbers]
            turn = 1 - turn

        game_results[n] = turn
        return turn

    maria_wins, ben_wins = 0, 0

    for n in nums:
        result = game_result(n)
        if result == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test the function with an example
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Expected output: "Ben"

