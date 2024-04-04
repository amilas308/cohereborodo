from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import PDFDocument, SummarizedDocument, TranslatedDocument
import cohere
from googletrans import Translator
from pdfminer.high_level import extract_text
from pdf_app.models import PDFDocument  # Assuming you have a model named PDFDocument

def upload_view(request):
    # Your view logic here
    return render(request, 'pdf_app/upload.html')
def upload_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']

        text = extract_text(f'pdfs/{pdf_file}')
        
        import re
        def clean_text(text):
            # Remove unnecessary characters and whitespace
            cleaned_text = text.replace('\n', ' ').replace('\x0c', '')

            # You can add more cleaning steps here if needed

            return cleaned_text
        new_text = clean_text(text)
        co = cohere.Client('ybxcZF4lez8qXL0mp4zKDxnfPxTfW9lZxJBgbfbj')
        response = co.summarize(
        text=new_text,
        length='medium',
        format='paragraph',
        model='summarize-xlarge',
        additional_command='',
        temperature=0.3,
        )

        translator = Translator()
        result = translator.translate(response.summary,dest='en').text
        return render(request, 'pdf_app/summary.html',{'summary':result})
    else:
        return render(request, 'pdf_app/upload.html')


def summarize_text(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']

        text = extract_text(f'pdfs/{pdf_file}')
        
        import re
        def clean_text(text):
            # Remove unnecessary characters and whitespace
            cleaned_text = text.replace('\n', ' ').replace('\x0c', '')

            # You can add more cleaning steps here if needed

            return cleaned_text
        new_text = clean_text(text)
        co = cohere.Client('ybxcZF4lez8qXL0mp4zKDxnfPxTfW9lZxJBgbfbj')
        response = co.summarize(
        text=new_text,
        length='medium',
        format='paragraph',
        model='summarize-xlarge',
        additional_command='',
        temperature=0.3,
        )

        translator = Translator()
        result = translator.translate(response.summary,dest='en').text
        return render(request, 'pdf_app/summary.html',{'summary':result})
    else:
        return render(request, 'pdf_app/upload.html')


# def translate_summary(request, summary_id):
#     summary_doc = SummarizedDocument.objects.get(pk=summary_id)
#     summary_text = summary_doc.summary_text
#     translator = Translator()
#     translated_text = translator.translate(summary_text, dest='your_language').text  # Replace 'your_language' with the language code you want
#     TranslatedDocument.objects.create(pdf_document=summary_doc.pdf_document, translated_text=translated_text)
#     return render(request, 'pdf_processor/translation.html', {'translated_text': translated_text})
