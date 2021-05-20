massage = "Was machst du?"

def greet():
    global massage
    massage = "Wie gehts dir?"
    print("Message inside function", massage)

greet()
print("Message outside funtion", massage)