import math
import numpy as np

#generador de un modulo memoria ROM de 2^n vectores con n bits cada vector 

def writeVHD(x):
    f.write('library IEEE;')
    f.write('use IEEE.STD_LOGIC_1164.ALL;\n')
    f.write('use IEEE.NUMERIC_STD.ALL;\n')
    
    f.write('entity ROM is\n')
    f.write('generic(\n')
    f.write('   width : natural := ')
    f.write(str(x))
    f.write('\n);\n')
        
    f.write('port(\n')
    f.write('   dir  : in std_logic_vector(width-1 downto 0);\n')
    f.write('   data : out std_logic_vector(width-1 downto 0)\n')
    f.write(');\n')
    f.write('end ROM;\n')
    f.write('architecture Behavioral of ROM is\n')
    f.write('type srom is array (0 to 2**width-1) of integer range 2**width - 1 downto 0;\n')
    f.write('signal srom_1 : srom;\n')
    f.write('begin\n')
    f.write('data <= std_logic_vector(to_signed(srom_1(to_integer(unsigned(dir))),width));\n')

cnt = 0

fs = 48000 #frecuencia de muestreo 48KHz
n = 24 #numero de bits en este caso un ADC de 24 bits es capaz de representar amplitudes de hasta 16,777,215 = 2^n - 1 

#El calculo de 1/fs no se realizo en el programa puesto que
#en python los flotantes muy pequenos tienden a 0.

freq = 523.25 #Equivalente a C5 (Do)

td = 2 #tiempo de duracion en segundos


#Vector tiempo generado de 0 a 3 segundos con pasos de 1/fs = 20.8333ms
t = np.arange(0,td,0.000020833)  
#Arreglo genera los valoresa reproducir
a= ((2**n - 1)/2)*(1 + np.sin(2*np.pi*freq*t)) 

print a
print len(a)

f = open('ROM.vhd', 'w')
            
writeVHD(n);
        
for i in a:
    f.write('srom_1(')
    f.write(str(cnt))
    f.write(') <= ')
    f.write(str(int(i)))
    f.write(';\n')
    cnt = cnt+1
    
f.write('end Behavioral;')
f.close()
    
