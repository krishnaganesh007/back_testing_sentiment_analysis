# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the bank's press releases page
# url = "https://www.societegenerale.com/en/press-release"

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find the elements containing the press release data
# press_release_elements = soup.find_all(class_="title h4")



# # Iterate over the press release elements and extract relevant information
# for press_release in press_release_elements:
#     title = press_release.find("h2").text
#     date = press_release.find("span", class_="date").text
#     content = press_release.find("div", class_="content").text

#     # Print or process the extracted data as desired
#     print("Title:", title)
#     print("Date:", date)
#     print("Content:", content)
#     print("------------------------------")




import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the bank's press releases page
url = "https://www.societegenerale.com/en/news/press-release/societe-generale-signs-new-global-agreement-uni-global-union"
url = "https://www.societegenerale.com/en/press-release"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements containing the press release data

# press_release_elements_links = soup.find_all("div", class_="views-element-container")

# for press_release in press_release_elements:
#     press_release.find("h1", class_="title").text



press_release_elements = soup.find_all("a", class_="link")


global_url = "https://www.societegenerale.com"

news_df = pd.DataFrame()
i = 0
for link in press_release_elements:
    # if
    
    print(i)
    i = i+1
    #press_release_url = link['href']  # Extract the URL of the press release
    #print(press_release_url)
    #print(global_url + press_release_url)
    # press_release_response = requests.get(global_url + link['href'])
    print(global_url + link['href'])
    # print(press_release_response)

    press_release_soup = BeautifulSoup(requests.get(global_url + link['href']).content, 'html.parser') 

    # BeautifulSoup(requests.get(global_url+press_release_elements[2]['href']).content, 'html.parser')
    # print(press_release_soup)
    # press_release_response = requests.get(press_release_url)

    #print(press_release_url)
    # pr_articles = press_release_soup.find(class_="layout-container")

    # print(pr_articles)
    # print(pr_articles.find("h1", class_="title"))
    try:

        inter_df = pd.DataFrame()

        # print(press_release_soup.find("h1", class_="title").text)

        # inter_df["checking"] = 0
        inter_df["Title"] = pd.Series(press_release_soup.find("h1", class_="title").text)
        inter_df["Date"] = pd.Series(press_release_soup.find("span", class_="date").text)
        inter_df["Content"]= pd.Series(press_release_soup.find("p", class_="CPChapo").text)

        news_df = pd.concat([news_df, inter_df], axis = 0)
        print(inter_df)
    
    except:
        pass



    



# # Iterate over the press release elements and extract relevant information
# for press_release in press_release_elements:
#     title = press_release.find("h1", class_="title").text
#     date = press_release.find("span", class_="date").text
#     content = press_release.find("p", class_="CPChapo").text
#     # content = press_release.find("div", class_="content").text

#     # Print or process the extracted data as desired
#     print("Title:", title)
#     print("Date:", date)
#     print("Content:", content)
#     print("------------------------------")


# BeautifulSoup(requests.get(global_url+press_release_elements[2]['href']).content, 'html.parser').find("p", class_="CPChapo").text