import PySimpleGUI as sg


dainas=[

  [sg.Text("Uzrakstīts teksts 1. rindā")],
  [sg.Text("Ievadi savu vārdu"), sg.InputText()],
  [sg.Button("Cancel")]


]

mans_logs=sg.Window("Ziema", dainas)

#title, layout(elementi/dalas ko pievieno logam)



# organizet procesu- radit logu EVENT, VALUES




while True:
 notikums, vertibas= mans_logs.read()
 if notikums==sg.WIN_CLOSED or notikums=="Cancel": # taja close vietaa jasakrit tekstam ar 8. rindu ("camcel")
  break
 

mans_logs.close()