import os
import re
from bs4 import BeautifulSoup as bs

tld_html = [x for x in os.listdir("./") if x.endswith(".html")]
include_identifier = re.compile("{{.+}}")

print("Formatting...")
for html_path in tld_html:
    with open(html_path, "r") as html_fobj:
        html = html_fobj.read()

    for include_fmt in include_identifier.findall(html):
        include_name = include_fmt.strip("{{").strip("}}") + ".html"
        try:
            with open(os.path.join("parts", include_name), "r") as include_fobj:
                include = include_fobj.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Page {html_path} seeks to include parts/{include_name}, which does not exist.")
        
        html = html.replace(include_fmt, "\n" + include + "\n")
    #soup = bs(html, features="lxml")

    with open(os.path.join("public", html_path), "w+") as html_fobj:
        html_fobj.write(html)
        print(f"> {html_path}")

print("\nFinished.")