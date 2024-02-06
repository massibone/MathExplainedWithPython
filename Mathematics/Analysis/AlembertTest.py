# Python program to demonstrate the d'Alembert's ratio test
def dAlembertTest(arr, n):
    # Find the limit of the ratio of successive terms
    lim = arr[n] / arr[n - 1]
    if lim < 1:
        return "The series is convergent"
    elif lim > 1:
        return "The series is divergent"
    else:
        return "The test is inconclusive"

# Example usage
arr = [2, 4, 8, 16, 32]
n = len(arr) - 1
result = dAlembertTest(arr, n)
print(result)
