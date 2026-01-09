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

def education(request):
    return render(request, 'blog/education.html')

def upcoming_events(request):
    return render(request, 'blog/upcoming_events.html')

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

def news25(request):
    return render(request, "blog/news/news25.html")

def news26(request):
    return render(request, "blog/news/news26.html")

def news27(request):
    return render(request, "blog/news/news27.html")

def news28(request):
    return render(request, "blog/news/news28.html")


def news29(request):
    return render(request, "blog/news/news29.html")


def news30(request):
    return render(request, "blog/news/news30.html")

def news31(request):
    return render(request, "blog/news/news31.html")
def news32(request):
    return render(request, "blog/news/news32.html")
def news33(request):
    return render(request, "blog/news/news33.html")
def news34(request):
    return render(request, "blog/news/news34.html")
def news35(request):
    return render(request, "blog/news/news35.html")
def news36(request):
    return render(request, "blog/news/news36.html")
def news37(request):
    return render(request, "blog/news/news37.html")
def news38(request):
    return render(request, "blog/news/news38.html")
def news39(request):
    return render(request, "blog/news/news39.html")
def news40(request):
    return render(request, "blog/news/news40.html")
def news41(request):
    return render(request, "blog/news/news41.html")
def news42(request):
    return render(request, "blog/news/news42.html")
def news43(request):
    return render(request, "blog/news/news43.html")
def news44(request):
    return render(request, "blog/news/news44.html")
# for news posts to here !!!

def events1(request):
    return render(request, "blog/for_events/events1.html")

def events1res(request):
    return render(request, "blog/for_events/events1res.html")

def events2(request):
    return render(request, "blog/for_events/events2.html")

def events2res(request):
    return render(request, "blog/for_events/events2res.html")

def events3(request):
    return render(request, "blog/for_events/events3.html")

def events4(request):
    return render(request, "blog/for_events/events4.html")
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

# Post creator views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from .models import DynamicPost
from django.conf import settings
import hashlib

def post_creator_auth(request):
    if request.method == 'POST':
        secret_code = request.POST.get('secret_code', '')
        # Hash the input and compare with stored hash
        hashed = hashlib.sha256(secret_code.encode()).hexdigest()
        # Replace this hash with your own secret code's hash
        correct_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'  # This is hash of 'password'

        if hashed == correct_hash:
            request.session['post_creator_authenticated'] = True
            return redirect('post_creator')
        else:
            messages.error(request, 'Invalid secret code')

    return render(request, 'blog/post_creator_auth.html')

import re
import os
from pathlib import Path
import json
import shutil

def post_creator(request):
    # Check if user is authenticated
    if not request.session.get('post_creator_authenticated'):
        return redirect('post_creator_auth')

    if request.method == 'POST':
        # Get form data
        category = request.POST.get('category')
        title_en = request.POST.get('title_en')
        title_ge = request.POST.get('title_ge')
        content_en = request.POST.get('content_en', '').replace('\n', '<br>')
        content_ge = request.POST.get('content_ge', '').replace('\n', '<br>')

        # Get main image (required)
        main_image = request.FILES.get('main_image')
        if not main_image:
            messages.error(request, 'Main image is required!')
            return render(request, 'blog/post_creator.html')

        # Handle main image upload
        images_dir = Path(settings.BASE_DIR) / 'blog' / 'static' / 'blog' / 'images'
        images_dir.mkdir(parents=True, exist_ok=True)

        # Save main image
        main_image_filename = f"{slugify(title_en)}_{main_image.name}"
        main_image_path = images_dir / main_image_filename
        with open(main_image_path, 'wb+') as destination:
            for chunk in main_image.chunks():
                destination.write(chunk)

        # Handle additional images
        additional_images = []
        image_captions_en = []
        image_captions_ge = []

        for i in range(1, 4):
            additional_image = request.FILES.get(f'additional_image{i}')
            if additional_image:
                add_image_filename = f"{slugify(title_en)}_add{i}_{additional_image.name}"
                add_image_path = images_dir / add_image_filename
                with open(add_image_path, 'wb+') as destination:
                    for chunk in additional_image.chunks():
                        destination.write(chunk)
                additional_images.append(add_image_filename)

                # Get captions
                caption_en = request.POST.get(f'image{i}_caption_en', '').replace('\n', '<br>')
                caption_ge = request.POST.get(f'image{i}_caption_ge', '').replace('\n', '<br>')
                image_captions_en.append(caption_en)
                image_captions_ge.append(caption_ge)
            else:
                additional_images.append('')
                image_captions_en.append('')
                image_captions_ge.append('')

        # Find the next number for this category
        next_number = get_next_post_number(category)

        # Create the new numbered post
        create_numbered_post(category, next_number, title_en, title_ge, content_en, content_ge,
                           main_image_filename, additional_images,
                           image_captions_en, image_captions_ge)

        messages.success(request, f'Post "{title_en}" created as {get_category_prefix(category)}{next_number}!')
        return redirect('post_creator')

    return render(request, 'blog/post_creator.html')

