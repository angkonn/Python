print("Hello")
my_list = [
    ("name", "Mahtab Haque"),
    ("Id", "2108008"),
    ("Hall", "Bangabandhu Hall")
]

# Print the second element of the second tuple in the list
# print(my_list[1][1])

# Loop through the list of tuples
for i in my_list:
    tup = i
    if tup[0] == 'Id':  # Be careful with case sensitivity ('Id' instead of 'id')
        print(tup[1])

# Creating a dictionary correctly with key-value pairs
my_dict = {
    "name": "Mahtab Haque",
    "Id": "2108008",
    "Hall": "Bangabandhu Hall"
}

# Accessing the value of key 'Id' (case-sensitive)
print(my_dict["Id"])        
print(my_dict.items())    
for key,value in my_dict.items():
    print(key)
    print(value)  

#  copying to another dictionary:
second_dict=my_dict.copy()
for key,value in second_dict.items():
    print(key)
    print(value)  


# adding new info to dictionary:
my_dict["abc"] = 123
for key,value in my_dict.items():
    print(key)
    print(value)  

# updating an info in dictionary:
my_dict["name"]="Angkon"
for key,value in my_dict.items():
    print(key)
    print(value)  

# clearing dictionary:
second_dict.clear()
print(second_dict)
