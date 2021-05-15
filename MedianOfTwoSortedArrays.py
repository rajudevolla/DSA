#User function Template for python3

class Solution:
    
    #Function to find the median of the two arrays when they get merged.
    def findMedianSortedArrays(self,arr1, n, arr2, n2):
       
        i=j=k=0
        arr3=[0]*(n+n2)
        while(i<n and j<n2):
            if(arr1[i]<arr2[j]):
                arr3[k]=arr1[i]
                i=i+1
            elif(arr1[i]>arr2[j]):
                arr3[k]=arr2[j]
                j=j+1
            else:
                arr3[k]=arr2[j]
                k=k+1
                arr3[k]=arr1[i]
                j=j+1
                i=i+1
            k=k+1
        while(i<n):
            arr3[k]=arr1[i]
            i=i+1
            k=k+1
        while(j<n2):
            arr3[k]=arr2[j]
            k=k+1
            j=j+1
        # print(arr3)
        median=int((n+n2)/2)
        if(len(arr3)%2==0):
            return int((arr3[median]+arr3[median-1])/2)
        return arr3[median]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n1,n2=list(map(int,(input().split())))
        arr1=list(map(int,(input().split())))
        arr2=list(map(int,(input().split())))
        
        if n1<n2:
            print(Solution().findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(Solution().findMedianSortedArrays(arr2,n2, arr1,n1))
# } Driver Code Ends