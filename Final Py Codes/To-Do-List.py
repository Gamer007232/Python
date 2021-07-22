from time import sleep


  


todolist = []

def addtask():

  add = input("\nWhat would you like to add to your todo list?\n")
  todolist.append(add)
  
  print("\033c")

def removetask():
  
  if len(todolist) == 0:
    print("You don't have anything to remove from your list!")
    sleep(2)
    print("\033c")
  else:
    print("\nWhat would you like to remove from your todo list?")
    print("You have the following items in your list:\n")
    
    for i in range(len(todolist)):
      print(str(i + 1) + ". " + str(todolist[i]))
    
    takeaway = int(input("\nPick the item that you want to remove from the list\n\n"))
    
    takeaway -= 1
      
    todolist.remove(todolist[takeaway])
    
    print("\033c")
    
  
x=0

for i in range(3):
  print("Loading —")
  sleep(0.3)
  print("\033c")
  
  print("Loading \\")
  sleep(0.3)
  print("\033c")
  
  print("Loading |")
  sleep(0.3)
  print("\033c")
  
  print("Loading /")
  sleep(0.3)
  print("\033c")
  
  
  



while True:
  #ignore this block of codeplease
  if x != 0:
    print("\nHere is what is on your todo list:")
    for i in range(len(todolist)):
      print(str(i + 1) + ". " + str(todolist[i]))
  #ignore above code
  print("\nWelcome to your todo list!")
  print("-------------------------\n\n")
  
  print("What would you like to do with your todo list?")
  print(" 1. Add a task")
  print(" 2. Remove a task")
  print(" 3. Exit")
  
  desicion = input("\nType in a number\n\n")
  
  
  if desicion != "1" and desicion != "2" and desicion != "3":
    print("\033c")
  
  if desicion == "1":
    print("\033c")
    addtask()
  elif desicion == "2":
    print("\033c")
    removetask()
  elif desicion == "3":
    print("\033c")
    print("\nThanks for using my To-Do List!. Bye, and have a nice day :)")
    print("------------------------------------------------------------")
    break
  print("\n")
  x=1
  

  