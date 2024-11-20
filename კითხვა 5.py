#გააკეთეთ 5 მაგალითი and და or ოპერატორზე
x = 5 
y = 10
result = (x > 0) and (y > 0)
print(result) #true

x = 5
y = -10
result = (x > 0) and (y > 0)
#მეორე პირობა false
print(result) #false

x = -5
y = -10
result = (x > 0) and (y > 0)
#ორივე პირობა false
print(result)  # false 

x = 5
y = 10
result = (x < 10) and (y == 10)
#ორივე პირობა  true
print(result) #true

x = 20
y = 10
result = (x >= 20) and (y <= 10)
#ორივე პირობა true
print(result) #true

#or ოპერატორი
x = 5
y = -10 
result = (x > 0) or (y > 0)
#პირველი პირობა true
print(result) # true

x = 5
x = 10
result = (x > 0) or (y > 0)
#ორივე პირობა  true
print(result) # true

x = -5
y = -10
result = (x > 0) or(y > 0)
#ორივე პირობა false
print(result) #false

x = -5 
y = -10
result = (x < 0) or (y > 0)
#მეორე პირობა true 
print(result) #true

x = 10
y = 0
result = (x == 10) or (y == 5)
# პირველი პირობა true  
print(result) #true