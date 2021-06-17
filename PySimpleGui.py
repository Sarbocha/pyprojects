import PySimpleGUI as sg

bt = {"size": (7, 2), "font": ("Franklin Gothic Book, ", 27), "button_color": "black"}
bw = {"size": (7, 2), "font": ("Franklin Gothic Book, ", 27), "button_color": "black"}
bo = {"size": (15, 2), "font": ("Franklin Gothic Book, ", 27), "button_color": "black"}

layout = [
    [sg.Text("Calculator Of Pandey Rocks")],
    [sg.Text("000000", key="_Display_")],
    [sg.Button("1", **bt), sg.Button("2", **bt), sg.Button("3", **bt), sg.Button("4", **bt), sg.Button("5", **bt)],
    [sg.Button("6", **bt), sg.Button("7", **bt), sg.Button("8", **bt), sg.Button("9", **bt), sg.Button("10", **bt)],
    [sg.Button("+", **bt), sg.Button("-", **bt), sg.Button("*", **bt), sg.Button("/", **bt), sg.Button("=", **bo)]

]

window = sg.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event is None:
        break
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    if event in number:
        window["_Display_"].update(event)


    if event in ["+", "-", "*", "/"]:
        if event == ["1"] and event == ["+"]:
            add = 1 + 1
            window["_Display_"].update(add)

        elif event == "-":
            sub = event - event
            window["_Display_"].update(sub)
        elif event == "*":
            multiply = event * event
            window["_Display_"].update(multiply)
        elif event == "/":
            divide = event / event
            window["_Display_"].update(divide)
        else:
            break




