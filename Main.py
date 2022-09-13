from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  l=len(array)
  for i in range(1,l-1):
    item=array[i]
    curitem=i-1
    while ((array[curitem]>item) and (curitem>-1)):
      array[curitem+1]=array[curitem]
      curitem=curitem-1

    #for j in range(l):
  return array  
      

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
