# this whole block is just defining our prompts
welcome_prompt = "Welcome homie G, what hell are we entering today?\n - To list all demon spawn, press 1\n - To do ur actual job, press 2\n - To escape not possible, press q\n"
# 1 lists patients 2 start diagnosis 3 quit
name_prompt = "What thou shall I call you?\n"
appearance_prompt = "How beat up is the patient looking?\n - 1: could run a marathon\n - 2: screaming at you or vomitting on his sweater\n"
# 1 is normal 2 is irritable or lethargic
assess_skin_prompt = "Pinch that skin bb\n - 1: boUncy\n - 2: elasticccc\n"
#1 is normal 2 is slow
assess_eyes_prompt = "How are the patient's eyes aka windows to the soul?\n - 1: Most boring eyes known to man\n - 2: maybe just flirty\n - 3: Set BACK\n"
#1 is normal, 2 is slightly sunken, 3 is severely sunken
severe_dehydration = "ur pee must look like the mississippi river"
some_dehydration = "drink a hydroflask"
no_dehydration = "u a perfect angel!"

patients_and_diagnoses = [
    "ana drink a hydroflask\n"
    "samara ur pee must look like the mississippi river\n"
    "kelly u a perfect angel!"
]


def main(): #this is our main menu
    while True:
        selection = input(welcome_prompt)  # this just says play welcome prompt
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
             print("\nCommiting Sudoku. Goodbye!")
             break # immediately stops the loop
        else:
            print("\nInvalid choice, idiot")

def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)

def save_new_diagnosis(name, final_diagnosis):
    final_diagnosis = name + " " + final_diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print("Final diagnosis:", final_diagnosis)

def start_new_diagnosis():
    name = input(name_prompt)
    final_diagnosis = assess_appearance() #so this works because assess appearance runs until it hits return, which is the end. this means that assess appearance goes to assess eyes or assess skin. then assess eyes has 3 options to end and assess skin has to options to end.
    save_new_diagnosis(name, final_diagnosis)

    #input("---------------------------------------------------")

def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        #eyes = input(assess_eyes_prompt)
        return assess_eyes() #doesn't end, just runs assess eyes
    elif appearance == "2":
        #skin = input(assess_skin_prompt)
         return assess_skin() #doesn't end, just runs assess skin

def assess_eyes():
    eyes = input(assess_eyes_prompt)
    if eyes == "1":
        return no_dehydration #ends
    elif eyes == "2":
        return no_dehydration #ends
    elif eyes == "3":
        return severe_dehydration #ends

def assess_skin():
    skin = input(assess_skin_prompt)
    if skin == "1":
        return some_dehydration #ends
    elif skin == "2":
        return severe_dehydration #ends



main()