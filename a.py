#-------- Ínicio das variaveis globais--------
lista_colaborador= [] 
id_global= 0

#-------- Fim das variaveis globais--------

#-------- Ínicio de cadastrar_colaborador()--------
def cadastrar_colaborador(id):
    print('---------Bem vindo(a) ao menu de Cadastrar Colaborador.---------')
    print('Id do colaborador: {}' .format(id))
    nome = input('Digite o Nome do colaborador: ')
    setor = input('Digite o Setor do colaborador: ')
    salario = int(input('Digite o Sálario do colaborador: '))
    dicionario_colaborador={'id'      :   id,
                            'nome'    :  nome,
                            'setor'   :  setor,
                            'salario' : salario}
    print('---------------------------------------------------------------')
    lista_colaborador.append(dicionario_colaborador.copy())
#-------- Fim de cadastrar_colaborador()--------

#-------- Ínicio de consultar_colaborador()--------
def consultar_colaborador():
    print('--------Bem vindo(a) ao menu de Consultar Colaborador.---------')
    while True:
        opcao_consultar= input('Escolha a opção desejada: \n' +
                            '1- Consultar Todos \n' +
                            '2- Consultar por Id \n' +
                            '3- Consultar por Setor \n' +
                            '4- Retornar ao menu \n' +
                            '>>')
        print('***************************************************************')
        if opcao_consultar== '1':
            print('Você escolheu a opção Consultar Todos os Colaboradores.')
            for colaborador in lista_colaborador: #colaborador vai varrer toda a lista de colaboradores
                print('-----------------------------------------------')
                for key, value in colaborador.items(): #varrer todos os conjuntos chave e valor do dicionario colaborador
                    print('{}:  {}' .format(key, value))
                print('-----------------------------------------------')
        elif opcao_consultar=='2':
           print('Você escolheu a opção Consultar por Id.') 
           id_desejado= int(input('Entre com o Id desejado: '))
           for colaborador in lista_colaborador:
               if colaborador ['id']== id_desejado: #o valor do campo id desse dicionario é igual o id desejado
                    print('-----------------------------------------------')
                    for key, value in colaborador.items(): #varrer todos os conjuntos chave e valor do dicionario colaborador
                        print('{}:  {}' .format(key, value))
                    print('-----------------------------------------------')
        elif opcao_consultar == '3':
            print('Você escolheu a opção Consultar por Setor.')
            setor_desejado= input('Entre com o Setor desejado: ')
            for colaborador in lista_colaborador:
               if colaborador ['setor']== setor_desejado: #o valor do campo id desse dicionario é igual o id desejado
                    print('-----------------------------------------------')
                    for key, value in colaborador.items(): #varrer todos os conjuntos chave e valor do dicionario colaborador
                        print('{}:  {}' .format(key, value))
                    print('-----------------------------------------------')
        elif opcao_consultar == '4':
            return #sai da função consultar_produto e volta para o main
        else:
            print('Opção inválida, tente novamente. ')
            continue
#-------- Fim de consultar_colaborador()--------

#-------- Ínicio de remover_colaborador()--------
def remover_colaborador():
    print('-------Bem vindo(a) ao menu de Remover Colaborador.-------')
    id_desejado= int(input('Entre com o Id do Colaborador que deseja remover: '))
    for colaborador in lista_colaborador:
        if colaborador ['id']== id_desejado: #o valor do campo id desse dicionario é igual o id desejado
            lista_colaborador.remove(colaborador)
            print('COLABORADOR REMOVIDO.')
            print('-----------------------------------------------------------')
#-------- Fim de remover_colaborador()--------

#-------------- Ínicio main-------------
print('--------------------------------------------------------------')
print('Bem vindo(a) ao Controle de Colaboradores da Maria Eduarda. ')
print('--------------------------------------------------------------')
while True:
    opcao_principal= input('Escolha a opção desejada: \n' +
                           '1- Cadastrar Colaborador \n' +
                           '2- Consultar Colaborador(es) \n' +
                           '3- Remover Colaborador \n' +
                           '4- Encerrar programa \n' +
                           '>>')
    print('***************************************************************')
    if opcao_principal== '1':
            id_global= id_global + 1 
            cadastrar_colaborador(id_global)
    elif opcao_principal=='2':
        consultar_colaborador()
    elif opcao_principal == '3':
        remover_colaborador()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida, tente novamente. ')
        continue
#-------- Fim de main--------





