# lassie
- using lassie to scrape data from webpages

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

val = input("Enter a url: ")
info = lassie.fetch(val)

print(info)

```
## TO DO
- export data fetched to a seperate file

read more [Here](https://lassie.readthedocs.io/en/latest/?ref=morioh.com&utm_source=morioh.com)
