
def sum(str, *nums) :
    
    print("sum nums   " , id(str), "  :: ", id(nums))
    print(nums)
    


def li_sum(str, nums=[]) :
    str="dddd"
    print("lisum nums   " , id(str), "  :: ", id(nums))
    print(nums)
    
bb=(2,3,4,5)
cc=[2,3,4,5] 
str="aaaa"
print ( id(str), "  :: ", id(bb), " : " , id(cc) )
sum( str, bb)
sum( str, *bb)
li_sum (str, cc) 
print(str)

