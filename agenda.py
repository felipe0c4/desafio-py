import time

numeros = [
    {"nome": "joao", "numero": 1998581044, "favorito": True}
]

while True:

    a = int(input("Bem Vindo a sua agenda!! \n"
                  "Oque deseja fazer: \n"
                  "[1] Contatos \n"
                  "[2] Favoritos \n"))
    if a == 1:
        contatos = int(input("Selecione umas das opções: \n"
                             "[1] Ver contatos \n"
                             "[2] Adicionar contatos \n"
                             "[3] Apagar contatos \n"))

        if contatos == 1:
            print(f"Contatos: \n")
            for num in numeros:
                print(f"Nome: {num["nome"]} Numero: {num["numero"]} \n")
            time.sleep(2)
        if contatos == 2:
            nome = str(input("Qual o nome do contato: "))
            numero = int(input("Qual o numero: "))
            favorito = int(input("Adicionar aos Favoritos: \n"
                                    "[1] Sim \n"
                                    "[2] Não \n"))
            fav = False
            if favorito == 1:
                fav = True
            elif favorito == 2:
                fav = False
            numeros.append(
                {"nome": nome, "numero": numero, "favorito": fav}
            )

        if contatos == 3:
            contato_atual = -1
            print("Contatos: \n")
            for num in numeros:
                contato_atual += 1
                print(f"[{contato_atual}] Nome: {num["nome"]} Numero: {num["numero"]}")
            qualdeletar = int(input("Qual deseja Apagar: "))
            del numeros[qualdeletar]
            print(numeros)

    elif a == 2:
        favoritos = int(input("[1] Ver contatos Favoritos \n"
                              "[2] Adicionar contatos ao Favoritos \n"
                              "[3] Remover dos favoritos \n"))
        if favoritos == 1:
            contato_atual = -1
            for num in numeros:
                if num["favorito"] == True:
                    print(f"Nome: {num["nome"]} Numero: {num["numero"]}")
            time.sleep(2)
        if favoritos == 2:
            contato_atual = -1
            print("Contatos: \n")
            for num in numeros:
                contato_atual += 1
                if num["favorito"] == False:
                    print(f"[{contato_atual}] Nome: {num["nome"]} Numero: {num["numero"]}")
            qualfavoritar = int(input("Qual deseja Apagar: "))
            numeros[qualfavoritar]["favorito"] = True
            print(numeros)
        if favoritos == 3:
            contato_atual = -1
            print("Contatos: \n")
            for num in numeros:
                contato_atual += 1
                if num["favorito"] == True:
                    print(f"{contato_atual} Nome: {num["nome"]} Numero: {num["numero"]} \n")
            qualdesfavoritar = int(input("Qual deseja Apagar: \n"))
            numeros[qualdesfavoritar]["favorito"] = False
            print(numeros)
