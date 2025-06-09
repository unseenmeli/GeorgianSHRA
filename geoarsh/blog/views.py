from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def about_association(request):
    return render(request, 'blog/aboutas.html')

def become_member(request):
    return render(request, 'blog/aboutbm.html')

def scientific_information(request):
    return render(request, 'blog/scientificinfo.html')

def publications(request):
    return render(request, 'blog/scientpb.html')

def about_congresses(request):
    return render(request, 'blog/scientac.html')

def guidelines(request):
    return render(request, 'blog/guidelines.html')

def national_guidelines(request):
    return render(request, 'blog/guideen.html')

def translated_guidelines(request):
    return render(request, 'blog/guidetr.html')

def english_guidelines(request):
    return render(request, 'blog/guident.html')

def events(request):
    return render(request, 'blog/events.html')

# for patients posts from here !!!

def for_patients(request):
    return render(request, 'blog/for_patients/forpatients.html')

def for_patients1(request):
    return render(request, 'blog/for_patients/forpatients1.html')

def for_patients2(request):
    return render(request, 'blog/for_patients/forpatients2.html')

def for_patients3(request):
    return render(request, 'blog/for_patients/forpatients3.html')

def for_patients4(request):
    return render(request, 'blog/for_patients/forpatients4.html')

def for_patients5(request):
    return render(request, 'blog/for_patients/forpatients5.html')

# for patients posts to here !!!

def contact(request):
    return render(request, 'blog/contact.html')

# for news posts from here !!!

def news(request):
    return render(request, 'blog/news/news.html')

def news1(request):
    return render(request, 'blog/news/news1.html')

def news2(request):
    return render(request, 'blog/news/news2.html')

def news3(request):
    return render(request, 'blog/news/news3.html')

def news4(request):
    return render(request, 'blog/news/news4.html')

def news5(request):
    return render(request, 'blog/news/news5.html')

def news6(request):
    return render(request, 'blog/news/news6.html')

def news7(request):
    return render(request, 'blog/news/news7.html')

def news8(request):
    return render(request, 'blog/news/news8.html')

def news9(request):
    return render(request, 'blog/news/news9.html')

def news10(request):
    return render(request, 'blog/news/news10.html')

def news11(request):
    return render(request, 'blog/news/news11.html')

def news12(request):
    return render(request, 'blog/news/news12.html')

def news13(request):
    return render(request, 'blog/news/news13.html')

def news14(request):
    return render(request, 'blog/news/news14.html')

def news15(request):
    return render(request, 'blog/news/news15.html')

def news16(request):
    return render(request, 'blog/news/news16.html')

def news17(request):
    return render(request, 'blog/news/news17.html')

def news18(request):
    return render(request, 'blog/news/news18.html')

def news19(request):
    return render(request, 'blog/news/news19.html')

def news20(request):
    return render(request, "blog/news/news20.html")

def news21(request):
    return render(request, "blog/news/news21.html")

def news22(request):
    return render(request, "blog/news/news22.html")

def news23(request):
    return render(request, "blog/news/news23.html")

def news24(request):
    return render(request, "blog/news/news24.html")

# for news posts to here !!!

def events1(request):
    return render(request, "blog/for_events/events1.html")

# translations from here !!!

from django.conf import settings
from pathlib import Path
import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def get_translations(request, lang):
    path = Path(settings.BASE_DIR) / 'blog' / 'static' / 'blog' / 'lang' / f'{lang}.json'
    if path.exists():
        with path.open(encoding='utf-8') as f:
            return JsonResponse(json.load(f))
    return JsonResponse({}, status=404)



# translations to here !!!