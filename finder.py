from bs4 import BeautifulSoup
import requests

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
#url = f"https://ru.pdfdrive.com/search?q={obj}&pagecount=&pubyear=&searchin=ru&em=&more=true"
#URL1 = "https://ru.pdfdrive.com/search?q="
#URL2 = "&pagecount=&pubyear=&searchin=ru&em=&more=true"


def find_books(string: str):
    obj = string.replace(" ", "+")
    url = f"https://ru.pdfdrive.com/search?q={obj}&pagecount=&pubyear=&searchin=&em=&more=true"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return("Error")
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(response.status_code)
    names = []
    pages = []
    languages = []
    links_to_show = []
    download_links = []

    all_books = soup.find_all("div", class_="row")
    a=1
    for i in all_books:  #Cделать ограничение на 10
        #print()
        try:
            names.append(f"{a}. {i.find('h2').text}")
        except AttributeError:
            names.append("NoName")
            continue
        try:
            pages.append(i.find(class_="fi-pagecount").text)
        except AttributeError:
            pages.append("NoPage")
            continue
        try:
            languages.append(i.find(class_="fi-lang").text)
        except AttributeError:
            continue

        link = i.find(class_="ai-search")["href"]
        links_to_show.append(f'https://ru.pdfdrive.com{link}')
        count = 0
        link_list = link.split("-")
        #print(link_list)
        for i in range(-1,1):
            link_list[i] = link_list[i].replace("e","d")
            count += 1
            if count >0:
                break
        
        done_link = 'https://ru.pdfdrive.com'+"-".join(link_list)
        
        download_links.append(done_link) #almost downloadable link
        #print
        a += 1
    result = list(zip(names, pages, languages))
    return result, download_links



if __name__ == "__main__":
    find_books(str(input("Type your book: ")))
    #grab_pdf("https://ru.pdfdrive.com/Освой-самостоятельно-c-по-одному-часу-в-день-d183944321.html")