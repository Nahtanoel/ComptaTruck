from flask import Flask, send_from_directory
from flask import render_template
from flask import request
import os
from dotenv import load_dotenv
import sqlite3
from datetime import datetime

def init():
    import sqlite3
    import os
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE ComptaTruck (numeroFacture number, libelleFacture text, nomFournisseur text, factureHT number, factureTTC number, dateAcquitement date, lienVersfichier text)''')

        conn.commit()
        conn.close()
        print("database created")
    else:
        print("database already exist")


init()

load_dotenv()  # chargement du fichier .env
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('acceuil.html')

@app.route("/ajoutLignes", methods=['GET', 'POST'])
def ajoutLignes():

    if request.method == 'POST':
        try:
            # Convertir la chaîne de date en objet datetime
            dateD = datetime.strptime(request.form['dateD'], '%Y-%m-%d')
            dateD_sqlite  = dateD.strftime('%d/%m/%Y')


            conn = sqlite3.connect('database.db')
            c = conn.cursor()

            unfichier=request.files['fichier']
            # Enregistrez le fichier téléchargé
            unfichier.save('./src/uploads/'+unfichier.filename)


            c.execute(f"INSERT INTO ComptaTruck (numeroFacture,libelleFacture,nomFournisseur,factureHT,factureTTC,dateAcquitement,lienVersfichier) VALUES ({request.form['numFact']},\"{request.form['libFact']}\",\"{request.form['nomFournisseur']}\",{request.form['factureHT']},{request.form['factureTTC']},\"'{dateD_sqlite}'\",\"{unfichier.filename}\")")
            conn.commit()
            conn.close()
            return render_template('succes.html')
        except Exception as err:
            print(err)
            
            return render_template('failed.html')
    
    else:
        return render_template('depot.html')


@app.route("/table")
def show_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ComptaTruck")
    data = c.fetchall()
    conn.close()
    return render_template('table.html', data=data)


@app.route("/download/<string:file_name>")
def download_file(file_name):
    return send_from_directory("./uploads/", file_name, as_attachment=True)