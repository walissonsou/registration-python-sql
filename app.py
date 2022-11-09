from PyQt5 import uic, QtWidgets
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
    print(dados_lidos)
    
    
  
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_datas.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)

formulario.show()
app.exec()
