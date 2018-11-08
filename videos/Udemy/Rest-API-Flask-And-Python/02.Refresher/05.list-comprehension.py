my_list = [0,1,2,3,4]
an_equal_list = [x for x in range(5)] # like a for loop, iterates over range 5, same as above

multiply_list = [x * 3 for x in range(5)]
print(multiply_list) # prints multiples of 3 

print(8 % 3) # modulus, same as other langs. any num % 2 is even

print([n for n in range (10) if n % 2 == 0]) # list of 0 to 9

people_you_know = ["Rolf", "John", "anna", "GREG"]
normalized_people = [person.strip().lower() for person in people_you_know]
print(normalized_people)