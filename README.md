# lassie
- Using lassie to scrape data from webpages

# logging my use of the library

### initial work

```bash
pip3 install lassie; python3
```
### in the python shell

```python
import lassie
help(lassie)
# look at the source files
# lassie.fetch(URL)
```

### program that scrapes information from a webpage based off user input (retrieve.py)
```python
import lassie
import json

val = input("Enter a url: ")
info = lassie.fetch(val)

json_object = json.dumps(info, indent = 4)
print(json_object)

with open('result.json', 'w') as fp:
    json.dump(json_object, fp)

```
## TO DO
- figure out what to do with raw data
- read about [market research](https://www.scrapingdog.com/blog/web-scraping-for-market-research/#The_Different_Types_of_Data_That_Can_Be_Collected_Through_Web_Scraping)
- go deeper into selenium

[Lassie documentation](https://lassie.readthedocs.io/en/latest/?ref=morioh.com&utm_source=morioh.com)
