from flask import Flask,render_template,request
import json
from flask_mail import Mail
with open('config.json','r') as c:
    parameter=json.load(c)['params']
app=Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=parameter['email'],
    MAIL_PASSWORD=parameter['password'],
)
mail=Mail(app)
@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('msg')
        mail.send_message("New Message From "+str(name),sender=email,recipients=[parameter['email'],email],body=message)
    return render_template('index.html',parameter=parameter)

app.run(debug=True)