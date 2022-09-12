from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  l=len(array)
  for i in range(1,l-1):
    if array[i]<array[i-1]:
      temp=array[i-1]
      array[i-1]=array[i]
      array[i]=temp
      
    #for j in range(l):
      
      

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
