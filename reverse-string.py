#define a function reversestring
def reversestring(x):
    #assigning a new variable to the empty string 
    x2 = "" 
    #using range with step 1 on reverse direction
    for i in range(len(x)-1,-1,-1):
        #interating the loop using i value
        x2 += x[i]
        #print new string value 
    print(x2)
reversestring("abhinav")

