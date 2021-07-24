def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        d={}
        for i in range(n):
            for j in range(m):
                if i+j not in d:
                    d[i+j]=[mat[i][j]]
                else:
                    d[i+j].extend([mat[i][j]])
        res =[]    
        print(d)
        for ele in d.items():
            if ele[0] % 2 != 0:
                res.extend(ele[1])
            else:
                res.extend(ele[1][::-1])
        return res
