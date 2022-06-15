import mysql.connector

class Model:
    def connect(self):
        return mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = "", 
            database = "tugasdb"
        )

    def read(self):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("SELECT * FROM db_karyawan")
        return cur.fetchall()
    
    #metode pada model yang digunakan untuk menyisipkan data
    def create(self,nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji):
        con =Model.connect(self)
        cur = con.cursor()
        sql =("INSERT INTO db_karyawan (nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        data=(nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji)
        cur.execute(sql,data)
        con.commit()
        return True

    #metode ini digunakan untuk mengambil semua nilai pada sebuah data yang dipilih
    def readbyid(self,id_karyawan):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("SELECT * FROM db_karyawan WHERE nik = %s",(id_karyawan,))
        return cur.fetchall()

    #metode pada yang digunakan untuk menyimpan data hasil perubahan ke basis data.
    def update(self,nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji,id_karyawan):
        con  = Model.connect(self)
        cur  = con.cursor()
        sql  = ("UPDATE db_karyawan SET nik=%s,nama=%s,jenis_kelamin=%s,tglMAsuk=%s,jabatan=%s,divisi=%s, gaji=%s WHERE nik = %s")
        data = (nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji,id_karyawan,)
        cur.execute(sql,data)
        con.commit()
        return True
    def detile(self,nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji,id_karyawan):
        con  = Model.connect(self)
        cur  = con.cursor()
        sql  = ("UPDATE db_karyawan SET nik=%s,nama=%s,jenis_kelamin=%s,tglMAsuk=%s,jabatan=%s,divisi=%s, gaji=%s WHERE nik = %s")
        data = (nik,nama,jenis_kelamin,tglMasuk,jabatan,divisi,gaji,id_karyawan,)
        cur.execute(sql,data)
        con.commit()
        return True

    #model yang memiliki query untuk menghapus data 
    def delete(self,id_karyawan):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("DELETE FROM db_karyawan WHERE nik = %s",(id_karyawan,))
        con.commit()
        return True
    
    def login(self,email,pasword):
        con = Model.connect(self)
        cur = con.cursor()
        cur.execute("SELECT * FROM db_user where email = %s and pasword = %s", (email, pasword))
        result = cur.fethcone()
        return result


    def hit(self,jabatan):
        con = Model.connect(self)
        cur=con.cursor
        cur.execute("SELECT COUNT jabatan FROM db_karyawann")
       
