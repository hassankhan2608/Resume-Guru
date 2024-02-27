# Resume Guru

Resume Guru is an application designed to assist job seekers in optimizing their resumes using GEMINI AI [LLM]. It provides various features such as tailored evaluation, keyword analysis, ATS integration, and cover letter generation to streamline the job application process.

![image](https://github.com/hassankhan2608/Resume-Guru/assets/149296407/769f1dbe-4b5e-40bd-9abe-c56a95b4819d)



## How it Works

The application utilizes GEMINI AI [LLM] to analyze resumes against specific job descriptions, providing users with valuable feedback and recommendations. Here's how to use the application:

1. **Input Job Description**: Enter the job description for the position you're applying for.
2. **Upload Resume**: Upload your resume in PDF format.
3. **Select Action**: Choose from different actions such as analyzing the resume, improving skills, identifying missing keywords, calculating the percentage match, generating a cover letter, or evaluating strengths and weaknesses.
4. **View Results**: Receive detailed feedback and insights based on the selected action.

## Requirements

To run this project, ensure you have the following:

- Python 3.x installed on your system.
- Required Python libraries: Streamlit, Pillow, pdf2image, base64.
- A Google API key for accessing GEMINI AI [LLM]. Follow the steps below to obtain the API key:
  - Visit [Google AI Studio](https://aistudio.google.com/app/apikey).
  - Click on "Create API Key".
  - Copy the generated API key and paste it into a `.env` file in the project directory.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python libraries using the following command:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project directory and add your Google API key:
   ```
   GOOGLE_API_KEY=<your_api_key>
   ```
5. Run the Streamlit app using the following command:
   ```
   streamlit run app.py
   ```
6. Access the application in your web browser at the provided URL.

## Contribution

Contributions are welcome! If you have any ideas for improvement or encounter any issues, feel free to open an issue or submit a pull request.
.
```
