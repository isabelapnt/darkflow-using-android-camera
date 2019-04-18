    
import os
import urllib.request as ulib
# import urllib
from bs4 import BeautifulSoup as Soup
import json

url_a = 'https://www.google.com/search?rlz=1C1GCEU_pt-BRBR821BR821&biw=1920&bih=947&tbm=isch&sa=1&ei=py23XOD5Cu-q5OUPldWdqAU&q={}&oq={}'
url_b = 'gs_l=img.3..0i19.999.999..1673...0.0..0.111.111.0j1......0....2j1..gws-wiz-img.tARoxBtWRf4'
# url_c = '&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg'
# url_d = '.i&ijn=1&asearch=ichunk&async=_id:rg_s,_pms:s'
url_base = ''.join((url_a, url_b))

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'}


def make_soup(url):
    req = ulib.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    html = ulib.urlopen(req)
    return Soup(html, 'html.parser')

def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name, search_name)
    
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    links = [each.get('src') for each in images]

    # request = ulib.Request(url, None, headers)
    # json_string = ulib.urlopen(request).read().decode('utf-8')
    # page = json.loads(json_string)
    # new_soup = Soup(page[1][1], 'lxml')
    # images = new_soup.find_all('img')
    # links = [image['src'] for image in images]
    del(links[0])
    return links


def save_images(links, search_name):
    directory = search_name.replace(' ', '_')
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
        savepath = os.path.join(directory, '{:06}.png'.format(i))
        ulib.urlretrieve(link, savepath)


if __name__ == '__main__':
    search_name = 'fidget toy spinners'
    links = get_links(search_name)
    save_images(links, search_name)