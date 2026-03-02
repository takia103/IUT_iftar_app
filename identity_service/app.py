identity_service/app.py:

from flask import Flask, request, jsonify
import sqlite3, jwt, time
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
SECRET = "iftar-secret"

def conn():
    return sqlite3.connect("students.db")

@app.route("/login", methods=["POST"])
def login():
    data=request.json
    c=conn()
    cur=c.cursor()
    cur.execute("SELECT password_hash,budget FROM students WHERE student_id=?",(data["student_id"],))
    row=cur.fetchone()
    c.close()

    if not row:
        return jsonify({"error":"Invalid"}),401
    if not check_password_hash(row[0],data["password"]):
        return jsonify({"error":"Invalid"}),401

    token=jwt.encode({"student":data["student_id"],"exp":time.time()+3600},SECRET,algorithm="HS256")
    return jsonify({"token":token,"budget":row[1]})

@app.route("/deduct",methods=["POST"])
def deduct():
    data=request.json
    c=conn()
    cur=c.cursor()
    cur.execute("UPDATE students SET budget=budget-? WHERE student_id=?",(data["amount"],data["student_id"]))
    c.commit()
    c.close()
    return jsonify({"status":"ok"})

@app.route("/add_student",methods=["POST"])
def add():
    d=request.json
    c=conn()
    cur=c.cursor()
    cur.execute("INSERT INTO students VALUES (?,?,?)",
        (d["student_id"],generate_password_hash(d["password"]),d["budget"]))
    c.commit()
    c.close()
    return jsonify({"added":True})

@app.route("/health")
def health():
    return jsonify({"service":"identity","status":"online","time":time.time()})

app.run(port=5001,debug=True)
