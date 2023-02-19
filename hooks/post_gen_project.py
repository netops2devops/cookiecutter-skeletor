import os 

if "{{cookiecutter.vcs}}" == "Gitlab":
    os.system('touch .gitlab-ci.yml')
    os.system('git init .')


elif "{{cookiecutter.vcs}}" == "Github":
    os.system('mkdir .github/workflows')
    os.system('git init .')
    
else:
    pass

os.system('chmod 644 .env')

if "{{cookiecutter.cli_builder}}" == "y":
    os.system('touch src/{{cookiecutter.project_slug}}/cli.py')
