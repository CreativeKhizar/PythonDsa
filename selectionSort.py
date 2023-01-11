def selectionSort(array,size):
    for ind in range(size):
        mid_index=ind
        for j in range(ind+1,size):
            if array[j]<array[mid_index]:
                min_index=j

        array[ind],array[min_index]=array[min_index],array[ind]


size=int(input("Enter the size of the list: "))
arr=[int(input()) for i in range(size)]
selectionSort(arr,size)
print(arr)
