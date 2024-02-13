if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # converting the set to list and naming the list as arr1
    arr1 = list(set(arr))      # first to remove the duplicate values we use set function to the array
    arr1.sort()     # then sort the arr1 , so that we can find the runner up in the race
    print(arr1[-2])
