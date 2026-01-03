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
    path('GAPAG/', views.guidelines, name='guidelines'),
    path('GAPAG/About/', views.national_guidelines, name='national_guidelines'),
    path('GAPAG/News/', views.translated_guidelines, name='translated_guidelines'),
    path('GAPAG/Events/', views.english_guidelines, name='english_guidelines'),
    path('education/', views.education, name='education'),
    path('education/upcoming-events/', views.upcoming_events, name='upcoming_events'),
    path('education/completed-events/', views.events, name='events'),

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
    path('news25/', views.news25, name='news25'),
    path('news26/', views.news26, name='news26'),
    path('news27/', views.news27, name='news27'),
    path('news28/', views.news28, name='news28'),
    path('news29/', views.news29, name='news29'),
    path('news30/', views.news30, name='news30'),
    path('news31/', views.news31, name='news31'),
    path('news32/', views.news32, name='news32'),
    path('news33/', views.news33, name='news33'),
    path('news34/', views.news34, name='news34'),
    path('news35/', views.news35, name='news35'),
    path('news36/', views.news36, name='news36'),
    path('news37/', views.news37, name='news37'),
    path('news38/', views.news38, name='news38'),
    path('news39/', views.news39, name='news39'),
    path('news40/', views.news40, name='news40'),
    path('news41/', views.news41, name='news41'),
    path('news42/', views.news42, name='news42'),
    path('news43/', views.news43, name='news43'),

    # for news posts to here !!!

    path('events1/', views.events1, name='events1'),
    path('events1res/', views.events1res, name='events1res'),
    path('events2/', views.events2, name='events2'),
    path('events2res/', views.events2res, name='events2res'),
    path('events3/', views.events3, name='events3'),
    path('events4/', views.events4, name='events4'),

    # translation thing

    path('api/translations/<str:lang>/', views.get_translations, name='get_translations'),

    # translation end

    # Post creator URLs
    path('create-post-admin/', views.post_creator_auth, name='post_creator_auth'),
    path('create-post/', views.post_creator, name='post_creator'),
    path('post/<slug:slug>/', views.view_dynamic_post, name='view_dynamic_post'),
    path('posts/<str:category>/', views.list_dynamic_posts, name='list_dynamic_posts'),
]
