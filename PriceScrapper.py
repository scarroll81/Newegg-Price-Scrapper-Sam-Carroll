# Sam Carroll
# 11/28/21

# Newegg Price Scrapper

# imports
import requests
from bs4 import BeautifulSoup
import string
import time

# my user agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}


# function to get the listed price from the HTML of newegg.com
def getListPrice():
    convertedPrice = ''
    # find the identifier for price
    price = soup.find_all(class_="price-current")
    # find the list of HTML and find the price (newegg stores it in the first index)
    tempPrice = price[0:5]
    convertedPrice = tempPrice[0]
    #print(convertedPrice)
    #return the string of the price
    return str(convertedPrice)

# function to trim the price to be readable
def trimPrice(convertedPrice):
    # remove quote marks so larger replace functions may happen
    trimQuotes = convertedPrice.replace('"', '', 10)
    # trim the excess HTML
    trimPre = trimQuotes.replace('<li class=price-current><span class=price-current-label></span>$<strong>', '', 1)
    trimMid = trimPre.replace('</strong><sup>', '', 1)
    trimSuf = trimMid.replace('</sup></li>', '', 5)
    trimPrice = trimSuf
    print('price = $' + trimPrice + "\n")
    # return the trimmed price
    return trimPrice

# function to get the product title
def getTitle():
    fullTitle = soup.find_all(class_="product-title")
    #print(fullTitle)
    return str(fullTitle)

# function to trim the product title to be readable
def trimTitle(fullTitle):
    # trim the quote marks
    noQuotesTitle = fullTitle.replace('"', '', 10)
    # trim the excess HTML
    trimPre = noQuotesTitle.replace('[<h1 class=product-title>', '', 1)
    trimSuf = trimPre.replace('</h1>]', '', 1)
    print(trimSuf)
    # return the trimmed title
    return trimSuf


# list of URLs from newegg to pull prices from
URLs = ['https://www.newegg.com/amd-ryzen-9-5950x/p/N82E16819113663?Description=amd%20processor&cm_re=amd_processor-_-19-113-663-_-Product',
        'https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664?Description=amd%20processor&cm_re=amd_processor-_-19-113-664-_-Product&quicklink=true',
        'https://www.newegg.com/amd-ryzen-7-5800x/p/N82E16819113665?Description=amd%20processor&cm_re=amd_processor-_-19-113-665-_-Product',
        'https://www.newegg.com/amd-ryzen-7-5700g-ryzen-7-5000-g-series/p/N82E16819113682?Description=amd%20processor&cm_re=amd_processor-_-19-113-682-_-Product',
        'https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?Description=amd%20processor&cm_re=amd_processor-_-19-113-666-_-Product',
        'https://www.newegg.com/intel-core-i9-11900k-core-i9-11th-gen/p/N82E16819118231?Description=intel%20processor&cm_re=intel_processor-_-19-118-231-_-Product&quicklink=true',
        'https://www.newegg.com/intel-core-i7-11700k-core-i7-11th-gen/p/N82E16819118233?Description=intel%20processor&cm_re=intel_processor-_-19-118-233-_-Product&quicklink=true',
        'https://www.newegg.com/intel-core-i5-11600k-core-i5-11th-gen/p/N82E16819118235?Description=intel%20processor&cm_re=intel_processor-_-19-118-235-_-Product&quicklink=true',
        'https://www.newegg.com/intel-core-i7-12700k-core-i7-12th-gen/p/N82E16819118343?Description=intel%20processor&cm_re=intel_processor-_-19-118-343-_-Product',
        'https://www.newegg.com/intel-core-i5-12600k-core-i5-12th-gen/p/N82E16819118347?Description=intel%20processor&cm_re=intel_processor-_-19-118-347-_-Product',]

# find the products and titles from the list
for URL in URLs:
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = getTitle()
    title = trimTitle(title)
    price = getListPrice()
    price = trimPrice(price)
    time.sleep(1)
    



