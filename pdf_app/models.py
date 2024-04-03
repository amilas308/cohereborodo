from django.db import models

class PDFDocument(models.Model):
    # title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

class SummarizedDocument(models.Model):
    pdf_document = models.OneToOneField(PDFDocument, on_delete=models.CASCADE, related_name='summary')
    summary_text = models.TextField()

class TranslatedDocument(models.Model):
    pdf_document = models.OneToOneField(PDFDocument, on_delete=models.CASCADE, related_name='translation')
    translated_text = models.TextField()
