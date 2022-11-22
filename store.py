
from ast import Continue
import os
import sys

class Tienda:
    
    def __init__(self):
        self.lista = []
        self.lista2 = []
        self.login
        self.verifylogin
        self.listacompra = []
        self.listacant = []
        
    def login(self):
        os.system("cls")
        print("\n---------------- FERRETERIA 'EL TORNILLO FELIZ' ----------------\n")
        print("------------------------- REGISTRATE -------------------------")
        self.lista = []
        user = input("Ingrese Usuario -> ")     
        self.lista.append(user)
        
        self.lista2 = []
        password = input("Ingrese Contraseña -> ")     
        self.lista2.append(password)

        print("\n---------------- INICIO DE SESIÓN ----------------")
        self.validate_user = input("\nIngrese Usuario -> ")
        validate_pass = input("Ingrese Contraseña -> ")

        for i in range(len(self.lista)):
            if self.validate_user == self.lista[i]:
                for j in range(len(self.lista2)):
                    if validate_pass == self.lista2[j]:
                        self.menu_opciones()
                    else:
                        print("\nDATOS INCORRECTOS")
                        self.verifylogin()
            else:
                print("\nDATOS INCORRECTOS")
                self.verifylogin()
        return self.lista, self.lista2

    def verifylogin(self):
        print("\n---------------- INICIO DE SESIÓN ----------------")
        self.validate_user = input("\nIngrese Usuario -> ")
        validate_pass = input("Ingrese Contraseña -> ")

        for i in range(len(self.lista)):
            if self.validate_user == self.lista[i]:
                for j in range(len(self.lista2)):
                    if validate_pass == self.lista2[j]:
                        self.menu_opciones()
                    else:
                        print("\nDATOS INCORRECTOS")
                        self.verifylogin()
                        continue
            else:
                print("\nDATOS INCORRECTOS")
                self.verifylogin()
                
    def menu_opciones(self):
        os.system("cls")
        print("\n---------------- FERRETERIA 'EL TORNILLO FELIZ' ----------------\n")
        print("-------------------- BIENVENIDO AL SISTEMA --------------------")
        print("\nEscoja una opción por favor\n")
        print(" [1] Compra producto \n [2] Buscar producto \n [3] Salir")
        opc = int(input("\nIngrese opción -> "))
        if opc == 1:
            self.compra_producto()
        elif opc == 2:
            self.buscar_producto()
        elif opc == 3:
            print("\nVuelva pronto\n")
            sys.exit()
        else:
            print("Opción incorrecta")
            self.menu_opciones()
           
    def buscar_producto(self):
        print("---------------- LISTA DE PRODUCTOS ----------------")
        print("\nEscoja una opción por favor\n")
        print(" [1] HERRAMIENTAS FUNDAMENTALES \n [2] HERRAMIENTAS DE MANO \n [3] HERRAMIENTAS DE CONSTRUCCIÓN \n [4] HERRAMIENTAS ABRASIVAS \n [5] HERRAMIENTAS DE CARPINTERÍA ")
        opc = int(input("\nIngrese opción -> "))
        value = True
        while value == True:
            if opc == 1:
                print("------- HERRAMIENTAS FUNDAMENTALES -------")
                print("[TF001] Taladro\n[TF002] Adhesivos\n[TF003] Alicate\n[TF004] Martillo\n[TF005] Brocha\n[TF006] Cinta Métrica\n[TF007] Llave ajustable")
                print("\n [1] Comprar un producto\n [2] Regresar")
                opc1 = int(input("\nIngrese opción -> "))
                if opc1 == 1:
                    self.compra_producto()
                    value = False
                elif opc1 == 2:
                    self.buscar_producto()
                    value = False
                else:
                    print("\nOpción incorrecta\n")

            elif opc == 2:
                print("------- HERRAMIENTAS DE MANO -------")
                print("[TF008] Llaves allen\n[TF009] Llaves fijas\n[TF010] Llaves de tubo\n[TF011] Mazas\n[TF013] Cepillos metálicos\n[TF014] Destornillador")
                print("\n [1] Comprar un producto\n [2] Regresar")
                opc1 = int(input("\nIngrese opción -> "))
                if opc1 == 1:
                    self.compra_producto()
                    value = False
                elif opc1 == 2:
                    self.buscar_producto()
                    value = False
                else:
                    print("\nOpción incorrecta\n")
                    
            elif opc == 3:
                print("------- HERRAMIENTAS DE CONSTRUCCIÓN -------")
                print("[TF015] Cuñas\n[TF016] Curvatubos\n[TF017] Niveles\n[TF018] Paletas\n[TF019] Cortavarillas\n[TF020] Pelacables y cortacables\n[TF021] Picos")
                print("\n [1] Comprar un producto\n [2] Regresar")
                opc1 = int(input("\nIngrese opción -> "))
                if opc1 == 1:
                    self.compra_producto()
                    value = False
                elif opc1 == 2:
                    self.buscar_producto()
                    value = False
                else:
                    print("\nOpción incorrecta\n")
                    
            elif opc == 4:
                print("------- HERRAMIENTAS ABRASIVAS -------")
                print("[TF022] Tuberías y sus accesorios\n[TF023] Tuberías y accesorios de acero\n[TF024] Tuberías y accesorios de plástico\n[TF025] Tubos y mangueras flexibles\n[TF026] Codos\n[TF027] Tuberías y accesorios de aluminio")
                print("\n [1] Comprar un producto\n [2] Regresar")
                opc1 = int(input("\nIngrese opción -> "))
                if opc1 == 1:
                    self.compra_producto()
                    value = False
                elif opc1 == 2:
                    self.buscar_producto()
                    value = False
                else:
                    print("\nOpción incorrecta\n")
                    
            elif opc == 5:
                print("------- HERRAMIENTAS DE CARPINTERÍA -------")
                print("[TF028] Hojas y sierras para madera\n[TF029] Cuchillas y discos para madera\n[TF030] Herramientas trituradoras para madera")
                print("\n [1] Comprar un producto\n [2] Regresar")
                opc1 = int(input("\nIngrese opción -> "))
                if opc1 == 1:
                    self.compra_producto()
                    value = False
                elif opc1 == 2:
                    self.buscar_producto()
                    value = False
                else:
                    print("\nOpción incorrecta\n")
                    
            else:
                print("Opción incorrecta")
                self.buscar_producto()
    
    def DatosPago(self):
        while True:
            print("\n---------- MÉTODO DE PAGO ----------\n")
            print("EL TOTAL A PAGAR ES -> S/", self.pago_total)
            pago = float(input("\nIngrese la cantidad con la que va a pagar -> S/"))
            if pago > self.pago_total:
                os.system("cls")
                vuelto = pago - self.pago_total
                print("**************************************")
                print("**          BOLETA DE PAGO          **")
                print("**************************************")
                print("Usuario: " + self.validate_user)
                print("Monto a pagar: " ,self.pago_total)
                print("Pagaste con: ", pago)
                print("Vuelto: ", vuelto)
                print("\n¡Gracias por su compra! Regrese pronto\n")
                sys.exit()
            elif pago == self.pago_total:
                os.system("cls")
                vuelto = pago - self.pago_total
                print("**************************************")
                print("**          BOLETA DE PAGO          **")
                print("**************************************")
                print("Usuario: " + self.validate_user)
                print("Monto a pagar: " ,self.pago_total)
                print("Pagaste con: ", pago)
                print("No hay vuelto")
                print("\n¡Gracias por su compra! Regrese pronto\n")
                sys.exit()
            else:
                print("\n----------------- DATO ERRÓNEO -----------------")
                print("\nIngrese un monto mayor a lo que se requiere para cancelar su pedido por favor")
                continue
    
    def compra_producto(self):
        self.codigos = {
            "TF001": 70,
            "TF002": 10,
            "TF003": 45,
            "TF004": 50,
            "TF005": 24,
            "TF006": 27,
            "TF007": 17,
            "TF008": 75,
            "TF009": 64,
            "TF010": 34,
            "TF011": 64,
            "TF012": 21,
            "TF014": 43,
            "TF013": 45,
            "TF015": 77,
            "TF016": 56,
            "TF017": 12,
            "TF018": 45,
            "TF019": 23,
            "TF020": 22,
            "TF021": 15,
            "TF022": 55,
            "TF023": 69,
            "TF024": 89,
            "TF025": 54,
            "TF026": 44,
            "TF027": 30,
            "TF028": 10,
            "TF029": 22,
            "TF030": 17 
        }

        self.pago_total = 0

        self.cod = input("\nDigite el codigo del producto: ")
        self.cod = self.cod.upper()
        while self.cod != "0":
            
            if self.cod in self.codigos:
                self.pago_total = self.pago_total + self.codigos.get(self.cod, 0) 
                
                while True:
                    print("\n [1] Seguir comprando\n [2] Terminar\n")
                    opcc = int(input("Ingrese opción -> "))
                    
                    if opcc == 1:                            
                        self.cod = input("\nDigite el codigo del producto: ")
                        self.cod = self.cod.upper()
                        self.pago_total = self.pago_total + self.codigos.get(self.cod, 0)
                        continue    
                        
                    elif opcc == 2:
                        ferreteria.DatosPago()
                        break
                    
                    elif opcc > 2 or opcc < 0:
                        print("\nOpción incorrecta")
                break
            else:
                print("Codigo inexistente")
            self.cod = input("\nDigite el codigo del producto: ")
            self.cod = self.cod.upper()
            

ferreteria=Tienda()
ferreteria.login()