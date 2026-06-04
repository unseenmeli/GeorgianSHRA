#!/usr/bin/env python3
"""
Generate PDF for GARSH First Congress Program
This script creates a PDF with the conference program matching the website styling
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os
import sys

# Register the custom Georgian font
try:
    custom_font_path = '/Users/unseenmeli/Downloads/bpg_glaho_sylfaen 2.ttf'

    if os.path.exists(custom_font_path):
        pdfmetrics.registerFont(TTFont('Georgian', custom_font_path))
        print(f"Registered Georgian font: {custom_font_path}")
    else:
        print(f"ERROR: Font not found at {custom_font_path}")
        sys.exit(1)

except Exception as e:
    print(f"Error registering font: {e}")
    sys.exit(1)

def create_program_pdf(output_filename="GARSH_First_Congress_Program.pdf"):
    """Create the conference program PDF"""

    # Create the PDF document
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=50
    )

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()

    # Custom styles matching the website - using Georgian font with better styling
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#20b4b9'),
        spaceAfter=25,
        alignment=TA_CENTER,
        fontName='Georgian',
        leading=34
    )

    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.HexColor('#1a2332'),
        spaceAfter=40,
        alignment=TA_LEFT,
        fontName='Georgian',
        leading=38
    )

    session_header_style = ParagraphStyle(
        'SessionHeader',
        parent=styles['Heading2'],
        fontSize=22,
        textColor=colors.HexColor('#20b4b9'),
        spaceAfter=12,
        spaceBefore=25,
        fontName='Georgian',
        leading=26
    )

    moderator_style = ParagraphStyle(
        'Moderator',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#6b7280'),
        spaceAfter=18,
        fontName='Georgian',
        leading=16
    )

    time_style = ParagraphStyle(
        'Time',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.white,
        fontName='Georgian',
        leading=14
    )

    program_title_style = ParagraphStyle(
        'ProgramTitle',
        parent=styles['Normal'],
        fontSize=13,
        textColor=colors.HexColor('#1a2332'),
        spaceAfter=6,
        fontName='Georgian',
        leading=17
    )

    speaker_style = ParagraphStyle(
        'Speaker',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#6b7280'),
        spaceAfter=12,
        fontName='Georgian',
        leading=15
    )

    break_style = ParagraphStyle(
        'Break',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.white,
        alignment=TA_CENTER,
        fontName='Georgian',
        leading=18,
        backColor=colors.HexColor('#20b4b9'),
        leftIndent=20,
        rightIndent=20,
        spaceBefore=12,
        spaceAfter=12
    )

    # Add cover image at top of first page
    cover_image_path = '/Users/unseenmeli/Documents/oneone.jpg'
    if os.path.exists(cover_image_path):
        # Get available width (accounting for margins)
        page_width, page_height = A4
        usable_width = page_width - 80  # 40 left + 40 right margin

        # Create image that fits full width, keeping aspect ratio
        from PIL import Image as PILImage
        pil_img = PILImage.open(cover_image_path)
        img_width, img_height = pil_img.size
        aspect_ratio = img_height / img_width

        # Calculate height based on width and aspect ratio
        cover_height = usable_width * aspect_ratio

        cover_img = Image(cover_image_path, width=usable_width, height=cover_height)
        elements.append(cover_img)
        elements.append(Spacer(1, 0.3*inch))
    else:
        print(f"Warning: Cover image not found at {cover_image_path}")

    # Add title
    title = Paragraph("კონფერენციის პროგრამა", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.15*inch))

    # Registration
    add_program_item(elements, "9:00-10:00", "მონაწილეთა რეგისტრაცია", "",
                    time_style, program_title_style, speaker_style)

    # Opening
    add_program_item(elements, "10:00-10:15", "კონგრესის გახსნა, მისალმება", "",
                    time_style, program_title_style, speaker_style)

    # Session I
    elements.append(Paragraph("I სესია", session_header_style))
    elements.append(Paragraph("მოდერატორები: პროფ. ჯენარო ქრისტესაშვილი, პროფ. არჩილ ხომასურიძე, პროფ. დავით მეტრეველი", moderator_style))

    add_program_item(elements,
        "10:15-10:30",
        "პრობიოტიკები საშარდე გზების ინფექციის მკურნალობაში",
        "არჩილ ჩხოტუა - მედიცინის დოქტორი, ლ. მანაგაძის სახ. უროლოგიის ეროვნული ცენტრის დირექტორი სამეცნიერო დარგში. საქართველოს უროლოგთა ასოციაციის გენერალური მდივანი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "10:30-10:40",
        "ჰიპერჰომოცისტეინემიისა და MTHFR გენების პოლიმორფიზმის გავლენა რეპროდუქციულ გამოსავლებზე პაციენტებში პოლიცისტური საკვერცხეების სინდრომით",
        "მანანა ურჯუმელაშვილი - მედიცინის დოქტორი, უნივერსიტეტი \"გეომედი\" - ასისტენტ პროფესორი, რმც \"უნივერსი\"",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "10:40-10:50",
        "განსხვავებული სქესობრივი განვითარების დიფერენციალური დიაგნოსტიკა ქალური ფენოტიპისა და საშვილოსნოს არარსებობის მქონე პირებში",
        "ანა ჯიბლაძე - თსუ-ს დოქტორანტი, რმც \"უნივერსი\", საქართველოს რეპროდუქციული და სქესობრივი ჯანმრთელობის ასოციაციის დოქტორანტურის და რეზიდენტურის სტუდენტებთან ურთიერთობის მიმართულების ხელმძღვანელი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "10:50-11:00",
        "მიულერის ანომალიების დიაგნოსტიკის შესაძლებლობები ქალებში რეპროდუქციული დარღვევებით",
        "ია ჩაფიძე - თსუ-ს დოქტორანტი, რეპროდუქციული მედიცინის ცენტრი \"უნივერსი\"",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "11:00-11:10",
        "პერიფერიული ნაადრევი სქესობრივი განვითარება საკვერცხის ცალმხრივი აგენეზიის ფონზე",
        "თინათინ გორშკოვა - პროფ. ჟორდანიას და პროფ. ხომასურიძის რეპროდუქტოლოგიის ინსტიტუტის რეზიდენტი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "11:10-11:25",
        "თანამედროვე მიდგომები ანდროგენიზაციის მკურნალობაში",
        "პროფესორი ჯენარო ქრისტესაშვილი - მედიცინის დოქტორი, თსუ, რმც \"უნივერსი\". საქართველოს რეპროდუქციული და სქესობრივი ჯანმრთელობის ასოციაციის მთავარი ექსპერტი",
        time_style, program_title_style, speaker_style
    )

    # Break - with full width background
    elements.append(Spacer(1, 0.1*inch))
    break_para = Paragraph("11:30-11:50 შესვენება - ყავა/ჩაი", break_style)
    elements.append(break_para)
    elements.append(Spacer(1, 0.1*inch))

    # Session II
    elements.append(Paragraph("II სესია", session_header_style))
    elements.append(Paragraph("მოდერატორები: პროფ. ელენე ასანიძე, პროფ. თამარ ალიბეგაშვილი, პროფ. მაია ჩხაიძე", moderator_style))

    add_program_item(elements,
        "11:50-12:00",
        "საქართველოში ექიმების სამუშაო რეალობა და მისი გავლენა მენტალურ ჯანმრთელობასა და ცხოვრების ხარისხზე",
        "ალექსანდრე ასანიძე - თსსუ, საქართველოს რეპროდუქციული და სქესობრივი ჯანმრთელობის ასოციაციის სამედიცინო უნივერსიტეტის სტუდენტებთან ურთიერთობის მიმართულების ხელმძღვანელი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "12:00-12:15",
        "მიო-ინოზიტოლი - ინსულინრეზისტენტობის მართვის ახალი სტანდარტი: მეთფორმინიდან კომპლექსურ მიდგომამდე",
        "შოთა ჯანჯღავა - მედიცინის დოქტორი, ასოცირებული პროფესორი, კლინიკური კვლევების დეპარტამენტის ხელმძღვანელი, \"ენდოკრინოლოგიის ეროვნული ინსტიტუტის\" დირექტორის მოადგილე",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "12:15-12:30",
        "მტკიცებულებებზე დაფუძნებული პრევენცია: ვაქცინაცია როგორც ჯანდაცვის გარანტი",
        "პროფესორი მაია ჩხაიძე - მედიცინის დოქტორი, ციციშვილის სახ. ბავშვთა კლინიკის სამედიცინო დირექტორი. პედიატრთა აკადემიის პრეზიდენტი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "12:30-12:45",
        "ადამიანი პაპილომავირუსის (HPV) ვაქცინაცია: კიბოს პრევენციის მთავარი სტრატეგია",
        "თამარ ალიბეგაშვილი - მედიცინის აკადემიური დოქტორი, საქართველოს საშვილოსნოს ყელის პათოლოგიის და კოლპოსკოპიის საზოგადოების თავმჯდომარე, ეროვნული სკრინინგ ცენტრის გინეკოლოგიური სამსახურის ხელმძღვანელი. IFCPC-IARC -ის კოლპოსკოპიის კურსის ტრენერი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "12:45-13:00",
        "ესტროგენდეფიციტური მდგომარეობების მართვის თანამედროვე მიდგომები",
        "პროფესორი ელენე ასანიძე - მედიცინის დოქტორი, თბილისის სამედიცინო აკადემია, საქართველოს რეპროდუქციული და სქესობრივი ჯანმრთელობის ასოციაციის პრეზიდენტი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "13:00-13:15",
        "ფერტილობის შენარჩუნება: თანამედროვე ტენდენციები და სტრატეგიული მიდგომები",
        "ლუდმილა ბარბაქაძე - მედიცინის დოქტორი, თსუ-ს ასისტენტ პროფესორი, კლინიკა ლიდერმედი, ინ ვიტრო განაყოფიერების განყოფილების ხელმძღვანელი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "13:15-13:25",
        "ჭარბი მენსტრუაციული სისხლდენა - კომპლექსური მართვა",
        "პროფესორი მარიამ ხარაიშვილი - მედიცინის დოქტორი, ქართულ-ამერიკული უნივერსიტეტი, \"ჯეო ჰოსპიტალი\"",
        time_style, program_title_style, speaker_style
    )

    # Break - with full width background
    elements.append(Spacer(1, 0.1*inch))
    break_para = Paragraph("13:30-14:30 შესვენება/ლანჩი", break_style)
    elements.append(break_para)
    elements.append(Spacer(1, 0.1*inch))

    # Session III
    elements.append(Paragraph("III სესია", session_header_style))
    elements.append(Paragraph("მოდერატორები: პროფ. მაკა გეგეჭკორი, პროფ. ლუდმილა ბარბაქაძე, პროფ. შორენა ჭიოკაძე", moderator_style))

    add_program_item(elements,
        "14:30-14:45",
        "რეპროდუქციული გენეტიკის პერსპექტივები: საქართველოს გამოცდილება და კლინიკური ინტეგრაციის გზები",
        "მარიამ ჭიპაშვილი - მედიცინის დოქტორი, ასოცირებული პროფესორი, თსუ, ჟორდანიას სამედიცინო ცენტრი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "14:45-14:55",
        "ადენომიოზის დიაგნოსტიკა: ტრანსვაგინური ულტრაბგერის, მაგნიტურ-რეზონანსული ტომოგრაფიისა და ჰისტეროსკოპიის შედარებითი ანალიზი",
        "ლელა თანდაშვილი - მედიცინის დოქტორი, ქართულ-ამერიკული უნივერსიტეტის შინაგანი მედიცინის დეპარტამენტის ხელმძღვანელი, ასოცირებული პროფესორი, ავერსის კლინიკა",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "14:55-15:10",
        "ენდომეტრიოზის მკურნალობის გრძელვადიანი შესაძლებლობები ახალგაზრდა ასაკის ქალებში",
        "პროფესორი მაკა გეგეჭკორი - მედიცინის დოქტორი, თსსუ - კლინიკური პროფესორი, ზურაბ საბახტარაშვილის რეპროდუქციული კლინიკის სასწავლო-სამეცნიერო მიმართულების ხელმძღვანელი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "15:10-15:20",
        "ქრონიკული ენდომეტრიტი - ძველი პრობლემის ახალი სახე. კავშირი რეპროდუქციულ დანაკარგებთან",
        "მაია ჭიოკაძე - მედიცინის დოქტორი, ქართულ-ამერიკული უნივერსიტეტი, ასისტენტ პროფესორი, რეპროდუქციული მედიცინის ცენტრი \\\"უნივერსი\\\"",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "15:20-15:30",
        "მენოპაუზის გენიტოურინარული სინდრომი",
        "შორენა გოგოხია - ინვიტრო ლაიფი, ქართულ-ამერიკული კლინიკა მედიქალ ჰაუსი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "15:30-15:40",
        "პათოლოგიური სისხლდენები საშვილოსნოდან მოზარდ გოგონებში",
        "მაკა ჯორბენაძე - მედიცინის დოქტორი, ასოცირებული პროფესორი ი. ჯავახიშვილის სახელობის თბილისის სახელმწიფო უნივერსიტეტი, ჟორდანიას სამედიცინო ცენტრი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "15:40-15:55",
        "მამაკაცის ფაქტორი უნაყოფობაში და ორსულობის განმეორებით დანაკარგებში",
        "თეიმურაზ გაგნიძე - მედიცინის დოქტორი, რეპროდუქციული მედიცინის ცენტრი \\\"უნივერსი\\\" - გენერალური დირექტორი",
        time_style, program_title_style, speaker_style
    )

    # Break - with full width background
    elements.append(Spacer(1, 0.1*inch))
    break_para = Paragraph("16:00-16:20 შესვენება - ყავა/ჩაი", break_style)
    elements.append(break_para)
    elements.append(Spacer(1, 0.1*inch))

    # Session IV
    elements.append(Paragraph("IV სესია", session_header_style))
    elements.append(Paragraph("მოდერატორები: პროფ. თეიმურაზ გაგნიძე, პროფ. ლევან კობალაძე, პროფ. ჯენარო ქრისტესაშვილი", moderator_style))

    add_program_item(elements,
        "16:20-16:30",
        "რეპროდუქციული პროგნოზის გაუმჯობესების პერსპექტივები აზოოსპერმიის მქონე უნაყოფო მამაკაცებში - კლინიკური შემთხვევის გარჩევა",
        "სოფიო კვალიაშვილი - მედიცინის დოქტორი, ჟორდანიას სამედიცინო ცენტრი, პინეოს სამედიცინო ეკოსისტემა, სამედიცინო ცენტრო ციტო",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "16:30-16:40",
        "უცნობი ეტიოლოგიის უნაყოფობა: თანამედროვე წარმოდგენები შესაძლო მიზეზების შესახებ",
        "ნანა ჯანელიძე-ყურაშვილი - თსუ-ს დოქტორანტი, ადამიანის რეპროდუქციისა და ემბრიოლოგიის საქართველოს ასოციაციის თანადამფუძნებელი, ჟორდანიას სამედიცინო ცენტრის რეპრიდუქციული დეპარტამენტიის მიმართულების ხელმძღვანელი",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "16:40-16:50",
        "კომბინირებული ქირურგიული და ჰორმონული მკურნალობის ეფექტურობა უნაყოფო პაციენტებში ღრმა ენდომეტრიოზით",
        "დავით სხირტლაძე - მედიცინის დოქტორი, ასოცირებული პროფესორი, უნივ. \\\"უნილეველი\\\", კლინიკა კარაპს მედლაინი, სს \\\"ვიან\\\"",
        time_style, program_title_style, speaker_style
    )

    add_program_item(elements,
        "16:50-17:05",
        "ქალი თუ მამაკაცი? სქესის იდენტიფიკაცია",
        "ლევან კობალაძე - მედიცინის დოქტორი, სახ. მართვის მაგისტრი, რეპროდუქციული მედიცინის ცენტრი \\\"უნივერსი\\\"",
        time_style, program_title_style, speaker_style
    )

    # Closing
    add_program_item(elements,
        "17:05–17:30",
        "დისკუსია, კონფერენციის შეჯამება, დახურვა",
        "",
        time_style, program_title_style, speaker_style
    )

    # Build PDF
    doc.build(elements)
    print(f"PDF generated successfully: {output_filename}")


def add_program_item(elements, time, title, speaker, time_style, title_style, speaker_style):
    """Add a program item with time badge, title and speaker to elements list - prettier version"""
    # Time badge as a table cell with background color and rounded corners - LEFT ALIGNED
    time_data = [[Paragraph(time, time_style)]]
    time_table = Table(time_data, colWidths=[1.5*inch])
    time_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#20b4b9')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Georgian'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))

    elements.append(time_table)
    elements.append(Spacer(1, 0.08*inch))

    # Title
    elements.append(Paragraph(title, title_style))

    # Speaker (if provided)
    if speaker:
        elements.append(Spacer(1, 0.05*inch))
        elements.append(Paragraph(speaker, speaker_style))

    elements.append(Spacer(1, 0.15*inch))


if __name__ == "__main__":
    create_program_pdf()
