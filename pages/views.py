import json
from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.db.models import F
from .models import Schedule
from .validation import validate
DEFAULT=json.loads((Path(__file__).parent/'default_schedule.json').read_text(encoding='utf-8'))
def record(request):
    if not request.session.session_key:request.session.create()
    return Schedule.objects.get_or_create(browser_key=request.session.session_key,defaults={'state':DEFAULT})[0]
@ensure_csrf_cookie
def cla(request):
    obj=record(request)
    return render(request,'pages/cla.html',{'initial':{'state':obj.state,'revision':obj.revision}})
def courses(request):return render(request,'pages/courses.html')
def focus(request):return render(request,'pages/focus.html')
@require_http_methods(['GET','POST'])
def api(request):
    obj=record(request)
    if request.method=='GET':return JsonResponse({'state':obj.state,'revision':obj.revision})
    try:
        if len(request.body)>2*1024*1024:raise ValueError('資料過大。')
        payload=json.loads(request.body)
        if not isinstance(payload,dict) or type(payload.get('revision'))!=int:raise ValueError('版本格式錯誤。')
        state=validate(payload.get('state'))
    except (ValueError,TypeError,KeyError) as e:return JsonResponse({'error':str(e)},status=400)
    n=Schedule.objects.filter(pk=obj.pk,revision=payload['revision']).update(state=state,revision=F('revision')+1)
    if not n:return JsonResponse({'error':'其他分頁已修改課表，請重新整理後再試。'},status=409)
    return JsonResponse({'revision':payload['revision']+1})
