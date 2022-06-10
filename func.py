from tkinter import *

def linha():
    print('=-'*45)


def listarMotos(a):
    global op_obj
    op_obj = 'motos'

    linha()
    print('\t\t\t\t\t\tMOTOCICLETAS')
    linha()
    n = 'Nº do Registro'
    print(f'{n: <15}', end='')
    for k in a[0].keys():
        print(f'{k: >15}', end='')
    print('')
    linha()
    for i in range(0, (len(a))):
        print(f'{i + 1: <15}', end='')
        for v in a[i].values():
            print(f'{v: >15}', end='')
        print('')


def listarClientes(a):
    global op_obj
    op_obj = 'clientes'

    linha()
    print('\t\t\t\t\tCLIENTES')
    linha()
    n = 'Nº do Registro'
    print(f'{n: <15}', end='')
    for k in a[0].keys():
        print(f'{k: >15}', end='')
    print('')
    linha()
    for i in range(0, (len(a))):
        print(f'{i + 1: <15}', end='')
        for v in a[i].values():
            print(f'{v: >15}', end='')
        print('')


def listarVendas(a):
    global op_obj
    op_obj = 'vendas'

    linha()
    print('\t\t\t\t\tVENDAS')
    linha()
    n = 'Nº da Venda'
    print(f'{n: <15}', end='')
    for k in a[0].keys():
        print(f'{k: >15}', end='')
    print('')
    linha()
    for i in range(0, (len(a))):
        print(f'{i + 1: <15}', end='')
        for v in a[i].values():
            print(f'{v: >15}', end='')
        print('')

def crud(a, b):
    # ============================== CRUD ========================
    while True:
        print('\nO que deseja fazer?\t(R)Registrar\t(L)Ler\t(A)Atualizar\t(D)Deletar\t(V)Retornar\nDigite uma operação: ', end='')
        res = str(input())
        # ======================= CASO NULO ===============================
        if len(res) == 0:
            print('Opção inválida!')
        # ==================== CASO REGISTRAR =============================
        elif res in 'rR':
            if op_obj == 'clientes':
                print('Digite abaixo o nome, idade e sexo do novo cliente:')
                nome = str(input('Nome: '))
                idade = str(input('Idade: '))
                sexo = str(input('Sexo(M ou F): '))

                a.append({'Nome': nome, 'Idade': idade, 'Sexo': sexo})
                listarClientes(a)

            elif op_obj == 'motos':
                print('Digite abaixo o fabricante, modelo, ano e preço da nova motocicleta:')
                fab = str(input('Fabricante: '))
                modelo = str(input('Modelo: '))
                ano = int(input('Ano: '))
                preco = float(input('Preço: '))

                b.append({'Fabricante': fab, 'Modelo': modelo, 'Ano': ano, 'Preço': preco})
                listarMotos(b)
        # ==================== CASO LER ===================================
        elif res in 'lL':
            i = int(input('Digite o número do registro que deseja ler: '))
            i = i - 1
            if op_obj == 'clientes':
                for k, v in a[i].items():
                    print(f'{k}: {v}')
                linha()
            elif op_obj == 'motos':
                for k, v in b[i].items():
                    print(f'{k}: {v}')
                linha()
            else:
                print('ERRO!')
                quit()
        # ================== CASO DELETAR ==================================
        elif res in 'dD':
            i = int(input('Digite o número do registro que deseja deletar: '))
            i = i - 1
            if op_obj == 'clientes':
                a.pop(i)
                listarClientes(a)
            elif op_obj == 'motos':
                b.pop(i)
                listarMotos(b)
            else:
                print('ERRO!')
                quit()
        # ================= CASO ATUALIZAR ================================
        elif res in 'aA':
            i = int(input('Digite o número do registro que deseja atualizar: '))
            i = i - 1
            if op_obj == 'clientes':
                print('Digite os novos valores:')
                nome = str(input('Nome: '))
                idade = str(input('Idade: '))
                sexo = str(input('Sexo(M ou F): '))

                a[i] = ({'Nome': nome, 'Idade': idade, 'Sexo': sexo})
                listarClientes(a)
            elif op_obj == 'motos':
                print('Digite os novos valores:')
                fab = str(input('Fabricante: '))
                modelo = str(input('Modelo: '))
                ano = int(input('Ano: '))
                preco = float(input('Preço: '))

                b[i] = ({'Fabricante': fab, 'Modelo': modelo, 'Ano': ano, 'Preço': preco})
                listarMotos(b)
            else:
                print('ERRO!')
                quit()
        # ==================== CASO VOLTAR ==============================
        elif res in 'vV':
            break
        # ==================== CASO INVÁLIDA ============================
        else:
            print('Opção inválida!')

