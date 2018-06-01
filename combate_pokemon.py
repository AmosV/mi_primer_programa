
pokemon_elegido = input("Contra que pokemon quieres combatir? Squirtle / Charmander / Bulbasaur").upper()
vida_pikachu=100
vida_squirtle=90
vida_charmander=80
vida_bulbasaur=100
vida_enemigo=0
daño_squirtle=10
daño_charmander=9
daño_bulbasaur=11
daño_chispazo=9
daño_bola_voltio=12

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = vida_squirtle
    daño_pokemon = daño_squirtle
elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = vida_charmander
    daño_pokemon = daño_charmander
elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = vida_bulbasaur
    daño_pokemon = daño_bulbasaur

while(vida_pikachu > 0 and vida_enemigo > 0):
    ataque_elegido = input("Elige el ataque a realizar (Chispazo / Bola Voltio)").upper()

    if ataque_elegido == "CHISPAZO":
        print("Pikachu uso Chispazo")
        vida_enemigo -=daño_chispazo
        if vida_enemigo < 0:
            vida_enemigo = 0
    elif ataque_elegido == "BOLA VOLTIO":
        print("Pikachu uso bola Voltio")
        vida_enemigo -=daño_bola_voltio
        if vida_enemigo < 0:
            vida_enemigo = 0
    else:
        print("Pikachu no ha atacado")

    print("La vida de {} ahora es de {}".format(pokemon_elegido , vida_enemigo))
    if vida_enemigo > 0:
        print("{} ha atacado".format(pokemon_elegido))
        vida_pikachu -= daño_pokemon
        print("La vida de pikachu ahora es de {}".format(vida_pikachu))

if vida_pikachu == 0:
    print("Pikachu se ha debilitado, {} gana1".format(pokemon_elegido))
elif vida_enemigo ==0:
    print("{} se ha debilitado, Pikachu gana!".format(pokemon_elegido))

print("El combate ha terminado")