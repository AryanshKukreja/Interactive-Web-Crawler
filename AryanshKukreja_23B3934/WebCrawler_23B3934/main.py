mport requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Error extracting links from {url}: {e}")
        return []

def recursive_crawler(url, depth, link_count_dict):
    if depth == 0:
        return

    print(f"Processing {url} at depth {depth}")

    links = extract_links(url)
    link_count_dict[depth] = link_count_dict.get(depth, 0) + len(links)

    for link in links:
        # You can add your customizations here based on your creativity
        # For example, you might want to filter certain types of links or perform additional processing

        # Recursively crawl the next level of links
        recursive_crawler(link, depth - 1, link_count_dict)

def plot_links_depth(link_count_dict):
    depths = list(link_count_dict.keys())
    link_counts = list(link_count_dict.values())

    plt.bar(depths, link_counts, color='blue')
    plt.xlabel('Recursive Depth')
    plt.ylabel('Number of Links')
    plt.title('Number of Links at Each Recursive Depth')
    plt.show()

# Example usage
starting_url = "https://example.com"
depth_limit = 3
link_count_dict = {}
recursive_crawler(starting_url, depth_limit, link_count_dict)

# Plot the results
plot_links_depth(link_count_dict)
