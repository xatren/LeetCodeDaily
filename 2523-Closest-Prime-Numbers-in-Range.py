class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            prime_numbers = []
            for p in range(2, n + 1):
                if is_prime[p]:
                    prime_numbers.append(p)
            return prime_numbers

        def is_prime(n, primes):
            if n <= 1:
                return False
            for p in primes:
                if p * p > n:
                    break
                if n % p == 0:
                    return False
            return True

        # Manually calculating the integer square root of 'right'
        upper_limit = int(math.sqrt(right)) + 1
        primes_up_to_sqrt = sieve_of_eratosthenes(upper_limit)
        
        primes_in_range = []
        for num in range(left, right + 1):
            if is_prime(num, primes_up_to_sqrt):
                primes_in_range.append(num)
        
        if len(primes_in_range) < 2:
            return [-1, -1]

        min_diff = float('inf')
        closest_pair = [-1, -1]

        for i in range(len(primes_in_range) - 1):
            diff = primes_in_range[i + 1] - primes_in_range[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes_in_range[i], primes_in_range[i + 1]]

        return closest_pair