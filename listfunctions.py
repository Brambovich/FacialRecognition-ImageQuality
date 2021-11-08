def average(lst): 
    return sum(lst) / len(lst) 

def sumlist(lists,no_res,no_faces):
    
    summedlist = list()
    for i in range(no_res):
        
        
        summedlist.append(sum(lists[::no_res])/no_faces)
        del lists[:1]

    return summedlist