import random

def remove_from_left(arr):
    left_part = 0
    value_left_part = arr[left_part]
    while arr[left_part]*2 < arr[-1]:
        left_part = bin_search(arr, value_left_part + 1)
        value_left_part = arr[left_part]
    return left_part


def remove_from_right(arr):
    right_part = len(arr) - 1
    value_right_part = arr[right_part]
    while arr[0]*2 < arr[right_part]:
        right_part = lower_bound(arr, value_right_part)
        value_right_part = arr[right_part]
    return len(arr) - 1 -right_part


def remove_from_both_sides(arr):
    l = 0
    r = len(arr) - 1
    diff = arr[r] - arr[l]
    while arr[l] * 2 < arr[r]:
        left_diff = arr[r] - arr[upper_bound(arr, arr[l])]
        right_diff = arr[lower_bound(arr, arr[r])] - arr[l]
        diff = right_diff - left_diff
        if diff > 0:
            l = upper_bound(arr, arr[l])
        elif diff < 0:
            r = lower_bound(arr, arr[r])
        else:
            l = upper_bound(arr, arr[l])
            r = lower_bound(arr, arr[r])

    return l + (len(arr) - 1 - r)


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

    """ n = int(input())
    data = list(map(int, input().split())) """

    data = [random.randint(4, 22) for _ in range(30)]

    data.sort()
    print(data)
    print(remove_from_left(data))
    print(remove_from_right(data))
    print(remove_from_both_sides(data))
    min_diff = min(remove_from_right(data), 
                remove_from_left(data), 
                remove_from_both_sides(data))
    print(min_diff)

