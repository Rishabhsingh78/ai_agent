
from django.conf import settings
import google.generativeai as genai
genai.configure(api_key=settings.OPENAI_API_KEY)
import os
import git
import glob




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
    


def analyze_github_repo(repo_url):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = f"/tmp/{repo_name}"


    try:
        # Clone the GitHub repo
        if os.path.exists(repo_path):
            os.system(f"rm -rf {repo_path}")  # Remove existing directory if already cloned

        git.Repo.clone_from(repo_url, repo_path)

        # Extract file structure
        file_list = []
        for root, dirs, files in os.walk(repo_path):
            for file in files:
                file_list.append(os.path.relpath(os.path.join(root, file), repo_path))

        # Extract backend & frontend detection logic
        backend_files = glob.glob(f"{repo_path}/**/*.py", recursive=True)  # Python (Django/Flask)
        backend_files += glob.glob(f"{repo_path}/**/*.js", recursive=True)  # Node.js (Express)
        frontend_files = glob.glob(f"{repo_path}/**/*.html", recursive=True)
        frontend_files += glob.glob(f"{repo_path}/**/*.tsx", recursive=True)  # React TypeScript
        frontend_files += glob.glob(f"{repo_path}/**/*.vue", recursive=True)  # Vue.js

        # Extract key files
        api_routes = glob.glob(f"{repo_path}/**/routes/*.js", recursive=True)  # Express
        django_urls = glob.glob(f"{repo_path}/**/urls.py", recursive=True)  # Django
        middleware_files = glob.glob(f"{repo_path}/**/middleware/*.js", recursive=True)

        # Construct prompt for AI
        prompt = f"""
        I have a GitHub project with the following structure:
        {file_list}

        Key Findings:
        - Backend: {backend_files[:5]}
        - Frontend: {frontend_files[:5]}
        - API Routes: {api_routes}
        - Django URLs: {django_urls}
        - Middleware: {middleware_files}

        Explain in simple words:
        1. What does this project do?
        2. How does it work?
        3. What technologies are used?
        """

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Error: {str(e)}"