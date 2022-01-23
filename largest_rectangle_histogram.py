"""
Given an array heights that contains the height of each bar in the histogram, and we are asked to return the area of the largest rectangle in the histogram. Note that eachbar has a width of 1.
"""
def largest_rectangle(heights):
    max_area=0
    for i in range(len(heights)):
        left=i
        while left-1 >= 0 and heights[left-1] >= heights[i]:
            left-=1
        right=i
        while right+1 < len(heights) and heights[right+1] >= heights[i]:
            right+=1
        max_area = max(max_area, heights[i]*(right-left+1))
    return  max_area

def rec(heights, low, high):
    if low > high:
        return 0
    elif low == high:
        return heights[low]
    else:
        minh=min(heights[low:high+1])
        pos_min=heights.index(minh,low,high+1)
        from_left=rec(heights, low,pos_min-1)
        from_right=rec(heights,pos_min+1,high)
        return max(from_left, from_right, minh*(high-low+1))

def largest_rectangle2(heights):
    return rec(heights, 0, len(heights)-1)

def largest_rectangle3(heights):
    heights = [-1]+heights+[-1]
    from_left = from_right = [0]*len(heights)
    stack = [0]
    for i in range(1, len(heights)-1):
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_left[i] = stack[-1]
        stack.append(i)
    stack = [len(heights)-1]
    for i in range(1, len(heights)-1)[::-1]:
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_right[i]=stack[-1]
        stack.append(i)
    max_area=0
    for i in range(1, len(heights)-1):
        max_area=max(max_area, heights[i]*(from_right[i]-from_left[i]-1))
    return max_area