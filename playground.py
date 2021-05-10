from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/play')
@app.route('/play/<int:number>')
@app.route('/play/<int:number>/<string:color>')
def times(number = 3, color = 'blue'):
    return render_template('play.html', color = color, number = number)

if __name__=="__main__":
    app.run(debug=True)