from film import Film

def main():
    #write your code below this line
    chipmunks = Film("Alvin and the Chipmunks: The Squeakquel", 0)
    age = int(input("How old are you?"))

    if (age >= chipmunks.age_rating):
        print("You may watch the film " + chipmunks.name)
    else:
        print("You may not watch the film " + chipmunks.name)


if __name__ == '__main__':
    main()
