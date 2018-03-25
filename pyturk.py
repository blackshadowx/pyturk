'Bu kitaplık Siyabend Ürün tarafından oluşturulmuştur.'
from datetime import datetime,timedelta,date
import sys,os,random,time,locale,getpass
try:
	if os.name=="posix":
		locale.setlocale(locale.LC_ALL,'tr_TR')
		locale.setlocale(locale.LC_ALL,'tr_TR.utf8')
	elif os.name=="nt":
		locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254')
		locale.setlocale(locale.LC_ALL,'Turkish')
except locale.Error:
	pass
class __Fonk__():
	def tamsayı(nesne):
		return int(nesne)
	def dizi(nesne):
		return str(nesne)
	def ondalık(nesne):
		return float(nesne)
	def bayt(nesne):
		return bytes(nesne)
	def bayt_dizisi(nesne):
		return bytearray(nesne)
	def sözlük(*nesneler):
		return dict(nesneler)
	def liste(*nesneler):
		return list(nesneler)
def demet(*nesneler):
	return tuple(nesneler)
class Sistem(object):
	def __init__(self):
		pass
	@staticmethod
	def konsol_boyutu():
		columns=os.get_terminal_size().columns
		lines=os.get_terminal_size().lines
		return (columns,lines)
	@staticmethod
	def dizin_dgstr(yol):
		try:
			os.chdir(str(yol))
		except FileNotFoundError:
			print("Belirtilen dizin bulunamadı.")
		except PermissionError:
			print("Belirtilen dizine giriş izniniz bulunmamaktadır.")
	@staticmethod
	def listele(yol=os.curdir,uzantı="",ara=""):
		try:
			lst1=os.listdir(yol)
			lst2=list(dosya for dosya in lst1 if dosya.endswith(uzantı) and ara in dosya)
			return lst2
		except FileNotFoundError:
			print("Belirtilen dizin bulunamadı.")
		except PermissionError:
			print("Belirtilen dizine giriş izniniz bulunmamaktadır.")
		except:
			print("Anlaşılamayan hata")
	@staticmethod
	def tara(yol=".",ara="",uzantı=""):
		lst=[]
		for kökdizinler,altdizinler,dosyalar in os.walk(yol):
			for dosya in dosyalar:
				if ara in dosya and dosya.endswith(uzantı):
					lst.append(dosya)
		return lst
		del kökdizinler,altdizinler
	@staticmethod
	def mevcutdzn():
		return os.getcwd()
	@staticmethod
	def dizin_olstr(ad,yol=os.curdir):
		os.chdir(yol)
		if ad not in os.listdir():
				os.mkdir(ad)
		elif ad in os.listdir():
			sil_onay=input("Bu klasör zaten var.Eskisi silinsin mi?(e/h)\n")
			if sil_onay.lower == "h":
				pass
			elif sil_onay.lower == "e":
				os.rmdir(ad)
				os.mkdir(ad)
		else:
			print("Başarısız")
	@staticmethod
	def dizinler_olstr(ad):
		try:
			os.makedirs(ad)
		except FileExistsError:
			sil_onay=input("Bu klasör zaten var.Eskisi silinsin mi?(e/h)\n")
			if sil_onay.lower == "h":
				pass
			elif sil_onay.lower == "e":
				os.removedirs(ad)
				os.mkdirs(ad)
	@staticmethod
	def dizin_sil(ad,yol=os.curdir):
		os.chdir(yol)
		try:
			os.rmdir(ad)
		except OSError:
			print("Klasör boş değil")
		except FileNotFoundError:
			print("Klasör bulunamadı")
	@staticmethod
	def dizinler_sil(ad):
		try:
			os.removedirs(ad)
		except OSError:
			print("Klasör boş değil")
		except FileNotFoundError:
			print("Klasör bulunamadı")
	@staticmethod
	def yeniden_adlandır(eski_dosya_adı,yeni_dosya_adı,dizin=os.curdir):
		try:
			return os.rename(eski_dosya_adı,yeni_dosya_adı)
		except FileNotFoundError:
			print("{} adında bir dosya bulunamadı".format(eski_dosya_adı))
	@staticmethod
	def dosya_sil(dosya_adı):
		try:
			os.remove(dosya_adı)
		except FileNotFoundError:
			print("Belirrtiğiniz dosya bulunamadı")
	çevre_değişkenleri=os.environ
	#@staticmethod
