num1 = 11
num2 = num1

print("Before num2 is updated")
print(f"num1 : {num1}")
print(f"num2 : {num2}")

print(f"num1 points to {id(num1)}")
print(f"num2 points to {id(num2)}")

num2 = 22

print("After num2 is updated")
print(f"\nnum1 : {num1}")
print(f"num2 : {num2}")

print(f"num1 points to {id(num1)}")
print(f"num2 points to {id(num2)}")


#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


