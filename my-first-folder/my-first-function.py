# for x in range(9001):
#     if x<=100:
#         print("less than 100")
#     elif x>100 and x<=200:
#         print(x)
#     elif x>200 and x<=300:
#         print(x)
#     elif x>300 and x<=400:
#         print(x)
#     elif x>400 and x<=500:
#         print(x)
#     elif x>500:
#         if x>=9000:
#             print("Vegeta likes it")
#         else: print(x)

def myfirstFunction(x):
    if x%2==0:
        print("number is even")
    else: print("number is odd")

# myfirstFunction(923)
            
def stairCase(maxRange):
    for x in range(maxRange):
        string=""
        for y in range(maxRange):
            if y <= x:
                string += "#"
            else:
                string = " " + string
        print(string)
stairCase(16)