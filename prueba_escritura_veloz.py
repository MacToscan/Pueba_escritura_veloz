#-Vamos a crear una ventana donde en ella se pueda escibir una frase y se detecte cuan rápido es tu escritura.
#-Crearemos una lista con varias frases y habrá un botón que seleccione una de ellas al azar.
import tkinter as tk
import random
import time

class PruebaEscritura:
    def __init__(self, ventana):
        self.ventana = ventana        
        self.mode = "on"
        self.inicio = None
        self.configurar_ventana() 

        self.texto = tk.StringVar(value="")
        self.texto.trace("w", self.actualizar_etiqueta)     #-Con .trace("w", función) llamamos a la función al mismo momento que el texto se esté modificando y actualizamos el texto de la etiqueta1. 
           
        self.etiqueta()
        self.etiqueta1()
        self.etiqueta2()
        self.etiqueta3()
        self.entrada()
        self.lista_frases()

        self.crear_boton()
        self.boton_reinicio()
        self.vincular_teclado()
        self.actualizar_hora()
        self.tiempo_cronometro = 0.0
        self.cronometro()

    def cronometro(self):
        if self.mode == "off" and self.inicio is not None:
            tiempo_actual = time.perf_counter()
            self.tiempo_cronometro = tiempo_actual - self.inicio
            self.etiqueta_cronometro.config(text=f"Cronómetro: {self.tiempo_cronometro:.2f} s")
        self.ventana.after(10, self.cronometro)

    def configurar_ventana(self):
        self.ventana.title("Prueba de escritura veloz.")
        self.ventana.geometry("1200x800+120+0")
        self.ventana.configure(bg="lightgray")
    
    
    def etiqueta(self):
        #--Creamos una etiqueta donde se escribirá la frase elegida al azar.
        self.etiqueta = tk.Label(self.ventana, text="Frase a escribir")    #-Creamos un label
        self.etiqueta.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
        self.etiqueta.grid(row=0, column=2, padx=10, pady=10)
    def etiqueta1(self):
        #--Etiqueta donde se escribirá la frase que escribimos simultáneamente y al acabar cambiará el mensaje de corrección final.
        self.etiqueta1 = tk.Label(self.ventana, text="")  
        self.etiqueta1.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
        self.etiqueta1.grid(row=2, column=2, padx=10, pady=10)
    def etiqueta2(self):
        #--Etiqueta donde mostraremos un reloj, para así tener cierta certeza de que el cálculo de palabras/minuto está bien hecho.
        self.etiqueta2 = tk.Label(self.ventana, text="Hora actual")
        self.etiqueta2.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
        self.etiqueta2.grid(row=0, column=5, padx=10, pady=10)
        self.etiqueta_cronometro = tk.Label(self.ventana, text="Cronómetro: 0.00 s")
        self.etiqueta_cronometro.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
        self.etiqueta_cronometro.grid(row=1, column=5, padx=10, pady=10)
    def etiqueta3(self):
        #--Etiqueta donde saldrá el mensaje con el cálculo final, tiempo de ejecución y palabras escritas por minuto
        self.etiqueta3 = tk.Label(self.ventana, text=(""))
        self.etiqueta3.config(fg="black", bg="lightgray", font=("Arial", 18, "normal"))
        self.etiqueta3.grid(row=3, column=2, padx=10, pady=10)
    def entrada(self):
        #--Cuadro de texto donde escribir nuestra frase.
        self.entrada = tk.Entry(self.ventana, textvariable = self.texto)       #-El parámetro de texto de nuestra tk.entry es la variable "texto" de tipo tk.StringVar
        self.entrada.config(fg="black", bg="ivory3", font=("Arial", 18, "normal"))
        self.entrada.grid(row=4, column=2, padx=10, pady=10)
    def lista_frases(self):
        #--Creamos lista de frases.
        self.lista_frases = ["Una madre es una manta que siempre te va a tapar", 
                             "No por mucho madrugar amanece más temprano", 
                             "Soy más duro que el acero antes roto que doblarme",
                             "Cuando el grajo vuela bajo, hace un frío del carajo"]
    #--Función para mostrar el reloj dentro de la ventana.
    def actualizar_hora(self):
        self.etiqueta2.config(text=time.strftime("%H:%M:%S"))
        self.ventana.after(1000, self.actualizar_hora)        #-Con .after(1000, función), acualizamos cada 1000 milisegundos la llamada de la función, por lo tanto el reloj se actualiza cada segundo.

    def inicio_temporizador(self, event):
        if self.mode == "on":
            self.inicio = time.perf_counter()
            self.tiempo_cronometro = 0.0
            self.mode = "off"
    def fin_temporizador(self, event):
        if self.etiqueta.cget("text").strip().lower() == self.etiqueta1.cget("text").strip().lower():                     #-Establecemos condicional, si la frase está correctamente escrita o no...
            self.etiqueta3.config(text="Texto escrito correctamente, buen trabajo!")
            self.mode = "pause"
        else:
            self.etiqueta3.config(text=("El texto que has escrito no se corresponde con el texto indicado."))
            self.mode = "pause"
        self.fin = time.perf_counter()               #-Final temporizador.
        self.tiempo_total = self.fin - self.inicio
        self.palabras_escritas = len(self.etiqueta1.cget("text").split())
        print("Número de palabras escritas", len(self.etiqueta1.cget("text").split()))   #-Imprimimos número de palabras escritas por consola.
        self.velocidad = (self.palabras_escritas / self.tiempo_total) * 60
        self.etiqueta1.config(text=f"Has tardado {self.tiempo_total:.2f} segundos, {self.velocidad:.2f} palabras por minuto")

    #--Función frase random.        
    def frase_random(self):
        self.frase = random.choice(self.lista_frases)     #-Elegimos una frase al azar de nuestra lista de frases.
        self.etiqueta.config(text=self.frase)
    #--Creamos función para que al clicar el botón creado salga frase al azar.
    def click_boton(self):         
        self.frase_random()
    def crear_boton(self):
        #--Creamos botón para activar la frase aleatoria.
        self.boton = tk.Button(self.ventana, text = "Frase aleatoria")
        self.boton.config(fg="black", bg="gray", font=("Arial", 18, "normal"), command=self.click_boton)
        self.boton.grid(row=0, column=0, padx=100, pady=10)
    #--Función que actualiza constantemente el texto escrito a la etiqueta1
    def actualizar_etiqueta(self, *args):
        self.etiqueta1.config(text=self.texto.get())        
      
    def vincular_teclado(self):
        #--Vincular teclado.
        self.ventana.bind("<Key>", self.inicio_temporizador)      #-Vinculamos cualquier tecla del teclado que se presione, e invocamos al inicio del temporizador.
        self.ventana.bind("<Return>", self.fin_temporizador)      #-Vinculamos la tecla enter con el final de la escritura y así invocamos al final del temporizador.
    #--Función de reinicio.
    def reinicio(self):            
        self.mode = "on"                 #-Volvemos a poner el mode = "on", para que al volver a escribir se inicie de nuevo el temporizador
        self.tiempo_cronometro = 0.0
        self.entrada.delete(0, tk.END)   #-El método .delete borra todo el contenido de nuestra tk.Entry
        self.etiqueta1.config(text="")
        self.etiqueta3.config(text="")
        self.etiqueta_cronometro.config(text="Cronómetro: 0.00 s")

    def boton_reinicio(self):
        #:--Creamos botón de reinicio.
        self.boton_reinicio = tk.Button(self.ventana, text = "Reiniciar prueba")
        self.boton_reinicio.config(fg="black", bg="gray", font=("Arial", 18, "normal"), command=self.reinicio)
        self.boton_reinicio.grid(row=4, column=0, padx=100, pady=10)
    #--Mantenemos la ventana abierta.
if __name__ == "__main__":
    ventana = tk.Tk()
    PruebaEscritura(ventana)
    ventana.mainloop()