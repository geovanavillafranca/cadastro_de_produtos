# uic le os elementos na tela, e o QtWidgets monta os elementos na tela
from PyQt5 import uic, QtWidgets
import mysql.connector

# conectando ao banco
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mysql>1234",
    database = "cadastro_produtos"
)


def funcao_principal():
    linha_codigo = formulario.lineEdit.text()
    linha_descricao = formulario.lineEdit_2.text()
    linha_preco = formulario.lineEdit_3.text()

    categoria = ''

    if formulario.radioButton.isChecked():
        categoria = 'Informcatica'
        print(f'Categoria Informática foi selecionado')

    elif formulario.radioButton.isChecked():
        categoria = 'Alimentos'
        print(f'Categoria Alimentos foi selecionado')
    
    else:
        categoria = 'Eletronicos'
        print(f'Categoria Eletronicos foi selecionado')

    print(f'Código: {linha_codigo}')
    print(f'Descrição: {linha_descricao}')
    print(f'Preço: {linha_preco}')

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) values (%s, %s, %s, %s)"
    dados = (str(linha_codigo), str(linha_descricao), str(linha_preco), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()


app = QtWidgets.QApplication([])
# carrega o arquivo
formulario = uic.loadUi("cadastro_produtos.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

