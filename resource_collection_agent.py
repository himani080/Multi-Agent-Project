import requests
import time
import random
from bs4 import BeautifulSoup

class ResourceCollector:
    def __init__(self, industry, use_cases, keywords, github_token=None):
        self.industry = industry
        self.use_cases = use_cases
        self.keywords = keywords  # New parameter for keywords
        self.datasets = []
        self.bonus_solutions = []
        self.github_token = github_token  # Token for GitHub API requests

    def search_datasets(self):
        dataset_sources = {
            "Kaggle": "https://www.kaggle.com/search?q={}",
            "HuggingFace": "https://huggingface.co/datasets?search={}",
            "GitHub": "https://api.github.com/search/repositories?q={}+dataset"
        }
        
        for keyword in self.keywords:  # Use keywords from the industry data
            for source, url in dataset_sources.items():
                search_url = url.format(keyword)
                headers = {'Authorization': f'token {self.github_token}'} if source == "GitHub" and self.github_token else {}
                
                try:
                    response = requests.get(search_url, headers=headers if source == "GitHub" else None)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Handle GitHub JSON response separately
                    if source == "GitHub":
                        results = response.json().get('items', [])[:5]
                        for result in results:
                            title = result['name']
                            link = result['html_url']
                            self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
                    
                    elif source == "Kaggle":
                        datasets = soup.select('a.sc-gKsewC')  # Adjust if necessary
                        for dataset in datasets[:5]:
                            title = dataset.get_text().strip()
                            link = f"https://www.kaggle.com{dataset.get('href')}"
                            self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
                    
                    elif source == "HuggingFace":
                        datasets = soup.select('a.card-link')
                        for dataset in datasets[:5]:
                            title = dataset.get_text().strip()
                            link = f"https://huggingface.co{dataset.get('href')}"
                            self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")

                except requests.exceptions.RequestException as e:
                    print(f"Failed to retrieve data from {source} for keyword '{keyword}': {e}")
                
                # Introduce a random delay between requests to avoid rate limiting
                time.sleep(random.uniform(3, 5))

    def propose_bonus_solutions(self):
        self.bonus_solutions = [
            "1. **Document Search System**: Implement a GenAI-powered document search tool to help employees quickly find relevant information within internal documents, research papers, and clinical guidelines.",
            "2. **Automated Report Generation**: Use AI to generate reports for healthcare practitioners by analyzing and summarizing patient records, lab results, and treatment plans.",
            "3. **AI-Powered Customer Service Chatbot**: Deploy a chatbot powered by GenAI to handle patient inquiries, provide appointment scheduling, and answer FAQs, thereby improving customer satisfaction and reducing the workload on staff."
        ]

    def save_to_markdown(self, filename='Healthcare_Resource_Assets.md'):
        with open(filename, 'w') as file:
            file.write("# Resource Asset Collection for Healthcare Industry\n\n")
            file.write("## Generated AI/ML Use Cases\n")
            for i, use_case in enumerate(self.use_cases, start=1):
                file.write(f"{i}. {use_case}\n")
            file.write("\n## Relevant Dataset Resources\n")
            for dataset in self.datasets:
                file.write(f"{dataset}\n")
            file.write("\n## Suggested GenAI Solutions\n")
            for solution in self.bonus_solutions:
                file.write(f"{solution}\n")
