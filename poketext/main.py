import random
import pokemons
import time

# CORES
def typecolor(tipo):
    if len(tipo) == 2:
        tipo = tipo[0]
    if tipo == "NORMAL":
        return "\033[38;2;170;170;170m"
    elif tipo == "FIRE":
        return "\033[38;2;255;69;0m"
    elif tipo == "WATER":
        return "\033[38;2;0;119;190m"
    elif tipo == "ELECTRIC":
        return "\033[38;2;255;214;0m"
    elif tipo == "GRASS":
        return "\033[38;2;0;166;51m"
    elif tipo == "ICE":
        return "\033[38;2;150;255;255m"
    elif tipo == "FIGHTING":
        return "\033[38;2;147;41;36m"
    elif tipo == "POISON":
        return "\033[38;2;160;0;160m"
    elif tipo == "GROUND":
        return "\033[38;2;155;118;83m"
    elif tipo == "FLYING":
        return "\033[38;2;136;153;255m"
    elif tipo == "PSYCHIC":
        return "\033[38;2;255;51;153m"
    elif tipo == "BUG":
        return "\033[38;2;168;184;32m"
    elif tipo == "ROCK":
        return "\033[38;2;160;144;80m"
    elif tipo == "GHOST":
        return "\033[38;2;102;102;187m"
    elif tipo == "DRAGON":
        return "\033[38;2;112;56;248m"
    elif tipo == "DARK":
        return "\033[38;2;112;88;72m"
    elif tipo == "STEEL":
        return "\033[38;2;184;184;208m"
    elif tipo == "FAIRY":
        return "\033[38;2;238;153;238m"
    else:
        return "\033[1;97m"


default = "\033[1;97;40m"
basic = "\033[1;97m"

# FUNCÕES

# mostrar a mochila
def mochila():
    check = ""
    valido = 0
    print("ITEMS\n")
    listaItens = list(pokemons.bag.keys())
    for i in range(0, len(listaItens)):
        print(f"{i+1} - {listaItens[i]}: {pokemons.bag[listaItens[i]]}")

    while valido != 1:
        escolhaItem = input("\nChoose an ITEM or CANCEL: ").upper()
        if escolhaItem == "CANCEL":
            break
        else:
            for i in range(0, len(listaItens)):
                check = str(i+1)
                if escolhaItem == check:
                    escolhaItem = listaItens[i]
                    if pokemons.bag[escolhaItem] >= 1:
                        valido = 1
                elif escolhaItem == listaItens[i]:
                    if pokemons.bag[escolhaItem] >= 1:
                        valido = 1
        if valido == 0:
            print(f"You don't have {escolhaItem}")

    return escolhaItem

# usar poções
def potionpoke():
    valido = 0
    check = ""
    print("TEAM\n")
    while valido != 1:
        for i in range(0, len(listaTime)):
            print(i + 1, "- ", end='')
            print(typecolor(pokemons.pokedex[listaTime[i]]['TYPE']), end='')
            print(listaTime[i], end=' ')
            print(basic, end='')
            print(pokemons.time[listaTime[i]]["HEALTH"], end=' HP\n')
        pokeCura = input("\n\nChoose a POKEMON to heal or CANCEL: ").upper()
        for i in range(0, len(listaTime)):
            check = str(i + 1)
            if pokeCura == listaTime[i]:
                valido = 1
            elif pokeCura == check:
                pokeCura = listaTime[i]
                valido = 1
        if pokeCura == "CANCEL":
            return pokeCura
            break
        if valido == 0:
            print("Invalid pokemon.")
    return pokeCura

# cura da poção
def potionheal(curado):
    if pokemons.time[curado]["HEALTH"] + 20 <= pokemons.time[curado]["MAX_HEALTH"]:
        heal = 20
    else:
        heal = pokemons.time[curado]["MAX_HEALTH"] - pokemons.time[curado]["HEALTH"]
    if heal == 0:
        print(f"{typecolor(pokemons.pokedex[curado]['TYPE'])}{curado}{basic} already has full health!")
    else:
        print(f"{typecolor(pokemons.pokedex[curado]['TYPE'])}{curado}{basic} healed {heal} HP!")
        time.sleep(1)
    return heal

# capturar pokemon, formula simplificada
def jogarpokebola(pokemon, vida, vidamax, vidamin):
    pego = 0
    print("Player used Pokeball!")
    time.sleep(0.5)
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("Click!")
    time.sleep(1)

    chance = round(((vidamax - vida) / (vidamax - vidamin)) * 100)

    aleatorio = random.randint(0, 155)

    if aleatorio < chance:
        pego = 1

    if pego == 1:
        print(f"Gotcha! {typecolor(pokemons.pokedex[pokemon]['TYPE'])}{pokemon}{basic} was caught!")
    else:
        print(f"Oh no! The {typecolor(pokemons.pokedex[pokemon]['TYPE'])}{pokemon}{basic} broke free!")


    return pego

# mostrar e escolher as opcões da batalha
def listalutas():
    valido = 0
    while valido != 1:
        for i in range(0, len(opcoesLuta)):
            print(i + 1, "- ", end='')
            print(opcoesLuta[i], end=' ')
        escolhaLuta = input(f"\nWhat will {typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} do?").upper()
        for i in range(0, len(opcoesLuta)):
            check = str(i + 1)
            if escolhaLuta == opcoesLuta[i]:
                valido = 1
            elif escolhaLuta == check:
                escolhaLuta = opcoesLuta[i]
                valido = 1
        if valido == 0:
            print("Invalid choice.")
        return escolhaLuta

# mostrar e escolher o ataque do jogador
def ataquepoke():
    valido = 0
    while valido != 1:
        print("Choose your attack: ")
        for i in range(0, len(listaAtaques)):
            print(i + 1, "- ", end='')
            print(typecolor(pokemons.attacks[listaAtaques[i]]['TYPE']), end='')
            print(listaAtaques[i], end=' ')
            print(basic, end='')
        ataque = input("\n")
        for i in range(0, len(listaAtaques)):
            check = str(i + 1)
            if ataque == listaAtaques[i]:
                valido = 1
            elif ataque == check:
                ataque = listaAtaques[i]
                valido = 1
        if valido == 0:
            print("Attack invalid!")
    return ataque

