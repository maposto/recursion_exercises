import turtle

def snowflake_wrap(t, order, size):
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        n = 3
        while n > 0:
            snowflake(t, order, size)
            t.right(120)
            n -= 1

def snowflake(t, order, size):

    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        snowflake(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        snowflake(t, order-1, size/3)
        t.right(120)
        snowflake(t, order-1, size/3)
        t.left(60)
        snowflake(t, order-1, size/3)


leopold = turtle.Turtle()
leopold.shape("turtle")
leopold.color("brown")
leopold.speed(10)

snowflake_wrap(leopold, 3, 200)

