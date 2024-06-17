from conexao import conectar


def cadastrar(frota):
    while True:
        veiculo = {}
        veiculo["Nome"] = input("Informe o modelo: ")
        veiculo["Ano"] = int(input("Informe o ano: "))
        veiculo["Valor"] = float(input("Informe o valor: "))
        veiculo["Descricao"] = input("Descrição: ")
        veiculo["Tipo"] = input("Tipo: Okm ou usado? ")

        # frota.append(veiculo)
        con = conectar()
        cursor = con.cursor()

        sql = """insert into veiculo (nome, valor, 
                descricao, tipo) values (%s, %s, %s, %s)"""
        cursor.execute(sql,
            (veiculo["Nome"], 
             veiculo["Valor"],
             veiculo["Descricao"],
             veiculo["Tipo"]))
        con.commit()     

        r = input("Deseja continuar (s/n)? ").lower()        
        if r == 'n':
            break

def listar(frota):
    for c in frota:
        for k, v in c.items():
            print (f"{k}: {v}")
        print('_'*50)

def cadastrarMarca():
    while True:
        nome = input("Informe o nome da marca: ")

        con = conectar()
        cursor = con.cursor()

        sql = "insert into marca (nome) values (%s)"
        cursor.execute( sql, (nome,) )
        con.commit()

        r = input("Deseja continuar (s/n)? ").lower()
        if r == 'n':
            break

def listarVeiculos():
    con = conectar()
    cursor = con.cursor()

    sql = 'select * from veiculo order by nome'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for v in resultado:
        print(v)

        