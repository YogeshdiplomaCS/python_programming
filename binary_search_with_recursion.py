def binarysearch(a,low,high,key):
    if low<=high:
        mid=(low+high)//2
        if a[mid]==key:
            print("Search successful key found at location : ",mid)
            return
        elif key<a[mid]:
            binarysearch(a,low,mid-1,key)
        else:
            binarysearch(a,mid+1,high,key)
    else:
        print("Key not found")
a=[10,20,30,40,50,60,70,80,90,100]
print("the array elements are:",a)
key=int(input("Enter the key element to be searched: "))
binarysearch(a,0,len(a)-1,key)
