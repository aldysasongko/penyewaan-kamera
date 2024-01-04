from cgitb import text
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import Frame, Label, Text, Button, StringVar, Radiobutton, ttk, Tk, END
import qrcode
import MySQLdb

def simpan():
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    insertdt = db.cursor()
    try:
        sql_input = "insert into datasewa(No_Antrian, Nama_Lengkap, Alamat, Email, Type_Kamera, Merk_Kamera, Keperluan) value('"+e_antri.get()+"','"+e_nama.get()+"', '"+e_almt.get()+"', '"+e_mail.get()+"', '"+r.get()+"', '"+c_merk.get()+"', '"+r2.get()+"')"
        insertdt.execute(sql_input)
        db.commit()
        messagebox.showinfo("Sukses", "Data berhasil disimpan")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Error: {str(e)}")
    finally:
        db.close()

def edit():
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    edit_cursor = db.cursor()
    try:
        sql_edit = "UPDATE datasewa SET Nama_Lengkap=%s, Alamat=%s, Email=%s, Type_Kamera=%s, Merk_Kamera=%s, Keperluan=%s WHERE No_Antrian=%s"
        edit_cursor.execute(sql_edit, (e_nama.get(), e_almt.get(), e_mail.get(), r.get(), c_merk.get(), r2.get(), e_antri.get()))
        db.commit()
        messagebox.showinfo("Sukses", "Data berhasil diupdate")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Error: {str(e)}")
    finally:
        db.close()

def hapus():
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    cursor = db.cursor()
    try:
        no_antrian = e_antri.get()
        sql_delete = f"DELETE FROM datasewa WHERE No_Antrian = '{no_antrian}'"
        cursor.execute(sql_delete)
        db.commit()
        messagebox.showinfo("Sukses", "Data berhasil dihapus")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Error: {str(e)}")
    finally:
        db.close()

def edit1():
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    edit_cursor = db.cursor()
    try:
        sql_edit = "UPDATE datatransaksi SET Tgl_Pinjam=%s, Tgl_Kembali=%s, Pembayaran=%s WHERE No_Antrian=%s"
        edit_cursor.execute(sql_edit, (e_pinjam.get(), e_kembali.get(), c_metode.get(), e_antri1.get()))
        db.commit()
        messagebox.showinfo("Sukses", "Data berhasil diupdate")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Error: {str(e)}")
    finally:
        db.close()

def hapus1():
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    cursor = db.cursor()
    try:
        no_antrian = e_antri1.get()
        sql_delete1 = f"DELETE FROM datatransaksi WHERE No_Antrian = '{no_antrian}'"
        cursor.execute(sql_delete1)
        db.commit()
        messagebox.showinfo("Sukses", "Data berhasil dihapus")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Error: {str(e)}")
    finally:
        db.close()

def simpan1():
    global e_antri1, e_pinjam, e_kembali, c_metode
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    insertdt = db.cursor()
    try:
        sql_input1 = "insert into datatransaksi(No_Antrian, Tgl_Pinjam, Tgl_Kembali, Pembayaran) value('"+e_antri1.get()+"','"+d_pinjam.get()+"', '"+d_kembali.get()+"', '"+c_metode.get()+"')"
        insertdt.execute(sql_input1)
        db.commit()
        messagebox.showinfo("Sukses", "Data berhasil disimpan")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Error: {str(e)}")
    finally:
        db.close()

def lihat():
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    cursor = db.cursor()
    no_antrian = e_antri.get()
    sql_select = f"SELECT * FROM datasewa WHERE No_Antrian = '{no_antrian}'"
    try:
        cursor.execute(sql_select)
        data = cursor.fetchone()
        cursor.close()
        db.close()

        tampilkan(data)

    except Exception as e:
        cursor.close()
        db.close()

        messagebox.showerror("Error", f"Error: {str(e)}")

def tampilkan(data):
    frame4 = Frame(notebook, width=400, height=400)
    frame4.pack_propagate(0)
    notebook.add(frame4, text="Hasil Pencarian")

    if data:
        l_judul3 = Label(frame4, text="HASIL PENCARIAN")
        l_judul3.place(x=120, y=10)

        hasil_pencarian = Text(frame4, height=10, width=40)
        hasil_pencarian.place(x=30, y=60)

        hasil_pencarian.insert(END, f"No. Antrian          : {data[0]}\n")
        hasil_pencarian.insert(END, f"Nama Lengkap         : {data[1]}\n")
        hasil_pencarian.insert(END, f"Alamat               : {data[2]}\n")
        hasil_pencarian.insert(END, f"Email                : {data[3]}\n")
        hasil_pencarian.insert(END, f"Type Kamera          : {data[4]}\n")
        hasil_pencarian.insert(END, f"Merk Kamera          : {data[5]}\n")
        hasil_pencarian.insert(END, f"Keperluan            : {data[6]}\n")

        btnttp = Button(frame4, text="tutup", command=frame4.destroy).place(x=300, y=330)
    else:
        l_tidak_ditemukan = Label(frame4, text="Data tidak ditemukan")
        l_tidak_ditemukan.place(x=120, y=10)
        btnttp = Button(frame4, text="tutup", command=frame4.destroy).place(x=300, y=330)

