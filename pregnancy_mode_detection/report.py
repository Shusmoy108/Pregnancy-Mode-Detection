class Report:
	def __init__(self, pname, hname,age,uterus,fetus,bpd,crl,fl,ac,efw,edd,pl,gage,fhb,fm,presentation,lv,diabetis,precz):
		self.pname = pname
		self.hname = hname
		self.age = age
		self.uterus = uterus
		self.fetus = fetus
		self.bpd = bpd
		self.crl = crl
		self.fl = fl
		self.ac = ac
		self.efw = efw
		self.edd = edd
		self.pl = pl
		self.gage = gage
		self.fhb = fhb
		self.fm = fm
		self.presentation = presentation
		self.lv = lv
		self.diabetis = diabetis
		self.precz = precz
		self.safe="X"
		self.controlword=""
	def createcontrol(self):
		if self.uterus=='Gravid':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if self.fetus=='Single':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if int(self.bpd)>90:
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		self.controlword=self.controlword+"X" #CRL
		self.controlword=self.controlword+"X" #FL
		self.controlword=self.controlword+"X" #AC
		if int(self.efw)>2.5:
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if int(self.edd)>37:
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if self.pl=='Anterior' or self.pl== "Posterior" or self.pl=='Fundal':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if int(self.gage)==39:
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if int(self.fhb)>=110 and int(self.fhb)<=160:
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if self.fm=='1':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if self.presentation=='Cephalic':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if self.lv=='Adequate':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		self.controlword=self.controlword+"X" #age
		if self.diabetis=='1':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
		if self.presentation=='1':
			self.controlword=self.controlword+"1"
		else:
			self.controlword=self.controlword+"0"
	def validate(self):
		error={}
		print(self.pname)
		if(self.pname==None):
			error["pname"]="A patient name must be given"
		if(self.hname==None):
			error["hname"]="A hospital name must be given"
		if(self.age==None):
			error["age"]="Patient age must be given"
		if(self.fetus==None):
			error["fetus"]="You must select a fetus type"
		if(self.uterus==None):
			error["uterus"]="You must select a uterus type"
		if(self.bpd==None):
			error["bpd"]="Biparietal diameter must be given"
		if(self.crl==None):
			error["crl"]="Crown-rump-length  must be given"
		if(self.fl==None):
			error["fl"]="Femur length must be given"
		if(self.ac==None):
			error["ac"]="Abdominal circumference must be given"
		if(self.efw==None):
			error["efw"]="Estimated fetal weight must be given"
		if(self.edd==None):
			error["edd"]="Expected date of delivery must be given"
		if(self.pl==None):
			error["pl"]="You must select a Placental localization type"
		if(self.gage==None):
			error["gage"]="Gestational age must be given"
		if(self.fhb==None):
			error["fhb"]="Fetal Heart beat must be given"
		if(self.fm==None):
			error["fm"]="Fetal Movement must be selected"
		if(self.presentation==None):
			error["presentation"]="You must select a presentation type"
		if(self.lv==None):
			error["lv"]="You must select a Liquor volume type"
		if(self.diabetis==None):
			error["diabetis"]="You must answer about diabetis"
		if(self.precz==None):
			error["precz"]="You must answer about previous czerian birth"
		print(error)
		return error