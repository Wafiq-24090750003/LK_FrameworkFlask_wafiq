from flask import Flask, render_template

app = Flask(__name__)

app_name="Aplikasi Python Flask saya.Mahasiswa BISDIG:Radikal,Smart,Sipakatau"

#1 Apk Route Hello World!
@app.route("/")
def hello_world():
    return "<p>Hello, World! I am a Flask App,How Are You?</p>"

#2 Apk Route Aplikasi ke halaman lebih spesifik
@app.route("/Aplikasi/")
def Aplikasi():
    return "<p> Hello Teman-teman, ini aplikasi Python Flask saya sebagai mahasiswa:)</p>"

#3 Apk Route ke halaman HTML yang mantap
@app.route("/page/mantap/")
def mantap():
    return render_template("mantap.html")

#4 Apk Route ke halaman HTML yang mantap part full
@app.route("/page/mantap/full/")
def mantap_name():
    return render_template("mantap part 2.html")


#5 Apk Route Dinamis 
@app.route('/page/mantap/<string:nama>')
def get_nama(nama):
    return "nama anda adalah {}".format(nama)

#6 Apk Route variabel Global
@app.route("/global/")
def global_name():
    return f"Nama Aplikasi{app_name}"

#7 Apk Route  Variabel Local
@app.route("/local/")
def local_name():
    user={
        "name":"Wafiq",
        "age":19,
        "gender":"Perempuan"
    }
    return render_template("local.html", user=user)

#8 Apk Route Menampilkan List Nama di HTML
@app.route('/users')
def users():
    user_list = ["Nur", "Cae", "Irma", "Alya"]
    return render_template('users.html', users=user_list)


#9 Apk Route Menampilkan Pesan Berdasarkan Skor
@app.route('/nilai/<int:score>')
def nilai(score):
    return render_template('nilai.html', score=score)



if __name__ == "__main__":
    app.run(debug=True)




    