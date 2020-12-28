# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.conf import settings
from pykakasi.kakasi import kakasi
from .pythonfiles import change_face
import datetime
import os

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #form.photo = japanese2romaji(form.photo)
            form.save()
            return redirect('result')
    else:
        form = DocumentForm()
        return render(request, 'app1/index.html')

    #return render(request, 'app1/index.html')

def result(request):
    # ファイル名の変更 
    max_id = Document.objects.latest('id').id
    obj = Document.objects.get(id = max_id)
    now = datetime.datetime.now()
    #picName = obj.photo.url.encode('unicode-escape')
    #picName = picName.decode('unicode-escape')
    #path1 = settings.BASE_DIR + picName
    #path2 = settings.BASE_DIR + '/media/documents/' + now.strftime('%Y%m%d_%H%M%S') + '.jpg'
    #os.rename(path1, path2) 
    input_path = settings.BASE_DIR + obj.photo.url
    output_path = settings.BASE_DIR + "/media/output/output.jpg"
    change_face.overlay_face(input_path,output_path)
    return render(request, 'app1/result.html', {
        'obj':obj,
    })


###########ここをカスタマイズ############

def gray(input_path,output_path):
    img = cv2.imread(input_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, img_gray)

def japanese2romaji(japanese):
    print(japanese)
    kakasiObj = kakasi()
    kakasiObj.setMode('H', 'a')
    kakasiObj.setMode('K', 'a')
    kakasiObj.setMode('J', 'a')
    conv = kakasiObj.getConverter()
    romaji = conv.do(japanese)
    return romaji

######################################