from flask import Flask,request,jsonify
import threading,time

app=Flask(__name__)

orders={}
metrics={"requests":0,"errors":0}

def process(oid):
    stages=["Pending","Stock Verification","Cooking","Ready"]
    for s in stages:
        orders[oid]["status"]=s
        time.sleep(3)

@app.route("/order",methods=["POST"])
def create():
    metrics["requests"]+=1
    oid=len(orders)+1
    orders[oid]={"id":oid,"status":"Pending"}
    threading.Thread(target=process,args=(oid,)).start()
    return jsonify({"order_id":oid})

@app.route("/status/<int:oid>")
def status(oid):
    return jsonify(orders[oid])

@app.route("/metrics")
def m():
    return jsonify(metrics)

@app.route("/health")
def h():
    return jsonify({"service":"order","status":"online","time":time.time()})

app.run(port=5002,debug=True)