class Fonksiyonlar(__Fonk__,object):
	def __init__(self):
		pass
	@staticmethod
	def bekle(saniye):
		time.sleep(saniye)
	@staticmethod
	def topla(*nums):
		toplam=0
		for sayi in nums:
			toplam+=sayi
		return toplam
	@staticmethod
	def carp(*nums):
        	carpim=1
       		for sayi in nums:
                	carpim*=sayi
        	return carpim
	@staticmethod
	def yazdır(*nesneler,ayır=" ",boşalt=False,son="\n",dosya=sys.stdout,kodlama="utf-8"):
		print(*nesneler,sep=ayır,flush=boşalt,end=son,file=dosya,encoding=kodlama)
	@staticmethod
	def yazdır_ynstr(*nesneler,ayır="\n",boşalt=False,son="\n",dosya=sys.stdout,kodlama="utf-8"):
		print(*nesneler,sep=ayır,flush=boşalt,end=son,file=dosya,encoding=kodlama)
	@staticmethod
	def giriş(text):
		name=input(text)
		return name
	@staticmethod
	def şifre_giriş(text="Şifre:\t"):
		return getpass.getpass(prompt=text)
	@staticmethod
	def yardım(nesne):
		return help(nesne)
	@staticmethod
	def uzunluk(text):
		_UZUNLUK=0
		for harf in text:
			_UZUNLUK+=1
		return _UZUNLUK
	@staticmethod
	def tür(object):
		return type(object)
	@staticmethod
	def numaralandır(number=0,*args):
		try:
			return dict(enumerate(args,number))
		except TypeError:
			print("İlk paramtetre bir tam sayı olmalıdır.")
	@staticmethod
	def kuvvet(number,number2):
		return number**number2
	@staticmethod
	def aralık(number1=0,number2=0,number3=1):
		return list(range(number1,number2,number3))
	@staticmethod
	def yenile(modül_ismi):
		from importlib import reload
		try:
			return reload(modül_ismi)
		except TypeError:
			#Class kısmını atmaya çalıştım
			print("Yenilemeye çalıştığınız öğe bir modül değil,bir {}".format(str(type(modül_ismi)).split("'")[1]))
	@staticmethod
	def sırala(nesne):
		return dir(nesne)
class Dosya(object):
	def __init__(self):
		pass
	def dosya_yardım():
		print(
'''
"r" | Okuma kipi
"w" | Yazma Kipi
"a" | Yazma Kipi(Mevcut Dosya Korunur)
"x" | Yazma Kipi(Mevcut Dosya Korunur)
"r+" | Okuma + Yazma Kipi
"w+" | Yazma + Okuma Kipi
"a+" | Yazma + Okuma Kipi(Mevcut Dosya Korunur)
"x+" | Yazma + Okuma Kipi(Mevcut Dosya Korunur)
"rb" | Okuma Kipi(İkili Sistem Dosyaları)
"wb" | Yazma  Kipi(İkili Sistem Dosyaları)
"ab" | Yazma Kipi(İkili Sistem Dosyaları)(Mevcut Dosya Korunur)
"xb" | Yazma Kipi(İkili Sistem Dosyaları)(Mevcut Dosya Korunur)
"rb+" | Okuma + Yazma Kipi(İkili Sistem Dosyaları)
"wb+" | Yazma + Okuma Kipi(İkili Sistem Dosyaları)
"ab+" | Yazma + Okuma Kipi(İkili Sistem Dosyaları)(Mevcut Dosya Korunur)
"xb+" | Yazma + Okuma Kipi(İkili Sistem Dosyaları)(Mevcut Dosya Korunur)
''')
	@staticmethod
	def dosya_oluştur(dosya_isim,kip,kodlama="utf-8",_hatalar="strict"):
		return open(dosya_isim,kip,encoding=kodlama,errors=_hatalar)
	@staticmethod
	def dosya_oku(dosya_adı,karakter=-1):
		return dosya_adı.read(karakter)
	@staticmethod
	def dosya_oku_satır(dosya_adı,karakter=-1):
		return dosya_adı.readline()
	@staticmethod
	def dosya_oku_satırlar(dosya_adı,karakter=-1):
		return dosya_adı.readlines(karakter)
	@staticmethod
	def dosya_yaz(dosya_adı,yazı,boşalt=True):
		print(yazı,file=dosya_adı,flush=boşalt)
	@staticmethod
	def dosya_yaz_satırlar(dosya_adı,yazı_yada_liste):
		dosya_adı.writelines(yazı_yada_liste)
	@staticmethod
	def dosya_imleç(dosya_adı,sayı):
		dosya_adı.seek(sayı)
	@staticmethod
	def dosya_temizle(dosya_adı):
		try:
			os.remove(dosya_adı)
		except FileNotFoundError:
			print("Dosya bulunamadı")
		with open(dosya_adı,"w") as dosya:
			pass
	@staticmethod
	def mod(dosya_adı):
		return dosya_adı.mode
	@staticmethod
	def kodlama(dosya_adı):
		return dosya_adı.encoding
	@staticmethod
	def okunabilir(dosya_adı):
		return dosya_adı.readable()
	@staticmethod
	def yazılabilir(dosya_adı):
		return dosya_adı.writable()
	@staticmethod
	def kapalı_mı(dosya_adı):
		return dosya_adı.closed
	@staticmethod
	def hatalar(dosya_adı):
		return dosya_adı.errors
