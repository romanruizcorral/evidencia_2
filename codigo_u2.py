



import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
import serial ,time


Puerto = 'COM7'



app = tk.Tk()
app.title("Comunicacion tipo serial")
app.geometry("200x100")
app.configure(bg='light green')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)



Comunicacion = serial.Serial(port=Puerto,baudrate=9600)
time.sleep(2)

xs = [0]
ys = [1]



#Esta funcion permie poder graficar 
def animar(i,xs,ys):
    Dato= Comunicacion.readline()
    DatoString = str(Dato,'UTF-8')
    DatoFloat = float(DatoString.strip())

    y = DatoFloat
    x = xs[-1] + 1
    
    xs.append(x)
    ys.append(y)

    ax.clear()
    ax.plot(xs,ys)

ani = animation.FuncAnimation(fig,animar, fargs=(xs,ys), interval = 500)



def action1():
    if Boton1['bg']=='red':
        Boton1['bg']='green'
        Boton1['text']='ON'
        Comunicacion.write(b'1')
    else:
        Boton1['bg']='red'
        Boton1['text']='OFF'
        Comunicacion.write(b'2')
    
def action2():
    if Boton2['bg']=='red':
        Boton2['bg']='green'
        Boton2['text']='ON'
        Comunicacion.write(b'A')
    else:
        Boton2['bg']='red'
        Boton2['text']='OFF'
        Comunicacion.write(b'B')



   

#Aplicacion inicializa con los LEDS apagados        
Comunicacion.write(b'2')
Comunicacion.write(b'B')
    
#Frame 1, para control LED1
Frame1 = tk.Frame(app)
Frame1.pack(side='left')

Label1 = tk.Label(Frame1,text="Led 1")
Label1.pack(side='top')

Boton1 = tk.Button(Frame1, text = "OFF",bg = "red", command = action1)
Boton1.pack()


#Frame 2, para control LED2
Frame2 = tk.Frame(app)
Frame2.pack(side='left')

Label2 = tk.Label(Frame2,text=" Led 2")
Label2.pack(side='top')

Boton2 = tk.Button(Frame2, text = "OFF",bg = "red", command = action2)
Boton2.pack()

plt.show()

app.mainloop()


