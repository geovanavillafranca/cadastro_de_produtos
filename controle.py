# uic le os elementos na tela, e o QtWidgets monta os elementos na tela
from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

# --- conectando ao banco --- #
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mysql>1234",
    database="cadastro_produtos"
    )


# --- metodos --- #

def gerar_pdf():
    cursor = banco.cursor()
    comandoSQL = "SELECT * FROM produtos"
    cursor.execute(comandoSQL)
    dados_lidos = cursor.fetchall()

    # cordenada para escrever no PDF
    y = 0

    # iniciando o PDF
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    # posicao       x    y
    pdf.drawString(200, 800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)

    # descricao das colunas
    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "CODIGO")
    pdf.drawString(210, 750, "PRODUTO")
    pdf.drawString(310, 750, "PRECO")
    pdf.drawString(410, 750, "CATEGORIA")

    # o Y é para escrever os dados e ir pulando uma linha toda vez que voltar no for
    for i in range(0, len(dados_lidos)):
        y += 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410, 750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO")




def funcao_principal():
    linha_codigo = formulario.lineEdit.text()
    linha_descricao = formulario.lineEdit_2.text()
    linha_preco = formulario.lineEdit_3.text()

    categoria = ''

    if formulario.radioButton.isChecked():
        categoria = 'Informcatica'
        print(f'Categoria Informática foi selecionado')

    elif formulario.radioButton_2.isChecked():
        categoria = 'Alimentos'
        print(f'Categoria Alimentos foi selecionado')
    
    else:
        categoria = 'Eletronicos'
        print(f'Categoria Eletronicos foi selecionado')

    print(f'Código: {linha_codigo}')
    print(f'Descrição: {linha_descricao}')
    print(f'Preço: {linha_preco}')

    # mandando os dados para o banco
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) values (%s, %s, %s, %s)"
    dados = (str(linha_codigo), str(linha_descricao), str(linha_preco), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()

    # limpando os campos
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


def chama_tela_lista():
    # abre a tela
    tela_listagem.show()

    # vamos executar o código dentro do banco
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM produtos")
    # pega o que foi executado no execute
    dados_lidos = cursor.fetchall()

    # definindo as colunas
    tela_listagem.tableWidget.setRowCount(len(dados_lidos))
    tela_listagem.tableWidget.setColumnCount(5)

    # mostrando na tabela
    for r in range(0, len(dados_lidos)):
        for c in range(0, 5):
            tela_listagem.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(dados_lidos[r][c])))



app = QtWidgets.QApplication([])
# carrega o arquivo
formulario = uic.loadUi("cadastro_produtos.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.show()
# chamando o botao listar
formulario.pushButton_2.clicked.connect(chama_tela_lista)

# tela de listagem
tela_listagem = uic.loadUi("listar_dados.ui")
tela_listagem.pushButton.clicked.connect(gerar_pdf)
app.exec()

