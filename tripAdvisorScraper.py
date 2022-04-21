from bs4 import BeautifulSoup
import requests


def print_reviews(url_head, url_trail, txt_name, n_reviews, filter_text):
    with open(txt_name, 'a') as f:
        f.write(url_head + url_trail + '\n')
        # For each comment page
        for i in range(0, n_reviews, 10):
            if i == 0:
                url = url_head + url_trail
            else:
                url = url_head + '-or' + str(i) + url_trail

            # Open and read HTML
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers)
            data = r.text
            soup = BeautifulSoup(data, features="html.parser")
            data = []

            # Parse HTML and obtain required data
            for e in soup.select('#tab-data-qa-reviews-0 [data-automation="reviewCard"]'):
                content = e.select_one('div:has(>a[tabindex="0"]) + div + div').text
                if any(s in content for s in filter_text):
                    data.append({
                        'rating':e.select_one('svg[aria-label]')['aria-label'],
                        #'profilUrl':e.select_one('a[tabindex="0"]').get('href'),
                        'content':content
                    })

            # Write rating and content of the review in the txt file
            for line in data:
                f.write('Rating: ' + line['rating'] + '\n' + 'Comment: ' + line['content'] + '\n\n')


filter_text = ("darkness", "dark", "shadow", "space", "experience", "light")

print_reviews(url_head='https://www.tripadvisor.com/Attraction_Review-g319796-d5988326-Reviews',
              url_trail='-Museo_de_Altamira-Santillana_del_Mar_Cantabria.html',
              txt_name='url1_filtered.txt',
              n_reviews=320,
              filter_text=filter_text)
print_reviews(url_head='https://www.tripadvisor.com/Attraction_Review-g2044790-d246632-Reviews',
              url_trail='-Lascaux_II-Montignac_Dordogne_Nouvelle_Aquitaine.html',
              txt_name='url2_filtered.txt',
              n_reviews=520,
              filter_text=filter_text)
print_reviews(url_head='https://www.tripadvisor.com/Attraction_Review-g2044790-d11907064-Reviews',
              url_trail='-Lascaux_IV-Montignac_Dordogne_Nouvelle_Aquitaine.html',
              txt_name='url2b_filtered.txt',
              n_reviews=340,
              filter_text=filter_text)
print_reviews(url_head='https://www.tripadvisor.com/Attraction_Review-g1379167-d283739-Reviews',
              url_trail='-Museu_da_Fundacao_do_Coa-Vila_Nova_de_Foz_Coa_Guarda_District_Central_Portug.html',
              txt_name='url3_filtered.txt',
              n_reviews=90,
              filter_text=filter_text)
