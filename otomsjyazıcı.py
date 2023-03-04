#OTOMATİK MESAJ YAZICI
#bu modulleri pip ile indirmenize gerek yok direk yazabilirsiniz
import pyautogui
import time

#DEĞİŞKENLER
#bekleme süresi
süre = 5
#yazılacak mesaj
msj = "."
#tekrar sayısı
tk = 1
while True:
 #DEĞİŞKENLERE DEĞER VERME
 print("Otomatik Mesaj Yazıcıya Hoşgeldiniz\nSürüm:0.1")
 msj = str(input("Göndermek İstediğiniz Mesaji Yazınız:"))
 tk = int(input("Kaç Defa Bu Mesaji Göndereceğinizi Yazınız:"))
 süre = int(input("Kaç Saniye Sonra Bu Mesajı Gönderelim:"))
 print("İşlem Tamam :) Mesaj Gönderilmesi Gereken Yeri Açınız")

 #MESAJI GÖNDERME
 #while için değişken
 i = 0
 time.sleep(süre)
 while i < tk:
    pyautogui.write(msj)
    pyautogui.press('enter')
    i = i + 1
 print("Mesaj Gönderilmiştir")
 #DEVAM SÜRECİ
 #sorgulaması için değişken
 sorgu = "A"
 sorgu = str(input("Devam Etmek İçin E,Programı Durdurmak İçin H Basınız:"))
 if sorgu == "E":
    continue
 if sorgu == "H":
    break
 else:
    print("İşlem Gerçekleştirilemedi :( Program Kapanıyor")
    break
  
#Eğer yazdığım kodlarda bir hata varsa şimdiden özür dilerim
#Made by h0taf
