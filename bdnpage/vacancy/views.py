from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Vacancy
from .forms import VacancyForm


# Create your views here.


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy/vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'vacancy/vacancy_detail.html', {'vacancy': vacancy})

def vacancy_create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy:vacancy_list')
    else:
        form = VacancyForm()
    return render(request, 'vacancy/vacancy_form.html', {'form': form})

class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'vacancy/vacancy_confirm_delete.html'
    success_url = reverse_lazy('vacancy:vacancy_list')
