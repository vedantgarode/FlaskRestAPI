from flask import Flask , jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    users = [{'id': 1, 'username': 'Alice'}, {'id': 2, 'username': 'Bob'}]
    return jsonify(users)

@app.route('/odd_even/<int:n>')

def odd_even(n):
    data = {"input" : n , "result" : ""}
    if(n % 2==0):
        data["result"] = "Even"
    else:
        data["result"] = "Odd"
    return jsonify(data ) ,200 





if __name__ == '__main__':
    app.run(debug=True )