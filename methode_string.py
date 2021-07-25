course = "   Python Progrming"

print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "C"))
print("Pro" in course)
print("Pre" not in course)

# structure de condition
temperature = 15
if temperature > 30:
    print("it's warm")
    print("drink water")
elif temperature > 20:
    print("it's nice")
else:
    print("it's cold")
print("done")

# operation ternaire
age = 20
message = "Eligeable" if age > 18 else "Not Eligeable"
print(message)


# exercice: boucle while
count = 0
for number in range(1, 10):
    while(number % 2 == 0):
        print(number)
        number += 1
        count += 1
print(f"we have {count} even number")

# exercice: condition if
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"we have {count} even number")
