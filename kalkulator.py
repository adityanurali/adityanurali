import os, sys, time, random, threading, random, socket, select, datetime
import os
import sys

def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [x for x in array if x]
#script berjalan
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.010)
mengetik('\033[0m')
mengetik('\033[0m')
mengetik('\033[1;31m<=========================================================>')
mengetik('\033[1;31m||   \033[0;35m      __    ____ \033[1;37m  ____  ____\033[0;35m  _  _    __           \033[1;31m||')
mengetik('\033[1;31m||   \033[1;32m     /__\  (  _ \ (_  _)\033[0;35m(_  _)( \/\033[1;32m )  /__\          \033[1;31m||')
mengetik('\033[1;31m||   \033[0;36m    /(__)\  )(_) ) _)(_   )\033[1;33m(   \  /  /(__)\         \033[1;31m||')
mengetik('\033[1;31m||   \033[0;31m   (__)(__)(____/ (____)\033[1;30m (__)  (__) (__)(__)        \033[1;31m||')
mengetik('\033[1;31m<=========================================================>')
mengetik('\033[1;32m ')

# fungsi penjumlahan
def add(x, y):
   return x + y
# fungsi pengurangan
def subtract(x, y):
   return x - y
# fungsi perkalian
def multiply(x, y):
   return x * y
# fungsi pembagian
def divide(x, y):
   return x / y
# menu operasi
print("Pilih Operasi.")
print("1.Jumlah = +")
print("2.Kurang = -")
print("3.Kali = ×")
print("4.Bagi = :")
# Meminta input dari user
choice = input("Masukkan pilihan(1/2/3/4) : ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Input salah")
   
