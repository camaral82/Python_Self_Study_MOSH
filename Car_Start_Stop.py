#Python Self Study - 23/09/2020
#Car Project - start, stop, quit
command = ""
started = 0

while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car s already started!")
        else:
            started = 1
            print("Car started ... Ready to go!")
    elif command == 'stop':
        if not started:
            print("Car is already stopped!")
        else:
            started = 0
            print('Car stopped.')
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        print("By by!")
        break
    else:
        print("Sorry, I don't understand that command...")