def get_category_prefix(category):
    prefixes = {
        'news': 'news',
        'publications': 'publication',
        'events': 'events',
        'gapag_news': 'gapag_news',
        'gapag_events': 'gapag_events'
    }
    return prefixes.get(category, 'post')

def get_next_post_number(category):
    # Read views.py to find existing numbered functions
    views_path = Path(__file__)
    with open(views_path, 'r') as f:
        content = f.read()

    prefix = get_category_prefix(category)

    # Find all existing numbered functions for this category
    if category == 'news':
        pattern = r'def news(\d+)\('
    elif category == 'events':
        pattern = r'def events(\d+)[^r]\('  # Exclude eventsXres
    elif category == 'publications':
        pattern = r'def publication(\d+)\('
    elif category == 'gapag_news':
        pattern = r'def gapag_news(\d+)\('
    elif category == 'gapag_events':
        pattern = r'def gapag_events(\d+)\('
    else:
        return 1

    matches = re.findall(pattern, content)
    if matches:
        numbers = [int(m) for m in matches]
        return max(numbers) + 1
    return 1

def create_numbered_post(category, number, title_en, title_ge, content_en, content_ge,
                        main_image_filename='', additional_images=[],
                        image_captions_en=[], image_captions_ge=[]):
    prefix = get_category_prefix(category)

    # Determine template directory
    if category == 'news':
        template_dir = 'blog/news'
        image_base = 'blog/images/'
        listing_template = 'blog/templates/blog/news/news.html'
    elif category == 'events' or category == 'gapag_events':
        template_dir = 'blog/for_events'
        image_base = 'blog/images/'
        listing_template = None  # Events don't have a listing page yet
    elif category == 'publications':
        template_dir = 'blog/publications'
        image_base = 'blog/images/'
        listing_template = None
    elif category == 'gapag_news':
        template_dir = 'blog/gapag_news'
        image_base = 'blog/images/'
        listing_template = None
    else:
        template_dir = 'blog'
        image_base = 'blog/images/'
        listing_template = None

    # Create template directory if it doesn't exist
    template_path = Path(settings.BASE_DIR) / 'blog' / 'templates' / template_dir
    template_path.mkdir(parents=True, exist_ok=True)

    # Format image paths for static files
    main_image_path = image_base + main_image_filename if main_image_filename else ''
    formatted_additional_images = [image_base + img if img else '' for img in additional_images]

    # Create the template file (without main image in the post itself)
    template_file = template_path / f'{prefix}{number}.html'
    template_content = create_post_template(title_en, title_ge, content_en, content_ge,
                                           '', formatted_additional_images,  # Empty string for main image
                                           image_captions_en, image_captions_ge)
    with open(template_file, 'w', encoding='utf-8') as f:
        f.write(template_content)

    # Add to listing page (e.g., news.html)
    if listing_template and category == 'news':
        add_to_news_listing(number, title_en, title_ge, content_en, content_ge, main_image_filename)

    # Add view function to views.py
    add_view_function(prefix, number, template_dir)

    # Add URL pattern to urls.py
    add_url_pattern(prefix, number)