def lihat1():
    db = MySQLdb.connect("localhost", "root", "", "sewakamera")
    cursor = db.cursor()
    no_antrian = e_antri1.get()
    sql_select1 = f"SELECT * FROM datatransaksi WHERE No_Antrian = '{no_antrian}'"
    try:
        cursor.execute(sql_select1)
        data = cursor.fetchone()
        cursor.close()
        db.close()

        tampilkan1(data)

    except Exception as e:
        cursor.close()
        db.close()

        messagebox.showerror("Error", f"Error: {str(e)}")

def tampilkan1(data):
    frame4 = Frame(notebook, width=400, height=400)
    frame4.pack_propagate(0)
    notebook.add(frame4, text="Hasil Pencarian")

    if data:
        l_judul3 = Label(frame4, text="HASIL PENCARIAN")
        l_judul3.place(x=120, y=10)

        hasil_pencarian = Text(frame4, height=10, width=40)
        hasil_pencarian.place(x=30, y=60)

        hasil_pencarian.insert(END, f"No. Antrian           : {data[0]}\n")
        hasil_pencarian.insert(END, f"Tanggal peminjaman    : {data[1]}\n")
        hasil_pencarian.insert(END, f"tanggal pengembalian  : {data[2]}\n")
        hasil_pencarian.insert(END, f"Email                 : {data[3]}\n")

        btnttp = Button(frame4, text="tutup", command=frame4.destroy).place(x=300, y=330)
    else:
        l_tidak_ditemukan = Label(frame4, text="Data tidak ditemukan")
        l_tidak_ditemukan.place(x=120, y=10)
        btnttp = Button(frame4, text="tutup", command=frame4.destroy).place(x=300, y=330)

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= 2,
        border= 2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def cetak():
    frame3 = Frame(notebook, width=400, height=400)
    frame3.pack_propagate(0)
    notebook.add(frame3, text="Laporan Sewa")
    frame3.place_forget()

    l_judul2 = Label(frame3, text="LAPORAN PERSEWAAN")
    l_judul2.place(x=120, y=10)
    laporan = Text(frame3, height=10, width=40)
    laporan.place(x=30, y=60)
    antri = e_antri.get()
    nama = e_nama.get()
    almt = e_almt.get()
    mail = e_mail.get()
    typek = r.get()
    merk = c_merk.get()
    perlu = r2.get()
    pnjm = d_pinjam.get()
    kmbl = d_kembali.get()
    bayar = c_metode.get()

    laporan.insert(END, f"No. Antrian          : {antri}\n")
    laporan.insert(END, f"Nama Lengkap         : {nama}\n")
    laporan.insert(END, f"Alamat               : {almt}\n")
    laporan.insert(END, f"Email                : {mail}\n")
    laporan.insert(END, f"Type Kamera          : {typek}\n")
    laporan.insert(END, f"Merk Kamera          : {merk}\n")
    laporan.insert(END, f"Keperluan            : {perlu}\n")
    laporan.insert(END, f"Tanggal Peminjaman   : {pnjm}\n")
    laporan.insert(END, f"Tanggal Pengembalian : {kmbl}\n")
    laporan.insert(END, f"Metode Pembayaran    : {bayar}\n")

    data_to_encode = f"No. Antrian: {antri}, Nama: {nama}, Alamat: {almt}, Email: {mail}, Type Kamera: {typek}, Merk Kamera: {merk}, Keperluan: {perlu}, Tanggal Peminjaman: {pnjm}, Tanggal Pengembalian: {kmbl}, Metode Pembayaran: {bayar}"
    
    qr_code_image = generate_qr_code(data_to_encode)
    qr_code_image = ImageTk.PhotoImage(qr_code_image)

    qr_label = Label(frame3, image=qr_code_image)
    qr_label.image = qr_code_image
    qr_label.place(x= 230, y= 225)

    btnttp = Button(frame3, text="tutup", command=frame3.destroy).place(x=30, y=330)

root = Tk()
root.geometry("380x500")
root.title("Project UAS")

notebook = ttk.Notebook(root)

