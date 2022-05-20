from bs4 import BeautifulSoup
import requests
import os

OUT_FOLDER = './out/'


def get_head_and_trail(url):
    """ Divide a TripAdvisor url in header and trailer.

    :param url: The object TripAdvisor url string.
    :return:    The header and trailer of the url.
    """
    x = url.split('-Reviews-')
    x[0] = x[0] + '-Reviews-'
    return x[0], x[1]


def print_reviews(url, n_reviews, filter_tuple):
    """ Save all reviews of a given TripAdvisor location into a txt file.

    :param url:             The url of the TripAdvisor location to analyze.
    :param n_reviews:       The total number of reviews in the TripAdvisor location. TODO extract from the HTML
    :param filter_tuple:    The tuple of words to filter (if any).
    :return:                Nothing.
    """
    print("Scraping link: " + url)

    # Create output folder (if it doesn't exist already)
    try:
        os.mkdir(OUT_FOLDER)
    except:
        pass
    url_head, url_trail = get_head_and_trail(url)

    # The filename of the output txt file (removing '.html')
    txt_file_name = url_trail[:-5] + '.txt'

    with open(OUT_FOLDER + txt_file_name, 'a') as f:
        f.write(url + '\n')
        # For each comment page
        for i in range(0, n_reviews, 10):
            if i != 0:
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
                if any(s in content for s in filter_tuple):
                    data.append({
                        'rating':e.select_one('svg[aria-label]')['aria-label'],
                        #'profilUrl':e.select_one('a[tabindex="0"]').get('href'),
                        'content':content # [:-9] # Remove 'Read more'
                    })

            # Write rating and content of the review in the txt file
            for line in data:
                f.write('Rating: ' + line['rating'] + '\n' + 'Comment: ' + line['content'] + '\n\n')


filter_text = ("darkness", "dark", "shadow", "space", "experience", "light")


print_reviews(url='https://www.tripadvisor.com/Attraction_Review-g319796-d5988326-Reviews-Museo_de_Altamira-Santillana_del_Mar_Cantabria.html',
              n_reviews=320,
              filter_tuple=filter_text)
print_reviews(url='https://www.tripadvisor.com/Attraction_Review-g2044790-d246632-Reviews-Lascaux_II-Montignac_Dordogne_Nouvelle_Aquitaine.html',
              n_reviews=520,
              filter_tuple=filter_text)
print_reviews(url='https://www.tripadvisor.com/Attraction_Review-g2044790-d11907064-Reviews-Lascaux_IV-Montignac_Dordogne_Nouvelle_Aquitaine.html',
              n_reviews=340,
              filter_tuple=filter_text)
print_reviews(url='https://www.tripadvisor.com/Attraction_Review-g1379167-d283739-Reviews-Museu_da_Fundacao_do_Coa-Vila_Nova_de_Foz_Coa_Guarda_District_Central_Portug.html',
              n_reviews=90,
              filter_tuple=filter_text)
