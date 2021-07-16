from flask import *

app = Flask(__name__)


@app.route('/')
def item_list():
    return render_template('items.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5050, debug=True)
