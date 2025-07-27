import subprocess as sub
import os

repo_path = r"D:\Py"
commands = [
    'git init',
    'git add a.py saveinGit.py support.py test.py',
    'git commit -m "Add support file for Manim"',
    'git branch -M main',
    'git remote add origin https://github.com/LuuLacDinh/support-manim-python.git',
    'git push -u origin main'
]

for cmd in commands:
    sub.run(cmd, cwd=repo_path, shell=True)
    
repo_path2 = r"D:\Py\support"
commands = [
    'git init',
    'git add axes.py effect.py transform.py',
    'git commit -m "Add support file for Manim"',
    'git branch -M main',
    'git remote add origin https://github.com/LuuLacDinh/support-manim-python.git',
    'git push -u origin main'
]
for cmd in commands:
    sub.run(cmd, cwd=repo_path2, shell=True)