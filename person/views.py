from django.shortcuts import render
from .models import person_collection
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt  


def index(request):
    return HttpResponse("<h1>App is running..</h1>")



def add_person(request):
    records={
        "firstname":"Deepali",
        "lastname":"Thakur",
        "Roll_No":"21/215",
        "Email" : "deepalithakur@gmail.com",
        "Marks" : 95
        
    }
    person_collection.insert_one(records)
    return HttpResponse("new person is added")




def get_all_person(request):
    person= person_collection.find()
    return HttpResponse(person)



# # recent added
# @api_view(['POST'])
# def add_person(request):
#     if request.method == 'POST':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
        
