"""
CV Analyzer
Author: Ibrahim Nuri
Date: 2024

This script extracts and analyzes key information from CVs, such as experience, education, and skills.
It supports PDF files and provides feedback on missing or important elements.
"""

import pdfplumber
import re
import pandas as pd
import spacy
import streamlit as st

nlp = spacy.load('en_core_web_sm')

# CV-dən mətn çıxarma funksiyası
def pdf_den_metin_cixar(pdf_dosyasi):
    metn = ""
    with pdfplumber.open(pdf_dosyasi) as pdf:
        for seyfe in pdf.pages:
            metn += seyfe.extract_text() if seyfe.extract_text() else ""
    return metn

# Dil aşkarlama funksiyası
def dil_tespit(metn):
    if re.search(r'(təcrübə|təhsil|bacarıqlar|layihələr)', metn, re.I):
        return 'Azerbaycan dili'
    else:
        return 'İngilis dili'

# CV-dən məlumatları çıxarma funksiyası
def cv_melumatlari_cixar(metn):
    doc = nlp(metn)
    ad = ""
    email = ""
    telefon = ""
    bacarıqlar = []

    # E-mail və telefon nömrəsi çıxarma
    email = re.findall(r'\S+@\S+', metn)
    telefon = re.findall(r'(\+?\d{1,3})?\s?\(?\d{3}\)?\s?\d{3}\s?\d{2}\s?\d{2}', metn)

    # CV-dəki ad və bacarıqları aşkarlama
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not ad:
            ad = ent.text
        if ent.label_ == "SKILL":
            bacarıqlar.append(ent.text)

    return {
        'Ad': ad,
        'E-mail': email[0] if email else 'Tapılmadı',
        'Telefon': telefon[0] if telefon else 'Tapılmadı',
        'Bacarıqlar': bacarıqlar if bacarıqlar else 'Tapılmadı'
    }

# Streamlit interfeysi
st.title("CV Analiz Aləti")
st.write("Bu tətbiq, PDF formatındakı CV-lərdən məlumat çıxarmaq və analiz etmək üçün hazırlanıb.")

uploaded_file = st.file_uploader("PDF faylı yükləyin", type="pdf")

if uploaded_file:
    metn = pdf_den_metin_cixar(uploaded_file)
    dil = dil_tespit(metn)
    st.write(f"Aşkarlanan dil: {dil}")
    melumatlar = cv_melumatlari_cixar(metn)
    st.write("Çıxarılan Məlumatlar:", melumatlar)
else:
    st.write("Zəhmət olmasa faylı yükləyin.")
