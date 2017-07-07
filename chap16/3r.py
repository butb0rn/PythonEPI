def find2Sum(arr, target):
    leftIdx = 0
    rightIdx = len(arr)-1
    result = []
    while leftIdx < rightIdx:
        number = arr[leftIdx]+arr[rightIdx]
        if number == target:
          result += [arr[leftIdx], arr[rightIdx]],
          leftIdx += 1
        elif number > target:
          rightIdx -= 1
        else:
          leftIdx += 1
    return result


def findKSum(arr, target, k):
  result = []
  if k == 2:
    result = find2Sum(arr, target)
  else:
    for i in range(len(arr)):
      newtarget = target - arr[i]
      partialRes = findKSum(arr[i+1:], newtarget,k - 1)
      result += map(lambda p: [arr[i]]+p,partialRes)

  return result





arr = [1,2,3,6,7,8,9]
print findKSum(arr, 15, 4)