def create_post_template(title_en, title_ge, content_en, content_ge, main_image_path='', additional_images=[], image_captions_en=[], image_captions_ge=[]):
    # Build gallery section if there are additional images
    gallery_section_en = ""
    gallery_section_ge = ""

    if additional_images:
        gallery_items_en = ""
        gallery_items_ge = ""

        for i, img in enumerate(additional_images):
            if img:
                caption_en = image_captions_en[i] if i < len(image_captions_en) else "Image"
                caption_ge = image_captions_ge[i] if i < len(image_captions_ge) else "სურათი"

                gallery_items_en += f'''
            <figure class="gallery-item">
                <img src="{{% static '{img}' %}}" alt="{caption_en}" class="gallery-image">
                <figcaption>{caption_en}</figcaption>
            </figure>'''

                gallery_items_ge += f'''
            <figure class="gallery-item">
                <img src="{{% static '{img}' %}}" alt="{caption_ge}" class="gallery-image">
                <figcaption>{caption_ge}</figcaption>
            </figure>'''

        if gallery_items_en:
            gallery_section_en = f'''
    <div class="article-gallery">
        <h2 class="gallery-title">Gallery</h2>
        <div class="gallery-grid">{gallery_items_en}
        </div>
    </div>'''

            gallery_section_ge = f'''
    <div class="article-gallery">
        <h2 class="gallery-title">გალერეა</h2>
        <div class="gallery-grid">{gallery_items_ge}
        </div>
    </div>'''

    # Format date
    from datetime import datetime
    current_date = datetime.now().strftime("%B %d, %Y")
    current_date_ge = datetime.now().strftime("%Y წლის %d %B")

    return f'''{{% extends "blog/base.html" %}}
{{% load static %}}
{{% block content %}}

<style>
    .language-toggle {{
        position: fixed;
        top: 100px;
        right: 30px;
        background: white;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        z-index: 100;
    }}
    .lang-btn {{
        display: block;
        width: 60px;
        padding: 10px;
        margin: 5px 0;
        background: #f8fafc;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.5rem;
        transition: all 0.3s ease;
    }}
    .lang-btn.active {{
        background: linear-gradient(135deg, #20b4b9 0%, #1a9399 100%);
        border-color: #20b4b9;
    }}
    .content-lang {{
        display: none;
    }}
    .content-lang.active {{
        display: block;
    }}
    .main-image {{
        width: 100%;
        max-width: 800px;
        margin: 2rem auto;
        display: block;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }}
</style>

<div class="language-toggle">
    <button class="lang-btn active" onclick="switchLanguage('en')">🇬🇧</button>
    <button class="lang-btn" onclick="switchLanguage('ge')">🇬🇪</button>
</div>

<div class="content-lang active" id="content-en">
<article class="news-article">
    <div class="article-header">
        <h1 class="article-title">{title_en}</h1>
        <div class="article-meta">
            <span class="article-date">{current_date}</span>
            <span class="article-category">News</span>
        </div>
    </div>

    {'<img src="{% static ' + repr(main_image_path) + ' %}" alt="' + title_en + '" class="main-image">' if main_image_path else ''}

    <div class="article-content">
        <p class="article-lead">
            {content_en}
        </p>
    </div>
    {gallery_section_en}

    <div class="article-footer">
        <a href="{{% url 'news' %}}" class="back-to-news">← Back to News</a>
        <div class="share-buttons">
            <span>Share:</span>
            <button class="share-btn" onclick="window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(window.location.href))">Facebook</button>
            <button class="share-btn" onclick="window.open('https://twitter.com/intent/tweet?url=' + encodeURIComponent(window.location.href))">Twitter</button>
        </div>
    </div>
</article>
</div>

<div class="content-lang" id="content-ge">
<article class="news-article">
    <div class="article-header">
        <h1 class="article-title">{title_ge}</h1>
        <div class="article-meta">
            <span class="article-date">{current_date_ge}</span>
            <span class="article-category">სიახლეები</span>
        </div>
    </div>

    {'<img src="{% static ' + repr(main_image_path) + ' %}" alt="' + title_ge + '" class="main-image">' if main_image_path else ''}

    <div class="article-content">
        <p class="article-lead">
            {content_ge}
        </p>
    </div>
    {gallery_section_ge}

    <div class="article-footer">
        <a href="{{% url 'news' %}}" class="back-to-news">← სიახლეებზე დაბრუნება</a>
        <div class="share-buttons">
            <span>გაზიარება:</span>
            <button class="share-btn" onclick="window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(window.location.href))">Facebook</button>
            <button class="share-btn" onclick="window.open('https://twitter.com/intent/tweet?url=' + encodeURIComponent(window.location.href))">Twitter</button>
        </div>
    </div>
</article>
</div>

<script>
function switchLanguage(lang) {{
    document.querySelectorAll('.content-lang').forEach(el => {{
        el.classList.remove('active');
    }});
    document.querySelectorAll('.lang-btn').forEach(btn => {{
        btn.classList.remove('active');
    }});
    document.getElementById('content-' + lang).classList.add('active');
    event.target.classList.add('active');
}}
</script>

{{% endblock content %}}'''

