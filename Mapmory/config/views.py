from django.shortcuts import render
# 언어 변경
from django.utils import translation
from django.http import HttpResponse, JsonResponse
from django.conf import settings
#비밀번호 변경
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth
# 연결된 이메일
from django.contrib.auth.models import AnonymousUser

#환경설정 홈
def config_home(request):
  return render(request, 'config_home.html')
#보안
def config_secuity(request):
  return render(request, 'security.html')
#다크모드
def dark_mode(request):
  return render(request, 'dark_mode.html')
#알림설정
def notification(request):
  return render(request, 'notification.html')
# 언어 변경
def ko_en(request):
  return render(request, 'lang_url.html')

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language', '')
        if language in [lang_code for lang_code, _ in settings.LANGUAGES]:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = language
            return render(request, 'set_lang.html')
    return render(request, 'set_lang.html')
  
  
# 비밀번호 변경
def change_password(request):
  if request.method == "POST":
    user = request.user
    current_password = request.POST["current_password"]
    if check_password(current_password, user.password): # 기존 비밀번호와 입력한 비밀번호가 같은지 확인
      new_password = request.POST["new_password"]
      confirm_password = request.POST["confirm_password"]
      if new_password == confirm_password: # 새로 변경할 입력한 비밀번호와 확인용 비밀번호가 같은지 확인
        user.set_password(new_password) # 같으면 비밀번호 변경
        user.save()
        messages.success(request, 'Password has been changed successfully.')
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('config_security') # 비밀번호 변경 완료 후 넘어갈 페이지 url
      else:
        messages.error(request, 'Password not same')
    else:
      messages.error(request, 'Password not correct')
    return render(request, 'change_password.html')
  else:
    return render(request, 'change_password.html')
  
# 연결된 이메일
def show_email(request):
    user = request.user
    if isinstance(user, AnonymousUser):
      return render(request, 'email.html', {'email':None})
    return render(request, 'email.html', {'email': user.email})

def config_secuity(request):
  return render (request, 'security.html')


#다크모드
def dark_mode(request):
  dark_mode_enabled = request.session.get('dark_mode', False)

  context = {
        'DARK_MODE': dark_mode_enabled,
    }
  return render(request, 'dark_mode.html', context)
def toggle_dark_mode(request):
    # Toggle the dark mode setting in the session
    current_dark_mode = request.session.get('dark_mode', False)
    request.session['dark_mode'] = not current_dark_mode
    request.session.modified = True
    return JsonResponse({'success': True})

#알림설정
def notification(request):
  return render(request, 'notification.html')

def ko_en(request):
   return render(request, 'lang_url.html')



