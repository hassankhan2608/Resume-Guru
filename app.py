from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import io
import pdf2image
import base64

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        # Take the first page for simplicity, or loop through images for all pages
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="Resume Expert", layout="wide")

st.header("Resume Guru")
st.subheader('This Application helps you in your Resume Review with help of GEMINI AI [LLM]')
input_text = st.text_input("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your Resume(PDF)...", type=["pdf"])
pdf_content = ""

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

button_col1, button_col2, button_col3 = st.columns(3)

with button_col1:
    submit1 = st.button("Tell Me About the Resume", key="submit1")

with button_col2:
    submit2 = st.button("How Can I Improvise my Skills", key="submit2")

with button_col3:
    submit3 = st.button("What are the Keywords That are Missing", key="submit3")

button_col4, button_col5, button_col6 = st.columns(3)

with button_col4:
    submit4 = st.button("Percentage match", key="submit4")

with button_col5:
    submit5 = st.button("Cover Letter", key="submit5")

with button_col6:
    submit6 = st.button("Strength & Weakness", key="submit6")

# Rest of your code remains unchanged

input_prompt1 = """
As an adept Technical Human Resource Manager with a focus on recruiting for Data Analyst or Data Scientist positions,
your mission is to meticulously assess the provided resume in direct correlation to the specific job description for the role in question. 
Delve into a comprehensive analysis, elucidating how the candidate's qualifications, skills, and experience align with the outlined job requirements. Explicitly highlight the strengths exhibited in the resume that resonate well with the demands of a Data Analyst or Data Scientist role, emphasizing key technical proficiencies, analytical skills, and relevant industry expertise. Concurrently, articulate any discernible weaknesses or areas where the candidate might fall short in meeting the specified job criteria, offering valuable insights into potential skill gaps or experiences that may require further exploration. Aim for conciseness while providing a nuanced evaluation that aids in making informed decisions about the candidate's suitability for the role.
"""

input_prompt2 = """
You are an Technical Human Resource Manager with expertise in data science, 
your role is to scrutinize the resume in light of the job description provided. 
Share your insights on the candidate's suitability for the role from an HR perspective. 
Additionally, offer advice on enhancing the candidate's skills and identify areas where improvement is needed.
"""

input_prompt3 = """
In your role as a proficient ATS (Applicant Tracking System) scanner well-versed in data science and ATS functionality, your primary objective is to evaluate the resume in direct alignment with the provided job description for a Data Science or Data Analyst position. Assess the compatibility of the resume by identifying missing keywords crucial for this role, such as specific programming languages, statistical methods, or analytical tools mentioned in the job description. Offer recommendations for enhancing the candidate's skills, pinpointing areas where additional emphasis or development is needed. This concise and precise evaluation ensures accurate results with each scan, providing actionable insights for optimizing the candidate's profile to better match the requirements of the Data Science or Data Analyst position.
"""
input_prompt4 = """
As a seasoned ATS (Applicant Tracking System) scanner equipped with an in-depth understanding of data science and ATS functionality, your mission is to meticulously evaluate a resume against the provided job description of Data Scientist or Data Analyst . The output should prominently display the ATS Score in a big, bold number, indicating the percentage match between the resume and the job description. Following the percentage, provide a list of missing keywords from the job description that are not present in the resume, presented in concise bullet points. Conclude your evaluation with final thoughts on how well the resume aligns with the job requirements and any notable areas for improvement. Ensure clarity and precision in your assessment, highlighting both strengths and potential gaps in the application.
"""

input_prompt5 = """
Compose a compelling cover letter tailored for the given job description by integrating key details from the provided resume. Prioritize emphasizing your relevant skills and experience while expressing genuine enthusiasm for the role. Ensure the letter strikes a balance between formality and interest, demonstrating your ability to quickly adapt and make a positive contribution to the team, addressing any experience gaps mentioned in the job description. Keep the letter concise, up to the point, and compelling. Additionally, provide a few tips for crafting an effective cover letter, such as showcasing specific achievements, aligning your skills with the company's needs, and expressing your passion for the industry.

Cover Letter Tips:
Introduce yourself to the hiring managers.
Provide details about your qualifications.
Tell employers why you want to work for them.
Illustrate why you're the best match for the job.
Highlight Achievements: Focus on specific accomplishments that showcase your skills.
Align with Company Needs: Clearly connect your skills with the requirements outlined in the job description.
Express Passion: Demonstrate genuine enthusiasm for the industry and the role.
Conciseness is Key: Keep the cover letter succinct, addressing key points without unnecessary details.
"""

input_prompt6 = """
Conduct a thorough analysis of my resume in relation to the provided job description. Read the resume meticulously, and provide a percentage match along with specific details on strengths and weaknesses. Use bold headers for 'Strengths' and 'Weaknesses' to clearly address each category. Emphasize qualifications, educational background, hands-on experience, technical skills, and certifications. Identify any potential gaps and assess alignment with job requirements, including industry knowledge, tools, and soft skills. Conclude with precise recommendations to enhance the resume's suitability for the given role.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt5, pdf_content, input_text)
        st.subheader("Cover letter")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit6:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt6, pdf_content, input_text)
        st.subheader("Test")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

st.markdown("---")
st.caption("Resume Guru - Making Job Applications Easier")