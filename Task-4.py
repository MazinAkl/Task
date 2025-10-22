def remove_from_list():
    my_list = ['learn','study','practice','success']
    print('current list',my_list)
    item=input('Enter the item you to remove : ')

    if item in my_list :
       my_list.remove(item)
       print(item,'has been removed successfully')
    else:
        print(item,'was not found in the list')
    print('updated list : ',my_list)
    
remove_from_list()           