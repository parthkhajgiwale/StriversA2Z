class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        """
        Problem:
        Given values and weights of n items, and a knapsack capacity,
        find the maximum total value that can be put into the knapsack.
        
        You are allowed to take fractions of items.
        
        The final answer must be rounded to exactly 6 decimal places.
        """

        # Step 1: Create list of items as (value/weight, value, weight)
        items = []
        for i in range(len(val)):
            items.append((val[i] / wt[i], val[i], wt[i]))

        # Step 2: Sort items by value/weight ratio in descending order
        items.sort(reverse=True)

        total_value = 0.0
        remaining_capacity = cap

        # Step 3: Fill the knapsack greedily
        for ratio, value, weight in items:
            if remaining_capacity == 0:
                break

            if weight <= remaining_capacity:
                # Take the whole item
                total_value += value
                remaining_capacity -= weight
            else:
                # Take only the fraction that fits
                fraction = remaining_capacity / weight
                total_value += value * fraction
                remaining_capacity = 0

        # Step 4: Return value rounded to 6 decimal places
        return round(total_value, 6)
