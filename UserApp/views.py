from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import urllib.parse
import json


def home_page(request):
    users = []
    with open('user_data.json', 'r') as infile:
        users_json = json.load(infile)
        for k, v in users_json.items():
            if k != 'count':
                users.append([v['first_name'], v['last_name'], v['email'], v['phone'], v['id']])
    return render(request, 'login.html', context={'users': users})

def urlencoded_to_json(urlencoded_data):
    parsed_data = urllib.parse.parse_qs(urlencoded_data)
    data_dict = {}
    for key, value in parsed_data.items():
        decoded_key = key
        decoded_value = value[-1]
        data_dict[decoded_key] = decoded_value
    json_data = json.dumps(data_dict)
    return json_data

@csrf_exempt
def create_user_view(request):
    data = json.loads(urlencoded_to_json(request.body.decode()))
    data = {
        'first_name': data['firstname'],
        'last_name': data['lastname'],
        'email': data['email'],
        'phone': data['phone'],
    }
    with open('user_data.json', 'r') as infile:
        users = json.load(infile)
        users['count']+=1
        data['id']=users['count']
        users[users['count']] = data

    with open('user_data.json', 'w') as outfile:
        json.dump(users, outfile, indent=2)

    users = []
    with open('user_data.json', 'r') as infile:
        users_json = json.load(infile)
        for k,v in users_json.items():
            if k != 'count':
                users.append([v['first_name'], v['last_name'], v['email'], v['phone'], v['id']])
    return render(request, 'login.html', context={'users': users})

# def list_users_view(request):
#     context = {}
#     context["data"] = GeeksModel.objects.get(id=id)
#     return render(request, "detail_view.html", context)



# class AppUserViewSet(viewsets.ModelViewSet):
#     def create(self, request):
#         data = request.data
#         serializer = UserAppSerializer(data=data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return HttpResponse("User is created successfully")
#         return  HttpResponse("User is not created")

