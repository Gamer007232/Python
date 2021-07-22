print('hello,welcome to trivia')
ans = input('are you ready to play(yes/no)')
score=0
total_q=4

if ans.lower()=='yes':
    ans=input('1.what is the best programming language?')
    if ans.lower()=='python':
      score+= 1
      print('correct')
else:
      print('incorrect')

ans=input('2.what is 2+8+5?')
if ans=='15':
  score+=1
  print('correct')
else:
  print('incorrect') 

ans=input('3.is plactic a conducter?')
if ans.lower()=='no':
  score+=1
  print('correct')
else:
  print('incorrect')
print('thank you for playing,you got',score,"questions correct.")
mark=(score/total_q)*100
print("Mark:",mark)
print('Goodbye')

