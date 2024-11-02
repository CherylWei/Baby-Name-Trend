"""
File: webcrawler.py
Name: Cheryl Lin
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        lines = []
        for tag in tags:
            text = tag.tbody.text
            lines = text.split()
        boy_total = 0
        girl_total = 0
        # print(lines)
        for index, number in enumerate(lines):
            try:
                if index % 5 == 2:
                    number = number.replace(",", "")
                    boy_total += int(number)
                elif index % 5 == 4:
                    number = number.replace(",", "")
                    girl_total += int(number)
            except:
                pass
        print("Male Number: ", boy_total)
        print("Female Number: ", girl_total)


if __name__ == '__main__':
    main()
