def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[i]:
            arr[j+1]=arr[j]
            j=j-1

        arr[j+1]=key

size=int(input("Enter the size of the list : "))
arr=[int(input()) for i in range(size)]

insertionSort(arr)

print("Sorted List is : ",arr)
