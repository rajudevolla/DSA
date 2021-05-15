rot = int(input())
strinput = input()
clues=strinput[1:len(strinput)-1].split("#")
mat=[]
rowStartIndex=0;
columnStartIndex=0
rowEndIndex=len(clues)
columnEndIndex=0
for clue in clues:
    mat.append(list(clue))
    columnEndIndex=len(clue)
i=0
print(columnEndIndex,rowEndIndex)
layers=[]
while(rowStartIndex<rowEndIndex and columnStartIndex<columnEndIndex):
    ring=[]
    for i in range(columnStartIndex,columnEndIndex):
        ring.append(mat[rowStartIndex][i])
        rowStartIndex+=1
    for i in range(rowStartIndex,rowEndIndex):
        ring.append(mat[i][columnEndIndex-1])
        columnEndIndex=columnEndIndex-1
    if(rowStartIndex<rowEndIndex):
        for i in range(columnEndIndex-1,columnStartIndex-1,-1):
            ring.append(mat[rowEndIndex-1][i])
            rowEndIndex=rowEndIndex-1
    if(columnStartIndex<columnEndIndex):
        for i in range(rowEndIndex-1,rowStartIndex-1,-1):
            # print(matrix[i][columnStartIndex])
            ring.append(mat[i][columnStartIndex])
            columnStartIndex+=1
    layers.append(ring)
print(layers)
for layer in layers:
    if(len(layer)>rot):
        layer[:]=layer[rot:]+layer[:rot]
        ans=ans+layer.join('')
print(ans)