# -*- coding: cp1254 -*-
#1.ÖRNEK
"""
+++
s1=raw_input("bir değer giriniz")

print "s1 türü", type(s1)

#
#try:
#   #hata oluşacak kod / hataların, denemelerin olduğu alan.
#    s1_int = int(s1)
#    print "başarılı"
#except ValueError:
#    #try içerisinde hata oluştuğunda çalışacak bölüm.
#    print "başarısız"
#

+++
"""

#2.ÖRNEK

"""
def sayi_mi():
    try:
        int(s1)
        int(s2)
        return True
    except ValueError:
        return False
s1=raw_input("ilk sayı")
s2=raw_input("ikinci sayı")
islem=raw_input("işlem seç, (+,-,/,*)")

/////burada sayı girildikten sonra if'e gelir. if'de gelen bu sayı değerini
/////sayi_mi() fonksiyonuna gönderir. fonksiyon gelen değere bakar. eğer ki
/////int'se yani fonksiyonun tanımlandığı gibi ise True değerini alıp if'e gider.
/////eğer kurala uymazsa False değerini alıp if'teki False'dan Else'ye geçer.

if sayi_mi()==True:
    if islem=="+":
        print "toplam :", (int(s1)+int(s2))
    if islem=="-":
        print "fark :", (int(s1)-int(s2))
    if islem=="/":
        print "bolme :", (int(s1)/int(s2))
    if islem=="*":
        print "çarpma :", (int(s1)*int(s2))
else:
    print "s1 veya s2 sayi degil"

"""

#3.ÖRNEK

#parametreli parametreli fonksiyonlar

#def yaz(param1, param2,..,param3):
#    parametreleri kullanarak işlemler yapar.

"""
def imza(ad,unvan,tel,mail,site):
    print "ad\t:",ad
    print "ünvan\t:",unvan
    print "telefon\t:",tel
    print "e-mail\t:",mail
    print "site\t:",site

imza("Selçuk Kara","Öğretmen","02124536895","selcukara@gmail.com","slckr.com")
print("")
imza("Durdur","Öğretmen","02124536895","selcukara@gmail.com","slckr.com")
print("")
imza("Ska","Öğretmen","02124536895","selcukara@gmail.com","slckr.com")
"""

#Bilgisayardaki açık ve kapalı portları listeleyiniz.

#4.ÖRNEK
"""
#soru: gönderilen herhangi bir ifadeyi istenen türden olup olmadığını kontrol eden bir fonksiyon.

def control(degisken, tur):
    try:
        #burada bir değişken daha atanabilir.
        if tur=='int':
            int(degisken)
        if tur=='str':
            str(degisken)
        return True #---->Bunu yazmadığında her seferinde al tarafta sayının değişken old. söyler.
    except ValueError:
        return False

#x=1
x=raw_input("değer giriniz\t:")

if control(x,'int'):
    print "%s değişkeni sayıdır"%(x)
else:
    print "%s değişkeni sayı değildir"%(x)

#http://www.pythondersleri.com/2013/05/fonksiyonlar_10.html

"""

#pythonda isimli argümanlar(parametreler)

#5.ÖRNEK
"""
def imza(x,y,z,t,u):

    print "ad\t:",x         #-->x str
    print "ünvan\t:",y      #-->y str
    print "telefon\t:",z    #-->z int
    print "e-mail\t:",t     #-->t str
    print "site\t:",u       #-->u str
    
imza(y="doctor",u="msn.com",x="ece",z="02145",t="k@x.au")
"""

#6.ÖRNEK

x = 4
def y():
    x=12
    global isim
    isim="karanlık"
    print "isim değişkeni",isim
    print "fonksiyon içindeki değişken:",x
y()
print "isim değişkeni",isim    
print "fonksiyon dışındaki değişken",x
#y() burada yazılırsa hata ile karşılaşılır. Çünkü y() çağrılmadan nasıl çalışsın ki? çağrıldıktan sonra işe yarar eleman.













































