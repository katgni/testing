from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def root():
  return render_template('navbar_root.html') 

@app.route("/albums/")
def page1():
  return render_template('navbar_albums.html')

@app.route("/artists/")
def page2():
  return render_template('navbar_artists.html')

@app.route("/genre/")
def page3():
  return render_template('navbar_genre.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
