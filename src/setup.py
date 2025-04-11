import argparse
import urllib.request
import subprocess


parser = argparse.ArgumentParser(description="Download and read data")
parser.add_argument('-c', '--catalog', required=True)
parser.add_argument('-s', '--schema', required=True)
parser.add_argument('-v', '--volume', required=True)
args = parser.parse_args()

catalog = args.catalog
schema = args.schema
volume = args.volume
directory = "lab4"
data_path = "data"

work_folder = f"dbfs:/Volumes/{catalog}/{schema}/{volume}/{directory}/{data_path}"

file_url = "https://raw.githubusercontent.com/MicrosoftLearning/mslearn-databricks/main/data/sample_sales.csv"
file_name = "sample_sales.csv"
urllib.request.urlretrieve(file_url, file_name)

subprocess.run(["databricks", "fs", "rm", "-r", work_folder], check=False)
subprocess.run(["databricks", "fs", "mkdir", work_folder], check=True)
subprocess.run(["databricks", "fs", "cp", file_name, work_folder], check=True)
