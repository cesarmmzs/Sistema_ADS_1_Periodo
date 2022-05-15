from func import *

clientes = [
    {'Nome': 'Cesar', 'Idade': '24', 'Sexo': 'M'},
    {'Nome': 'Daiana', 'Idade': '23', 'Sexo': 'F'},
    {'Nome': 'Cadu', 'Idade': '29', 'Sexo': 'M'},
    {'Nome': 'Andressa', 'Idade': '29', 'Sexo': 'F'},
    {'Nome': 'Moises', 'Idade': '24', 'Sexo': 'M'},
    {'Nome': 'Adriana', 'Idade': '48', 'Sexo': 'F'}
]
motos = [
    {'Fabricante': 'Honda', 'Modelo': 'XRE 190', 'Ano': '2020', 'Preço': 12000.00},
    {'Fabricante': 'Yamaha', 'Modelo': 'Fazer 250', 'Ano': '2022', 'Preço': 15000.00},
    {'Fabricante': 'Kawasaki', 'Modelo': 'Ninja 400', 'Ano': '2020', 'Preço': 34690.00}
]
vendas = []

linha()
print('\t\t\t\tSISTEMA DE CONCESSIONÁRIA')
linha()

while True:
    print('O que deseja fazer?\n(R) Acessar registros | (V) Acessar vendas')
    action = str(input())
    if len(action) == 0:
        print('Opção inválida!')
# =============================== ACESSANDO REGISTROS =================================================
    elif action in 'rR':
        while True:
            print('(C) Exibir Clientes | (M) Exibir Motocicletas | (L) Exibir Vendas  (R) Retornar')
            res = str(input())  # recebe a resposta
        # ======================= CASO NULO ===============================
            if len(res) == 0:
                print('Opção inválida!')
        # ==================== CASO CLIENTES ============================
            elif res in 'cC':
                listarClientes(clientes)
                linha()
                crud(clientes, motos)
        # ==================== CASO MOTOS ============================
            elif res in 'mM':
                listarMotos(motos)
                linha()
                crud(clientes, motos)
        # =================== CASO VENDAS ============================
            elif res in 'lL':
                listarVendas(vendas)
                linha()
        # =================== CASO RETORNAR ==========================
            elif res in 'rR':
                break
        # ==================== CASO RESPOSTA ERRADA ===================
            else:
                print('Resposta Inválida. Tente novamente com uma resposta válida: ')
                

# =============================== ACESSANDO VENDAS =================================================
    elif action in 'vV':
        while True:
            print('(E) Efetuar uma venda | (B) Buscar uma venda | (R) Retornar à Seção Anterior')
            res = str(input())

            # ======================= CASO NULO ===============================
            if len(res) == 0:
                print('Opção inválida!')
                
            elif res in 'eE':
            # RECEBE ÍNDICE DO CLIENTE DA OPERAÇÃO
                ncliente = str(input('Digite o nome do cliente que comprará a motocicleta: '))
                ic = next((i for i, x in enumerate(clientes) if x["Nome"] == ncliente), None)
                if ic == None:
                    print('Cadastro de cliente inexistente. Verifique os registros.')
                    break
            # RECEBE ÍNDICE DA MOTO DA OPERAÇÃO
                nmoto = str(input('Digite o modelo da moto a ser vendida: '))
                im = next((i for i, x in enumerate(motos) if x["Modelo"] == nmoto), None)
                if im == None:
                    print('Moto inexistente. Verifique os registros.')
                    break
            # CRIAR REGISTRO DE VENDA
                iv = len(vendas)
                for k in clientes[ic]:
                    if k == 'Nome':
                        vendas = [{'Cliente': clientes[ic]["Nome"]}]

                for k in motos[im]:
                    if k == 'Modelo':
                        vendas[iv]['Modelo'] = motos[im]["Modelo"]

                for k in motos[im]:
                    if k == 'Fabricante':
                        vendas[iv]['Fabricante'] = motos[im]["Fabricante"]

                for k in motos[im]:
                    if k == 'Preço':
                        vendas[iv]['Preço'] = motos[im]["Preço"]

                metodo = str(input('Informe qual será o método de pagamento: '))
                vendas[iv]['Método'] = metodo
                
                listarVendas(vendas)

        # ========================= CASO BUSCAR ===========================================
            if res in 'bB':
                modelo = str(input('Informe o modelo da motocicleta: '))
                cliente = str(input('Informe o nome do cliente:'))
                print(next((x for x in vendas if (x["Modelo"] == modelo) and (x["Cliente"] == cliente)), None))
        # ======================== CASO RETORNAR =========================================
            elif res in 'rR':
                break