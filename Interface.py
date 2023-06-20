import tkinter as tk
import tkinter.messagebox
import json
from Traveler import Traveler
from App import runApp

def loadAirports():
  # AIRPORTS
  airportsData = open('./data/airportData.json')
  airports = json.load(airportsData)

  _airports = {}
  for key in airports:
    _airports[airports[key]['code']] = airports[key]['visaRequired']

  return _airports

root = tk.Tk()

airports = loadAirports()

firstName = tk.Entry(root)
firstName.grid(row=0, column=1)
tk.Label(root, text="Nombre:").grid(row=0, column=0)

lastName = tk.Entry(root)
lastName.grid(row=0, column=3)
tk.Label(root, text="Apellido").grid(row=0, column=2)

checked = tk.IntVar()
visa = tk.Checkbutton(root, variable=checked)
visa.grid(row=0, column=5)
tk.Label(root, text="Tiene visa?").grid(row=0, column=4)

traveler = None

def createTraveler():
  if firstName.get() == "" and lastName.get() == "":
    return tkinter.messagebox.showinfo("Error", "Ingrese nombre y/o apellido validos")

  global traveler
  traveler = Traveler(firstName.get(), lastName.get(), checked.get())
  tkinter.messagebox.showinfo("", "Viajero guardado con exito")

  return traveler

tk.Button(root, text="Guardar viajero", command=lambda: createTraveler()).grid(row=0, column=7)

tk.Label(root, text="Aeropuertos").grid(row=1)
for num, key in enumerate(airports.items()):
  label = tk.Label(root, text=key[0])
  label.grid(row=2, column=num)

originEntry = tk.Entry(root)
originEntry.grid(row=3, column=1)
tk.Label(root, text="Origen:").grid(row=3, column=0)

destinyEntry = tk.Entry(root)
destinyEntry.grid(row=3, column=3)
tk.Label(root, text="Destino:").grid(row=3, column=2)

def createTravel(traveler):
  origin = originEntry.get().upper()
  destination = destinyEntry.get().upper()

  if not traveler:
    return tkinter.messagebox.showinfo("Error", "El viajero no esta registrado")

  if origin not in airports.keys() or destination not in airports.keys():
    return tkinter.messagebox.showinfo("Error", "El aeropuerto que ingreso no existe")

  if not traveler.hasVisa and airports[origin]:
    return tkinter.messagebox.showinfo("Error", "El viajero no tiene visa y el punto de origen requiere visa. Elija otro punto de origen")

  resultPath, resultCost = runApp(traveler, origin, destination)
  resultString = ""

  for item in range(len(resultPath)):
    if item == len(resultPath) - 1:
      resultString += resultPath[item]
    else:
      resultString += resultPath[item] + "\n"

  result = f"El viajero {traveler.firstName.capitalize()} {traveler.lastName.capitalize()} debe visitar estos aeropuertos: \n\n{resultString} \nCosto total: {resultCost}"

  tkinter.messagebox.showinfo("Resultado", result)


button = tk.Button(root, text="Guardar viaje", command=lambda: createTravel(traveler))
button.grid(row=3, column=4)

button = tk.Button(root, text="Ver grafo")
button.grid(row=4)


# root.mainloop()

