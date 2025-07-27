import subprocess as sub
import os

repo_path = r"D:\Py"
commands = [
    'git init',
    'git add .',  # thêm tất cả bao gồm thư mục support/
    'git commit -m "Add all Manim support files"',
    'git branch -M main',
    'git remote add origin https://github.com/LuuLacDinh/support-manim-python.git',
    'git push -u origin main'
]

for cmd in commands:
    sub.run(cmd, cwd=repo_path, shell=True)