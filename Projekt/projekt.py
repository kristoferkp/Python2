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
app.geometry("1200x900")
app.title("Arvuti komponentide inventuur")


# Funktsioonid, mis lahutavad/liidavad komponendi arvust
def decrement_quantity(key, item, label):
    item[2] -= 1
    label.configure(text=f"{item[0]} (Qty: {item[2]})")
  
def increase_quantity(key, item, label):
    item[2] += 1
    label.configure(text=f"{item[0]} (Qty: {item[2]})")

# Funktsioonid, mis lahutavad/liidavad komponendi ostukorvis
def cart_increase_quantity(key, item, label):
    item[3] += 1
    label.configure(text=f"{item[3]}x {item[0]}")

    if item[3] > item[2]:
        item[3] = item[2]
        label.configure(text=f"{item[3]} (Max) x {item[0]}")

def cart_decrement_quantity(key, item, label):
    item[3] -= 1
    label.configure(text=f"{item[3]}x {item[0]}")

    if item[3] == 0:
        for frame in cartFrame.winfo_children():
            if frame.winfo_children()[0].cget("text") == f"{item[3]}x {item[0]}":
                item[3] = 1
                frame.destroy()
                added_items.remove(item)
                cart.remove(item)
                cartLabel.configure(text=f"Ostukorvis on {len(cart)} asja")
                break

            
# Ostukorv
cart = []
added_items = []

# Funktsioon, mis lisab komponendi ostukorvi
def shoppingcart(key, item, label):

    if item not in cart:
        cart.append(item)


    if item not in added_items:
        item.append(1)
        added_items.append(item)
        # Lisab komponendi ostukorvi
        # Igale reale oma raam, et nuppud ja tekst ei läheks omavahel sassi
        frame = customtkinter.CTkFrame(cartFrame)
        frame.pack(padx=10, pady=10)
                
        # Lisa komponendi nimetus
        label = customtkinter.CTkLabel(frame, text=f"{item[3]}x {item[0]}")
        label.pack(side="left", padx=10)
                
        # Ära võtmise nupp
        buttonMinus = customtkinter.CTkButton(frame, text="-", command=lambda k=key, i=item, lbl=label: cart_decrement_quantity(k, i, lbl), width=10)
        buttonMinus.pack(side="right", padx=5)
                
        #Lisamise nupp
        buttonPlus = customtkinter.CTkButton(frame, text="+", command=lambda k=key, i=item, lbl=label: cart_increase_quantity(k, i, lbl), width=10)
        buttonPlus.pack(side="right", padx=5)

    else:
        for frame in cartFrame.winfo_children():
            if frame.winfo_children()[0].cget("text") == f"{item[3]}x {item[0]}":
                label = frame.winfo_children()[0]
                cart_increase_quantity(key, item, label)
                break
    
    cartLabel.configure(text=f"Ostukorvis on {len(cart)} asja")
    cartFrame.update()

# Tühjenda ostukorv
def clear_cart():
    print(cart)
    
    for frame in cartFrame.winfo_children():
        frame.destroy()

    for item in cart:
        item[3] = 1
    
    cart.clear()
    added_items.clear()
    cartLabel.configure(text=f"Ostukorvis on {len(cart)} asja")
    

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

        # Lisa komponent ostukorvi
        buttonPlus = customtkinter.CTkButton(frame, text="Lisa ostukorvi", command=lambda k=key, i=item, lbl=label: shoppingcart(k, i, lbl))
        buttonPlus.pack(side="right", padx=20)

# Ostukorvi raam
cartFrame = customtkinter.CTkScrollableFrame(app, width=900, height=250)
cartFrame.pack()

# Ostukorvi raami alumine raam
bottomFrame = customtkinter.CTkFrame(app)
bottomFrame.pack(pady=10)

# Ostukorvi asjade arv
cartLabel = customtkinter.CTkLabel(bottomFrame, text=f"Ostukorvis on {len(cart)} asja")
cartLabel.pack(side="left", padx=10)

#Ostukorvi tühjendamise nupp
clearCart = customtkinter.CTkButton(bottomFrame, text="Tühjenda ostukorv", command=clear_cart)
clearCart.pack()


# Kasutajaliidese tsükkel
app.mainloop()