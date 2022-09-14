#Laboratorio 2 Seguridad Informatica
#Alumno: Cristian Madariaga
#Profesor: Manuel Alba Escobar

from tkinter import filedialog
import hashlib

#Abecedario en lista
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
       'P','Q','R','S','T','U','V','W','X','Y','Z']

#Función para obtener archivo
def GetFile(titulo):
    file_path = filedialog.askopenfilename(title = titulo,
                                                filetypes=[("Archivo de Texto","*.txt")])
    return file_path

#Hasheo sha512
def sha512(text):
    hashed = hashlib.sha512(text.encode('utf-8')).hexdigest()
    return hashed

#Funcion encriptado ROT(8)
def rot8(s):
    def lookup(v):  
        c = v.upper()
        if c in a:
            i = a.index(c)
            if i + 8 > 25:
                x = i - 26 + 8
                return a[x]
            elif i + 8 <= 25:
                x = i + 8
                return a[x]
        return v
    return''.join(map(lookup, s))

#Funcion desencriptado ROT(-8)
def des_rot8(s):
    def lookup(v):  
        c = v.upper()
        if c in a:
            i = a.index(c)
            if i + 8 > 25:
                x = i - 26 - 8
                return a[x]
            elif i + 8 <= 25:
                x = i - 8
                return a[x]
        return v
    return''.join(map(lookup, s))

#Main
while True:
    s = input("\nMenu de entrada:\n"
              "1. Encriptar Mensaje\n"
              "2. Descentriptar Mensaje y Verificar Hash\n"
              "3. Salir\n\nSeleccione opcion --> ")
    #Encriptar Mensaje ROT (8) doble vuelta, posterior hasheo
    if s == "1":
        path = GetFile("Seleccionar archivo de entrada")
        if path != '':
            with open(path) as opened_file:
                content = opened_file.read()
                encrypted = rot8(content)
                encrypted2 = rot8(encrypted)
                with open('MensajeSeguro.txt', 'w') as salida:
                          salida.write(encrypted2)
                          print("\nMensaje Guardado en 'MensajeSeguro.txt'")
                          print("\nEl hash del archivo es: \n")
                          hashing = sha512(encrypted2)
                          print(hashing)
                i = input("\nIngrese 1 para otra operacion, ingrese otro caracter para finalizar --> ")
                if i == "1":
                    continue
                else:
                    break
        else:
            print ("\nArchivo no seleccionado")
            
    #Desencriptar Mensaje ROT(8) doble vuelta,
    #posterior verificación de hasheo respecto al archivo original
    elif s == "2":
        path = GetFile("Seleccionar archivo a desencriptar")
        if path != '':
            with open(path) as opened_file:
                content = opened_file.read()
                decrypted2 = des_rot8(content)
                decrypted = des_rot8(decrypted2)
                print("\nDesencriptado exitoso, el mensaje es: ", decrypted)
                d = input("\n¿Desea verificar con hash si el mensaje ha sido modificado?\n"
                          "1. Verificar\n"
                          "2. Finalizar programa\n\nSeleccione opcion --> ")
                if d == "1":
                    path2 = GetFile("Seleccionar archivo original")
                    with open(path2) as opened_file2:
                        content2 = opened_file2.read()
                        e = rot8(content2)
                        e2 = rot8(e)
                        hashing1 = sha512(e2)
                    hashing2 = sha512(content)
                    if hashing2 == hashing1:
                        print("Mensaje integro, no ha sido modificado")
                    else:
                        print("El mensaje ha sufrido adulteracion")
            break
        
    elif s == "3":
        break
    
    else:
        print("\nOpcion no valida, por favor seleccione nuevamente\n")

