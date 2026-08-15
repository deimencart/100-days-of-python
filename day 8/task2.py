def greet(): 
    print("This is a greeting function")
    print("Nice to meet you")
    print("please wait until next")


def greet_with_name(name): 
    print(f"This is a greeting function for {name}")
    print("Nice to meet you")
    print("please wait until next")


if __name__ == "__main__":
    greet()
    greet_with_name("Alice")