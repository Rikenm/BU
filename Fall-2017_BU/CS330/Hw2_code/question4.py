# Riken Maharjan
# CAS CS 330
# BU ID: U67259975
# Prof. Dora Erdos




import sys

def question4(n):
   "return the minimum weighted sum of our scheduling"
   # to run the code in terminal type:                       
   #                                                          $python question4.py 200 1 300 4
   #
   # where 200 is a weight for 1 and 300 is a weight for 4
   # note: The number of arguments must be even.
   #input should be w t w t w t w t format
   # hence n = [w,t,w,t,w,t....]
   
   assert (len(n)%2 == 0) # creates error if the input length is not even. for example $question4.py 200 1 300 creates error as there is no time duration for 300 weight. 
   
   fsum = 0     # for the summation of the final return value
   memotization_of_t = 0   # we have to keep on adding t as time increases
   
   
   t_ratio = [((n[i]*1.0)/(n[i+1]),n[i],n[i+1]) for i in range(len(n)-1) if i%2 == 0] # list comphresion that returns a tuplets of format (w[i]/t[i],w[i],t[i])   #O(n)
   
   t_ratio.sort()   # sort the above returned t_ratio list by the first element which is w/t   # O n(logn)
   
   for i in range(len(t_ratio)):   # iterating our t_ratio for the final summation      O (n/2) = O(n)
       
       fsum+= t_ratio[i][1]*(memotization_of_t+t_ratio[i][2])  # S + = w[i] * (t_old _ t[i]) # constant time
       memotization_of_t += t_ratio[i][2]                      # updating our t_old = t_old + t[i] # constant time
   return fsum    #the minimum weighted sum is returned
  
# the running time would be the sorting time. O n(log n)

if __name__=="__main__":
     results = [int(i) for i in sys.argv[1:]]   # for the argument
     print(question4(results))

    
         
