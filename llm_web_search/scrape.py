import requests
import os
import re
from datetime import datetime
from get_links import get_links
from bs4 import BeautifulSoup


def initialize_logs(topic):
    """
    Create a folder named as the topic with timestamp
    Returns the path to the created folder
    """
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    topic_folder = os.path.join(logs_dir, f"{topic}_{timestamp}")
    os.makedirs(topic_folder, exist_ok=True)
    
    return topic_folder

def scrape_links(links, save_logs=True, log_folder=None):
    """
    Scrape data from the provided links
    
    Args:
        links: List of URLs to scrape
        save_logs: Boolean to decide if we want to save logs or not
        log_folder: Path to the folder where logs should be saved
    
    Returns:
        If save_logs is False, returns combined content as a string
        If save_logs is True, saves files and returns None
    """
    combined_content = ""
    
    for i, link in enumerate(links, 1):
        try:
            response = requests.get(link, timeout=10)
            if response.status_code == 200:
                print(f"Successfully scraped {link}")
                
                # Parse HTML content
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract title
                title = soup.find('title')
                title_text = title.get_text().strip() if title else f"Article_{i}"
                
                # Clean title for filename
                safe_title = re.sub(r'[^\w\s-]', '', title_text)
                safe_title = re.sub(r'[-\s]+', '_', safe_title)
                
                # Extract content
                content_selectors = [
                    'article', 'main', '.content', '.post-content', 
                    '.entry-content', '.article-content', 'body'
                ]
                
                content_text = ""
                for selector in content_selectors:
                    content = soup.select_one(selector)
                    if content:
                        # Remove script and style elements
                        for script in content(["script", "style"]):
                            script.decompose()
                        content_text = content.get_text(separator='\n', strip=True)
                        break
                
                if not content_text:
                    content_text = soup.get_text(separator='\n', strip=True)
                
                markdown_content = f"# {title_text}\n\n"
                markdown_content += f"**Source:** {link}\n\n"
                markdown_content += f"**Scraped on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                markdown_content += "---\n\n"
                markdown_content += content_text
                
                if save_logs and log_folder:
                    # Save to markdown file
                    filename = f"{i:03d}_{safe_title}.md"
                    filepath = os.path.join(log_folder, filename)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    
                    print(f"Saved content to {filepath}")
                else:
                    # Add to combined content
                    combined_content += markdown_content + "\n\n" + "="*80 + "\n\n"
                
        except Exception as e:
            print(f"Failed to scrape {link}: {str(e)}")
    
    if save_logs and log_folder:
        print(f"All scraped content saved in: {log_folder}")
        return None
    else:
        return combined_content