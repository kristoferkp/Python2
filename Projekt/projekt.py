import customtkinter

# Ava fail ning tee topelt list
with open('computerparts.csv', "r", encoding="UTF-8") as file:
    comp = []
    for rida in file:
        osad = rida.split(',')
        comp.append(osad)
    comp.pop(0)
 
file.close()

võtmed = []
parts = {}

# Leia kõik erinevad kategooriad
for i in range(len(comp)):
    if comp[i][1] not in võtmed:
        võtmed.append(comp[i][1])

# Lisa kategooriad sõnestikku
for võti in võtmed:
    parts[võti] = []

# Lisa elemendid sõnestikku
for element in comp:
    parts[element[1]].append(element)
 
# Muuda kõik arvud int'ideks
for key in parts:
    for item in parts[key]:
        item[-1] = int(item[-1].strip())



# Kasutajaliidese värvid
customtkinter.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Init kasutajaliides
app = customtkinter.CTk()
app.geometry("1200x600")
app.title("Arvuti komponentide inventuur")


# Funktsioonid, mis lahutavad/liidavad komponendi arvust
def decrement_quantity(key, item, label):
    item[2] -= 1
    label.configure(text=f"{item[0]} (Qty: {item[2]})")
  
def increase_quantity(key, item, label):
    item[2] += 1
    label.configure(text=f"{item[0]} (Qty: {item[2]})")
    

# Lisa kategooriate valik
tabview = customtkinter.CTkTabview(master=app, width=500)
tabview.pack(pady=10, padx=10)

# Lisa andmed kasutajaliidesesse
for key in parts:
    # Lisa kategooria valikusse
    tabview.add(key)
    
    # Lisa suur scroll'itav raam kategooria alla
    bigframe = customtkinter.CTkScrollableFrame(tabview.tab(key), width=900, height=500)
    bigframe.pack()
    
    # Lisa andmed kategooriasse
    for item in parts[key]:
        # Igale reale oma raam, et nuppud ja tekst ei läheks omavahel sassi
        frame = customtkinter.CTkFrame(bigframe)
        frame.pack(padx=10, pady=10)
        
        # Lisa komponendi nimetus
        label = customtkinter.CTkLabel(frame, text=f"{item[0]} (Qty: {item[2]})")
        label.pack(side="left", padx=20)
        
        # Ära võtmise nupp
        buttonMinus = customtkinter.CTkButton(frame, text="Eelmalda üks", command=lambda k=key, i=item, lbl=label: decrement_quantity(k, i, lbl))
        buttonMinus.pack(side="right", padx=20)
        
        #Lisamise nupp
        buttonPlus = customtkinter.CTkButton(frame, text="Lisa üks", command=lambda k=key, i=item, lbl=label: increase_quantity(k, i, lbl))
        buttonPlus.pack(side="right", padx=20)

# Kasutajaliidese tsükkel
app.mainloop()