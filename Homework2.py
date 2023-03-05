while True:
    try:
        age = int(input('Age: '))
    except ValueError:
        print("Invalid valid. Try again.")
        print( "Out of tries! ")
        break

    if age >= 18:
        print("You are a grown up!")
    else:
        print("You are a child!")

    break