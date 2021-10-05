print("Welcome to my computer quiz!")

playing = input("do you want to play? ")

text = "JuStIn LeE"
print(text.lower())

score = 0

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play")

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
    score+= 1
else:
    print('Incorrect!')

print("you got " + str(score) + " questions correct")