# Frame for 1
frame1 = Frame(notebook, width=400, height=400)
frame1.pack_propagate(0)
notebook.add(frame1, text="Data Sewa")

l_judul = Label(frame1, text= "PERSEWAAN KAMERA")
l_antri = Label(frame1, text= "No. Antrian")
l_nama = Label(frame1, text= "Nama Lengkap")
l_almt = Label(frame1, text= "Alamat")
l_mail = Label(frame1, text= "Email")
l_type = Label(frame1, text= "Type Kamera")
l_merk = Label(frame1, text= "Merk Kamera")
l_perlu = Label(frame1, text= "Keperluan")


e_antri = Entry(frame1, width= 10)
e_nama = Entry(frame1, width= 35)
e_almt = Entry(frame1, width= 35)
e_mail = Entry(frame1, width= 35)

l_judul.place(x= 120, y= 10)
l_antri.place(x= 30, y= 60)
l_nama.place(x= 30, y= 90)
l_almt.place(x= 30, y= 120)
l_mail.place(x= 30, y= 150)
l_type.place(x= 30, y= 180)
l_merk.place(x= 30, y= 210)
l_perlu.place(x= 30, y= 240)

e_antri.place(x= 125, y= 60)
e_nama.place(x= 125, y= 90)
e_almt.place(x= 125, y= 120)
e_mail.place(x= 125, y= 150)

r = StringVar()
r.set(None)

r2 = StringVar()
r2.set(None)

rdtype1 = Radiobutton(frame1, text= "DSLR", variable= r, value= "DSLR").place(x= 125, y= 180)
rdtype2 = Radiobutton(frame1, text= "Mirorrles", variable= r, value= "Mirorrles").place(x= 190, y= 180)
rdtype3 = Radiobutton(frame1, text= "Hybrid", variable= r, value= "Hybrid").place(x= 270, y= 180)

rdperlu1 = Radiobutton(frame1, text= "Fotografi", variable= r2, value= "Fotografi").place(x= 125, y= 240)
rdperlu2 = Radiobutton(frame1, text= "Videografi", variable= r2, value= "Videografi").place(x= 220, y= 240)

btnsmpn = Button(frame1, text= "simpan", command= simpan).place(x= 203, y= 330)
btnedit = Button(frame1, text="Edit", command= edit).place(x=170, y=330)
btnhapus = Button(frame1, text= "hapus", command= hapus).place(x= 125, y= 330)
btnlht = Button(frame1, text= "lihat data", command= lihat).place(x= 300, y= 330)
btnklr = Button(frame1, text= "keluar", command= root.destroy).place(x= 30, y= 330)


merk = ["Canon", "Nikon", "FujiFilm", "Sony", "Lumix", "Olimpus"]
perlu = ["Fotografer", "Videografer"]

c_merk = ttk.Combobox(frame1, values= merk)
c_merk.place(x= 125, y= 210)

# Frame for 2
frame2 = Frame(notebook, width=400, height=400)
frame2.pack_propagate(0)
notebook.add(frame2, text="Data Transaksi")

l_judul1 = Label(frame2, text= "TRANSAKSI")
l_antri1 = Label(frame2, text= "No. Antrian")
l_pinjam = Label(frame2, text= "Tanggal Peminjaman")
l_kembali = Label(frame2, text= "Tanggal Pengembalian")
l_metode = Label(frame2, text= "Metode Pembayaran")

e_antri1 = Entry(frame2, width= 10)
d_pinjam = DateEntry(frame2, datefomat= '%Y-%m-%d')
d_kembali = DateEntry(frame2, datefomat= '%Y-%m-%d')

l_judul1.place(x= 150, y= 10)
l_antri1.place(x= 30, y= 60)
l_pinjam.place(x= 30, y= 90)
l_kembali.place(x= 30, y= 120)
l_metode.place(x= 30, y= 150)

e_antri1.place(x= 180, y= 60)
d_pinjam.place(x= 180, y= 90)
d_kembali.place(x= 180, y= 120)

metode = ["Tunai", "Tranfer Bank", "E-Money", "PayPal"]
c_metode = ttk.Combobox(frame2, values= metode)
c_metode.place(x= 180, y= 150)

btnctk = Button(frame2, text= "cetak", command= cetak).place(x= 300, y= 330)
btnsmpn = Button(frame2, text= "simpan", command= simpan1).place(x= 203, y= 330)
btnedit = Button(frame2, text="Edit", command= edit1).place(x=170, y=330)
btnhapus = Button(frame2, text= "hapus", command= hapus1).place(x= 125, y= 330)
btnlht = Button(frame2, text= "lihat data", command= lihat1).place(x= 30, y= 330)

notebook.pack(expand=1, fill="both")

root.mainloop()