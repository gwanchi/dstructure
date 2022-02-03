"""
Given values and weights of n items, we want to put them in a knapsack in a way to have the greatest possible value but without exceeding the maxWeight, so you are asked to create a function that returns that greatest possbile value.
"""
def knapsack(values, weights, maxWeight, i = 0):
    if i == len(values):
        return 0
    elif weights[i] > maxWeight:
        return knapsack(values, weights, maxWeight, i+1)
    else:
        return max(values[i] + knapsack(values, weights, maxWeight-weights[i], i+1))

def knapsack2(values, weights, maxWeight, i = 0, memoiz={}):
    key = str(i) + " " + str(maxWeight)
    if memoiz.get(key) is not None:
        return memoiz[key]
    elif weights[i] > maxWeight:
        output = knapsack2(values, weights, maxWeight, i+1)
        memoiz[key] = output
        return output
    else:
        output = max(values[i] + knapsack2(values, weights, maxWeight-weights[i], i+1), knapsack2(values, weights, maxWeight, i+1))
        memoiz[key] = output
        return output