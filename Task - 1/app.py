from flask import Flask, request, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return render_template("home_page.html")

@app.route('/about')
def about():
    return "This is about page"

@app.route('/magic')
def add():
    a = 1
    b = 2
    sum = a+b
    return str(sum)

@app.route('/add')
def addition():
    var1 = int(request.args.get('a'))
    var2 = int(request.args.get('b'))
    summ = var1 + var2
    return str(summ)

@app.route('/signin')
def signup():
    return render_template("signup.html")

@app.route('/thankyou', methods=['POST'])
def thankyou():
    return render_template("thankyou.html")



if __name__ == "__main__":
    app.run(debug=True)