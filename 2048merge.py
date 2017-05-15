# Accelerated Computer Science @ BDFZ Spring 2017
# Assignment: 2048 Merge
# By Zhang Zhifei

def merge(list_a):
    
    new_list=[]
    final_list=[]   
    k=0 

    
    for num in list_a:
        if num!=0:
            new_list.append(num)
             
    while k < len(new_list)-1:
        if new_list[k]!=new_list[k+1]:
            final_list.append(new_list[k])
            k+=1
        else:
            final_list.append(2*new_list[k])
            k+=2
    else:
        final_list.append(new_list[k])
    
    
    while len(final_list)<len(list_a):
        final_list.append(0)
            
    return final_list

a=[8,16,16,8]

print (merge(a))
