import wave 
import numpy as np
import matplotlib.pyplot as plt

#Cargar  archivo wav en la variable 

good_morning = wave.open('good-morningMan.wav', 'r')

good_afternoon = wave.open('good-afternoon.wav', 'r')

kepasa = wave.open('kepasa.wav', 'r')

laguerra = wave.open('laguerra.wav', 'r')

#Otener todos los frames del objeto wave
frames = good_morning.readframes(-1)
framesan = good_afternoon.readframes(-1)
framesapa = kepasa.readframes(-1)
framesare = laguerra.readframes(-1)


#Convierte el audio good morning de byte a enteros
ondaconvertida = np.frombuffer (frames, dtype='int16')
ondaconvertidaAn = np.frombuffer (framesan, dtype='int16')
ondaconvertidapasa = np.frombuffer (framesapa, dtype='int16')
ondaconvertidare = np.frombuffer (framesare, dtype='int16')

#mostrar el resultado frames
framerate_gm = good_morning.getframerate()
framerate_an = good_afternoon.getframerate()
framerate_pa = kepasa.getframerate()
framerate_re = laguerra.getframerate()

print(framerate_gm)
print(framerate_an)
print(framerate_pa)
print(framerate_re)

time_gm = np.linspace(start=0, stop=len(ondaconvertida)/framerate_gm, num=len(ondaconvertida))
time_an = np.linspace(start=0, stop=len(ondaconvertidaAn)/framerate_an, num=len(ondaconvertidaAn))
time_pa = np.linspace(start=0, stop=len(ondaconvertidapasa)/framerate_pa, num=len(ondaconvertidapasa))
time_re = np.linspace(start=0, stop=len(ondaconvertidare)/framerate_re, num=len(ondaconvertidare))

#Muestra los primeros 10 int
print(time_gm[:10])
print(time_an[:10])
print(time_pa[:10])
print(time_re[:10])

#Generacion de la grafica
plt.title('Good morning vs Good afternoon ft. KE PASA... and LAGUERRA DE CLANES')

#etiquetas de los ejes
plt.xlabel('Tiempo (segundos: ')
plt.ylabel('Amplitud: ')

#Agregar informacion de las ondas para graficar
plt.plot(time_gm, good_morning, lanel='Good morning')
plt.plot(time_an, good_afternoon, lanel='Good afternoon', alpha=0.5)
plt.plot(time_pa, kepasa, lanel='Kepasa', alpha=0.5)
plt.plot(time_re, laguerra, lanel='La guerra', alpha=0.5)

plt.legend()
plt.show()