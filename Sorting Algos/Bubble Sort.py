def bubble_sort(l1):
    print("Before Sorting ", l1)
    for i in range(len(l1) - 1):
        for j in range(len(l1) - 1):
            if l1[j] > l1[j + 1]:
                l1[j] = l1[j] + l1[j + 1]
                l1[j + 1] = l1[j] - l1[j + 1]
                l1[j] = l1[j] - l1[j + 1]

    print("after Sorting", l1)


l = [77, 44, 788, 29, 4, 5, 55]
bubble_sort(l)
