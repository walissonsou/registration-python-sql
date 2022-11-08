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
  linha2= formulario.lineEdit.text()
  
  if formulario.radioButton.isChecked():
    print("Sexo masculino foi selecionado")
  elif formulario.radioButton_2.isChecked():
    print("Sexo feminino foi selecionado")
  else:
    print("Outro sexo foi selecionado")


  print("Nome: ", linha1)
  print("Idade: ", linha2)


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
