#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
         rowStartIndex=0;
         columnStartIndex=0
         rowEndIndex=r
         columnEndIndex=c
         i=0
         lstAns=[]
         while(rowStartIndex<rowEndIndex and columnStartIndex<columnEndIndex):
             
            # print first row values
            for i in range(columnStartIndex,columnEndIndex):
                #  print(matrix[rowStartIndex][i])
                 lstAns.append(matrix[rowStartIndex][i])
            rowStartIndex+=1
            
            # //print last column values
            
            for i in range(rowStartIndex,rowEndIndex):
                # print(matrix[i][columnEndIndex-1])
                lstAns.append(matrix[i][columnEndIndex-1])
            columnEndIndex=columnEndIndex-1
            
            # //print last row column values
            if(rowStartIndex<rowEndIndex):
                for i in range(columnEndIndex-1,columnStartIndex-1,-1):
                    # print(matrix[rowEndIndex-1][i])
                    lstAns.append(matrix[rowEndIndex-1][i])
                rowEndIndex=rowEndIndex-1
            
            # //print first column values
            if(columnStartIndex<columnEndIndex):
                for i in range(rowEndIndex-1,rowStartIndex-1,-1):
                    # print(matrix[i][columnStartIndex])
                    lstAns.append(matrix[i][columnStartIndex])
                columnStartIndex+=1
         return lstAns
                
        
                
            
                            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends