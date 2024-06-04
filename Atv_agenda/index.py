# ATIVIDADE AGENDA ELETRÔNICA

"""
Criar uma agenda eletrônica, em Python que armazene em uma lista nome, telefone, empresa em que trabalha. 
Criar um Menu com as seguintes opções:  

1- Adicionar Contato  
2- Excluir Contato  
3- Listar todos os Contatos  
4- Alterar Contato  
5- Listar dados de um determinado contato 
6- Sair  

"""
print('\nprograma que simula uma agenda eletrônica\n')
#abrindo a agenda
agenda = []
i = 1

while i != 0:
    #menu
    print("\nAGENDA ELETRÔNICA\n")
    print("1- Adicionar Contato")
    print("2- Excluir Contato")
    print("3- Listar todos os Contatos")
    print("4- Alterar Contato")
    print("5- Listar dados de um determinado contato")
    print("6- Sair")
    opcao = input("Escolha uma opção: ")


   #opção para adicionar o contato
    if opcao == '1':
        nomes = input("Nome: ")
        telefones = input("Telefone: ")
        empresas = input("Empresa: ")
        agenda.append([nomes, telefones, empresas])
        print("Contato adicionado")
    
    #opção para excluir contato
    elif opcao == '2':
        nomes = input("Nome do contato a ser excluído: ")
        contatoAgenda = False
        for contato in agenda:
            if contato[0].lower() == nomes.lower():
                agenda.remove(contato)
                print("Contato excluído")
                contatoAgenda = True
                break
        if not contatoAgenda:
            print("Contato não encontrado!")

    #opção para listar contatos
    elif opcao == '3':
        if not agenda:
            print("Nenhum contato na agenda.")
        else:
            print("\nLista de Contatos: ")
            for contato in agenda:
                print(f"Nome: {contato[0]}, Telefone: {contato[1]}, Empresa: {contato[2]}")


    #opção para alterar dados do contato
    elif opcao == '4':
        nome = input("Nome do contato a ser alterado: ")
        contatoAgenda = False
        for contato in agenda:
            if contato[0].lower() == nomes.lower():
                contato[1] = input(f"Novo telefone (antigo: {contato[1]}): ")
                contato[2] = input(f"Nova empresa (antiga: {contato[2]}): ")
                print("Contato alterado")
                contatoAgenda = True
                break
        if not contatoAgenda:
            print("Contato não encontrado!")


    #opção para listar dados de um contato específico
    elif opcao == '5':
        nomes = input("Nome do contato: ")
        contatoAgenda = False
        for contato in agenda:
            if contato[0].lower() == nomes.lower():
                print(f"Nome: {contato[0]}, Telefone: {contato[1]}, Empresa: {contato[2]}")
                contatoAgenda = True
                break
        if not contatoAgenda:
            print("Contato não encontrado!")


    #opção para sair da agenda
    elif opcao == '6':
        print("Saindo da agenda eletrônica.")
        break

    else:
        print("Opção inválida! Tente novamente.")