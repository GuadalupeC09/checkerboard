from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def play():
    return render_template('index.html')
@app.route('/play/<num>')
def repeat_play(num):
    return render_template('index.html', num=8)

# @app.route('/play/<int:times>/<color>')
# def repeat_play_color(times):
#     return render_template('index.html', times=times)




if __name__ == "__main__":
    app.run(debug=True)