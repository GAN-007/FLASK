form flask import Flask,render_template,request,redirect,url_for
 app =Flask(__name__)
app.secret_key = 'any random string'

 @app.route('/',methods=['GET','POST'])
 def home():
    if 'username' in session:
        username = session['username']
        return 'Logged in as '+ username + ' <br>' + \
            "<b><a href = '/logout'>Click here to log out</a></b>"
    return "Your not logged in <br><a href ='/login '></b>" + \
            "Click here to log in </b></a>" 



 @app.route('/login',methods=['GET','POST'])
 def login():
     if request.method =='POST':
         session['username'] = request.form['username']
         return redirect(url_for('home'))
     return  '''

     <form action = "" method ='POST' :>
            <p><input type =text  name = username /></p>
            <p><input type =submit  value = login /></p>
            </form>

            '''
            

 @app.route('/logout')
 def logout():
     session.pop('username',None)
     return redirect(url_for('home'))
