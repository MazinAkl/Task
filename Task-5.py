def calculate_factorial():
    Number = int(input('enter postive integer : '))
    result = 1

    for i in range(1 , Number + 1):
        result *=i
    print('the factorial of ',str(Number),'is',str(result))

calculate_factorial()        
