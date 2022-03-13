for i in range(100):
    print('Nikdy nebudu odsazovat o tři mezery!')

for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
    print(pozdrav + '!') 

for i in range(5):
    print(i)  

from turtle import forward, penup, pendown, exitonclick, left, right
"""for i in range(30):
    forward(i)
    penup()
    forward(5)
    pendown()

exitonclick()"""
"""for i in range(3):
    for i in range(4):
        forward(50)
        left(90)
    left(20)    

exitonclick()"""

forward(50)
left(60)
forward(50)
right(60)
for i in range(6):
    for i in range(6):
        forward(50)
        left(60)
    forward(50)
    right(60)

exitonclick()
