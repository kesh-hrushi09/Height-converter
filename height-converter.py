name = input("what is your name?: ")
height = float(input("what is you height in centimetres?: "))
inch = 2.54

m = height/100
h_in = height/inch

if height >= 180:
    taller = True
else:
    taller = False
    
print(f"Hi {name}!",end=" ")
print(f"your height is {m} meters", end=" ")
print(f"that is {round(h_in,2)} inches")
print(taller)