PLACEHOLDER = "[name]"

with open("email_project\\Input\\Letters\\starting_letter.txt","r") as letter:
    old_letter = letter.read()
    print(old_letter)

with open("email_project\\Input\\Names\\invited_names.txt","r") as invited_names:
    names = invited_names.readlines()
    for name in names:
        stripped_name = name.strip()
        invitation_letters = old_letter.replace(PLACEHOLDER,stripped_name)
        
        with open(f"email_project\\Output\\ReadyToSend\\{stripped_name}_invitation","w") as invitation:    
                invitation.write(invitation_letters)
