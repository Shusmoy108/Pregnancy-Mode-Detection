from django.http import HttpResponse
from django.shortcuts import render,redirect
import pymongo
from pregnancy_mode_detection.report import Report 
import json

# connection = pymongo.MongoClient("ds035557.mlab.com", 35557)
# db = connection["pregnancy-database"]
reports=[]
client = pymongo.MongoClient("mongodb://Shusmoy13:Sucharita13@ds035557.mlab.com:35557/pregnancy-database?retryWrites=false")
db = client['pregnancy-database']
db.logout()
db.authenticate("pregnancy", "southern13")
pregnancy_data = db["pregnancy-data"]

def templateexample(request):
    return render(request,'base.html', {'title': "Pregnancy Mode Detection","body":"inherit template page"})

def form(request):
    return render(request,'form.html', {'title': "Pregnancy Mode Detection"})
def showreport(request):
    x=pregnancy_data.find()
    # print(x[0])
    reports=[]
    for r in x: 
        rep=Report(r['pname'],r['hname'],r['age'],r['uterus'],r['fetus'],r['bpd'],r['crl'],r['fl'],r['ac'],r['efw'],r['edd'],r['pl'],r['gage'],r['fhb'],r['fm'],r['presentation'],r['lv'],r['diabetis'],r['precz'])
        rep.controlword=r['controlword']
        rep.safe=r['safe']
        reports.append(rep)
    #print(reports)
    return render(request,'reports.html',{'title': "Pregnancy Mode Detection",'reports':reports})
def report(request,id):
    #   r = request.GET
    #   print(r.get('id'))
    #   id= r.get('id')
      #print(id)
      return render(request,'report.html',{'title': "Pregnancy Mode Detection",'report':reports[int(id)-1]})

def login(request):
    if request.method == 'POST':
        r = request.POST
        username = r.get('username')
        password = r.get('pswd')
        # print(mname)
        # print(morder)
        if(username == "pregnancy" and password=="1234"):
            return redirect('addreport')
        # M = Module(name=mname, order=morder, category="config")
        # M.save()
        else:
            return redirect('login')
    else:
        context = {

        }
        return render(request, 'login.html', context)
        # M = Module(name=mname, order=morder, category="config")
        # M.save()
def addreport(request):
    # print(db)
    
    # print(pregnancy_data)
    # mydict = { "name": "John", "address": "Highway 37" }
    # x = db.data.insert_one(mydict)
    # print(x)
    if request.method == 'POST':
        r = request.POST
        print(r.get('gage'))
        print(r.get('FHB'))
        #print(r.get('pname')+r.get('hname')+r.get('age')+r.get('uterus')+r.get('fetus')+r.get('BPD')+r.get('CRL')+r.get('FL')+r.get('AC')+r.get('EFW')+r.get('EDD')+r.get('PL')+r.get('gage')+r.get('FHB')+r.get('FM')+r.get('presentation')+r.get('LV')+r.get('Diabetis')+r.get('PC'))
        rep= Report(r.get('pname'),r.get('hname'),r.get('age'),r.get('uterus'),r.get('fetus'),r.get('BPD'),r.get('CRL'),r.get('FL'),r.get('AC'),r.get('EFW'),r.get('EDD'),r.get('PL'),r.get('gage'),r.get('FHB'),r.get('FM'),r.get('presentation'),r.get('LV'),r.get('Diabetis'),r.get('PC'))
        err= rep.validate()
        #print(err)
        if(err!={}):
             return render(request,'form.html', {'title': "Pregnancy Mode Detection",'err':err})

        # uterus = r.get('uterus')
        # fetus = r.get('fetus')
        # print(uterus)
        # print(fetus)
        # if(username == "shusmoy" and password=="1234"):
        #     return redirect('appointment')
        # M = Module(name=mname, order=morder, category="config")
        # M.save()
        # else:
        else:
            rep.createcontrol()
            report_json = json.dumps(rep.__dict__)
            # print(report_json)
            pregnancy_data.insert_one(rep.__dict__)
            #x = db.data.insert_one(rep.__dict__)
            return render(request,'thanks.html', {'title': "Pregnancy Mode Detection"})
    else:
        context = {

        }
        return render(request,'form.html', {'title': "Pregnancy Mode Detection",'err':{}})