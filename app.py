from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/buy-sell')
def buy_sell():
    items = [
        {'name': 'Blue Gem Lock', 'logo': 'BGL.png'},
        {'name': 'Black Gem Lock', 'logo': 'BBGL.png'}
    ]
    return render_template('buy_sell.html', items=items)

@app.route('/contact')
def contact():
    links = [
        {'name': 'WhatsApp', 'url': 'https://wa.me/6287770085140'},
        {'name': 'Discord', 'url': 'https://discord.com/users/1087472588344803478'},
        {'name': 'Server and Testimoni', 'url': 'https://discord.com/invite/nbK8XG8HFr'},
    ]
    return render_template('contact.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
