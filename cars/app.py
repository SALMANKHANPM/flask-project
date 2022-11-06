from email.policy import default
from importlib.metadata import requires
# import re
from this import d
from urllib import request
from wsgiref.simple_server import demo_app
from flask import Flask, render_template, redirect, request,url_for
from Cars_Database import Cars_Database
app = Flask(__name__)


@app.route('/reviews')
def reviews():
    
    return render_template('review page.html')

@app.route('/services')
def services():
    
    return render_template('services page.html')

@app.route('/services2')
def services2():
    
    return render_template('services page 2.html')

@app.route('/kodiAQ')
def kodiAQ():
    
    return render_template('skoda kodiAQ.html')


@app.route('/kodiAQpay')
def kodiAQpay():
    
    return render_template('purchasepage.html')


@app.route('/rapid')
def rapid():
    
    return render_template('skoda rapid.html')

@app.route('/rapidpay')
def rapidpay():
    
    return render_template('purchasepage.html')

@app.route('/polo')
def polo():
    
    return render_template('polo.html')

@app.route('/polopay')
def polopay():
    
    return render_template('purchasepage.html')

@app.route('/jetta')
def jetta():
    
    return render_template('jetta.html')

@app.route('/jettapay')
def jettapay():
    
    return render_template('purchasepage.html')

@app.route('/verna')
def verna():
    
    return render_template('verna.html')

@app.route('/vernapay')
def vernapay():
    
    return render_template('purchasepage.html')

@app.route('/creta')
def creta():
    
    return render_template('creta.html')

@app.route('/cretapay')
def cretapay():
    
    return render_template('purchasepage.html')


@app.route('/city')
def city():
    
    return render_template('city.html')

@app.route('/citypay')
def citypay():
    
    return render_template('purchasepage.html')


@app.route('/civic')
def civic():
    
    return render_template('civic.html')

@app.route('/civicpay')
def civicpay():
    
    return render_template('purchasepage.html')


@app.route('/ecosport')
def ecosport():
    
    return render_template('ecosport.html')

@app.route('/ecosportpay')
def ecosportpay():
    
    return render_template('purchasepage.html')


@app.route('/endeavour')
def endeavour():
    
    return render_template('endeavour.html')

@app.route('/endeavourpay')
def endeavourpay():
    
    return render_template('purchasepage.html')


@app.route('/fortuner')
def fortuner():
    
    return render_template('fortuner.html')

@app.route('/fortunerpay')
def fortunerpay():
    
    return render_template('purchasepage.html')


@app.route('/innova')
def innova():
    
    return render_template('innova.html')

@app.route('/innovapay')
def innovapay():
    
    return render_template('purchasepage.html')


@app.route('/seltos')
def seltos():
    
    return render_template('seltos product details.html')

@app.route('/seltospay')
def seltospay():
    
    return render_template('purchasepage.html')

@app.route('/sonet')
def sonet():
    
    return render_template('sonet product details.html')

@app.route('/sonetpay')
def sonetpay():
    
    return render_template('purchasepage.html')

@app.route('/carnival')
def carnival():
    
    return render_template('carnival product  details.html')

@app.route('/carnivalpay')
def carnivalpay():
    
    return render_template('purchasepage.html')

@app.route('/register')
def register():
    
    return render_template('Signuppage.html')
@app.route('/audiq7')
def audiq7():
    
    return render_template('audi-q7.html')

@app.route('/audiq7pay')
def audiq7pay():
    
    return redirect(url_for('purchasepage'))

@app.route('/audiq3')
def audiq3():
    
    return render_template('audi-q3.html')

@app.route('/audiq3pay')
def audiq3pay():
    
    return render_template('purchasepage.html')

@app.route('/audia4')
def audia4():
    
    return render_template('audi-a4.html')


@app.route('/audia4pay')
def audia4pay():
    
    return render_template('purchasepage.html')
@app.route('/purchasepage',methods=['POST','GET'])
def purchasepage():
    if request.method=='POST':
        email=request.form.get("email")
        firstname=request.form.get("fname")
        lastname=request.form.get("lname")
        gender=request.form.get("gender")
        date=request.form.get("date")
        month=request.form.get("month")
        year=request.form.get("year")
        cardmethod=request.form.get("cardmethod")
        cardnumber=request.form.get("cardnumber")
        cardcv=request.form.get("cardcv")
        cars_database = Cars_Database()
        
        
        val=cars_database.payment(email,firstname,lastname,gender,date,month,year,cardnumber,cardmethod,cardcv)
        if val==True:
            return render_template('purchasepage.html')
        else:
             return render_template('purchasepage.html')
        
        # redirect('/login')
        
    elif request.method == 'GET':
        
        return render_template('purchasepage.html')

#
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    
    
    if request.method == 'POST':
        
        default_value = 0
        email = request.form.get('Email', default_value)
        password = request.form.get('Password', default_value)
        
        if(email == 0 or password == 0):
            
            print("couldn't find the elements")
            
        cars_database = Cars_Database()
        
        result = cars_database.add_user(email, password)
        
        if(result == True):
            
            return redirect('/login')
        else:
            return redirect('/signup')
        
    elif request.method == 'GET':
        
        return render_template('SignupPage.html')






@app.route('/contact')
def contact():
    
    return render_template('contact us page.html')


    


@app.route('/')
def home():
    
    print("redirected")
    return render_template('project 4 index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if(request.method == 'GET'):
        
        return render_template('login.html')
    
    elif(request.method == 'POST'):
        
        return redirect('/')

if __name__ == "__main__":
      
    app.run(host='0.0.0.0', debug=True)
