import mimetypes
import os

import cv2
from django.conf import settings as django_settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.defaults import page_not_found, server_error

from FSSApp.LSBSteg import LSBSteg
from accounts.models import Company
from accounts.models import ExtendedUsers


# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
def home(request):
    # encoding part
    if request.method == 'POST' and 'enc_apply' in request.POST:
        content = request.FILES['enc_c_file'].read()
        file = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'encryptsourceimage.png'), 'wb+')
        file.write(content)
        # text encoding
        if request.POST['enc_selectchoice'] == 'enc_text':
            steg = LSBSteg(cv2.imread(file.name))
            processed_text = request.POST['enc_steg_text']
            processed_text = processed_text.replace(' ', '_')
            img_encoded = steg.encode_text(processed_text)
            # path = str('../media/' + {user.username} + '_steg.png')
            BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filename = 'steg_image.png'
            filepath = BASEDIR + '/media/' + filename
            cv2.imwrite(filepath, img_encoded)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            # Return the response value
            return response

        # image encoding
        if request.POST['enc_selectchoice'] == 'enc_image':
            content = request.FILES['enc_c_img'].read()
            imgfile = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'encryptstegimage.png'), 'wb+')
            imgfile.write(content)
            steg = LSBSteg(cv2.imread(file.name))
            # instead of encode image using encode binary
            data = open(imgfile.name, "rb").read()
            new_im = steg.encode_binary(data)
            # new_im = steg.encode_image(cv2.imread(imgfile.name))
            BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filename = 'steg_image.png'
            filepath = BASEDIR + '/media/' + filename
            cv2.imwrite(filepath, new_im)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        # binary encoding
        if request.POST['enc_selectchoice'] == 'enc_binary':
            content = request.FILES['enc_c_bfile'].read()
            binfile = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'encryptstegbinary.bin'), 'wb+')
            binfile.write(content)
            steg = LSBSteg(cv2.imread(file.name))
            # instead of encode image using encode binary
            data = open(binfile.name, "rb").read()
            new_bin = steg.encode_binary(data)
            # new_im = steg.encode_image(cv2.imread(imgfile.name))
            BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filename = 'steg_image.png'
            filepath = BASEDIR + '/media/' + filename
            cv2.imwrite(filepath, new_bin)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response
        return render(request, 'home.html')

    if request.method == 'POST' and 'dec_retrieve' in request.POST:
        print('dec')
        content = request.FILES['dec_c_file'].read()
        file = open(os.path.join(django_settings.STATICFILES_DIRS[4], f'decryptsourceimage.png'), 'wb+')
        file.write(content)
        file.close()
        BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = f'decryptsourceimage.png'
        filepath = BASEDIR + '\\media\\' + filename
        print(filepath)
        # text decoding
        if request.POST['dec_selectchoice'] == 'dec_text':
            im = cv2.imread(filepath)
            steg = LSBSteg(im)
            dec_text = steg.decode_text()
            print(dec_text)
            dec_text = dec_text.replace('_', ' ')
            print(dec_text)
            return render(request, 'home.html', context={'dec_text': dec_text})

        # image decoding
        if request.POST['dec_selectchoice'] == 'dec_image':
            steg = LSBSteg(cv2.imread(filepath))
            binary = steg.decode_binary()
            filename = 'newimage.png'
            filepath = BASEDIR + '/media/' + filename
            with open(filepath, "wb+") as f:
                f.write(binary)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response

        # binary decoding
        if request.POST['dec_selectchoice'] == 'dec_binary':
            steg = LSBSteg(cv2.imread(filepath))
            binary = steg.decode_binary()
            filename = 'newbinary.bin'
            filepath = BASEDIR + '/media/' + filename
            with open(filepath, "wb+") as f:
                f.write(binary)
            path = open(filepath, 'rb')
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            return response

        return render(request, 'home.html')
    return render(request, 'home.html')


@login_required(redirect_field_name=None)
def find_contacts(request):
    if request.user.is_authenticated:
        company = Company.objects.filter(comp_name=request.user.extendedusers.comp_name).values()
        print('company', company)
        extendedusers = ExtendedUsers.objects.filter(user_id__in=company.values_list('emp_id').all())
        print('extended users', extendedusers)
        users = User.objects.filter(id__in=company.values_list('emp_id')).all()
        print('users', users)
        return render(request, 'find_contacts.html', {'company': company, 'eusers': extendedusers, 'users': users})
    return render(request, 'find_contacts.html')


def about_us(request):
    return render(request, 'about_us.html')


@login_required(redirect_field_name=None)
def company_list(request):
    if request.method == 'POST':
        query = request.POST['query']
        if query == '':
            com = Company.objects.filter(emp_position='Owner').distinct('comp_name')
        else:
            com = Company.objects.filter(comp_name__icontains=query, emp_position='Owner').distinct('comp_name')
        return render(request, 'find_contacts.html', {'companies': com})
    return render(request, 'find_contacts.html')


@login_required(redirect_field_name=None)
def join_company(request, name):
    if request.method == 'POST':
        com = Company.objects.get(comp_name=name, emp_position='Owner')
        print(com)
        # join company for user.
        newextendeduser = ExtendedUsers.objects.filter(user=request.user)
        company = Company(comp_name=com.comp_name, emp_id=request.user, emp_position='Employee')
        newextendeduser.update(own_comp=False, comp_name=com.comp_name)
        company.save()
        return HttpResponseRedirect('/find_contacts')
    return render(request, 'find_contacts.html')


@login_required(redirect_field_name=None)
def manage_users(request):
    if request.user.is_authenticated:
        if request.user.extendedusers.own_comp:
            company = Company.objects.filter(comp_name=request.user.extendedusers.comp_name).order_by('id')
            return render(request, 'manage_users.html', {'companies': company})
    return render(request, 'manage_users.html')


@login_required(redirect_field_name=None)
def approve_request(request, username):
    # print('company', company.emp_id.username)
    if request.method == 'POST':
        company = Company.objects.filter(emp_id__username=username)
        company.update(verify=True)

        return HttpResponseRedirect('/manage_users')
    return render(request, 'manage_users.html')


@login_required(redirect_field_name=None)
def deny_request(request, username):
    if request.method == 'POST':
        company = Company.objects.get(emp_id__username=username)
        company.delete()
        newextendedusers = ExtendedUsers.objects.filter(user_id=company.emp_id.id)
        newextendedusers.update(comp_name='')
        return HttpResponseRedirect('/manage_users')
    return render(request, 'manage_users.html')


@login_required(redirect_field_name=None)
def temp_remove_user(request, username):
    if request.method == 'POST':
        company = Company.objects.filter(emp_id__username=username)
        company.update(verify=False)
        return HttpResponseRedirect('/manage_users')
    return render(request, 'manage_users.html')


def error_404(request, exception):
    page_not_found(request, template_name='404.html')
    # return render(request, '404.html', status=404)


def error_500(request):
    server_error(request, template_name='500.html')
    # return render(request, '500.html', status=500)
