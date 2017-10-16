#Riken Maharjan

import copy as cp
import argparse
import sys

def zerosum(x):
    '''exhaustive process: going each '''
    assert (len(x)>0)
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                if x[i]+x[j]+x[k] == 0:
                    return (x[i],x[j],x[k])
    return (0)             
                    



def binary_search(list_1, x):
    min = 0
    max = len(list_1) - 1
    while True:
        if max < min:
            return -1
        mid = (min + max) // 2
        if list_1[mid] < x:
            min = mid + 1
        elif list_1[mid] > x:
            max = mid - 1
        else:
            return mid


def zerosum_sort(x):
    '''exhaustive process: going each '''
    #assert (len(x)>0)
    list_1 = cp.deepcopy(x)
    dict_x = {x[index]: index for index in range(0,len(x))}
    list_1.sort()

    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if list_1[i] != -(list_1[i]+list_1[j]) and list_1[j] != -(list_1[i]+list_1[j]):
                k = binary_search(list_1,-(list_1[i]+list_1[j]))
                if k != -1:
                    return (dict_x[list_1[i]],dict_x[list_1[j]],dict_x[-(list_1[i]+list_1[j])])
    return ("No")             
                    
def zerosum_fast(x):
    dict_x = {x[index]: index for index in range(0,len(x))}
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
           if x[i] != -(x[i]+x[j])  and x[j] != -(x[i]+x[j]): 
            if -(x[i]+x[j]) in dict_x:
                return(i,j,dict_x[x[i]+x[j]])
    return ("No") 
    

if __name__=="__main__":
     zerosum(sys.argv[1:])
     zerosum_sort(sys.argv[1:])
     zerosum_fast(sys.argv[1:])
     
     
           
            
                
