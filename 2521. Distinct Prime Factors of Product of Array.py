class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # Create a set to store the distinct prime factors
        prime_factors = set()
        
        # Iterate through each element in the array
        for num in nums:
            # Get the prime factors of the current element
            current_prime_factors = self.get_prime_factors(num)
            # Add the prime factors to the set
            prime_factors.update(current_prime_factors)
        
        # Return the size of the set, which is the number of distinct prime factors
        return len(prime_factors)
    
    def get_prime_factors(self, num: int) -> set:
        # Create a set to store the prime factors
        prime_factors = set()
        
        # Keep dividing the number by 2 until it is odd
        while num % 2 == 0:
            prime_factors.add(2)
            num /= 2
        
        # Check for other prime factors from 3 to sqrt(num)
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            # Keep dividing the number by i until it is not divisible by i
            while num % i == 0:
                prime_factors.add(i)
                num /= i
        
        # If the number is greater than 2, it is a prime number itself
        if num > 2:
            prime_factors.add(num)
        
        return prime_factors
        