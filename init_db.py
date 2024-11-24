import sqlite3

conn = sqlite3.connect('diario_de_trading.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS operaciones (
    id INTEGER PRIMARY KEY,
    fecha TEXT,
    tipo TEXT,
    resultado TEXT,
    monto REAL
)
''')
conn.commit()
conn.close()
