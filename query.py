import mysql.connector
import streamlit as st

# Connection
conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    db="myDb"
)
c = conn.cursor()

def view_all_data():
    c.execute('SELECT * FROM insurance ORDER BY id ASC')
    data = c.fetchall()  # Usa fetchall() per ottenere i dati
    return data
