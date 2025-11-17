nums = [1,2,3]
tupls = (1,2)


## An Object is iterable if it has the thunder method __iter__


# Creates Iterator
#i_nums = nums.__iter__()
i_nums_2 = iter(nums)

while True:
    try:
        item = next(i_nums_2)
        print(item)
    except StopIteration:
        break



# print(next(i_nums))
# print(next(i_nums))




#print(dir(nums))

