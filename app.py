from flask import Flask, render_template, request, redirect, url_for
from pony.orm import db_session, select
from models import db, Proizvod
from datetime import date
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = "YOUR_SECRET_KEY_HERE"

@app.route('/')
@db_session
def index():
    products = select(p for p in Proizvod)[:]

    to_buy_products = select(p for p in Proizvod if p.toBuy)[:]
    to_buy_count = len(to_buy_products)

    return render_template('index.html', products=products, to_buy_count=to_buy_count)

@app.route('/all_products')
@db_session
def all_products():
    products = select(p for p in Proizvod)[:]
    all_types = set(p.type for p in products)
    return render_template('products.html', products=products, display_mode='All Products', all_types=all_types)

@app.route('/to_buy')
@db_session
def to_buy():
    products = select(p for p in Proizvod if p.toBuy)[:]
    all_types = set(p.type for p in products)
    return render_template('products.html', products=products, display_mode='To Buy', all_types=all_types)

@app.route('/add_product', methods=['POST'])
@db_session
def add_product():
    name = request.form['name']
    type = request.form['type']
    expiration = request.form['expiration']
    toBuy = True if request.form.get('toBuy', False) == 'on' else False
    
    if expiration.isdigit():
        expiration = int(expiration)
    else:
        return redirect(request.referrer)
    
    Proizvod(name=name, date=date.today(), type=type, expiration=expiration, toBuy=toBuy)
    db.commit()

    return redirect(request.referrer)

@app.route('/toggle_buy/<int:product_id>')
@db_session
def toggle_buy(product_id):
    product = Proizvod[product_id]
    product.toBuy = not product.toBuy
    db.commit()

    return redirect(request.referrer)

@app.route('/remove_product', methods=['POST'])
@db_session
def remove_product():
    product_id = request.form['productToRemove']
    if product_id.isdigit():
        product = Proizvod.get(id=int(product_id))
        if product:
            product.delete()
            db.commit()
    return redirect(request.referrer)

@app.route('/charts')
@db_session
def charts():
    to_buy_products = select(p for p in Proizvod if p.toBuy)[:]
    types = set(p.type for p in to_buy_products)
    type_count = {type: sum(1 for p in to_buy_products if p.type == type) for type in types}
    pie_labels = list(type_count.keys())
    pie_data = list(type_count.values())
    pie_colors = ['#FF5733', '#33FF57', '#5733FF']

    products = select(p for p in Proizvod)[:]
    dates = sorted(set(p.date for p in products))
    product_count_by_date = [sum(1 for p in products if p.date == d) for d in dates]
    line_labels = [str(d) for d in dates]
    line_data = product_count_by_date

    return render_template('charts.html', 
                           pie_labels=pie_labels, pie_data=pie_data, pie_colors=pie_colors,
                           line_labels=line_labels, line_data=line_data)


if __name__ == '__main__':
    app.run(debug=True)
