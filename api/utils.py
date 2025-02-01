
from django.conf import settings
import re
import google.generativeai as genai
genai.configure(api_key=settings.OPENAI_API_KEY)
def code_converter(source_code,source_language,target_language):

    prompt = f"Convert the following {source_language} code to {target_language}:{source_code}Equivalent {target_language} code without any explanation or formatting symbols:"
    try:
        model = genai.GenerativeModel("gemini-pro")  
        response = model.generate_content(prompt)
        

        return response.text.strip()
    except Exception as e:
        return str(e)



def code_explainer(code,language):
    print("ADFADFADFADFASDFA",code)
    prompt = f"Explain this {language} code in simple words line by line :\n\n{code}\n\nExplanation:"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        return response.text.strip()
    except Exception as e:
        return str(e)