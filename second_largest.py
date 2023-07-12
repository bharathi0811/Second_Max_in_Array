array=list(map(int,input().split()))
class SecondMaxCount:
    @staticmethod
    def second_largest(arr):
        max_element=0
        second_max=0
        array2=[]
    
        if len(arr)==1 or len(arr)==0:
            return -1
    
        for i in array:
            if i >=max_element:
                max_element=i
            else:
                array2.append(i)
    
        for j in array2:
        
            if j>=second_max:
                second_max=j
        count=0
        for k in arr:
            if k ==second_max:
                count+=1
            
        else:
            return count
obj=SecondMaxCount()
print(obj.second_largest(array))
