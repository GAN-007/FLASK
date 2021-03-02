from flask import Flask,redirect,url_for

app=Flask(__name__)


@app.route('/admin')
def admin():
    return 'Hello Admin'

@app.route('/guest/<ges>')
def guest(ges):
     return 'Hello %s as Guest' % ges




@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('admin'))
   else:
      return redirect(url_for('guest' , ges = name))


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)