def add_view_function(prefix, number, template_dir):
    views_path = Path(__file__)
    with open(views_path, 'r') as f:
        content = f.read()

    # Find the comment marker for this category
    if prefix == 'news':
        marker = '# for news posts to here !!!'
    elif prefix == 'events':
        marker = '# for events posts to here !!!'
    else:
        marker = None

    if marker and marker in content:
        # Insert before the marker - only replace in the actual code section, not in string literals
        # Find the marker that's actually a comment line, not inside a string
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.strip() == marker.strip() and not any(q in lines[max(0,i-5):i] for q in ["'''", '"""', "marker = '"]):
                # Found the actual comment line, not in a string literal
                new_view = f'''def {prefix}{number}(request):
    return render(request, "{template_dir}/{prefix}{number}.html")

'''
                lines.insert(i, new_view.rstrip())
                content = '\n'.join(lines)
                break
    else:
        # Find the last function of this type and insert after it
        pattern = rf'def {prefix}\d+\(request\):\s*\n\s*return render'
        matches = list(re.finditer(pattern, content))

        if matches:
            last_match = matches[-1]
            insert_pos = last_match.end()
            # Find the end of the line
            while insert_pos < len(content) and content[insert_pos] != '\n':
                insert_pos += 1
            insert_pos += 1  # Move past the newline

            new_view = f'''
def {prefix}{number}(request):
    return render(request, "{template_dir}/{prefix}{number}.html")
'''
            content = content[:insert_pos] + new_view + content[insert_pos:]
        else:
            # Just append to the end if no similar functions found
            new_view = f'''
def {prefix}{number}(request):
    return render(request, "{template_dir}/{prefix}{number}.html")
'''
            content = content + new_view

    with open(views_path, 'w') as f:
        f.write(content)

def add_url_pattern(prefix, number):
    urls_path = Path(settings.BASE_DIR) / 'blog' / 'urls.py'
    with open(urls_path, 'r') as f:
        lines = f.readlines()

    # Find where to insert the new URL pattern
    insert_index = len(lines) - 1
    for i in range(len(lines) - 1, -1, -1):
        if f"path('{prefix}" in lines[i] or (prefix == 'news' and "path('news" in lines[i]):
            insert_index = i + 1
            break

    # Create the new URL pattern
    new_pattern = f"    path('{prefix}{number}/', views.{prefix}{number}, name='{prefix}{number}'),\n"

    lines.insert(insert_index, new_pattern)

    with open(urls_path, 'w') as f:
        f.writelines(lines)

def add_to_news_listing(number, title_en, title_ge, content_en, content_ge, main_image_filename):
    """Add the new post to the top of news.html listing page"""
    news_html_path = Path(settings.BASE_DIR) / 'blog' / 'templates' / 'blog' / 'news' / 'news.html'

    with open(news_html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create the new news container HTML
    # Truncate content for preview (first 200 characters)
    preview_en = content_en[:200] + '...' if len(content_en) > 200 else content_en
    preview_ge = content_ge[:200] + '...' if len(content_ge) > 200 else content_ge

    new_news_item = f'''
    <div class="news-container" onclick="window.location.href=`{{% url 'news{number}' %}}`;" style="cursor: pointer;">
        <a href="{{% url 'news{number}' %}}">
            <img src="{{% static 'blog/images/{main_image_filename}' %}}" class="news-image">
        </a>
        <div>
            <h1 class="news-title" data-translation-key="news{number}Title">
                {title_en}
            </h1>
            <p class="news-text" data-translation-key="homeNews{number}Paragraph">
                {preview_en}
            </p>
        </div>
    </div>
'''

    # Find the position right after <div class="body-container">
    insert_position = content.find('<div class="body-container">') + len('<div class="body-container">')

    # Insert the new news item at the top
    new_content = content[:insert_position] + new_news_item + content[insert_position:]

    # Write back the updated content
    with open(news_html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Also update the translation files
    add_translation_keys(number, title_en, title_ge, preview_en, preview_ge)

def add_translation_keys(number, title_en, title_ge, preview_en, preview_ge):
    """Add translation keys for the new post"""
    # Update English translations
    en_json_path = Path(settings.BASE_DIR) / 'blog' / 'static' / 'blog' / 'lang' / 'english.json'
    if en_json_path.exists():
        import json
        with open(en_json_path, 'r', encoding='utf-8') as f:
            translations = json.load(f)

        translations[f'news{number}Title'] = title_en
        translations[f'homeNews{number}Paragraph'] = preview_en

        with open(en_json_path, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)

    # Update Georgian translations
    ge_json_path = Path(settings.BASE_DIR) / 'blog' / 'static' / 'blog' / 'lang' / 'georgian.json'
    if ge_json_path.exists():
        import json
        with open(ge_json_path, 'r', encoding='utf-8') as f:
            translations = json.load(f)

        translations[f'news{number}Title'] = title_ge
        translations[f'homeNews{number}Paragraph'] = preview_ge

        with open(ge_json_path, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)

def view_dynamic_post(request, slug):
    post = get_object_or_404(DynamicPost, slug=slug)
    return render(request, 'blog/dynamic_post.html', {'post': post})

def list_dynamic_posts(request, category):
    posts = DynamicPost.objects.filter(category=category)
    return render(request, 'blog/dynamic_posts_list.html', {
        'posts': posts,
        'category': category
    })