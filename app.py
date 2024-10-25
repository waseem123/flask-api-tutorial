from flask import Flask,request
import bikecontroller as controller
from bike import Bike

app = Flask(__name__)

@app.route('/bikes')
def getbikes():
    return controller.getallbikes()

@app.route("/bikes/<int:id>")
def getBike(id):
    return controller.getBike(id)

@app.route("/bikes/add",methods=['GET','POST'])
def addBike():
    name = request.form['name']
    desc = request.form['desc']
    model = request.form['model']
    img = request.form['img']
    price = request.form['price']
    
    b = Bike()
    b.setbikename(name)
    b.setbikedesc(desc)
    b.setbikemodel(model)
    b.setbikeimage(img)
    b.setbikeprice(price)
    return controller.addBike(b)