# calculo do dano, baseado no calculo do Pokemon GO
def tipagem(danopoke, tipoataque, danoataque, defesapoke, *defesatipo):
    mult = 1
    for i in range(0, len(defesatipo)):
        mult = mult * (pokemons.tipos[tipoataque][defesatipo[i]])
    if mult == 2:
        print("It's super effective!")
    elif mult == 0.5:
        print("It's not very effective...")
    elif mult == 0:
        print("It doesn't affect the POKEMON...")
    time.sleep(1)

    calc = round((0.5 * danoataque * (danopoke / defesapoke) * mult) + 1)

    return calc

# calcular o dano do ataque
def fight(atacantepoke,ataquepoke, defesapoke):
    if len(pokemons.pokedex[defesapoke]["TYPE"]) > 2:
        tipoDefesa = (pokemons.pokedex[defesapoke]["TYPE"])
        dano = tipagem(pokemons.pokedex[atacantepoke]["ATTACK_POWER"], pokemons.attacks[ataquepoke]["TYPE"], pokemons.attacks[ataquepoke]["POWER"], pokemons.pokedex[defesapoke]["DEFENSE"], tipoDefesa)
    else:
        tipoDefesa = list((pokemons.pokedex[defesapoke]["TYPE"]))
        dano = tipagem(pokemons.pokedex[atacantepoke]["ATTACK_POWER"], pokemons.attacks[ataquepoke]["TYPE"], pokemons.attacks[ataquepoke]["POWER"], pokemons.pokedex[defesapoke]["DEFENSE"], tipoDefesa[0], tipoDefesa[1])
    return dano

def ataqueinimigo(ataqueInimigo):
    print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} used {typecolor(pokemons.attacks[ataqueInimigo]['TYPE'])}{ataqueInimigo}{basic}!\n")
    dano = fight(inimigo, ataqueInimigo, primeiro)

    time.sleep(1)
    print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} recieved {dano} damage!\n")
    time.sleep(1)
    return dano

# ATAQUES DE STATUS
# pokemon atacante, pokemon defesa, ataque,  defesa e ataque origem(pokedex,team,duelist)
def ataquestatus(atacantepoke, defesapoke, ataque, defendente, ataqueori):
    # aplicar os efeitos
    if ataque == "GROWL":
        pokemons.effects[defendente]["GROWL"] = 8
        pokemons.effects[defendente]["origatack"] = pokemons.pokedex[defesapoke]["ATTACK_POWER"]
        print(f"{typecolor(pokemons.pokedex[defesapoke]['TYPE'])}{defesapoke}{basic} attack fell!")
        time.sleep(1)
    elif ataque == "STRING SHOT":
        pokemons.effects[defendente]["STRING SHOT"] = 2
        pokemons.effects[defendente]["origspeed"] = pokemons.pokedex[defesapoke]["SPEED"]
        print(f"{typecolor(pokemons.pokedex[defesapoke]['TYPE'])}{defesapoke}{basic} speed fell!")
        time.sleep(1)
    elif ataque == "LEECH SEED":
        pokemons.effects[defendente]["LEECH SEED"] = 4
        print(f"{typecolor(pokemons.pokedex[defesapoke]['TYPE'])}{defesapoke}{basic} was seeded!")
        time.sleep(1)
    elif ataque == "POISON POWDER":
        pokemons.effects[defendente]["POISON POWDER"] = 8
        print(f"{typecolor(pokemons.pokedex[defesapoke]['TYPE'])}{defesapoke}{basic} was poisoned!")
        time.sleep(1)
    elif ataque == "CHARM":
        pokemons.effects[defendente]["CHARM"] = 2
        pokemons.effects[defendente]["origatack"] = pokemons.pokedex[defesapoke]["ATTACK_POWER"]
        print(f"{typecolor(pokemons.pokedex[defesapoke]['TYPE'])}{defesapoke}{basic} is in love with {typecolor(pokemons.pokedex[atacantepoke]['TYPE'])}{atacantepoke}{basic}")
        time.sleep(1)
    elif ataque == "TAIL WHIP":
        pokemons.effects[defendente]["TAIL WHIP"] = 8
        pokemons.effects[defendente]["origdefense"] = pokemons.pokedex[defesapoke]["DEFENSE"]
        print(
            f"{typecolor(pokemons.pokedex[defesapoke]['TYPE'])}{defesapoke}{basic} defense fell!")
        time.sleep(1)
    elif ataque == "SNOWSCAPE":
        pokemons.effects[ataqueori]["SNOWSCAPE"] = 4
        pokemons.effects[ataqueori]["origdefense"] = pokemons.pokedex[atacantepoke]["DEFENSE"]
        print(
            f"{typecolor(pokemons.pokedex[atacantepoke]['TYPE'])}{atacantepoke}{basic} defense grew!")
        time.sleep(1)
    elif ataque == "DEFENSE CURL":
        pokemons.effects[ataqueori]["DEFENSE CURL"] = 4
        pokemons.effects[ataqueori]["origdefense"] = pokemons.pokedex[atacantepoke]["DEFENSE"]
        print(
            f"{typecolor(pokemons.pokedex[atacantepoke]['TYPE'])}{atacantepoke}{basic} defense grew!")
        time.sleep(1)

