#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    contents = file.read()
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

for name in names:
    striped_name = name.strip()
    new_letter = contents.replace("[name]", striped_name)
    with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)




