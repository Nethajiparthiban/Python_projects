import random

question = [
    ["1) Who developed Python Programming Language?", "Guido van Rossum", "a) Wick van Rossum", "b) Rasmus Lerdorf",
     "c) Guido van Rossum", "d) Niene Stom"],
    ["2) Which type of Programming does Python support?","all of the mentioned", "a) object-oriented programming",
     "b) structured programming", "c) functional programming", "d) all of the mentioned"],
    ["3) Is Python case sensitive when dealing with identifiers?", "yes", "a) no", "b) yes", "c) machine dependent",
     "d) none of the mentioned"],
    ["4) Which of the following is the correct extension of the Python file?", ".py", "a) .python", "b) .pl", "c) .py",
     "d) .p"],
    ["5) Is Python code compiled or interpreted?", "Python code is both compiled and interpreted",
     "a) Python code is both compiled and interpreted",
     "b) Python code is neither compiled nor interpreted",
     "c) Python code is only compiled", "d) Python code is only interpreted"],
    ["6) All keywords in Python are in _________", "None of the mentioned", "a) Capitalized", "b) lower case",
     "c) UPPER CASE", "d) None of the mentioned"],
    ["7) What will be the value of the following Python expression? 4 + 3 % 5", "7", "a) 7", "b) 2", "c) 4", "d) 1"],
    ["8) Which of the following is used to define a block of code in Python language?", "Indentation", "a) Indentation",
     "b) Key", "c) Brackets", "d) All of the mentioned"],
    ["9) Which keyword is used for function in Python language?", "def", "a) Function", "b) def", "c) Fun",
     "d) Define"],
    ["10 Which of the following character is used to give single-line comments in Python?", "#", "a) //", "b) #",
     "c) !", "d) /*"]]
model=input("Do you want to play Y/N :").lower()
Total = 0
while model=="y":
    selection=random.choice(question)
    qtion,ans=(selection[0],selection[2:]),selection[1]
    print(qtion)
    inp=input("Pls Enter the Answer as it is in the option : ")
    if inp!=ans:
        print("incorrect answer the correct Answer is ",ans)
    else:
        print("Correct answer ",ans)
        Total+=1
    print(f'You got {Total} out of 10')