
number_to_guess=2
oportunidades=4
user_number= int(input("Adivina un numero: "))

while oportunidades>0:
    if number_to_guess==user_number:
        print("Enhorabuena, has acertado")
        oportunidades=0
    else:
        oportunidades=oportunidades-1
        user_number = int(input("Prueba otra vez: "))
        if oportunidades==0:
            print("Has perdido")