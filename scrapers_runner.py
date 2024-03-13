import glob, os

os.chdir("./")

ignoredScripts = ['scrapers_runner.py', 'flight.py', 'scrape.py']
ranScripts = []

for file in glob.glob("*.py"):
    if file not in ignoredScripts and file not in ranScripts:
        print(f"\nRunning script {file}")
        ranScripts.append(file)
        os.system(f"python {file}");