import json
from rich import print
from rich.markdown import Markdown

if __name__ == "__main__":
    with open("en.json", "r") as json_file:
        markdown_data = json.load(json_file)
        
        for key, value in markdown_data["app"].items():
            print(Markdown(value))
            print("\n")
