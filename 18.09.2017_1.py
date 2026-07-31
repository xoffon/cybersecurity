# -*- coding: cp1254 -*-

#İdeal kilo hesaplama programı =>

"""
print "
1)Erkek
2)Kadın
"

cinsiyet = input("Cinsiyetinizi belirleyiniz! > ")
if cinsiyet == 1:
    e_boy = input("Boyunuzu giriniz > ")
    e_yas = input ("Yaşınızı giriniz > ")
    e_top = (e_boy-100+e_yas/10)*0.9    #Erkek için formül.
    print "İdeal kilonuz >> ", e_top
    
if cinsiyet == 2:
    k_boy = input("Boyunuzu giriniz > ")
    k_yas = input ("Yaşınızı giriniz > ")
    k_top = (k_boy-100+k_yas/10)*0.8    #Kadın için formül.
    print "İdeal kilonuz >> ", k_top


"""

#hocanın yaptığı 
print "1) erkek"
print "2) kadın"
b = float(raw_input("Boyunuz (cm) : "))
y = int(raw_input("Yaşınız : "))
c = int(raw_input("Cinsiyetiniz "))

if c == 1:
    top = (b-100+y/10)*0.9    #Erkek için formül.
else:
    top = (b-100+y/10)*0.8    #Kadın için formül.

print "İdeal kilonuz >> ", top
