import PySimpleGUI as sg
# kā izveidot sava loga vizuālo izskatu
"""
1. definejam mainigo figuriekavas


"""

"""
mana_theme={
 "BACKGROUND"="#b8cd9e"
}
"""
sg.theme_add_new("mans", mana_theme)
sg.theme("darkAmber")
dainas=[

  [sg.Text("Uzrakstīts teksts 1. rindā")],
  [sg.Text("Ievadi savu vārdu"), sg.InputText()],
 
  [sg.Button("Cancel")],


]
bilde="qwerty.ico"
mans_logs=sg.Window("Ziema", dainas,size=(320,150),icon=bilde)

#title, layout(elementi/dalas ko pievieno logam)


# organizet procesu- radit logu EVENT, VALUE

while True:
 notikums, vertibas= mans_logs.read()
 if notikums==sg.WIN_CLOSED or notikums=="Cancel": # taja close vietaa jasakrit tekstam ar 8. rindu ("camcel")
   break
 


 #kā zivadīt terminālī savu ievadito vardu
 print("Mans vārds ir:", vertibas[0]) # nultais elements
mans_logs.close()