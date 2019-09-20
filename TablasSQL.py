import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
  host="localhost",
  user="esantiago",
  passwd="M1n0mbr3",
  database = "QTLs"
)

cursor=mydb.cursor()
#######################################################################
Creación y llenado de tabla con Datos generales de los participantes
######################################################################
cursor.execute("CREATE TABLE Datos_Generales (Persona_ID INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(100), Sexo ENUM('M','H'), Edad INT, Estado VARCHAR(20)")

cursor.execute("SHOW TABLES")
for x in cursor:
  print(x)

data=pd.read_csv('Mediciones.csv', usecols=[0,1,2,3])
for row in data.iterrows():
    sql= "INSERT INTO Datos_Generales (Nombre, Sexo, Edad, Estado) VALUES (%s, %s, %s, %s)"
    values=list(row[1])
    cursor.execute(sql,values)

cursor.execute("SELECT * FROM Datos_Generales")
for x in cursor:
  print(x)

mydb.commit()

########################################################################
#Creación y llenado de tabla con las mediciones de los participantes
#########################################################################
cursor.execute("CREATE TABLE Mediciones (Persona_ID INT, CONSTRAINT Persona_ID_FK FOREIGN KEY (Persona_ID) REFERENCES Datos_Generales(Persona_ID), Medicion_ID INT AUTO_INCREMENT PRIMARY KEY, Tipo VARCHAR(12), Valor FLOAT, No_Medicion INT)")

data=pd.read_csv('/home/esantiago/Clase 30-09/ClassDB/MedicionesMean.csv', usecols=[4,5,6,7,8,9,10,11,12,13,14,15,16,17])

sql= "INSERT INTO Mediciones (Persona_ID,Tipo, Valor, No_Medicion) VALUES (%s, %s, %s, %s)"

for row in data.iterrows():
    values=list(row[1])
    Alt=[]
    Alt.append(row[0]+1)
    Alt.append("Altura")
    Alt.append(values[0])
    Alt.append(1)
    cursor.execute(sql,Alt)
    for i in range(1,6):
        Frente=[]
        Frente.append(row[0]+1)
        Frente.append("Frente")
        Frente.append(values[i])
        Frente.append(i)
        cursor.execute(sql,Frente)
    num=1
    for i in range(6,11):
        Brazo=[]
        Brazo.append(row[0]+1)
        Brazo.append("Brazo")
        Brazo.append(values[i])
        Brazo.append(num)
        num=num+1
        cursor.execute(sql,Brazo)
    for i in range(11,14):
        Med=[]
        Med.append(row[0]+1)
        if(i==11):
            Med.append("Calzado")
            Med.append(values[i])
        if(i==12):
            Med.append("Sistólica")
            Med.append(values[i])
        if(i==13):
            Med.append("Diastólica")
            Med.append(values[i])
        Med.append(1)
        cursor.execute(sql,Med)
mydb.commit()

#cursor.execute("SELECT * FROM Mediciones")
#for x in cursor:
#  print(x)
