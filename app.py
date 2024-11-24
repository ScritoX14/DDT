from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('diario_de_trading.db')

@app.route('/')
def index():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM operaciones')
    operaciones = c.fetchall()
    conn.close()
    return render_template('index.html', operaciones=operaciones)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        fecha = datetime.now().strftime("%Y-%m-%d")
        tipo = request.form['tipo']
        resultado = request.form['resultado']
        monto = float(request.form['monto'])
        
        conn = connect_db()
        c = conn.cursor()
        c.execute("INSERT INTO operaciones (fecha, tipo, resultado, monto) VALUES (?, ?, ?, ?)",
                  (fecha, tipo, resultado, monto))
        conn.commit()
        conn.close()
        return redirect('/')
    
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
