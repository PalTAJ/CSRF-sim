from flask import jsonify, request
from random import random,randint
from flask import request, Response, render_template, Flask, redirect, make_response, url_for
from cachetools import TTLCache

from .products_operations import search_products, add_products, USAdapter
from ..app import app

# from ..models import db, Products, Customers, Transactions







cache = TTLCache(maxsize=10, ttl=86400)
## ttl represnt the time in seconds the data will be saved in the cache


users_data = {'taj@dofo.com':['Taj Saleh','123456'],
              'erva@gmail.com':['Ervanur dundar','123456'],
              'ayse@gmail.com':['Ayse Can','123456'],
              'akif@gmail.com':['akif idkwhat','123456']}

@app.route('/')
def MainLogin():

    if 'UserCookie' not in dict(cache):
        return render_template("index.html")
    else:
        return render_template('main.html')


@app.route('/error')
def error():
    return render_template('loginError.html')



@app.route('/dc', methods=['POST'])
def delete_cookie():
    ''' to immediately delete cookie navigate to thiss'''

    cache.clear()
    return redirect(url_for('MainLogin'))



@app.route('/login', methods=['POST'])
def login_enpoint():
    # if len(list(cache.keys())) == 0:
    #     return redirect(url_for('MainLogin'))

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

    if email in users_data and password == users_data[email][1]:

        value = str(randint(10000,1000000000))
        cache['UserCookie'] = value
        cache['email'] = email

        return redirect(url_for('mainPage'))

    else:
        return redirect(url_for('error'))


@app.route('/viewprofile',methods=['POST','GET'])
def profile():
    if 'UserCookie' not in dict(cache):
        return redirect(url_for('MainLogin'))
    else:

        cookie = cache['UserCookie']
        email = cache['email']
        fname = users_data[email][0].split(' ')[0]
        lname = users_data[email][0].split(' ')[1]
        password = users_data[email][1]

        resp = make_response(render_template('profile.html', fname=fname,lname = lname, email=email,password=password))
        return resp



@app.route('/change-password',methods=['POST','GET'])
def changePass():

    if 'UserCookie' not in dict(cache):
        return redirect(url_for('MainLogin'))
    else:
        cookie = cache['UserCookie']
        email = cache['email']

        if request.method == "POST":
            password = request.form['password']
            users_data[email][1] = password

        cache.clear()
        return redirect(url_for('MainLogin'))



@app.route('/change-email',methods=['POST','GET'])
def changeMail():

    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        cookie = cache['UserCookie']
        email = cache['email']

        if request.method == "POST":
            email2 = request.form['email'] ## receive new email
            name = users_data[email][0] # save name
            password = users_data[email][1] # save password
            del users_data[email] # delete dict key -  the old email
            users_data[email2] = [name,password] # add new item to dictionary with new email and old info

        cache.clear()
        return redirect(url_for('MainLogin'))




# ///////////////////////////
# no need to look below for this project.


@app.route('/searchdb-products', methods=['POST', 'GET'])
def searchDB_product():

    keyword  = request.form['data'].strip()
    if len(keyword) == 0:
        keyword = '--empty--'
    result = USAdapter(keyword).search_prod()
    print(result)

    return render_template('result_table.html',result=result)


@app.route('/adddb-products', methods=['POST', 'GET'])
def addDB_product():

    data = dict(request.form)
    result = USAdapter(data['product_name'][0]).search_prod()
    if len(result) == 0:
        add_products(data)

    return render_template('main.html')


@app.route('/main', methods=['POST', 'GET'])
def mainPage():
    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        dicte  = dict(request.form)
        if '1' in dicte:
            # return render_template('main_switch.html')
            return render_template('main.html')

        elif '2' in dicte:
            return render_template('main.html')
        else:
            return render_template('main.html')


@app.route('/add-customers', methods=['POST', 'GET'])
def add_customer():
    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        return render_template('add_customers.html')


@app.route('/add-products', methods=['POST', 'GET'])
def add_product():
    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        return render_template('add_products.html')


@app.route('/add-trans', methods=['POST', 'GET'])
def add_tran():
    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        return render_template('add_trans.html')


@app.route('/search-customers', methods=['POST', 'GET'])
def search_customer():
    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        return render_template('search_customers.html')


@app.route('/search-products', methods=['POST', 'GET'])
def search_product():
    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        return render_template('search_products.html')


@app.route('/search-trans', methods=['POST', 'GET'])
def search_tran():
    if 'UserCookie' not in list(cache.keys()):
        return redirect(url_for('MainLogin'))
    else:
        return render_template('search_trans.html')


