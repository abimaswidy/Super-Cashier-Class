import pandas as pd
import os

class Transaction:
   
    #Sebuah class untuk kasir self-service cashier
    #Attributes
    #id_transaksi : int, berupa input untuk menandai kode transaksi customer
    #data_item : dict, data item merupakan tempan tersimpannya semua transaksi yang dilakukan fungsi   

    data_item = {"Nama item": [], "Jumlah item": [], "harga item": [], "Total Harga": []}

    
    def __init__(self):
    
      print("<-----------------Super Cashier Pacmann----------------->")
      while 1:
          try:
              id_transaksi = int(input("Id transaksi: "))
              print("Id transaksi anda {}".format(id_transaksi))
              print("\n")
              break
          except ValueError:
              print("Id transaksi tidak sesuai")
              continue
      while 1:
          print("<-----------------------list Opsi----------------------->")
          print("1. menambahkan item")
          print("2. merubah nama item") 
          print("3. merubah jumlah item") 
          print("4. merubah harga item")
          print("5. mengecek item transaksi")
          print("6. menghapus salah satu item transaksi")
          print("7. menghapus semua item transaksi")
          print("8. menampilkan total biaya item transaksi")
          print("9. menyelesaikan program")
          print("\n")
          opsi = input("Masukkan nomor sesuai opsi: ")
          if opsi.lower() == "1":
              self.add_item()
              print("\n")
          elif opsi.lower() == "2":
              self.update_item_name()
              print("\n")
          elif opsi.lower() == "3":
              self.update_item_jumlah()
              print("\n")
          elif opsi.lower() == "4":
              self.update_item_harga()
              print("\n")
          elif opsi.lower() == "5":
              self.check_order_item()
              print("\n")
          elif opsi.lower() == "6":
              self.delete_item()
              print("\n")
          elif opsi.lower() == "7":
              self.reset_transaction()
              print("\n")
          elif opsi.lower() == "8":
              self.total_price()
              print("\n")
          elif opsi.lower() == "9":
              # break
              os._exit(0)
          else:
              print("Input tidak sesuai")
              print("\n")

    def add_item(self):
      
      #fungsi untuk menambahkan item yang di input customer ke dict data_item
      #nama_item : str, berupa input yang akan masuk ke dict data_item
      #jumlah_item : int, berupa input yang akan masuk ke dict data_item
      #harga : int, berupa input yang akan masuk ke dict data_item
      #total_harga : int, berupa input yang akan masuk ke dict data_item

      nama_item = input("Nama item : ")

      while 1:
          try:
              jumlah_item = int(input("Jumlah item : "))
              break
          except ValueError:
              print("input harus angka")
              continue

      while 1:
          try:
              harga = int(input("harga item : "))
              break
          except ValueError:
              print("Input harus angka")
              continue

      self.data_item["Nama item"].append(nama_item)
      self.data_item["Jumlah item"].append(jumlah_item)
      self.data_item["harga item"].append(harga)
      self.data_item["Total Harga"].append(jumlah_item * harga)

    def update_item_name(self):

      #fungsi untuk merubah nama pada item yang sudah dimasukkan pada dict data_item
      #nama_item : str, berupa input nama item yang sudah di dict data_item dan akan dirubah
      #update_nama_item : str, berupa input nama item baru
      #index_item : str, variabel untuk menyimpan perubahan

      while 1:
          nama_item = input("Nama item: ")

          if nama_item in self.data_item.get("Nama item"):
              update_nama_item = input("Update nama item yang diubah: ")
              index_item = self.data_item['Nama item'].index(nama_item)
              self.data_item['Nama item'][index_item] = update_nama_item
              print("Berhasil")
              break

          else:
              print("nama item tidak ada")
              break

    def update_item_jumlah(self):

      #fungsi untuk merubah jumlah pada item yang sudah dimasukkan pada dict data_item
      #nama_item : str, berupa input nama item yang sudah di dict data_item dan akan dirubah
      #update_jumlah_item : int, berupa input jumlah item baru
      #index_item : int, variabel untuk menyimpan perubahan

      while 1:
          nama_item = input("Nama item: ")

          if nama_item in self.data_item.get("Nama item"):
              while 1:
                  try:
                      update_jumlah_item = int(input("Update jumlah item dibeli: "))
                      break
                  except ValueError:
                      print("Input harus angka")
                      continue
              index_item = self.data_item['Nama item'].index(nama_item)
              self.data_item['Jumlah item'][index_item] = update_jumlah_item

              self.data_item["Total Harga"][index_item] = (
                          update_jumlah_item * self.data_item["harga item"][index_item])

              print("Berhasil")
              break

          else:
              print("nama item tidak ada")

    def update_item_harga(self):

      #fungsi untuk merubah harga pada item yang sudah dimasukkan pada dict data_item
      #nama_item : str, berupa input nama item yang sudah di dict data_item dan akan dirubah
      #update_harga_item : int, berupa input harga item baru
      #index_item : int, variabel untuk menyimpan perubahan

      while 1:
          nama_item = input("Nama item : ")

          if nama_item in self.data_item.get("Nama item"):
              while 1:
                  try:
                      update_harga_item = int(input("Update harga item dibeli: "))
                      break
                  except ValueError:
                      print("Input harus angka")
                      continue
              index_item = self.data_item['Nama item'].index(nama_item)
              self.data_item['harga item'][index_item] = update_harga_item

              self.data_item["Total Harga"][index_item] = (update_harga_item * self.data_item["Jumlah item"][index_item])

              print("Berhasil")
              break

          else:
              print("nama item tidak ada")

    def check_order_item(self):

      #fungsi untuk mengakses atau melihat transaksi yang sudah dilakukan pada dict data_item
      #df : dataframe, untuk menampilkan dict dalam bentuk tabel

      if not any(self.data_item.values()):
          print("belum ada transaksi")
      elif '' in self.data_item['Nama item']:
          print("nama item tidak terisi")
          print("<--------List transaksi item-------->")
          df = pd.DataFrame(self.data_item)
          print(df)
      else:
          print("transaksi sesuai")
          print("<--------List transaksi item-------->")
          df = pd.DataFrame(self.data_item)
          print(df)

    def delete_item(self):
      
      #fungsi untuk delete salah satu item yang sudah di input di dict data_item
      #nama_item : str, nama item yang akan dihapus
      #df : dataframe, untuk menampilkan dict dalam bentuk tabel
      #index_item : int, variabel untuk menyimpan perubahan

      while 1:
          nama_item = input("Nama item: ")

          if nama_item in self.data_item.get("Nama item"):
              index_item = self.data_item['Nama item'].index(nama_item)
              for key in list(self.data_item.keys()):
                  del self.data_item[key][index_item]

              print("Berhasil")
              if not any(self.data_item.values()):
                  print("belum ada transaksi")
              else:
                  df = pd.DataFrame(self.data_item)
                  print(df)
              break

          else:
              print("nama item tidak ada")

    def reset_transaction(self):
      
      #fungsi untuk mereset/delete semua transaksi yang sudah masuk ke dict data_item

      for key in list(self.data_item.keys()):
          del self.data_item[key][:]

      print("Berhasil")


    def total_price(self):

      #fungsi untuk melihat total biaya pada transaksi yang sudah dimasukkan pada dict data_item
      #df : dataframe, untuk menampilkan dict dalam bentuk tabel

      if not any(self.data_item.values()):
          print("belum ada transaksi")
      else:
          df = pd.DataFrame(self.data_item)
          print(df)
          if sum(self.data_item["Total Harga"]) > 500000:
              print("sebelum diskon 10%: Rp.{}".format(sum(self.data_item["Total Harga"])))
              print("setelah diskon 10%: Rp.{}".format(int(sum(self.data_item["Total Harga"]) - (sum(self.data_item["Total Harga"]) * 0.10))))
          elif sum(self.data_item["Total Harga"]) > 300000:
              print("sebelum diskon 8%: Rp.{}".format(sum(self.data_item["Total Harga"])))
              print("setelah diskon 8%: Rp.{}".format(int(sum(self.data_item["Total Harga"]) - (sum(self.data_item["Total Harga"]) * 0.08))))
          elif sum(self.data_item["Total Harga"]) > 200000:
              print("sebelum diskon 5%: Rp.{}".format(sum(self.data_item["Total Harga"])))
              print("setelah diskon 5%: Rp.{}".format(int(sum(self.data_item['Total Harga']) - (sum(self.data_item["Total Harga"]) * 0.05))))
          index_item = self.data_item["Total Harga"]
          index_item.clear()

Transaction()
