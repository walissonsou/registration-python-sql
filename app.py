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

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
