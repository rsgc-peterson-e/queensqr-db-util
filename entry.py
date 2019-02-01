# Prompt User For all Data needed for a new Building Object in the DB
# return a dictionary that can be posted to the DB in the main.py file

b = {}

def  fieldPrompt(prompt, dbField):
    ans = input(prompt)
    ans = ans.strip()
    b[str(dbField)] = ans
    print("")

def arrayField(prompt, dbField):
    arr = []
    print("ARRAY FIELD (GIVE COMMA SEPERATED LIST)")
    ans = input(prompt)
    ans = ans.split(",")
    for i in range(0, len(ans)):
        ans[i] = ans[i].strip()
        arr.append(ans[i])
    b[str(dbField)] = arr
    print("")

def newBuilding():
    print("Welcome to Building Entry Wizard")
    print("Press enter to move onto the next property (all fields mandatory)\n")
    
    fieldPrompt("name: ", "name")
    fieldPrompt("address: ", "address")
    fieldPrompt("faculty: ", "faculty")
    fieldPrompt("hours: ", "hours")
    fieldPrompt("history: ", "history")
    arrayField("alias: ", "alias")
    fieldPrompt("services (give comma seperated list of strings no spaces between commas): ", "services")

    print("Final Document:\n")
    print(b)
    return b