from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/association/', views.about_association, name='about_association'),
    path('about/become-member/', views.become_member, name='become_member'),
    path('scientific-information/', views.scientific_information, name='scientific_information'),
    path('scientific-information/publications/', views.publications, name='publications'),
    path('scientific-information/about-congresses/', views.about_congresses, name='about_congresses'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('guidelines/national/', views.national_guidelines, name='national_guidelines'),
    path('guidelines/translated/', views.translated_guidelines, name='translated_guidelines'),
    path('guidelines/english/', views.english_guidelines, name='english_guidelines'),
    path('events/', views.events, name='events'),

    # for patients posts from here !!!
    
    path('for-patients/', views.for_patients, name='for_patients'),
    path('for-patients1/', views.for_patients1, name='for_patients1'),
    path('for-patients2/', views.for_patients2, name='for_patients2'),
    path('for-patients3/', views.for_patients3, name='for_patients3'),
    path('for-patients4/', views.for_patients4, name='for_patients4'),
    path('for-patients5/', views.for_patients5, name='for_patients5'),

    # for patients posts to here !!!

    path('contact/', views.contact, name='contact'),

    # for news posts from here !!!

    path('news/', views.news, name='news' ),
    path('news1/', views.news1, name='news1' ),
    path('news2/', views.news2, name='news2' ),
    path('news3/', views.news3, name='news3' ),
    path('news4/', views.news4, name='news4' ),
    path('news5/', views.news5, name='news5' ),
    path('news6/', views.news6, name='news6' ),
    path('news7/', views.news7, name='news7' ),
    path('news8/', views.news8, name='news8' ),
    path('news9/', views.news9, name='news9' ),
    path('news10/', views.news10, name='news10' ),
    path('news11/', views.news11, name='news11' ),
    path('news12/', views.news12, name='news12' ),
    path('news13/', views.news13, name='news13' ),
    path('news14/', views.news14, name='news14' ),
    path('news15/', views.news15, name='news15' ),
    path('news16/', views.news16, name='news16' ),
    path('news17/', views.news17, name='news17' ),
    path('news18/', views.news18, name='news18' ),
    path('news19/', views.news19, name='news19' ),
    path('news20/', views.news20, name='news20'),
    path('news21/', views.news21, name='news21'),
    path('news22/', views.news22, name='news22'),
    path('news23/', views.news23, name='news23'),
    path('news24/', views.news24, name='news24'),

    # for news posts to here !!!

    path('events1/', views.events1, name='events1'),

    # translation thing 
    
    path('api/translations/<str:lang>/', views.get_translations, name='get_translations'),

    # translation end
]
