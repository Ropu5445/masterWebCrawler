import glob, os

os.chdir("./")

for file in glob.glob("*.py"):
    os.system(f"python {file}");