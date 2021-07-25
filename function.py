def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


result = multiply(2, 3, 4, 5)
print(result)


def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="Sow", age=28)
