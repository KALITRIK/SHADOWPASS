#!/usr/bin/env python3
#-*-encoding:utf8-*-
print("""BU PROGRAM KALİTRİK TARAFINDAN YAPILMIŞTIR!
BÜTÜN HAKLARI KALİTRİK'E AİTTİR!\n
THİS PROGRAM WRİTTED BY KALITRIK!""")
print("""SHADOWPASS UYGULAMASI\n
ŞİFRELEME METODU 1-2 GÜNDE BİR DEĞİŞMEKTEDİR\n
LÜTFEN GİTHUB'UMU TAKİP EDİNİZ!\n""")
enc={
"i":"o",
"o":"i",
"ı":"ü",
"ü":"ı",
"e":"o",
"o":"e",
"a":"ö",
"ö":"a",
"b":"z",
"z":"b",
"c":"y",
"y":"c",
"ç":"v",
"v":"ç",
"d":"t",
"t":"d",
"f":"ş",
"ş":"f",
"g":"s",
"s":"g",
"ğ":"n",
"n":"ğ",
"h":"m",
"m":"h",
"j":"l",
"l":"j",
"p":"r",
"r":"p",
"e":"u",
"u":"e",
"o":"i",
"i":"o",
"k":"k",
"w":"x",
"x":"w",
" ":" "
}
print("SHADOWPASS V1.0\n")
print("ŞİFRELER VE ÇÖZER\n")
print("""Programı kullanmak için
 örnek olarak
 şifrelencek kelime
 Programda Şifrelenmiş Kelimeyi Çözmek içinse
 örnek olarak:
 çözülecek kelime""")
while 1:
	q = input("Şifrele veya Çöz:")
	out=""
	oldlen=len(q)
	q=list(q)
	while len(out)!=oldlen:
		for a,b in enc.items():
			if q[0]==a:
				out+=b
				del q[0]
				break
	q=''.join(q)
	print(out)