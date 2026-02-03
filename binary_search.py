def binarysearch(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==key:
            return mid
        elif key<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return-1
a=[10,20,30,40,50,60,70,80,90,100]
k=int(input("Enter the key element to be searched: "))
r=binarysearch(a,k)
if r==-1:
    print("Sorry, key is not present in the array.")
else:
    print("Search successful. key found at location: ",r+1)
