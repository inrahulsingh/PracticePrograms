#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spygames(nums):
    code=[0,0,7,'x']

    for num in nums:
        if num==code[0]:
            code.pop(0)

    return len(code)==1

result=spygames([1,0,2,4,0,5,7])
print(result)