# ATIVANDO EFEITOS DE STATUS
# declarar qual o pokemon e se ele é selvagem, do player, ou do duelista (pokedex,team,duelist), pokemon atacante e sua origem
def statuseffects(pokemon, origem, atacapoke, atacaorigem):
    # checando efeitos pre existentes e diminuindo os turnos

    # GROWL
    if "GROWL" in pokemons.effects[origem]:
        pokemons.effects[origem]["GROWL"] -=1
        pokemons.effects[origem]["origatack"] = pokemons.pokedex[pokemon]["ATTACK_POWER"]
        if origem == "pokedex":
            pokemons.pokedex[pokemon]["ATTACK_POWER"] = round(pokemons.effects["pokedex"]["origatack"]/2)
            if pokemons.effects[origem]["GROWL"] == 0:
                pokemons.pokedex[pokemon]["ATTACK_POWER"] = pokemons.effects["pokedex"]["origatack"]
                del pokemons.effects[origem]["GROWL"]
        elif origem == "time":
            pokemons.time[pokemon]["ATTACK_POWER"] = round(pokemons.effects["time"]["origatack"]/2)
            if pokemons.effects[origem]["GROWL"] == 0:
                pokemons.time[pokemon]["ATTACK_POWER"] = pokemons.effects["time"]["origatack"]
                del pokemons.effects[origem]["GROWL"]
        elif origem == "duelist":
            pokemons.duelist[pokemon]["ATTACK_POWER"] = round(pokemons.effects["duelist"]["origatack"] / 2)
            if pokemons.effects[origem]["GROWL"] == 0:
                pokemons.duelist[pokemon]["ATTACK_POWER"] = pokemons.effects["duelist"]["origatack"]
                del pokemons.effects[origem]["GROWL"]
    # STRING SHOT
    if "STRING SHOT" in pokemons.effects[origem]:
        pokemons.effects[origem]["STRING SHOT"] -= 1
        pokemons.effects[origem]["origspeed"] = pokemons.pokedex[pokemon]["SPEED"]
        if origem == "pokedex":
            pokemons.pokedex[pokemon]["SPEED"] = round(pokemons.effects["pokedex"]["origspeed"] / 8)
            if pokemons.effects[origem]["STRING SHOT"] == 0:
                pokemons.pokedex[pokemon]["SPEED"] = pokemons.effects["pokedex"]["origspeed"]
                del pokemons.effects[origem]["STRING SHOT"]
        if origem == "time":
            pokemons.time[pokemon]["SPEED"] = round(pokemons.effects["time"]["origspeed"] / 8)
            if pokemons.effects[origem]["STRING SHOT"] == 0:
                pokemons.time[pokemon]["SPEED"] = pokemons.effects["time"]["origspeed"]
                del pokemons.effects[origem]["STRING SHOT"]
        if origem == "duelist":
            pokemons.duelist[pokemon]["SPEED"] = round(pokemons.effects["duelist"]["origspeed"] / 8)
            if pokemons.effects[origem]["STRING SHOT"] == 0:
                pokemons.duelist[pokemon]["SPEED"] = pokemons.effects["duelist"]["origspeed"]
                del pokemons.effects[origem]["STRING SHOT"]
    # LEECH SEED
    if "LEECH SEED" in pokemons.effects[origem]:
        pokemons.effects[origem]["LEECH SEED"] -= 1
        print(f"{typecolor(pokemons.pokedex[pokemon]['TYPE'])}{pokemon}{basic} was hurt by LEECH SEED!")
        time.sleep(1)
        if origem == "pokedex":
            pokemons.pokedex[pokemon]["HEALTH"] -= round(pokemons.pokedex[pokemon]["MAX_HEALTH"] / 8)
            if pokemons.effects[origem]["LEECH SEED"] == 0:
                del pokemons.effects[origem]["LEECH SEED"]
        if origem == "time":
            pokemons.time[pokemon]["HEALTH"] -= round(pokemons.time[pokemon]["MAX_HEALTH"] / 8)
            if pokemons.effects[origem]["LEECH SEED"] == 0:
                del pokemons.effects[origem]["LEECH SEED"]
        if origem == "duelist":
            pokemons.duelist[pokemon]["HEALTH"] -= round(pokemons.duelist[pokemon]["MAX_HEALTH"] / 8)
            if pokemons.effects[origem]["LEECH SEED"] == 0:
                del pokemons.effects[origem]["LEECH SEED"]
        if atacaorigem == "pokedex":
            pokemons.pokedex[atacapoke]["HEALTH"] += round((pokemons.pokedex[pokemon]["MAX_HEALTH"] / 8)/2)
            if pokemons.pokedex[atacapoke]["HEALTH"] > pokemons.pokedex[atacapoke]["MAX_HEALTH"]:
                pokemons.pokedex[atacapoke]["HEALTH"] = pokemons.pokedex[atacapoke]["MAX_HEALTH"]
        if atacaorigem == "time":
            pokemons.time[atacapoke]["HEALTH"] += round((pokemons.pokedex[pokemon]["MAX_HEALTH"] / 8)/2)
            if pokemons.time[atacapoke]["HEALTH"] > pokemons.pokedex[atacapoke]["MAX_HEALTH"]:
                pokemons.time[atacapoke]["HEALTH"] = pokemons.pokedex[atacapoke]["MAX_HEALTH"]
        if atacaorigem == "duelist":
            pokemons.duelist[atacapoke]["HEALTH"] += round((pokemons.pokedex[pokemon]["MAX_HEALTH"] / 8)/2)
            if pokemons.duelist[atacapoke]["HEALTH"] > pokemons.pokedex[atacapoke]["MAX_HEALTH"]:
                pokemons.duelist[atacapoke]["HEALTH"] = pokemons.pokedex[atacapoke]["MAX_HEALTH"]
    # POISON POWDER
    if "POISON POWDER" in pokemons.effects[origem]:
        pokemons.effects[origem]["POISON POWDER"] -= 1
        print(f"{typecolor(pokemons.pokedex[pokemon]['TYPE'])}{pokemon}{basic} was hurt by POISON!")
        time.sleep(1)
        if origem == "pokedex":
            pokemons.pokedex[pokemon]["HEALTH"] -= round(pokemons.pokedex[pokemon]["MAX_HEALTH"] / 8)
            if pokemons.effects[origem]["POISON POWDER"] == 0:
                del pokemons.effects[origem]["POISON POWDER"]
        if origem == "time":
            pokemons.time[pokemon]["HEALTH"] -= round(pokemons.time[pokemon]["MAX_HEALTH"] / 8)
            if pokemons.effects[origem]["POISON POWDER"] == 0:
                del pokemons.effects[origem]["POISON POWDER"]
        if origem == "duelist":
            pokemons.duelist[pokemon]["HEALTH"] -= round(pokemons.duelist[pokemon]["MAX_HEALTH"] / 8)
            if pokemons.effects[origem]["POISON POWDER"] == 0:
                del pokemons.effects[origem]["POISON POWDER"]
    # CHARM
    if "CHARM" in pokemons.effects[origem]:
        pokemons.effects[origem]["CHARM"] -=1
        pokemons.effects[origem]["origatack"] = pokemons.pokedex[pokemon]["ATTACK_POWER"]
        if origem == "pokedex":
            pokemons.pokedex[pokemon]["ATTACK_POWER"] = round(pokemons.effects["pokedex"]["origatack"] * 2 / 3)
            if pokemons.effects[origem]["CHARM"] == 0:
                pokemons.pokedex[pokemon]["ATTACK_POWER"] = pokemons.effects["pokedex"]["origatack"]
                del pokemons.effects[origem]["CHARM"]
        elif origem == "time":
            pokemons.time[pokemon]["ATTACK_POWER"] = round(pokemons.effects["time"]["origatack"] * 2 / 3)
            if pokemons.effects[origem]["CHARM"] == 0:
                pokemons.time[pokemon]["ATTACK_POWER"] = pokemons.effects["time"]["origatack"]
                del pokemons.effects[origem]["CHARM"]
        elif origem == "duelist":
            pokemons.duelist[pokemon]["ATTACK_POWER"] = round(pokemons.effects["duelist"]["origatack"] * 2 / 3)
            if pokemons.effects[origem]["GROWL"] == 0:
                pokemons.duelist[pokemon]["ATTACK_POWER"] = pokemons.effects["duelist"]["origatack"]
                del pokemons.effects[origem]["GROWL"]
    # TAIL WHIP
    if "TAIL WHIP" in pokemons.effects[origem]:
        pokemons.effects[origem]["TAIL WHIP"] -=1
        pokemons.effects[origem]["origdefense"] = pokemons.pokedex[pokemon]["DEFENSE"]
        if origem == "pokedex":
            pokemons.pokedex[pokemon]["DEFFENSE"] = round(pokemons.effects["pokedex"]["origdefense"] / 2)
            if pokemons.effects[origem]["TAIL WHIP"] == 0:
                pokemons.pokedex[pokemon]["DEFFENSE"] = pokemons.effects["pokedex"]["origdefense"]
                del pokemons.effects[origem]["TAIL WHIP"]
        elif origem == "time":
            pokemons.time[pokemon]["DEFFENSE"] = round(pokemons.effects["time"]["origdefense"] / 2)
            if pokemons.effects[origem]["TAIL WHIP"] == 0:
                pokemons.time[pokemon]["DEFFENSE"] = pokemons.effects["time"]["origdefense"]
                del pokemons.effects[origem]["TAIL WHIP"]
        elif origem == "duelist":
            pokemons.duelist[pokemon]["DEFFENSE"] = round(pokemons.effects["duelist"]["origdefense"] / 2)
            if pokemons.effects[origem]["TAIL WHIP"] == 0:
                pokemons.duelist[pokemon]["DEFFENSE"] = pokemons.effects["duelist"]["origdefense"]
                del pokemons.effects[origem]["TAIL WHIP"]
        # SNOWSCAPE
        if "SNOWSCAPE" in pokemons.effects[origem]:
            pokemons.effects[origem]["SNOWSCAPE"] -= 1
            pokemons.effects[origem]["origdefense"] = pokemons.pokedex[pokemon]["DEFENSE"]
            if origem == "pokedex":
                pokemons.pokedex[pokemon]["DEFFENSE"] += round(pokemons.effects["pokedex"]["origdefense"] / 2)
                if pokemons.effects[origem]["SNOWSCAPE"] == 0:
                    pokemons.pokedex[pokemon]["DEFFENSE"] = pokemons.effects["pokedex"]["origdefense"]
                    del pokemons.effects[origem]["SNOWSCAPE"]
            elif origem == "time":
                pokemons.time[pokemon]["DEFFENSE"] += round(pokemons.effects["time"]["origdefense"] / 2)
                if pokemons.effects[origem]["SNOWSCAPE"] == 0:
                    pokemons.time[pokemon]["DEFFENSE"] = pokemons.effects["time"]["origdefense"]
                    del pokemons.effects[origem]["SNOWSCAPE"]
            elif origem == "duelist":
                pokemons.duelist[pokemon]["DEFFENSE"] += round(pokemons.effects["duelist"]["origdefense"] / 2)
                if pokemons.effects[origem]["SNOWSCAPE"] == 0:
                    pokemons.duelist[pokemon]["DEFFENSE"] = pokemons.effects["duelist"]["origdefense"]
                    del pokemons.effects[origem]["SNOWSCAPE"]
        # DEFENSE CURL
        if "DEFENSE CURL" in pokemons.effects[origem]:
            pokemons.effects[origem]["DEFENSE CURL"] -= 1
            pokemons.effects[origem]["origdefense"] = pokemons.pokedex[pokemon]["DEFENSE"]
            if origem == "pokedex":
                pokemons.pokedex[pokemon]["DEFFENSE"] += round(pokemons.effects["pokedex"]["origdefense"] / 2)
                if pokemons.effects[origem]["DEFENSE CURL"] == 0:
                    pokemons.pokedex[pokemon]["DEFFENSE"] = pokemons.effects["pokedex"]["origdefense"]
                    del pokemons.effects[origem]["DEFENSE CURL"]
            elif origem == "time":
                pokemons.time[pokemon]["DEFFENSE"] += round(pokemons.effects["time"]["origdefense"] / 2)
                if pokemons.effects[origem]["DEFENSE CURL"] == 0:
                    pokemons.time[pokemon]["DEFFENSE"] = pokemons.effects["time"]["origdefense"]
                    del pokemons.effects[origem]["DEFENSE CURL"]
            elif origem == "duelist":
                pokemons.duelist[pokemon]["DEFFENSE"] += round(pokemons.effects["duelist"]["origdefense"] / 2)
                if pokemons.effects[origem]["DEFENSE CURL"] == 0:
                    pokemons.duelist[pokemon]["DEFFENSE"] = pokemons.effects["duelist"]["origdefense"]
                    del pokemons.effects[origem]["DEFENSE CURL"]

