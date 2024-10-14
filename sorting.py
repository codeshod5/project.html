# bubble selection insertion sort 

def selectionsort(listt):
    # Iterate over the entire list
    for i in range(len(listt)):
        # Assume the current element is the minimum
        min_index = i
        # Iterate over the unsorted part of the list
        for j in range(i + 1, len(listt)):
            # Find the index of the minimum element
            if listt[min_index] > listt[j]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        listt[i], listt[min_index] = listt[min_index], listt[i]

def bubblesort(listt):
    for i in range(len(listt)):
        for j in range(0,len(listt)-1):
            if listt[j]>listt[j+1]:
                listt[j],listt[j+1] = listt[j+1],listt[j]
                print(listt)
        print(f"pass {i} done")

def insertionsort(listt):
    for i in range(0,len(listt)):
        temp = listt[i]
        j = i-1
        while(j>=0 and listt[j]>temp):
            listt[j+1] = listt[j]
            j-=1
        listt[j+1] = temp

# listt = [42, 75, 8, 9, 4]

def quicksort(listt,low ,high):
    if(low<high):
        l = low+1
        r = high
        pivot = low
        while(l<r):

         while(listt[l]<listt[pivot]):
            l+=1
         while(listt[r]>listt[pivot]):
            r-=1
         if l<r:
            listt[l],listt[r] = listt[r],listt[l]

        listt[pivot],listt[r] = listt[r],listt[pivot]
        quicksort(listt,0,r-1)
        quicksort(listt,r+1,high)


def binarysearch(listt,low,high,se):
     mid = (high+low)//2



     if listt[mid]==se:
        return mid
     elif listt[mid]<se:
         return binarysearch(listt,mid+1,high,se)
     elif listt[mid]>se:
         return binarysearch(listt,low,mid-1,se)
     else:
         return -1


listt = [42, 75, 8, 9, 4,7]
listt.sort()
print(listt)

# selectionsort(listt)
# quicksort(listt,0 ,len(listt)-1)

res = binarysearch(listt,0,5,7)

print(res)


