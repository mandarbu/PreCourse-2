# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)>1:
    left_arr=arr[:len(arr)//2]
    right_arr=arr[len(arr)//2:]
    mergeSort(left_arr)
    mergeSort(right_arr)
    i=0
    j=0
    k=0
    while i<len(left_arr) and j<len(right_arr):
      if left_arr[i]<right_arr[j]:
        arr[k]=left_arr[i]
        i+=1
      else:
        arr[k]=right_arr[j]
        j+=1
        k+=1
    while i<len(left_arr):
      arr[k]=left_arr[i]
      i+=1
      k+=1

    while j < len(right_arr):
      arr[k]=right_arr[j]
      j+=1
      k+=1


  
  #write your code here
  
# Code to print the list 



  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
