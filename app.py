from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about me')
def about():
    return render_template('about.html')

@app.route('/New')
def New():
    return render_template('New.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/activities2')
def activities2():
    return render_template('activities2.html')

@app.route('/service')
def product_service():
    return render_template('service.html')

@app.route('/Concrete_truck_brand')
def Concrete_truck_brand_service():
    return render_template('Concrete_truck_brand.html')

@app.route('/cement_products')
def cement_products():
    return render_template('cement_products.html')

@app.route('/Selling products')
def Selling_products():
    return render_template('Selling_products.html')

if __name__ == '__main__':
    app.run(debug=True)