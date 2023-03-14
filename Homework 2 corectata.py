for age  in range(6):
    try:
        age = int(input('Age: '))
    except ValueError:
        print("Invalid value. Try again.")
        continue

    if age >= 18:
        print("You are a grown up!")
    else:
        print("You are a child!")

    break
else:
    print("Out of tries!")
