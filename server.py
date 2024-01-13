from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'shh its a secret'

@app.route('/')
def visits():
    if "count" not in session:
        session["count"]=1
    else:
        session["count"]+=1
    return render_template("index.html")

@app.route('/plus_two', methods=['POST'])
def plus_two():
    customize=int(request.form.get("custom", 1))
    if request.form["change"]=="add":
        session["count"] += customize
    elif request.form["change"]=="restart":
        session["count"] = 0
    return redirect("/")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")








if __name__=="__main__":  
    # app.run(debug=True)
    app.run(debug=True, host="localhost", port=8000)