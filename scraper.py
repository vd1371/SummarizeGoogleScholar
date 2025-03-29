import requests
from bs4 import BeautifulSoup
from typing import List
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

def get_scholar_papers(scholar_url: str, sort_by: str = 'citations', num_papers: int = 10) -> List[str]:
    """
    Scrape paper links from a Google Scholar profile using BeautifulSoup
    
    Args:
        scholar_url (str): URL of the Google Scholar profile
        sort_by (str): Sort criteria - 'citations' or 'year'
        num_papers (int): Number of paper links to return
    
    Returns:
        List[str]: List of paper URLs
    """
    time.sleep(random.uniform(1, 2))

    # Add sorting parameter to URL
    scholar_url += '&view_op=list_works'
    if sort_by.lower() == 'year':
        scholar_url += '&sortby=pubdate'

    elif sort_by.lower() == 'citations':
        scholar_url += '&sort=citations'
    else:
        raise ValueError("sort_by must be either 'citations' or 'year'")
    
    paper_links = []
    
    try:
        # Make request with headers
        response = requests.get(scholar_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all paper links
        articles = soup.find_all('a', class_='gsc_a_at')
        
        # Extract links from articles
        for article in articles[:num_papers]:
            if article.get('href'):
                paper_links.append('https://scholar.google.com' + article.get('href'))
            
            # Add random delay between requests
            time.sleep(random.uniform(1, 2))
            
        return paper_links[:num_papers]
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []



def get_paper_details(paper_url: str) -> dict:
    """
    Scrape paper details from a Google Scholar paper URL
    
    Args:
        paper_url (str): URL of the Google Scholar paper
    
    Returns:
        dict: Dictionary containing paper details (title, description, year, journal)
    """
    paper_details = {
        'title': '',
        'description': '',
    }


    # title xpath: //*[@id="gsc_oci_title"]/a/text()
    # Description xpath: //*[@id="gsc_oci_descr"]/div/div/div
    
    try:
        # Add random delay before request
        time.sleep(random.uniform(1, 2))
        
        response = requests.get(paper_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse with lxml for xpath support
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Extract title
        title_elem = soup.find('div', id='gsc_oci_title')
        if title_elem:
            paper_details['title'] = title_elem.text.strip()
        
        # Extract description using xpath
        desc_elem = soup.find('div', id='gsc_oci_descr')
        if desc_elem:
            paper_details['description'] = desc_elem.text.strip()
        
        return paper_details
        
    except Exception as e:
        print(f"Error fetching paper details: {e}")
        return paper_details
