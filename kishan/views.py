from django.http import HttpResponse

from kishan.models import Staff


def kishanmethod(request):
    return HttpResponse('Hello, World!   ' + str(Staff.objects.filter(staff_name="Arjun").first().staff_salary))
