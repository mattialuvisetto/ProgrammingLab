def transform_nums (mylist):  
    new_list = []

    dict = {0 : "zero", 1 : "uno", 2 : "due", 3 : "tre", 4 : "quattro", 5 : "cinque", 6 : "sei", 7 : "sette", 8 : "otto", 9 : "nove"}

    for num in mylist:
        new_list.append(dict[num])
    
    return new_list

mylist3 = [1,7,3,5,9,0,0,0]
new_list = transform_nums(mylist3)
print(new_list)

