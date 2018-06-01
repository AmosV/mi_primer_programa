
apetece_heladoinput=input("Te apetece un helado?(Si/No)").upper()

if apetece_heladoinput == "SI":
    apetece_helado = True
elif apetece_heladoinput == "NO":
    apetece_helado=False
else:
    print("Cazurro, te he dicho que contestes como si o no, si no contestas asi yo contare como que no")
    apetece_helado=False

dineroinput=input("Tienes dinero?(Si/No)").upper()
esta_tu_tiainput=input("Estas con tu tia?").upper()
esta_el_heladeroinput=input("Esta el heladero?").upper()



puedes_permitirtelo = dineroinput=="SI" or esta_tu_tiainput=="SI"
esta_el_heladero = esta_el_heladeroinput=="SI"

if apetece_helado and puedes_permitirtelo and esta_el_heladero:
    print("Vamos a comprar")
else:
    print("Pues nada")