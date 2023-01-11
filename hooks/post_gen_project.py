import os 

if "{{cookiecutter.vcs}}" == "Gitlab":
    os.system('touch .gitlab-ci.yml')
    os.system('git init .')


elif "{{cookiecutter.vcs}}" == "Github":
    os.system('mkdir .github/workflows')
    os.system('git init .')
    
else:
    pass

os.system('touch .envs/dev.env')
os.system('touch .envs/prod.env')

if "{{cookiecutter.cli_builder}}" == "y":
    os.system('touch src/{{cookiecutter.project_slug}}/cli.py')