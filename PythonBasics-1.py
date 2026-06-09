# # # # squares = [x**2 for x in range(10)]
# # # # print(f"Squares of numbers from 0 to 9: {squares} (with list comprehension)")

# # # # The same example using for loop
# # # squares_for_loop = []
# # # for x in range(10):
# # #     squares_for_loop.append(x**2)
# # # print(f"Squares of numbers from 0 to 9: {squares_for_loop} (without list comprehension)")



# # # Conditional list comprehension
# # even_squares = [x**2 for x in range(10) if x % 2 == 0]
# # print(f"Squares of even numbers from 0 to 9: {even_squares} (with list comprehension)")

# # # Without list comprehension
# # even_squares_for_loop = []
# # for x in range(10):
# #     if x % 2 == 0:
# #         even_squares_for_loop.append(x**2)
# # print(f"Squares of even numbers from 0 to 9: {even_squares_for_loop} (without list comprehension)")


# # Example of a dictionary
# person = {
#     'name': 'Alice',
#     'age': 25,
#     'city': 'New York'
# }
# print(f"Person dictionary: {person}")

# # Accessing a value
# # print(f"Name: {person['name']}")

# # Adding a new key-value pair
# person['email'] = 'alice@example.com'
# # print(f"Updated person dictionary: {person}")

# for val in person:
#     print(val)

# for key, value in person.items():
#     print(f"Key: {key}\tValue: {value}")



people = [
    {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice.johnson@example.com",
        "location": "New York, NY"
    },
    {
        "name": "Michael Smith",
        "age": 34,
        "email": "michael.smith@example.com",
        "location": "Los Angeles, CA"
    },
    {
        "name": "Emily Davis",
        "age": 22,
        "email": "emily.davis@example.com",
        "location": "Austin, TX"
    },
    {
        "name": "John Brown",
        "age": 45,
        "email": "john.brown@example.com",
        "location": "Chicago, IL"
    },
    {
        "name": "Sarah Wilson",
        "age": 31,
        "email": "sarah.wilson@example.com",
        "location": "Seattle, WA"
    }
]

# First, create an empty list to store the sentences:
t = []
# Iterate over the list of dictionary
for person_info_dict in people:
    # person_info_dict is a dict and you can access its values using the keys
    layout_string = f"Name: {person_info_dict['name']}, Age: {person_info_dict['age']}, E-mail: {person_info_dict['email']}, Location: {person_info_dict['location']}"
    # Append the string with the desired information into the list
    t.append(layout_string) # Add a new line character at the end
# Create the result layout by using the .join method
# The .join function concatenates every string in the list 't', separated by the specified delimiter. Here, each element of 't' is joined using the newline character '\n'.print(formatted_string)
formatted_string = "\n".join(t) 
print(formatted_string)