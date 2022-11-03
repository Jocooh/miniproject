from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/members/1')
def member_1_home():
   return render_template('member_ksm.html')

@app.route('/members/2')
def member_2_home():
   return render_template('member_khj.html')

@app.route('/members/3')
def member_3_home():
   return render_template('member_pjs.html')

@app.route('/members/4')
def member_4_home():
   return render_template('member_lyj.html')

@app.route('/members/5')
def member_5_home():
   return render_template('member_jsa.html')

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.dh1dzr3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 김성민 방명록
@app.route("/members/1/board", methods=["POST"])
def web_member1_post():
    name_receive = request.form['name_give']
    board_receive = request.form['board_give']
    date_receive = request.form['date_give']
    doc = {
       'name': name_receive,
       'board': board_receive,
        'date': date_receive
    }
    db.member1.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/members/1/board", methods=["GET"])
def web_member1_get():
   guest_list = list(db.member1.find({}, {'_id': False}))
   return jsonify({'guest': guest_list})

# 김혜진 방명록
@app.route("/members/2/board", methods=["POST"])
def web_member2_post():
    name_receive = request.form['name_give']
    board_receive = request.form['board_give']
    date_receive = request.form['date_give']
    doc = {
       'name': name_receive,
       'board': board_receive,
        'date': date_receive
    }
    db.member2.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/members/2/board", methods=["GET"])
def web_member2_get():
   guest_list = list(db.member2.find({}, {'_id': False}))
   return jsonify({'guest': guest_list})

# 박진산 방명록
@app.route("/members/3/board", methods=["POST"])
def web_member3_post():
    name_receive = request.form['name_give']
    board_receive = request.form['board_give']
    date_receive = request.form['date_give']
    doc = {
       'name': name_receive,
       'board': board_receive,
        'date': date_receive
    }
    db.member3.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/members/3/board", methods=["GET"])
def web_member3_get():
   guest_list = list(db.member3.find({}, {'_id': False}))
   return jsonify({'guest': guest_list})

# 이유정 방명록
@app.route("/members/4/board", methods=["POST"])
def web_member4_post():
    name_receive = request.form['name_give']
    board_receive = request.form['board_give']
    date_receive = request.form['date_give']
    doc = {
       'name': name_receive,
       'board': board_receive,
        'date': date_receive
    }
    db.member4.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/members/4/board", methods=["GET"])
def web_member4_get():
   guest_list = list(db.member4.find({}, {'_id': False}))
   return jsonify({'guest': guest_list})

# 조성아 방명록
@app.route("/members/5/board", methods=["POST"])
def web_member5_post():
    name_receive = request.form['name_give']
    board_receive = request.form['board_give']
    date_receive = request.form['date_give']
    doc = {
       'name': name_receive,
       'board': board_receive,
        'date': date_receive
    }
    db.member5.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

@app.route("/members/5/board", methods=["GET"])
def web_member5_get():
   guest_list = list(db.member5.find({}, {'_id': False}))
   return jsonify({'guest': guest_list})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