# resetar os efeitos
def reset(pokemon, origem):
    if origem == "pokedex":
        if "origatack" in pokemons.effects[origem]:
            pokemons.pokedex[pokemon]["ATTACK_POWER"] = pokemons.effects[origem]["origatack"]
        if "origspeed" in pokemons.effects[origem]:
            pokemons.pokedex[pokemon]["SPEED"] = pokemons.effects[origem]["origspeed"]
        if "origdefense" in pokemons.effects[origem]:
            pokemons.pokedex[pokemon]["SPEED"] = pokemons.effects[origem]["origdefense"]
    elif origem == "time":
        if "origatack" in pokemons.effects[origem]:
            pokemons.time[pokemon]["ATTACK_POWER"] = pokemons.effects[origem]["origatack"]
        if "origspeed" in pokemons.effects[origem]:
            pokemons.time[pokemon]["SPEED"] = pokemons.effects[origem]["origspeed"]
        if "origdefense" in pokemons.effects[origem]:
            pokemons.time[pokemon]["SPEED"] = pokemons.effects[origem]["origdefense"]
    for i in range(0, len(pokemons.effects[origem])):
        pokemons.effects[origem].popitem()


# calculo para chance de fugir (calculo pokemon gen 1 e 2)
def fugir(velpoke, velinimigo, tentativas):
    fuga = 0
    den = (velinimigo / 4)
    chancefuga = ((velpoke * 32) / den) + 30 * tentativas
    if chancefuga > 255:
        fuga = 1
    else:
        ran = random.randint(0,255)
        if ran < chancefuga:
            fuga = 1
    return fuga

