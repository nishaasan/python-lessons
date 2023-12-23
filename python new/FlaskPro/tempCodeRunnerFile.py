from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
#MYSQL CONNECTION
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="123456"
app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)
