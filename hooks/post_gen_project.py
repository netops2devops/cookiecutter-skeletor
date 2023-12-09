import shutil
import subprocess

# *.env is in .gitignore
subprocess.run(["chmod", "644", ".env"])

subprocess.run(["git", "init", "."])

if "{{cookiecutter.vcs}}" == "Gitlab":
    subprocess.run(["touch", ".gitlab-ci.yml"])

elif "{{cookiecutter.vcs}}" == "Github":
    subprocess.run(["mkdir", ".github"])
    subprocess.run(["mkdir", ".github/workflows"])
    
else:
    pass

if "{{cookiecutter.project_layout}}" == "flat":
    shutil.rmtree("src")
    shutil.rmtree("docs")
    shutil.rmtree("tests")
    subprocess.run(["rm", "Makefile"])
    subprocess.run(["rm", "docker-compose.yml"])
    subprocess.run(["rm", "Dockerfile"])
    subprocess.run(["touch", "main.py"])

if "{{cookiecutter.config_file}}":
    subprocess.run(["touch", "config.yaml"])

subprocess.run(["sh", "-c", "poetry install --with=dev"])