# libertar um pokemon
def freepoke():
    listaTime = list(pokemons.time.keys())
    valido = 0
    check = ""
    print("Your team is: ")
    while valido != 1:
        for i in range(0, len(listaTime)):
            print(i + 1, "- ", end='')
            print(typecolor(pokemons.pokedex[listaTime[i]]['TYPE']), end='')
            print(listaTime[i], end=': ')
            print(basic, end='')
            print(pokemons.time[listaTime[i]]["HEALTH"], end=' HP\n')
        time.sleep(1)
        pokeChoose = input("\nChoose a POKEMON or CANCEL: ").upper()
        for i in range(0, len(listaTime)):
            check = str(i + 1)
            if pokeChoose == listaTime[i]:
                free = pokeChoose
                valido = 1
            elif pokeChoose == check:
                pokeChoose = listaTime[i]
                free = pokeChoose
                valido = 1
        if pokeChoose == "CANCEL":
            free = "CANCEL"
            return free
            break
        if valido == 0:
            print("Invalid pokemon.")
    return free
# mudar o time
def mudartime(primeiro):
    listaTime = list(pokemons.time.keys())
    valido = 0
    check = ""
    print("Your team is: ")
    while valido != 1:
        for i in range(0, len(listaTime)):
            print(i + 1, "- ", end='')
            print(typecolor(pokemons.pokedex[listaTime[i]]['TYPE']), end='')
            print(listaTime[i], end=': ')
            print(basic, end='')
            print(pokemons.time[listaTime[i]]["HEALTH"], end=' HP\n')
        time.sleep(1)
        pokeChoose = input("\nChoose a POKEMON or CANCEL: ").upper()
        for i in range(0, len(listaTime)):
            check = str(i + 1)
            if pokeChoose == listaTime[i]:
                primeiro = pokeChoose
                valido = 1
            elif pokeChoose == check:
                pokeChoose = listaTime[i]
                primeiro = pokeChoose
                valido = 1
        if pokeChoose == "CANCEL":
            primeiro = primeiro
            return primeiro
            break
        if valido == 0:
            print("Invalid pokemon.")
    return primeiro

# JOGO
print(default)


# escolher o primeiro pokemon
start = 0
while start == 0:
    print("Choose your first pokemon!")
    time.sleep(1)
    print(f"\033[38;2;255;69;0m 1 - CHARMANDER  \033[38;2;0;166;51m2 - BULBASSAUR  \033[38;2;0;119;190m3 - SQUIRTLE{basic}")
    primeiro = input("").upper()
    if primeiro == "1":
        primeiro = "CHARMANDER"
        start = 1
    elif primeiro == "2":
        primeiro = "FROAKIE"
        start = 1
    elif primeiro == "3":
        primeiro = "SQUIRTLE"
        start = 1
    elif primeiro != "CHARMANDER" and primeiro != "BULBASSAUR" and primeiro != "SQUIRTLE":
        print("Invalid option.")
    else:
        start = 1
