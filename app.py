from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.dh1dzr3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route("/member_list", methods=["POST"])
def web_member_list_post():
    name_receive = request.form['name_give']
    board_receive = request.form['board_give']
    date_receive = request.form['date_give']
    doc = {
       'name': name_receive,
       'board': board_receive,
        'date': date_receive
    }
    db.member_list.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/member_list", methods=["GET"])
def web_member_list_get():
   guest_list = list(db.member_list.find({}, {'_id': False}))
   return jsonify({'guest': guest_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)