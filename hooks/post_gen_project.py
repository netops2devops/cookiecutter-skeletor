import os 

if "{{cookiecutter.vcs}}" == "Gitlab":
    os.system('touch .gitlab-ci.yml')
    os.system('git init .')


elif "{{cookiecutter.vcs}}" == "Github":
    os.system('mkdir .github/workflows')
    os.system('git init .')
    
else:
    pass
