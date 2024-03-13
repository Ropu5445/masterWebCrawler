import glob, os

os.chdir("./")

for file in glob.glob("*.py"):
    if file in ['flight.py', 'scrape.py']:
        pass
    else:
        print(f"Running script {file}")
        os.system(f"python {file}");