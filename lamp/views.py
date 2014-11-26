from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse

    
def index(request):
    return render(request, 'lamp/index.html')
    
def initialsubmission(request):
    if(request.POST["lamptype"]=='1'):
        f = open('temp.yaml','w+')
        ren=open('lamp/heat_template/lamp_1.txt','r')
        my_str=ren.read()
        f.write(my_str)
        f.close()
        return render(request, 'lamp/initialsubmission.html')
    elif(request.POST["lamptype"]==2 or request.POST["lamptype"]==3 or request.POST["lamptype"]==4):
        f = open('temp.yaml','w+')
        ren=open('lamp/heat_template/lamp_2.txt','r')
        my_str=ren.read()
        f.write(my_str)
        f.close()
        return render(request, 'lamp/initialsubmission.html')
    elif(request.POST["lamptype"]==5):
        f = open('temp.yaml','w+')
        ren=open('lamp/heat_template/lamp_5.txt','r')
        my_str=ren.read()
        f.write(my_str)
        f.close()
        return render(request, 'lamp/initialsubmission.html')

def submission(request) :
    #print "submitting " + request.POST["image"]
    f =open('config.yaml','w+')
    f.write('image :'+ request.POST["image"]+'\n')
    f.write('flavor :'+ request.POST["flavor"]+'\n')
    f.write('key_name :'+ request.POST["key_name"]+'\n')
    f.write('public_net_id :'+ request.POST["public_net_id"]+'\n')
    f.write('public_subnet_id :'+ request.POST["public_subnet_id"]+'\n')
    f.write('private_net_id :'+ request.POST["private_net_id"]+'\n')
    f.write('private_subnet_id :'+ request.POST["private_subnet_id"]+'\n')
    
    x={'image_x':request.POST["image"],'flavor_x':request.POST["flavor"],'key_name_x':request.POST["key_name"],'public_net_id_x':request.POST["public_net_id"],'public_subnet_id_x':request.POST["public_subnet_id"],'private_net_id_x':request.POST["private_net_id"],'private_subnet_id_x':request.POST["private_subnet_id"] };
    #print x
    return render(request, 'lamp/submission.html',{'x': x})
   
    
def edited(request) :
    print "submitting " + request.POST["image"]
    y={'image_y':request.POST["image"],'flavor_y':request.POST["flavor"],'key_name_y':request.POST["key_name"],'public_net_id_y':request.POST["public_net_id"],'public_subnet_id_y':request.POST["public_subnet_id"],'private_net_id_y':request.POST["private_net_id"],'private_subnet_id_y':request.POST["private_subnet_id"] };
    return render(request, 'lamp/edited.html',{'y': y})    