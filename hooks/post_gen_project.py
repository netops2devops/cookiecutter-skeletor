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

subprocess.run(["sh", "-c", "poetry install --with=dev"])
