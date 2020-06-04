from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                     

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_orders():

    ordername_receive = request.form['ordername_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    order = {
        'ordername' : ordername_receive,
        'number' : number_receive,
        'address' : address_receive,
        'phone' : phone_receive
    }

    db.orders.insert_one(order)

    return jsonify({'result':'success', 'msg': '주문 작성이 완료되었습니다!'})


@app.route('/orders', methods=['GET'])
def read_orders():

    orders = list(db.orders.find({}, {'_id':0}))

    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)