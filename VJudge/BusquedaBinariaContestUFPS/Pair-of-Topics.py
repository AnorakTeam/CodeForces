def upper_bound(arr, target):
    n = len(arr)
    l = 0
    r = n - 1
    while l < r and l != n:
        mid = l + (r - l) // 2
        if target >= arr[mid]:
            l = mid + 1
        else:
            r = mid

    return l


def bin_search(arr, target):
    return lower_bound(arr, target) + 1


def lower_bound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans - 1

if __name__ == "__main__":
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    arr_a.sort()
    arr_b.sort()

    """The pair of topics i and j (i<j) is called 
    good if ai+aj>bi+bj (i.e. it is more interesting for the teacher).
    ai > bi + bk - aj
    """

    for i in range(n):
        
        pass

    print(arr_a, "\n", arr_b)
