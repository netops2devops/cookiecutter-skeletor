import os 

if "{{cookiecutter.vcs}}" == "Gitlab":
    os.system('touch .gitlab-ci.yml')
    os.system('git init .')


elif "{{cookiecutter.vcs}}" == "Github":
    os.system('mkdir .github/workflows')
    os.system('git init .')
    
else:
    pass

os.system('mkdir .envs')
os.system('touch .envs/dev.env')
os.system('touch .envs/prod.env')
os.system('chmod 700 .envs')
os.system('chmod 600 .envs/*.env')

if "{{cookiecutter.cli_builder}}" == "y":
    os.system('touch src/{{cookiecutter.project_slug}}/cli.py')