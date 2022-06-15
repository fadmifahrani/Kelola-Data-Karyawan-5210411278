from flask import Flask, render_template,session, request, flash,redirect,url_for
from model import Model
from flask_mysqldb import MySQL
app = Flask (__name__)
db = Model()

app.secret_key= "1234566789"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='tugasdb'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form:
        email = request.form['inpEmail']
        passwd = request.form['inpPass']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM db_user where email = %s and pasword = %s", (email, passwd))
        result = cur.fetchone()
        if result:
            session['is_logged_in'] = True
            session['username'] = result[1]
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    if 'is_logged_in' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route("/registrasi",methods=["GET","POST"])
def regis():
    if request.method == 'GET':
        return render_template('registrasi.html')
    else:
        nama=request.form['nama']
        email=request.form['email']
        pasword=request.form['pw']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO db_user(nama,email,pasword) VALUES(%s,%s,%s)",(nama,email,pasword))
        registrasi = mysql.connection.commit()
        cur.close()
        session['nama'] = request.form['nama']
        session['password'] = request.form['pw']

        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('is_logged_out',None)
    session.pop('username', None)
    return redirect(url_for('login'))
          
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    dt = db.read()
    ddt = db.hit
    return render_template('dashboard.html',data = dt, dat = ddt)

@app.route('/edit', methods=["GET", "POST"])
def edit():
    dt=db.read()
    return render_template("edit.html", data = dt)

@app.route('/tambah')
def add():
    return render_template('add.html')

#metode pada app yang mana metode ini nantinya akan mengeksekusi metode tambah data yang ada pada model.
@app.route('/tambahkaryawan', methods =['POST','GET'])
def addkaryawan():
    if request.method == 'POST' and request.form['submit']:
        nik           = request.form['nik']
        nama          = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        tglMasuk      = request.form['tglMasuk']
        jabatan       = request.form['jabatan']
        divisi        = request.form['divisi']
        gaji          = request.form['gaji']
    
        if db.create(nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji):
            flash('Data Tersimpan')
        else:
            flash('Data Gagal Disimpan')
        return redirect(url_for('edit'))
    else:
        return redirect(url_for('edit'))
        
#metode pada app yang digunakan untuk mengeksekusi metode readbyid yang ada pada model
@app.route('/update/<int:id_karyawan>')
def update(id_karyawan):
    dt = db.readbyid(id_karyawan)
    session ['update'] = id_karyawan
    return render_template('update.html', data = dt)

@app.route('/detile/<int:id_karyawan>')
def detile(id_karyawan):
    dt = db.readbyid(id_karyawan)
    session ['detile'] = id_karyawan
    return render_template('detile.html', data = dt)

@app.route('/detilekaryawan', methods = ['POST','GET'])
def detilekaryawan():
    if  request.method== 'POST' and request.form['detile']:
        nik           = request.form['nik']
        nama          = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        tglMasuk      = request.form['tglMasuk']
        jabatan       = request.form['jabatan']
        divisi        = request.form['divisi']
        gaji          = request.form['gaji']
        
        if db.detile(nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji,session['detile']):
            flash('Data Berubah')
        else:
            flash('Data Gagal Berubah')
        
        return redirect(url_for('edit'))
    else:
        return redirect(url_for('edit'))

#metode yang digunakan untuk mengeksekusi metode update yang ada pada model
@app.route('/updatekaryawan', methods = ['POST','GET'])
def updatekaryawan():
    if  request.method== 'POST' and request.form['update']:
        nik           = request.form['nik']
        nama          = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        tglMasuk      = request.form['tglMasuk']
        jabatan       = request.form['jabatan']
        divisi        = request.form['divisi']
        gaji          = request.form['gaji']
        
        if db.update(nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji,session['update']):
            flash('Data Berubah')
        else:
            flash('Data Gagal Berubah')
        
        return redirect(url_for('edit'))
    else:
        return redirect(url_for('edit'))

#metode pada app untuk mengeksekusi metode hapus data yang ada pada model s
@app.route('/deletekaryawan/<int:id_karyawan>', methods=['POST','GET'])
def deletekaryawan(id_karyawan):
    if request.method =='GET':
        if db.delete(id_karyawan):
            flash('Terhapus')
        else :
            flash ('Gagal terhapus')
        
        return redirect(url_for('edit'))
if __name__ == '__main__':
    app.run(debug=True)