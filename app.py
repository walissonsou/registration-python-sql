from PyQt5 import uic, QtWidgets
from reportlab.pdfgen import canvas
import mysql.connector

# criar uma variavel que recebe o mysql.connector 
# para conectar ao BANCO DE DADOS.

banco = mysql.connector.connect(
  host='localhost', 
  user="root",
  passwd="",
  database="super_hero"
)

def funcao_principal():
  linha1= formulario.lineEdit.text()
  linha2= formulario.lineEdit_2.text()  
  escolha = ""
  sexo = ""
  if formulario.buttonman.isChecked() :    
    sexo="Masculino"
  elif formulario.buttonwomen.isChecked() :    
    sexo="Feminino"
  else:    
    sexo="Outro"
  
  if formulario.buttonsuper.isChecked():      
    escolha="superman"
  elif formulario.buttonbatman.isChecked():   
    escolha='batman'
    

  print("Nome: ", linha1)
  print("Idade: ", linha2)  
  print("Sexo:", sexo)
  print("Heroi", escolha)
 
  cursor = banco.cursor()
  comando_SQL = "INSERT INTO herois (nome,idade,sexo,escolha) VALUES (%s, %s, %s, %s)"
  dados = (str(linha1), int(linha2), escolha, sexo)
  cursor.execute(comando_SQL, dados)
  banco.commit()
  
  formulario.lineEdit.setText("")
  formulario.lineEdit_2.setText("")

def chama_segunda_tela():
    segunda_tela.show()
    ## lendo os dados do banco
    cursor = banco.cursor()    
    comando_SQL = "SELECT * FROM herois"
    cursor.execute(comando_SQL)    
    
    ## mostrando os dados do banco
    #método fetchall pega tudo que foi feito no cursor execute, salvo isso na variavel dados_lidos
    dados_lidos = cursor.fetchall()    
    # RouCount - quantas linhas vou ter na tela
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
     # setcolumnCount - quantas colunas
    segunda_tela.tableWidget.setColumnCount(5)
      ## pecorrendo uma matriz
    for i in range(0, len(dados_lidos)):
      for j in range(0,5):
        segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))   
    
def porcentagem():    
    cursor = banco.cursor()
    comando_RESUMOSQL= "Select sexo, count(sexo) from herois group by sexo having count('superman' or 'batman')"        
    cursor.execute(comando_RESUMOSQL)    
    dados_lidos = cursor.fetchall()   
    
    segunda_tela.tableWidget_2.setRowCount(len(dados_lidos))
     # setcolumnCount - quantas colunas
    segunda_tela.tableWidget_2.setColumnCount(2)
    
    for i in range(0, len(dados_lidos)):
      for j in range(0,2):
        segunda_tela.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))   
    
    
def gerar_pdf():     
    cursor = banco.cursor()   
    comando_SQL = "SELECT * FROM herois"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()     
    y = 0
    pdf = canvas.Canvas("escolhas_superheroi.pdf")
    pdf.setFont("Arial", 12)
    pdf.drawString(200,800, "Produtos cadastrados: ")
    pdf.setFont('Arial', 18)
    
    pdf.drawString(10,750, "ID")
    pdf.drawString(100,750, "NAME")
    pdf.drawString(200,750, "AGE")
    pdf.drawString(300,750, "TEAM")
    pdf.drawString(400,750, "SEX")
    
    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(100,750 -y, str(dados_lidos[i][1]))
        pdf.drawString(200,750 -y, str(dados_lidos[i][2]))
        pdf.drawString(300,750 -y, str(dados_lidos[i][3]))
        pdf.drawString(400,750 -y, str(dados_lidos[i][4]))
    
    pdf.save()
    print('PDF GERADO COM SUCESSO')

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_datas.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(porcentagem)

formulario.show()
app.exec()