pokemons.time[primeiro] = pokemons.pokedex[primeiro].copy()
listaAtaques = list(pokemons.time[primeiro]["ATTACKS"])
print(f"You chose {typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}!")
time.sleep(1)
opcoes = "0"
opcoesLuta = ["FIGHT", "BAG", "POKEMON", "RUN"]
escolhas = ["EXPLORE", "DUEL","TEAM", "BAG", "POKE CENTER", "CLOSE GAME"]
wilds = list(pokemons.pokedex.keys())
while opcoes != "CLOSE GAME":
    print("\n-------------------------")
    print("\n\n")
    valido = 0
    check = ""
    while valido != 1:
        for i in range(0, len(escolhas)):
            print(i + 1, "- ", end='')
            print(escolhas[i], end=' ')
        opcoes = input("\nChoose your option: ").upper()
        for i in range(0, len(escolhas)):
            check = str(i + 1)
            if opcoes == escolhas[i]:
                valido = 1
            elif opcoes == check:
                opcoes = escolhas[i]
                valido = 1

    # poke center
    if opcoes == "POKE CENTER":
        for i in (pokemons.time.keys()):
            pokemons.time[i]["HEALTH"] = pokemons.time[i]["MAX_HEALTH"]
        pokemons.bag["POTION"] = 10
        pokemons.bag["POKEBALL"] = 10
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("Thank you for waiting!\nWe've restored your Pokémon to full health.")
        time.sleep(1)

    # mudar o time
    if opcoes == "TEAM":
        listaTime = list(pokemons.time.keys())
        primeiro = mudartime(primeiro)
        print(f"You chose {typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}!")
        time.sleep(1)
        # lista de ataques do pokemon
        listaAtaques = list(pokemons.time[primeiro]["ATTACKS"])

    # mochila
    if opcoes == "BAG":
        listaTime = list(pokemons.time.keys())
        escolhaMochila = mochila()
        if escolhaMochila == "POKEBALL":
            print("You can't use that here!")

        # cura
        elif escolhaMochila == "POTION":
            pokecurado = potionpoke()
            if pokecurado != "CANCEL":
                cura = potionheal(pokecurado)
                if cura != 0:
                    pokemons.time[pokecurado]["HEALTH"] += cura
                    pokemons.bag["POTION"] -= 1

    # sair do jogo
    if opcoes == "CLOSE GAME":
        print("Thanks for playing!")
        time.sleep(3)
        break


    # luta
    if opcoes == "EXPLORE":
        if pokemons.time[primeiro]["HEALTH"] <= 0:
            print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} can't battle!")
            end = 1
        else:

            # escolher um inimigo aleatorio
            inimigo = wilds[random.randint(0, (len(wilds) - 1))]

            # zerando tentativas de fuga
            tryRun = 0
            fuga = 0
            end = 0

            # inimigo aparece
            print(f"Wild {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} appeared!\n")
            time.sleep(1)

            # jogando seu primeiro pokemon
            print(f"Go!{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}!\n")
            time.sleep(1)

            # loop do combate
            while pokemons.pokedex[inimigo]["HEALTH"] > 0:
                print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} health: {pokemons.pokedex[inimigo]['HEALTH']}")
                print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} health: {pokemons.time[primeiro]['HEALTH']}")
                print("\n")
                time.sleep(1)

                # inimigo mais rapido
                if pokemons.pokedex[inimigo]["SPEED"] > pokemons.time[primeiro]["SPEED"]:
                    # status inimigo
                    statuseffects(inimigo, "pokedex", primeiro, "time")
                    if pokemons.pokedex[inimigo]["HEALTH"] <= 0:
                        print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} fainted!")
                        break
                    # ataque do inimigo
                    listaInimigo = list(pokemons.pokedex[inimigo]["ATTACKS"])
                    ataqueInimigo = listaInimigo[random.randint(0,3)]
                    dano = ataqueinimigo(ataqueInimigo)
                    ataquestatus(inimigo, primeiro, ataqueInimigo, "time", "pokedex")
                    pokemons.time[primeiro]["HEALTH"] -= dano

                    print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} health: {pokemons.pokedex[inimigo]['HEALTH']}")
                    print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} health: {pokemons.time[primeiro]['HEALTH']}")
                    time.sleep(1)

                # morte
                if pokemons.time[primeiro]["HEALTH"] <= 0:
                    reset(primeiro, "time")
                    pokemons.time[primeiro]["HEALTH"] = 0
                    print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} fainted!")
                    vivo = 0
                    # trocar de pokeon, se possivel
                    while vivo == 0:
                        pokedown = 0
                        if len(pokemons.time.keys()) > 1:
                            for i in (pokemons.time.keys()):
                                if pokemons.time[i]["HEALTH"] <= 0:
                                    pokedown +=1
                            if pokedown >= len(pokemons.time.keys()):
                                print("All of your Pokemon have fainted!")
                                time.sleep(1)
                                end = 1
                                break
                            primeiro = mudartime(primeiro)
                            if pokemons.time[primeiro]["HEALTH"] <= 0:
                                print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} is unable to battle!")
                                time.sleep(1)
                            else:
                                listaAtaques = list(pokemons.time[primeiro]["ATTACKS"])
                                print(f"Go! {typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}!")
                                time.sleep(1)
                                vivo = 1
                        else:
                            end = 1
                            break
                    if end == 1:
                        break

                # vez do jogador
                turno = 0
                statuseffects(primeiro, "time", inimigo, "pokedex")
                while turno == 0:

                    escolhaLuta = listalutas()

                    if escolhaLuta == "FIGHT":
                        # escolha do ataque
                        ataque = ataquepoke()
                        print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} used {typecolor(pokemons.attacks[ataque]['TYPE'])}{ataque}{basic}!\n")
                        time.sleep(1)

                        # calcular o dano
                        dano = fight(primeiro, ataque, inimigo)

                        print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} recieved {dano} damage!\n")
                        time.sleep(1)
                        pokemons.pokedex[inimigo]["HEALTH"] -= dano
                        ataquestatus(primeiro, inimigo, ataque, "pokedex", "time")
                        turno = 1
                        tryRun = 0
                        if pokemons.pokedex[inimigo]["HEALTH"] <= 0:
                            print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} fainted!")
                            break

                    # trocar pokemon
                    if escolhaLuta == "POKEMON":
                        trocado = 0
                        while trocado == 0:
                            equip = primeiro
                            primeiro = mudartime(primeiro)
                            listaAtaques = list(pokemons.time[primeiro]["ATTACKS"])

                            if equip != primeiro:
                                if pokemons.time[primeiro]["HEALTH"] <= 0:
                                    print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} is unable to battle!")
                                    time.sleep(1)
                                else:
                                    reset(equip,"time")
                                    trocado = 1
                                    tryRun = 0
                                    turno = 1
                                    print(f"Go! {typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}!")
                                    time.sleep(1)
                                    break
                            else:
                                break
                    # abrir a mochila
                    if escolhaLuta == "BAG":
                        listaTime = list(pokemons.time.keys())
                        escolhaMochila = mochila()
                        repetido = 0
                        for i in (pokemons.time.keys()):
                            if i == inimigo:
                                repetido = 1
                        if escolhaMochila == "POKEBALL" and len(pokemons.time.keys()) == 6:
                            print(f"You already have 6 pokemon! Choose one to free?")
                            free = input("YES or NO: ").upper()
                            if free =="YES":
                                print("Choose the POKEMON you want to free")
                                libertar = freepoke()
                                if libertar == "CANCEL":
                                    print()
                                elif libertar == primeiro:
                                    print("You can't free a pokemon that is fighting!")
                                else:
                                    del pokemons.time[libertar]
                        elif escolhaMochila == "POKEBALL" and repetido == 0:
                            turno = 1
                            tryRun = 0
                            pokemons.bag["POKEBALL"] -= 1
                            vidamin = pokemons.pokedex[inimigo]["MAX_HEALTH"] / 3
                            pegarpoke = jogarpokebola(inimigo, pokemons.pokedex[inimigo]["HEALTH"], pokemons.pokedex[inimigo]["MAX_HEALTH"], vidamin)
                            if pegarpoke == 1:
                                pokemons.time[inimigo] = pokemons.pokedex[inimigo].copy()
                                end = 1
                                break
                        elif escolhaMochila == "POKEBALL" and repetido == 1:
                            print(f"You already have a {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic}")
                            break

                        # cura
                        elif escolhaMochila == "POTION":
                            pokecurado = potionpoke()
                            if pokecurado != "CANCEL":
                                cura = potionheal(pokecurado)
                                if cura != 0:
                                    tryRun = 0
                                    pokemons.time[pokecurado]["HEALTH"] += cura
                                    pokemons.bag["POTION"] -= 1
                                    turno = 1
                    # fugir
                    if escolhaLuta == "RUN":
                        turno = 1
                        tryRun += 1
                        fuga = fugir(pokemons.time[primeiro]["SPEED"], pokemons.pokedex[inimigo]["SPEED"], tryRun)
                        if fuga == 1:
                            end = 1
                            reset(primeiro, "time")
                            print(f"Got away safely!")
                            time.sleep(1)
                            break
                        else:
                            time.sleep(1)
                            print("Can't escape!")
                if end == 1:
                    break


                # inimigo mais lento
                if pokemons.pokedex[inimigo]["SPEED"] <= pokemons.time[primeiro]["SPEED"] and pokemons.pokedex[inimigo]["HEALTH"] > 0:
                    print(f"{typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} health: {pokemons.pokedex[inimigo]['HEALTH']}")
                    print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} health: {pokemons.time[primeiro]['HEALTH']}")
                    time.sleep(1)
                    # status inimigo
                    statuseffects(inimigo, "pokedex", primeiro, "time")
                    if pokemons.pokedex[inimigo]["HEALTH"] <= 0:
                        print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} fainted!")
                        break
                    # ataque do inimigo
                    listaInimigo = list(pokemons.pokedex[inimigo]["ATTACKS"])
                    ataqueInimigo = listaInimigo[random.randint(0, 3)]
                    dano = ataqueinimigo(ataqueInimigo)
                    ataquestatus(inimigo, primeiro, ataqueInimigo, "time", "pokedex")
                    pokemons.time[primeiro]["HEALTH"] -= dano
        # FIM DO COMBATE

        # zerar a vida do inimigo apos o combate
        pokemons.pokedex[inimigo]["HEALTH"] = pokemons.pokedex[inimigo]["MAX_HEALTH"]
        reset(inimigo, "pokedex")
        reset(primeiro, "time")

    # combate de 6 x 6
    if opcoes == "DUEL":
        print("A trainer wants to battle!")
        time.sleep(1)
        duel = 0

        # oponente recebe pokemons aleatorios
        while len(pokemons.duelist.keys()) < 6:
            randompoke = wilds[random.randint(0, (len(wilds) - 1))]
            pokemons.duelist[randompoke] = pokemons.pokedex[randompoke].copy()
        timeInimigo = list(pokemons.duelist.keys())
        #inimigo joga um pokemon
        inimigo = timeInimigo[len(timeInimigo) - 1]
        listaInimigo = list(pokemons.duelist[inimigo]["ATTACKS"])
        print(f"Trainer sent out {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic}!")
        time.sleep(1)
        # loop da batalha
        while duel == 0:
            inimigo = timeInimigo[len(timeInimigo) - 1]
            print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} health: {pokemons.duelist[inimigo]['HEALTH']}")
            print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} health: {pokemons.time[primeiro]['HEALTH']}")
            print("\n")
            time.sleep(1)

            # inimigo mais rapido
            if pokemons.duelist[inimigo]["SPEED"] > pokemons.time[primeiro]["SPEED"]:
                # status inimigo
                statuseffects(inimigo, "duelist", primeiro, "time")
                if pokemons.duelist[inimigo]["HEALTH"] <= 0:
                    print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} fainted!")
                    break
                # ataque do inimigo
                ataqueInimigo = listaInimigo[random.randint(0, 3)]
                dano = ataqueinimigo(ataqueInimigo)
                ataquestatus(inimigo, primeiro, ataqueInimigo, "time", "duelist")
                pokemons.time[primeiro]["HEALTH"] -= dano

                print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} health: {pokemons.duelist[inimigo]['HEALTH']}")
                print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} health: {pokemons.time[primeiro]['HEALTH']}")
                time.sleep(1)

            # morte
            if pokemons.time[primeiro]["HEALTH"] <= 0:
                pokemons.time[primeiro]["HEALTH"] = 0
                reset(primeiro, "time")
                print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} fainted!")
                vivo = 0
                # trocar de pokeon, se possivel
                while vivo == 0:
                    pokedown = 0
                    if len(pokemons.time.keys()) > 1:
                        for i in (pokemons.time.keys()):
                            if pokemons.time[i]["HEALTH"] <= 0:
                                pokedown += 1
                        if pokedown >= len(pokemons.time.keys()):
                            print("All of your Pokemon have fainted!")
                            time.sleep(1)
                            duel = 1
                            break
                        primeiro = mudartime(primeiro)
                        if pokemons.time[primeiro]["HEALTH"] <= 0:
                            print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}is unable to battle!")
                            time.sleep(1)
                        else:
                            listaAtaques = list(pokemons.time[primeiro]["ATTACKS"])
                            print(f"Go! {typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}!")
                            time.sleep(1)
                            vivo = 1
                    else:
                        duel = 1
                        break
                if duel == 1:
                    break

            # vez do jogador
            turno = 0
            statuseffects(primeiro, "time", inimigo, "pokedex")
            while turno == 0:

                escolhaLuta = listalutas()

                if escolhaLuta == "FIGHT":
                    # escolha do ataque
                    ataque = ataquepoke()
                    print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} used {typecolor(pokemons.attacks[ataque]['TYPE'])}{ataque}{basic}!\n")
                    time.sleep(1)

                    # calcular o dano
                    dano = fight(primeiro, ataque, inimigo)

                    print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} recieved {dano} damage!\n")
                    time.sleep(1)
                    pokemons.duelist[inimigo]["HEALTH"] -= dano
                    ataquestatus(primeiro, inimigo, ataque, "duelist", "time")
                    turno = 1
                    tryRun = 0
                    if pokemons.duelist[inimigo]["HEALTH"] <= 0:
                        print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} fainted!")
                        break

                # trocar pokemon
                if escolhaLuta == "POKEMON":
                    trocado = 0
                    while trocado == 0:
                        equip = primeiro
                        primeiro = mudartime(primeiro)
                        listaAtaques = list(pokemons.time[primeiro]["ATTACKS"])

                        if equip != primeiro:
                            if pokemons.time[primeiro]["HEALTH"] <= 0:
                                print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} is unable to battle!")
                                time.sleep(1)
                            else:
                                reset(equip, "time")
                                trocado = 1
                                tryRun = 0
                                turno = 1
                                print(f"Go! {typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic}!")
                                time.sleep(1)
                                break
                        else:
                            break
                # abrir a mochila
                if escolhaLuta == "BAG":
                    listaTime = list(pokemons.time.keys())
                    escolhaMochila = mochila()
                    if escolhaMochila == "POKEBALL":
                        print("You can't steal another Trainer's Pokemon!")

                    # cura
                    elif escolhaMochila == "POTION":
                        pokecurado = potionpoke()
                        if pokecurado != "CANCEL":
                            cura = potionheal(pokecurado)
                            if cura != 0:
                                tryRun = 0
                                pokemons.time[pokecurado]["HEALTH"] += cura
                                pokemons.bag["POTION"] -= 1
                                turno = 1
                # fugir
                if escolhaLuta == "RUN":
                    turno = 1
                    tryRun += 1
                    fuga = fugir(pokemons.time[primeiro]["SPEED"], pokemons.duelist[inimigo]["SPEED"], tryRun)
                    if fuga == 1:
                        duel = 1
                        print(f"Got away safely!")
                        time.sleep(1)
                        break
                    else:
                        time.sleep(1)
                        print("Can't escape!")
            if duel == 1:
                break
            # inimigo troca de pokemon/perde
            if pokemons.duelist[inimigo]["HEALTH"] <= 0:
                # tirar pokemon do time inimigo quando ele morre
                timeInimigo.pop()
                # checa se o treinador ainda tem pokemons
                if len(timeInimigo) > 0:
                    # treinador joga outro pokemon
                    inimigo = timeInimigo[len(timeInimigo) - 1]
                    listaInimigo = list(pokemons.duelist[inimigo]["ATTACKS"])
                    print(f"Trainer sent out {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic}!")
                    time.sleep(1)
                else:
                    print("You deafeated the trainer!")
                    duel = 1
                    break


            # inimigo mais lento
            if pokemons.duelist[inimigo]["SPEED"] <= pokemons.time[primeiro]["SPEED"] and pokemons.duelist[inimigo]["HEALTH"] > 0:
                print(f"{typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} health: {pokemons.duelist[inimigo]['HEALTH']}")
                print(f"{typecolor(pokemons.pokedex[primeiro]['TYPE'])}{primeiro}{basic} health: {pokemons.time[primeiro]['HEALTH']}")
                time.sleep(1)
                statuseffects(inimigo, "duelist", primeiro, "time")
                if pokemons.duelist[inimigo]["HEALTH"] <= 0:
                    print(f"Foe {typecolor(pokemons.pokedex[inimigo]['TYPE'])}{inimigo}{basic} fainted!")
                    break
                # ataque do inimigo
                ataqueInimigo = listaInimigo[random.randint(0, 3)]
                dano = ataqueinimigo(ataqueInimigo)
                ataquestatus(inimigo, primeiro, ataqueInimigo, "time", "duelist")
                pokemons.time[primeiro]["HEALTH"] -= dano
        # FIM DO COMBATE


        # Zerar os pokes do treinador
        while len(pokemons.duelist.keys()) > 0:
            pokemons.duelist.popitem()
        reset(primeiro, "time")
