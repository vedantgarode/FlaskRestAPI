from flask import Flask , jsonify , redirect, url_for, request ,render_template
import requests as rs
import json

app = Flask(__name__)
app.template_folder = "templates"
@app.route("/")
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    PARAMS = {"access_token" : "admin1122"}
    api_response = rs.get(url = 'https://spartex.pythonanywhere.com/get_users' , params= PARAMS).text
    data = json.loads(api_response)


    username = request.form['username']
    password = request.form['password']


    if(username == "admin" and  password== "admin"):
        table_data = (( user['id'], user['username'], user['password']) for user in data["data"])
        heading = ("ID" , "Username" , "Password")
        return render_template("table.html", heading = heading , data = table_data)
    else :
        for user_data in data['data']:
            if user_data['username'] == username:
                if(user_data['password'] == password):
                    return render_template("profile.html" , id =user_data["id"] , username = user_data['username'] , password = user_data['password'] )
                
    return "<h1> Wrong Credentials <h1>"
app.run(debug=True);