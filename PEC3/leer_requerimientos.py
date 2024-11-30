import yaml
import subprocess
import sys

# Path to the YAML file
archivo_yaml = 'environment_uoc20241pec3.yml'

# Read the YAML file
with open(archivo_yaml, 'r') as file:
    requerimientos = yaml.safe_load(file)

# Install the packages listed in the YAML file
dependencies = requerimientos.get('dependencies', [])
for dep in dependencies:
    if isinstance(dep, str):
        dep_formatted = dep.replace("=", "==")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep_formatted])
            print(f"Successfully installed: {dep_formatted}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install: {dep_formatted}. Error: {e}")
    else:
        print(f"Unsupported dependency format: {dep_formatted}")

pip_req = requerimientos.get('pip',[])
for pip in pip_req:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip])
        print(f"Successfully installed: {pip}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install: {pip}. Error: {e}")
