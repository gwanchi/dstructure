"""
Qn.
You are driving along a straight long road with gas stations placed at equal distances from each other. Each gas station has a separate price for fuelling up your car.

You can either drive 1 or 2 gas stations forward from the previous one. You have to refill your fuel tank every 2nd station. You start with a full tank, so you can choose if you want to stop at index [0] or index [1]

For input, you are given an array, prices[}, containing the cost of gas at each station. Your job is to plan the most efficient order to visit the gas stations to reach the end of the road and calculate the price of that route. You can assume no costs are negative.

Return the minimum price for reaching the end of the road.

Algorithm:
1.
 """
def lowestSum(prices):
    # Write your solution here
    stack = []
    localSum = 0
    for p in prices:
        stack.append(p)


print(lowestSum([5,20,3,2,20,1,1,20])) # 12 (optimal route = [0] -> [2] -> [3] -> [5] -> [6] -> Finish) [5, 20, 3, 2, 20, 1, 1, 20]
print(lowestSum([10,15,20,5])) # 20 (optimal route = [1] -> [3] -> Finish) [10, 15, 20, 5]
