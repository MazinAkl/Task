# Name : Mazin Ahmed Akl
# Section : (4)

#Task-2
def Title_case_formatting():
    sentence=input('Enter a sentence')
    Title_case_sentence=sentence.title()
    print('the original sentence',sentence)
    print('Title case sentence',Title_case_sentence)
Title_case_formatting() 

#Task-4
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

#Task-5
def calculate_factorial():
    Number = int(input('enter postive integer : '))
    result = 1

    for i in range(1 , Number + 1):
        result *=i
    print('the factorial of ',str(Number),'is',str(result))

calculate_factorial()  