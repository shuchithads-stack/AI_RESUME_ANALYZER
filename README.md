# AI Resume Analyzer & Job Recommendation System

## 📌 Project Overview

The AI Resume Analyzer & Job Recommendation System is a web-based application that analyzes a candidate's resume and recommends suitable job roles based on the skills found in the resume.

The system extracts resume text, identifies technical skills, compares the candidate's skills with predefined job requirements, calculates matching scores, identifies missing skills, and provides a learning roadmap.

The application is developed using Python and Streamlit.

---

## 🎯 Objectives

The main objectives of this project are:

- Extract information from resumes automatically.
- Identify technical skills from the resume.
- Compare candidate skills with job requirements.
- Calculate job matching scores.
- Recommend suitable job roles.
- Identify missing skills for a selected job role.
- Generate a learning roadmap for missing skills.
- Provide a downloadable analysis report.

---

## 🚀 Features

### 1. Resume Upload

The system supports:

- PDF resumes
- DOCX resumes

### 2. Resume Text Extraction

The uploaded resume is processed and the text is extracted automatically.

### 3. Skill Extraction

The system identifies technical skills such as:

- Python
- SQL
- Pandas
- NumPy
- Machine Learning
- Scikit-learn
- Deep Learning
- And other predefined skills

### 4. Job Matching

The system compares the extracted resume skills with the required skills for different job roles.

### 5. Match Score

A percentage-based matching score is calculated for each job role.

### 6. Job Recommendations

The system displays job roles ranked according to their matching scores.

### 7. Skill Gap Analysis

The user can select a target job role and identify:

- Skills already available
- Missing skills

### 8. Learning Roadmap

A learning roadmap is generated based on the missing skills.

### 9. Downloadable Report

The complete analysis can be downloaded as a text report.

---

## 💼 Job Roles

The current dataset contains the following job roles:

- Data Analyst
- Machine Learning Engineer
- AI Engineer
- NLP Engineer
- Computer Vision Engineer

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries and Frameworks

- Streamlit
- Pandas
- Scikit-learn
- PyPDF
- Python-docx

### Development Environment

- Visual Studio Code
- Python Virtual Environment

---

## 📁 Project Structure

```text
AI_RESUME_ANALYZER/
│
├── app.py
├── analyzer.py
├── job_matcher.py
├── resume_parser.py
├── roadmap_generator.py
├── skill_extractor.py
├── requirements.txt
├── README.md
│
├── test_jobs.py
├── test_match.py
├── test_roadmap.py
├── test_skills.py
│
└── data/
    └── job_roles.csv