# Conditional Statements 

# if , if else  , if else if 



# age = int(input('please enter your age'))

# if(age > 18):
#     print('you are allowed')
# else:
#     print('you are not allowed')
    

# enter into college only when id card is weared

# idcard = False

# if(idcard == True):
#     print('you are allowed')
# else:
#     print('you are not allowed')



# tickets = 250

# if(tickets>=250):
#     print('you are allowed')
# else:
#     print('you are not allowed') 




# what if we have more than 2 conditions 

# ticket1 = 100

# if(ticket1 <= 500):
#     print('this is balcony enterence ')
# elif(ticket1 <= 200):
#     print('this is classic enterence')
# else:
#     print('this is a vip enterence')



# classify your marks is wether average, good or outstanding 

studentMarks = int(input('please enter your marks : '))

if(studentMarks <= 100 and studentMarks >= 70):
    print('you have outstanding marks')
elif(studentMarks <70 and studentMarks >=50 ):
    print('you have a good marks')
elif(studentMarks < 50 and studentMarks >=30):
    print('you have a average marks , please study hard next time ')
else:
    print('you have failed')