class Rastgele(object):
	def __init__(self):
		pass
	@staticmethod
	def rast_sayı(num1,num2):
			return random.uniform(num1,num2)
	@staticmethod
	def rast_tamsayı(num1,num2):
		return random.randint(num1,num2)
	@staticmethod
	def rast_sec(_list):
		rast_=random.randrange(0,len(_list))
		return _list[rast_]
	@staticmethod
	def rast_karıştır(_list):
		try:
			return random.shuffle(_list)
		except TypeError:
			print("Bu fonksiyon sadece listeler üzerinde kullanılabilir")
	@staticmethod
	def rast_örnek(population,num):
		try:
			return random.sample(population,num)
		except ValueError:
			print("Verilecek örnek aayısı değerin uzunluğundan fazla olamaz.")
class Tarih(object):
	def __new__(self):
		an=datetime.now()
		self.yıl=an.year
		self.ay=an.month
		self.gün=an.day
		self.saat=an.hour
		self.dakika=an.minute
		self.saniye=an.second
		self.mikrosaniye=an.microsecond
	@staticmethod
	def tarih_yardım():
		print("""\t%a Hafta gününün kısaltılmış adı,
	%A Hafta gününün tam adı.
	%b Ayın kısaltılmış  adı.
	%B Ayın tam adı.
	%c Tam tarih,saat ve zaman bilgisi.
	%d Sayı değerli karakter dizisi olarak gün.
	%j Belli bir tarihin yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı.
	%m Sayı değerli bir karakter dizisi olarak ay.
	%U Belli bir tarihin yılın kaçıncı haftasına denk geldiğini gösteren 0-53 arası bir sayı.
	%y Yılın son iki rakamı.
	%Y Yılın dört haneli tam hali.
	%x Tam tarih bilgisi.
	%X Tam saat bilgisi.
Örnek:
	>>> bugün=Tarih.bugün()
	>>> print(bugün)
	2018-03-17 11:25:05.030233
	>>> format = "%d/%m/%Y"
	>>> Tarih.tarih_biçimlendir(bugün,format)
	'17/03/2018'
	>>> format = "%X"
	>>> Tarih.tarih_biçimlendir(bugün,format)
	'11:25:06'
""")
	@classmethod
	def tarih_an(cls):
		return datetime.now()
	@staticmethod
	def bugün():
		return datetime.today()
	@staticmethod
	def tarih_ileri(gün,saniye=0,mikrosaniye=0):
		bugün=datetime.today()
		fark=timedelta(days=abs(gün),microseconds=abs(mikrosaniye),seconds=abs(saniye))
		gelecek=(bugün)+(fark)
		return gelecek
	@staticmethod
	def tarih_geri(gün,saniye=0,mikrosaniye=0):
		bugün=datetime.today()
		fark=timedelta(days=abs(gün),microseconds=abs(mikrosaniye),seconds=abs(saniye))
		geçmiş=(bugün)-(fark)
		return geçmiş
	@staticmethod
	def aylar():
		return Fonksiyonlar.numarala(1,"Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık")
	@classmethod
	def aylar_günler(cls):
		günler={"Ocak":31,"Şubat":28,"Mart":31,"Nisan":30,"Mayıs":31,"Haziran":30,"Temmuz":31,"Ağustos":31,"Eylül":30,"Ekim":31,"Kasım":30,"Aralık":31}
		if cls.tarih_an().year % 4 == 0:
			#Eğer içinde bulunduğumuz yıl 4 sayısının katı ise Şubat ayı 29 güne tekabül eder.
			günler["Şubat"]=29
			return günler
		elif cls.tarih_an().year %4 != 0:
			return günler
	@staticmethod
	def tarih_biçimlendir(nesne,format):
		return datetime.strftime(nesne,format)
	@staticmethod
	def tarih_dönüştür(nesne,format):
		return datetime.strptime(nesne,format)
	@staticmethod
	def tarih_birleştir(tarih_nesnesi,zaman_nesnesi):
		return datetime.combine(tarih_nesnesi,zaman_nesnesi)
	@staticmethod
	def tarih_demet(tarih_nesnesi):
		return datetime.timetuple(tarih_nesnesi)
	@staticmethod
	def zaman_damgası(damgalanacak_nesne):
		return datetime.timestamp(damgalanacak_nesne)
	@staticmethod
	def zaman_damgası_çöz(damgalanmış_nesne):
		return datetime.fromtimestamp(damgalanmış_nesne)
	tarih_son = datetime.max
	@staticmethod
	def hafta_gün(nesne):
		try:
			return datetime.isoweekday(nesne)
		except TypeError:
			print("Verilen değer tarih nesnesi olmalıdır!")

	@staticmethod
	def zaman_dilimi(nesne):
		try:
			return datetime.astimezone(nesne)
		except TypeError:
			print("Verilen değer datetime nesnesi olmalıdır!")
	@staticmethod
	def takvim(nesne):
		try:
			return datetime.isocalendar(nesne)
		except TypeError:
			print("Verilen değer date nesnesi olmalıdır!")
	@staticmethod
	def tam_tarih(nesne):
		return datetime.ctime(nesne)
	def değiştir(self,yıl=None,ay=None,gün=None,saat=None,dakika=None,saniye=None,mikrosaniye=None):
		if yıl is None:
			yıl=self.year
		if ay is None:
			ay=self.month
		if gün is None:
			gün=self.day
		if saat is None:
			saat=self.hour
		if dakika is None:
			dakika=self.minute
		if saniye is None:
			saniye=self.second
		if mikrosaniye is None:
			mikrosaniye=self.microsecond
		return type(self)(yıl,ay,gün,saat,dakika,saniye,mikrosaniye)
	def tarih(self):
		return date(self.year,self.month,self.day)
