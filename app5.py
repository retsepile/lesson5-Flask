from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/showitems', methods=['POST'])
def showitems():
    Item_Name = request.form['Name']
    Item_ID = request.form['id']
    Quantity = request.form['Quantity']
    Price = request.form['Price']
    total_price = int(Price)*int(Quantity)
    return render_template('/item_list.html',
                           Item_Name=Item_Name,
                           Item_ID=Item_ID,
                           Quantity=Quantity,
                           Price=Price,
                           total=total_price
                           )


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