class Matematik(object):
	def __init__(self):
		pass
	mat_pi=3.1415926536
	@staticmethod
	def mat_üçgen_test(kenar1,kenar2,kenar3):
		kenar1,kenar2,kenar3=float(kenar1),float(kenar2),float(kenar3)
		if all([kenar1+kenar2>kenar3,
			kenar2+kenar3>kenar1,
			kenar1+kenar3>kenar2]):
			print("Bu üçgen olabilir")
		else:
			print("Bu üçgen olamaz")
	@staticmethod
	def mutlak(num):
		if num < 0:
			return -1 * num
		elif num >= 0:
			return num
	@staticmethod
	def pisagor(dk1=None,dk2=None,hptenüs=None):
		if all([dk1,dk2,hptenüs]) or all([not dk1,not dk2,not hptenüs]):
			return None
		if all([dk1,dk2]):
			hptenüs=((dk1**2)+(dk2**2))**0.5
			return hptenüs
		elif all([dk1,hptenüs]):
			dk2=((hptenüs**2)-(dk1**2))**0.5
			return dk2
		elif all([dk2,hptenüs]):
			dk1=((hptenüs**2)-(dk2**2))**0.5
			return dk1
	@staticmethod
	def faktöriyel(sayı):
		return Fonksiyonlar.carp(*range(1,sayı+1))
	@staticmethod
	def mat_alan(kenar1=None,kenar2=None,şekil=None):
		try:
			if şekil.capitalize() == "Kare" and all([kenar1,not kenar2]):
				return kenar1 ** 2.0
			elif şekil.capitalize() == "Dikdörtgen" and all([kenar1,kenar2]):
				return float(kenar1)*kenar2
			else:
				print("""\tBu fonksiyonun şekil adlı parametresi Kare ve Dikdörtgen olmak üzere sadece 2 adet değer alabilir.
	Doğru kullanım:
	>>> Matematik.mat_alan(9,5,şekil="dikdörtgen")
	45.0
""")
		except AttributeError:
			print("Şekil adlı parametrenin değerini lütfen yazın.")
