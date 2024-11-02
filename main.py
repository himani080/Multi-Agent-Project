# # # # # from industry_research_agent import fetch_industry_data
# # # # # from resource_collection_agent import ResourceCollector
# # # # # import requests
# # # # # from bs4 import BeautifulSoup
# # # # # import cohere
# # # # # from dotenv import load_dotenv
# # # # # import os
# # # # # load_dotenv()


# # # # # # Initialize Cohere with your API key
# # # # # cohere_api_key = os.getenv("COHERE_API_KEY")  # Replace with your actual API key
# # # # # cohere_client = cohere.Client(cohere_api_key)

# # # # # def print_industry_data(industry_info):
# # # # #     print("\nIndustry Overview:")
# # # # #     print(industry_info.get('overview', 'No overview found.'))

# # # # #     print("\nKey Offerings:")
# # # # #     for offering in industry_info.get('key_offerings', []):
# # # # #         print(f"- {offering}")

# # # # #     print("\nStrategic Focus Areas:")
# # # # #     for focus in industry_info.get('strategic_focus', []):
# # # # #         print(f"- {focus}")

# # # # # class MarketStandardsAgent:
# # # # #     def __init__(self, industry):
# # # # #         self.industry = industry
# # # # #         self.trends = []
# # # # #         self.standards = []

# # # # #     def fetch_market_standards(self):
# # # # #         try:
# # # # #             # Example URL for industry trends & standards
# # # # #             url = f"https://example.com/industry/{self.industry.lower()}/trends-standards"
# # # # #             response = requests.get(url)
# # # # #             soup = BeautifulSoup(response.text, 'html.parser')

# # # # #             # Parse trends and standards (customize as per actual data source)
# # # # #             self.trends = [trend.get_text() for trend in soup.select(".trend-class")]
# # # # #             self.standards = [standard.get_text() for standard in soup.select(".standard-class")]

# # # # #             print("Trends and Standards Retrieved Successfully.")
        
# # # # #         except Exception as e:
# # # # #             print(f"Error fetching market standards: {e}")

# # # # #     def analyze_trends(self):
# # # # #         analysis = f"Industry Trends for {self.industry}:\n"
# # # # #         for trend in self.trends:
# # # # #             analysis += f"- {trend}\n"
# # # # #         return analysis

# # # # #     def analyze_standards(self):
# # # # #         standards_analysis = f"Industry Standards for {self.industry}:\n"
# # # # #         for standard in self.standards:
# # # # #             standards_analysis += f"- {standard}\n"
# # # # #         return standards_analysis


# # # # # class UseCaseGenerator:
# # # # #     def __init__(self, industry_trends, industry_standards):
# # # # #         self.industry_trends = industry_trends
# # # # #         self.industry_standards = industry_standards
# # # # #         self.use_cases = []

# # # # #     def generate_use_cases(self):
# # # # #         prompt = (f"Based on the following industry trends:\n{self.industry_trends}\n"
# # # # #                   f"And industry standards:\n{self.industry_standards}\n"
# # # # #                   "Suggest AI, GenAI, LLMs, and ML-based use cases for improving operational efficiency, "
# # # # #                   "customer satisfaction, and business processes in the industry.")

# # # # #         try:
# # # # #             response = cohere_client.generate(
# # # # #                 model="command-xlarge",  # Updated model name
# # # # #                 prompt=prompt,
# # # # #                 max_tokens=500,
# # # # #                 temperature=0.7,
# # # # #                 stop_sequences=["--end--"]
# # # # #             )
# # # # #             self.use_cases = response.generations[0].text.strip().split('\n')
        
# # # # #         except Exception as e:
# # # # #             print(f"Error generating use cases: {e}")

# # # # #     def display_use_cases(self):
# # # # #         print("Suggested AI/ML Use Cases:")
# # # # #         for case in self.use_cases:
# # # # #             print(f"- {case}")


# # # # # if __name__ == "__main__":
# # # # #     # Industry input
# # # # #     industry = input("Enter the industry (e.g., Automotive, Healthcare, Finance, etc.): ")

# # # # #     # Fetch and display industry data
# # # # #     industry_data = fetch_industry_data(industry)
# # # # #     print_industry_data(industry_data)

# # # # #     # Get relevant keywords for the industry
# # # # #     keywords = industry_data.get('keywords', ["default", "keywords"])  # Default keywords if none found

# # # # #     # Define general use cases for any industry
# # # # #     use_cases = [
# # # # #         f"{industry} Decision Support",
# # # # #         f"Predictive Analytics and Operations Optimization in {industry}",
# # # # #         f"R&D Enhancement in {industry}",
# # # # #         "Chatbots and Virtual Assistants",
# # # # #         f"Risk Assessment and Management in {industry}",
# # # # #         "Data Analysis and Monitoring",
# # # # #         "Personalized Services and Customer Support",
# # # # #         "Fraud Detection and Cybersecurity"
# # # # #     ]

# # # # #     # Collect resources and propose bonus solutions
# # # # #     github_token = os.getenv("GITHUB_TOKEN")  # Replace with your actual GitHub token
# # # # #     collector = ResourceCollector(industry, use_cases, keywords, github_token=github_token)
# # # # #     collector.search_datasets()
# # # # #     collector.propose_bonus_solutions()
# # # # #     collector.save_to_markdown(filename=f"{industry}_Resource_Assets.md")

# # # # #     print(f"{industry} Resource Assets saved to '{industry}_Resource_Assets.md'.")

# # # # #     # Step 1: Fetch and analyze trends & standards
# # # # #     market_agent = MarketStandardsAgent(industry)
# # # # #     market_agent.fetch_market_standards()
# # # # #     industry_trends = market_agent.analyze_trends()
# # # # #     industry_standards = market_agent.analyze_standards()

# # # # #     # Step 2: Generate relevant use cases based on trends and standards
# # # # #     use_case_generator = UseCaseGenerator(industry_trends, industry_standards)
# # # # #     use_case_generator.generate_use_cases()
    
# # # # #     # Step 3: Display the suggested use cases
# # # # #     use_case_generator.display_use_cases()


# # # # from industry_research_agent import fetch_industry_data
# # # # from resource_collection_agent import ResourceCollector
# # # # import requests
# # # # from bs4 import BeautifulSoup
# # # # import cohere
# # # # from dotenv import load_dotenv
# # # # import os
# # # # import time  # Add this import
# # # # import random  

# # # # load_dotenv()

# # # # # Initialize Cohere with your API key
# # # # cohere_api_key = os.getenv("COHERE_API_KEY")  # Replace with your actual API key
# # # # cohere_client = cohere.Client(cohere_api_key)

# # # # def print_industry_data(industry_info):
# # # #     print("\nIndustry Overview:")
# # # #     print(industry_info.get('overview', 'No overview found.'))

# # # #     print("\nKey Offerings:")
# # # #     for offering in industry_info.get('key_offerings', []):
# # # #         print(f"- {offering}")

# # # #     print("\nStrategic Focus Areas:")
# # # #     for focus in industry_info.get('strategic_focus', []):
# # # #         print(f"- {focus}")

# # # # class MarketStandardsAgent:
# # # #     def __init__(self, industry):
# # # #         self.industry = industry
# # # #         self.trends = []
# # # #         self.standards = []

# # # #     def fetch_market_standards(self):
# # # #         try:
# # # #             # Example URL for industry trends & standards
# # # #             url = f"https://example.com/industry/{self.industry.lower()}/trends-standards"
# # # #             response = requests.get(url)
# # # #             soup = BeautifulSoup(response.text, 'html.parser')

# # # #             # Parse trends and standards (customize as per actual data source)
# # # #             self.trends = [trend.get_text() for trend in soup.select(".trend-class")]
# # # #             self.standards = [standard.get_text() for standard in soup.select(".standard-class")]

# # # #             print("Trends and Standards Retrieved Successfully.")
        
# # # #         except Exception as e:
# # # #             print(f"Error fetching market standards: {e}")

# # # #     def analyze_trends(self):
# # # #         analysis = f"Industry Trends for {self.industry}:\n"
# # # #         for trend in self.trends:
# # # #             analysis += f"- {trend}\n"
# # # #         return analysis

# # # #     def analyze_standards(self):
# # # #         standards_analysis = f"Industry Standards for {self.industry}:\n"
# # # #         for standard in self.standards:
# # # #             standards_analysis += f"- {standard}\n"
# # # #         return standards_analysis


# # # # class UseCaseGenerator:
# # # #     def __init__(self, industry_trends, industry_standards):
# # # #         self.industry_trends = industry_trends
# # # #         self.industry_standards = industry_standards
# # # #         self.use_cases = []

# # # #     def generate_use_cases(self):
# # # #         prompt = (f"Based on the following industry trends:\n{self.industry_trends}\n"
# # # #                   f"And industry standards:\n{self.industry_standards}\n"
# # # #                   "Suggest AI, GenAI, LLMs, and ML-based use cases for improving operational efficiency, "
# # # #                   "customer satisfaction, and business processes in the industry.")

# # # #         try:
# # # #             response = cohere_client.generate(
# # # #                 model="command-xlarge",  # Updated model name
# # # #                 prompt=prompt,
# # # #                 max_tokens=500,
# # # #                 temperature=0.7,
# # # #                 stop_sequences=["--end--"]
# # # #             )
# # # #             self.use_cases = response.generations[0].text.strip().split('\n')
        
# # # #         except Exception as e:
# # # #             print(f"Error generating use cases: {e}")

# # # #     def display_use_cases(self):
# # # #         print("Suggested AI/ML Use Cases:")
# # # #         for case in self.use_cases:
# # # #             print(f"- {case}")
# # # #         return self.use_cases  # Return use cases for further processing


# # # # class ResourceCollector:
# # # #     def __init__(self, industry, use_cases, keywords, github_token=None):
# # # #         self.industry = industry
# # # #         self.use_cases = use_cases
# # # #         self.keywords = keywords
# # # #         self.datasets = []
# # # #         self.bonus_solutions = []
# # # #         self.github_token = github_token

# # # #     def search_datasets(self):
# # # #         dataset_sources = {
# # # #             "Kaggle": "https://www.kaggle.com/search?q={}",
# # # #             "HuggingFace": "https://huggingface.co/datasets?search={}",
# # # #             "GitHub": "https://api.github.com/search/repositories?q={}+dataset"
# # # #         }

# # # #         relevant_keywords = self.extract_relevant_keywords()  # Extract relevant keywords from use cases

# # # #         for keyword in relevant_keywords:
# # # #             for source, url in dataset_sources.items():
# # # #                 search_url = url.format(keyword)
# # # #                 headers = {'Authorization': f'token {self.github_token}'} if source == "GitHub" and self.github_token else {}

# # # #                 try:
# # # #                     response = requests.get(search_url, headers=headers if source == "GitHub" else None)
# # # #                     response.raise_for_status()

# # # #                     if source == "GitHub":
# # # #                         results = response.json().get('items', [])[:5]
# # # #                         for result in results:
# # # #                             title = result['name']
# # # #                             link = result['html_url']
# # # #                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")

# # # #                     elif source == "Kaggle":
# # # #                         soup = BeautifulSoup(response.text, 'html.parser')
# # # #                         datasets = soup.select('a.sc-gKsewC')
# # # #                         for dataset in datasets[:5]:
# # # #                             title = dataset.get_text().strip()
# # # #                             link = f"https://www.kaggle.com{dataset.get('href')}"
# # # #                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")

# # # #                     elif source == "HuggingFace":
# # # #                         soup = BeautifulSoup(response.text, 'html.parser')
# # # #                         datasets = soup.select('a.card-link')
# # # #                         for dataset in datasets[:5]:
# # # #                             title = dataset.get_text().strip()
# # # #                             link = f"https://huggingface.co{dataset.get('href')}"
# # # #                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")

# # # #                 except requests.exceptions.RequestException as e:
# # # #                     print(f"Error retrieving data from {source} for keyword '{keyword}': {e}")
                
# # # #                 time.sleep(random.uniform(3, 5))

# # # #     def extract_relevant_keywords(self):
# # # #         # Extract keywords relevant to use cases
# # # #         relevant_keywords = []
# # # #         for use_case in self.use_cases:
# # # #             # You can customize this logic to extract keywords more intelligently
# # # #             words = use_case.split()
# # # #             relevant_keywords.extend(words)  # This will add all words; you can refine the logic
# # # #         return set(relevant_keywords)  # Use a set to avoid duplicates

# # # #     def propose_bonus_solutions(self):
# # # #         self.bonus_solutions = [
# # # #             "1. **Document Search System**: Implement a GenAI-powered document search tool to help employees quickly find relevant information within internal documents, research papers, and clinical guidelines.",
# # # #             "2. **Automated Report Generation**: Use AI to generate reports for healthcare practitioners by analyzing and summarizing patient records, lab results, and treatment plans.",
# # # #             "3. **AI-Powered Customer Service Chatbot**: Deploy a chatbot powered by GenAI to handle patient inquiries, provide appointment scheduling, and answer FAQs, thereby improving customer satisfaction and reducing the workload on staff."
# # # #         ]

# # # #     def save_to_markdown(self, filename='Resource_Assets.md'):
# # # #         with open(filename, 'w') as file:
# # # #             file.write(f"# Resource Asset Collection for {self.industry} Industry\n\n")
# # # #             file.write("## Generated AI/ML Use Cases\n")
# # # #             for i, use_case in enumerate(self.use_cases, start=1):
# # # #                 file.write(f"{i}. {use_case}\n")
# # # #             file.write("\n## Relevant Dataset Resources\n")
# # # #             for dataset in self.datasets:
# # # #                 file.write(f"{dataset}\n")
# # # #             file.write("\n## Suggested GenAI Solutions\n")
# # # #             for solution in self.bonus_solutions:
# # # #                 file.write(f"{solution}\n")


# # # # if __name__ == "__main__":
# # # #     # Industry input
# # # #     industry = input("Enter the industry (e.g., Automotive, Healthcare, Finance, etc.): ")

# # # #     # Fetch and display industry data
# # # #     industry_data = fetch_industry_data(industry)
# # # #     print_industry_data(industry_data)

# # # #     # Get relevant keywords for the industry
# # # #     keywords = industry_data.get('keywords', ["default", "keywords"])  # Default keywords if none found

# # # #     # Define general use cases for any industry
# # # #     use_cases = [
# # # #         f"{industry} Decision Support",
# # # #         f"Predictive Analytics and Operations Optimization in {industry}",
# # # #         f"R&D Enhancement in {industry}",
# # # #         "Chatbots and Virtual Assistants",
# # # #         f"Risk Assessment and Management in {industry}",
# # # #         "Data Analysis and Monitoring",
# # # #         "Personalized Services and Customer Support",
# # # #         "Fraud Detection and Cybersecurity"
# # # #     ]

# # # #     # Step 1: Fetch and analyze trends & standards
# # # #     market_agent = MarketStandardsAgent(industry)
# # # #     market_agent.fetch_market_standards()
# # # #     industry_trends = market_agent.analyze_trends()
# # # #     industry_standards = market_agent.analyze_standards()

# # # #     # Step 2: Generate relevant use cases based on trends and standards
# # # #     use_case_generator = UseCaseGenerator(industry_trends, industry_standards)
# # # #     use_case_generator.generate_use_cases()
    
# # # #     # Step 3: Display the suggested use cases
# # # #     generated_use_cases = use_case_generator.display_use_cases()

# # # #     # Collect resources and propose bonus solutions
# # # #     github_token = os.getenv("GITHUB_TOKEN")  # Replace with your actual GitHub token
# # # #     collector = ResourceCollector(industry, generated_use_cases, keywords, github_token=github_token)
# # # #     collector.search_datasets()
# # # #     collector.propose_bonus_solutions()
# # # #     collector.save_to_markdown(filename=f"{industry}_Resource_Assets.md")

# # # #     print(f"{industry} Resource Assets saved to '{industry}_Resource_Assets.md'.")


# # # from industry_research_agent import fetch_industry_data
# # # from resource_collection_agent import ResourceCollector
# # # import requests
# # # from bs4 import BeautifulSoup
# # # import cohere
# # # from dotenv import load_dotenv
# # # import os
# # # import time
# # # import random  

# # # load_dotenv()

# # # # Initialize Cohere with your API key
# # # cohere_api_key = os.getenv("COHERE_API_KEY")  # Replace with your actual API key
# # # cohere_client = cohere.Client(cohere_api_key)

# # # def print_industry_data(industry_info):
# # #     print("\nIndustry Overview:")
# # #     print(industry_info.get('overview', 'No overview found.'))

# # #     print("\nKey Offerings:")
# # #     for offering in industry_info.get('key_offerings', []):
# # #         print(f"- {offering}")

# # #     print("\nStrategic Focus Areas:")
# # #     for focus in industry_info.get('strategic_focus', []):
# # #         print(f"- {focus}")

# # # class MarketStandardsAgent:
# # #     def __init__(self, industry):
# # #         self.industry = industry
# # #         self.trends = []
# # #         self.standards = []

# # #     def fetch_market_standards(self):
# # #         try:
# # #             # Example URL for industry trends & standards
# # #             url = f"https://example.com/industry/{self.industry.lower()}/trends-standards"
# # #             response = requests.get(url)
# # #             soup = BeautifulSoup(response.text, 'html.parser')

# # #             # Parse trends and standards (customize as per actual data source)
# # #             self.trends = [trend.get_text() for trend in soup.select(".trend-class")]
# # #             self.standards = [standard.get_text() for standard in soup.select(".standard-class")]

# # #             print("Trends and Standards Retrieved Successfully.")
        
# # #         except Exception as e:
# # #             print(f"Error fetching market standards: {e}")

# # #     def analyze_trends(self):
# # #         analysis = f"Industry Trends for {self.industry}:\n"
# # #         for trend in self.trends:
# # #             analysis += f"- {trend}\n"
# # #         return analysis

# # #     def analyze_standards(self):
# # #         standards_analysis = f"Industry Standards for {self.industry}:\n"
# # #         for standard in self.standards:
# # #             standards_analysis += f"- {standard}\n"
# # #         return standards_analysis

# # # class UseCaseGenerator:
# # #     def __init__(self, industry_trends, industry_standards):
# # #         self.industry_trends = industry_trends
# # #         self.industry_standards = industry_standards
# # #         self.use_cases = []

# # #     def generate_use_cases(self):
# # #         prompt = (f"Based on the following industry trends:\n{self.industry_trends}\n"
# # #                   f"And industry standards:\n{self.industry_standards}\n"
# # #                   "Suggest AI, GenAI, LLMs, and ML-based use cases for improving operational efficiency, "
# # #                   "customer satisfaction, and business processes in the industry.")

# # #         try:
# # #             response = cohere_client.generate(
# # #                 model="command-xlarge",
# # #                 prompt=prompt,
# # #                 max_tokens=500,
# # #                 temperature=0.7,
# # #                 stop_sequences=["--end--"]
# # #             )
# # #             self.use_cases = response.generations[0].text.strip().split('\n')
        
# # #         except Exception as e:
# # #             print(f"Error generating use cases: {e}")

# # #     def display_use_cases(self):
# # #         print("Suggested AI/ML Use Cases:")
# # #         for case in self.use_cases:
# # #             print(f"- {case}")
# # #         return self.use_cases  # Return use cases for further processing

# # # class ResourceCollector:
# # #     def __init__(self, industry, use_cases, keywords, github_token=None):
# # #         self.industry = industry
# # #         self.use_cases = use_cases
# # #         self.keywords = keywords
# # #         self.datasets = []
# # #         self.bonus_solutions = []
# # #         self.github_token = github_token

# # #     def search_datasets(self):
# # #         dataset_sources = {
# # #             "Kaggle": "https://www.kaggle.com/search?q={}",
# # #             "HuggingFace": "https://huggingface.co/datasets?search={}",
# # #             "GitHub": "https://api.github.com/search/repositories?q={}+dataset"
# # #         }

# # #         relevant_keywords = self.extract_relevant_keywords()

# # #         for keyword in relevant_keywords:
# # #             for source, url in dataset_sources.items():
# # #                 search_url = url.format(keyword)
# # #                 headers = {'Authorization': f'token {self.github_token}'} if source == "GitHub" and self.github_token else {}

# # #                 try:
# # #                     response = requests.get(search_url, headers=headers if source == "GitHub" else None)
# # #                     response.raise_for_status()

# # #                     if source == "GitHub":
# # #                         results = response.json().get('items', [])[:5]
# # #                         for result in results:
# # #                             title = result['name']
# # #                             link = result['html_url']
# # #                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")

# # #                     elif source == "Kaggle":
# # #                         soup = BeautifulSoup(response.text, 'html.parser')
# # #                         datasets = soup.select('a.sc-gKsewC')
# # #                         for dataset in datasets[:5]:
# # #                             title = dataset.get_text().strip()
# # #                             link = f"https://www.kaggle.com{dataset.get('href')}"
# # #                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")

# # #                     elif source == "HuggingFace":
# # #                         soup = BeautifulSoup(response.text, 'html.parser')
# # #                         datasets = soup.select('a.card-link')
# # #                         for dataset in datasets[:5]:
# # #                             title = dataset.get_text().strip()
# # #                             link = f"https://huggingface.co{dataset.get('href')}"
# # #                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")

# # #                 except requests.exceptions.RequestException as e:
# # #                     print(f"Error retrieving data from {source} for keyword '{keyword}': {e}")
                
# # #                 time.sleep(random.uniform(3, 5))

# # #     def extract_relevant_keywords(self):
# # #         relevant_keywords = []
# # #         for use_case in self.use_cases:
# # #             words = use_case.split()
# # #             relevant_keywords.extend(words)
# # #         return set(relevant_keywords)  # Use a set to avoid duplicates

# # #     def propose_bonus_solutions(self):
# # #         self.bonus_solutions = [
# # #             "1. **Document Search System**: Implement a GenAI-powered document search tool to help employees quickly find relevant information within internal documents, research papers, and clinical guidelines.",
# # #             "2. **Automated Report Generation**: Use AI to generate reports for healthcare practitioners by analyzing and summarizing patient records, lab results, and treatment plans.",
# # #             "3. **AI-Powered Customer Service Chatbot**: Deploy a chatbot powered by GenAI to handle patient inquiries, provide appointment scheduling, and answer FAQs, thereby improving customer satisfaction and reducing the workload on staff."
# # #         ]

# # #     def save_to_markdown(self, filename='Resource_Assets.md'):
# # #         with open(filename, 'w') as file:
# # #             file.write(f"# Resource Asset Collection for {self.industry} Industry\n\n")
# # #             file.write("## Generated AI/ML Use Cases\n")
# # #             for i, use_case in enumerate(self.use_cases, start=1):
# # #                 file.write(f"{i}. {use_case}\n")
# # #             file.write("\n## Relevant Dataset Resources\n")
# # #             for dataset in self.datasets:
# # #                 file.write(f"{dataset}\n")
# # #             file.write("\n## Suggested GenAI Solutions\n")
# # #             for solution in self.bonus_solutions:
# # #                 file.write(f"{solution}\n")

# # # if __name__ == "__main__":
# # #     # Industry input
# # #     industry = input("Enter the industry (e.g., Automotive, Healthcare, Finance, etc.): ")

# # #     # Fetch and display industry data
# # #     industry_data = fetch_industry_data(industry)
# # #     print_industry_data(industry_data)

# # #     # Get relevant keywords for the industry
# # #     keywords = industry_data.get('keywords', ["default", "keywords"])  # Default keywords if none found

# # #     # Define general use cases for any industry
# # #     use_cases = [
# # #         f"{industry} Decision Support",
# # #         f"Predictive Analytics and Operations Optimization in {industry}",
# # #         f"R&D Enhancement in {industry}",
# # #         "Chatbots and Virtual Assistants",
# # #         f"Risk Assessment and Management in {industry}",
# # #         "Data Analysis and Monitoring",
# # #         "Personalized Services and Customer Support",
# # #         "Fraud Detection and Cybersecurity"
# # #     ]

# # #     # Step 1: Fetch and analyze trends & standards
# # #     market_agent = MarketStandardsAgent(industry)
# # #     market_agent.fetch_market_standards()
# # #     industry_trends = market_agent.analyze_trends()
# # #     industry_standards = market_agent.analyze_standards()

# # #     # Step 2: Generate relevant use cases based on trends and standards
# # #     use_case_generator = UseCaseGenerator(industry_trends, industry_standards)
# # #     use_case_generator.generate_use_cases()
    
# # #     # Step 3: Display the suggested use cases
# # #     generated_use_cases = use_case_generator.display_use_cases()

# # #     # Collect resources and propose bonus solutions
# # #     github_token = os.getenv("GITHUB_TOKEN")  # Replace with your actual GitHub token
# # #     collector = ResourceCollector(industry, generated_use_cases, keywords, github_token=github_token)
    
# # #     # Correctly call the search_datasets method
# # #     collector.search_datasets()

# # #     # Propose bonus solutions
# # #     collector.propose_bonus_solutions()
    
# # #     # Save to markdown file
# # #     collector.save_to_markdown(filename=f"{industry}_Resource_Assets.md")

# # #     print(f"{industry} Resource Assets saved to '{industry}_Resource_Assets.md'.")
# # from industry_research_agent import fetch_industry_data
# # from resource_collection_agent import ResourceCollector
# # import requests
# # from bs4 import BeautifulSoup
# # import cohere
# # from dotenv import load_dotenv
# # import os
# # import time
# # import random  

# # load_dotenv()

# # # Initialize Cohere with your API key
# # cohere_api_key = os.getenv("COHERE_API_KEY")  # Replace with your actual API key
# # cohere_client = cohere.Client(cohere_api_key)

# # def print_industry_data(industry_info):
# #     print("\nIndustry Overview:")
# #     print(industry_info.get('overview', 'No overview found.'))

# #     print("\nKey Offerings:")
# #     for offering in industry_info.get('key_offerings', []):
# #         print(f"- {offering}")

# #     print("\nStrategic Focus Areas:")
# #     for focus in industry_info.get('strategic_focus', []):
# #         print(f"- {focus}")

# # class MarketStandardsAgent:
# #     def __init__(self, industry):
# #         self.industry = industry
# #         self.trends = []
# #         self.standards = []

# #     def fetch_market_standards(self):
# #         try:
# #             # Example URL for industry trends & standards
# #             url = f"https://example.com/industry/{self.industry.lower()}/trends-standards"
# #             response = requests.get(url)
# #             response.raise_for_status()  # Ensure we raise an error for bad responses
# #             soup = BeautifulSoup(response.text, 'html.parser')

# #             # Parse trends and standards (customize as per actual data source)
# #             self.trends = [trend.get_text() for trend in soup.select(".trend-class")]
# #             self.standards = [standard.get_text() for standard in soup.select(".standard-class")]

# #             print("Trends and Standards Retrieved Successfully.")
        
# #         except Exception as e:
# #             print(f"Error fetching market standards: {e}")

# #     def analyze_trends(self):
# #         return f"Industry Trends for {self.industry}:\n" + "\n".join([f"- {trend}" for trend in self.trends])

# #     def analyze_standards(self):
# #         return f"Industry Standards for {self.industry}:\n" + "\n".join([f"- {standard}" for standard in self.standards])

# # class UseCaseGenerator:
# #     def __init__(self, industry_trends, industry_standards):
# #         self.industry_trends = industry_trends
# #         self.industry_standards = industry_standards
# #         self.use_cases = []

# #     def generate_use_cases(self):
# #         prompt = (f"Based on the following industry trends:\n{self.industry_trends}\n"
# #                   f"And industry standards:\n{self.industry_standards}\n"
# #                   "Suggest AI, GenAI, LLMs, and ML-based use cases for improving operational efficiency, "
# #                   "customer satisfaction, and business processes in the industry.")

# #         try:
# #             response = cohere_client.generate(
# #                 model="command-xlarge",
# #                 prompt=prompt,
# #                 max_tokens=500,
# #                 temperature=0.7,
# #                 stop_sequences=["--end--"]
# #             )
# #             self.use_cases = response.generations[0].text.strip().split('\n')
        
# #         except Exception as e:
# #             print(f"Error generating use cases: {e}")

# #     def display_use_cases(self):
# #         print("Suggested AI/ML Use Cases:")
# #         for case in self.use_cases:
# #             print(f"- {case}")
# #         return self.use_cases  # Return use cases for further processing

# # class ResourceCollector:
# #     def __init__(self, industry, use_cases, keywords, github_token=None):
# #         self.industry = industry
# #         self.use_cases = use_cases
# #         self.keywords = keywords
# #         self.datasets = []
# #         self.bonus_solutions = []
# #         self.github_token = github_token

# #     def extract_relevant_keywords(self):
# #         relevant_keywords = []
# #         for use_case in self.use_cases:
# #             words = use_case.split()
# #             relevant_keywords.extend(words)
# #         return set(relevant_keywords)  # Use a set to avoid duplicates
# # def search_datasets(self):
# #     dataset_sources = {
# #         "Kaggle": "https://www.kaggle.com/search?q={}",
# #         "HuggingFace": "https://huggingface.co/datasets?search={}",
# #         "GitHub": "https://api.github.com/search/repositories?q={}+dataset"
# #     }

# #     relevant_keywords = self.extract_relevant_keywords()  # Keep this as a set for unique keywords
# #     relevant_keywords_list = list(relevant_keywords)  # Convert to list for indexing
# #     max_requests_per_source = 5  # Limit the number of requests to each source

# #     for i, keyword in enumerate(relevant_keywords_list):  # Use index for tracking
# #         for source, url in dataset_sources.items():
# #             search_url = url.format(keyword)
# #             headers = {'Authorization': f'token {self.github_token}'} if source == "GitHub" and self.github_token else {}

# #             try:
# #                 print(f"Searching datasets for keyword: {keyword} in {source}...")
# #                 response = requests.get(search_url, headers=headers if source == "GitHub" else None)
# #                 response.raise_for_status()

# #                 if source == "GitHub":
# #                     results = response.json().get('items', [])[:max_requests_per_source]
# #                     for result in results:
# #                         title = result['name']
# #                         link = result['html_url']
# #                         self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
# #                         print(f"Found: [{title}]({link})")  # Print link with title

# #                 elif source == "Kaggle":
# #                     soup = BeautifulSoup(response.text, 'html.parser')
# #                     datasets = soup.select('a.sc-gKsewC')
# #                     for dataset in datasets[:max_requests_per_source]:
# #                         title = dataset.get_text().strip()
# #                         link = f"https://www.kaggle.com{dataset.get('href')}"
# #                         self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
# #                         print(f"Found: [{title}]({link})")  # Print link with title

# #                 elif source == "HuggingFace":
# #                     soup = BeautifulSoup(response.text, 'html.parser')
# #                     datasets = soup.select('a.card-link')
# #                     for dataset in datasets[:max_requests_per_source]:
# #                         title = dataset.get_text().strip()
# #                         link = f"https://huggingface.co{dataset.get('href')}"
# #                         self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
# #                         print(f"Found: [{title}]({link})")  # Print link with title

# #                 print(f"Completed search for {source} with keyword: {keyword}")

# #             except requests.exceptions.RequestException as e:
# #                 print(f"Error retrieving data from {source} for keyword '{keyword}': {e}")

# #             # Sleep only after every max_requests_per_source requests
# #             if (i + 1) % max_requests_per_source == 0:
# #                 print("Sleeping to avoid overwhelming the server...")
# #                 time.sleep(random.uniform(2, 5))  # Reduced sleep duration
# #             else:
# #                 time.sleep(random.uniform(1, 3))  # Shorter sleep between individual requests

# #     def propose_bonus_solutions(self):
# #         self.bonus_solutions = [
# #             "1. **Document Search System**: Implement a GenAI-powered document search tool to help employees quickly find relevant information within internal documents, research papers, and clinical guidelines.",
# #             "2. **Automated Report Generation**: Use AI to generate reports for healthcare practitioners by analyzing and summarizing patient records, lab results, and treatment plans.",
# #             "3. **AI-Powered Customer Service Chatbot**: Deploy a chatbot powered by GenAI to handle patient inquiries, provide appointment scheduling, and answer FAQs, thereby improving customer satisfaction and reducing the workload on staff."
# #         ]

# #     def save_to_markdown(self, filename='Resource_Assets.md'):
# #         with open(filename, 'w') as file:
# #             file.write(f"# Resource Asset Collection for {self.industry} Industry\n\n")
# #             file.write("## Generated AI/ML Use Cases\n")
# #             for i, use_case in enumerate(self.use_cases, start=1):
# #                 file.write(f"{i}. {use_case}\n")
# #             file.write("\n## Relevant Dataset Resources\n")
# #             for dataset in self.datasets:
# #                 file.write(f"{dataset}\n")
# #             file.write("\n## Suggested GenAI Solutions\n")
# #             for solution in self.bonus_solutions:
# #                 file.write(f"{solution}\n")

# # if __name__ == "__main__":
# #     # Industry input
# #     industry = input("Enter the industry (e.g., Automotive, Healthcare, Finance, etc.): ")

# #     # Fetch and display industry data
# #     industry_data = fetch_industry_data(industry)
# #     print_industry_data(industry_data)

# #     # Get relevant keywords for the industry
# #     keywords = industry_data.get('keywords', ["default", "keywords"])  # Default keywords if none found

# #     # Define general use cases for any industry
# #     use_cases = [
# #         f"{industry} Decision Support",
# #         f"Predictive Analytics and Operations Optimization in {industry}",
# #         f"R&D Enhancement in {industry}",
# #         "Chatbots and Virtual Assistants",
# #         f"Risk Assessment and Management in {industry}",
# #         "Data Analysis and Monitoring",
# #         "Personalized Services and Customer Support",
# #         "Fraud Detection and Cybersecurity"
# #     ]

# #     # Step 1: Fetch and analyze trends & standards
# #     market_agent = MarketStandardsAgent(industry)
# #     market_agent.fetch_market_standards()
# #     industry_trends = market_agent.analyze_trends()
# #     industry_standards = market_agent.analyze_standards()

# #     # Step 2: Generate relevant use cases based on trends and standards
# #     use_case_gen = UseCaseGenerator(industry_trends, industry_standards)
# #     use_case_gen.generate_use_cases()
# #     use_case_gen.display_use_cases()

# #     # Step 3: Collect resources based on generated use cases
# #     resource_collector = ResourceCollector(industry, use_case_gen.use_cases, keywords)
# #     resource_collector.search_datasets()
# #     resource_collector.propose_bonus_solutions()
# #     resource_collector.save_to_markdown()



# from industry_research_agent import fetch_industry_data
# from resource_collection_agent import ResourceCollector
# import requests
# from bs4 import BeautifulSoup
# import cohere
# from dotenv import load_dotenv
# import os
# import time
# import random  

# load_dotenv()

# # Initialize Cohere with your API key
# cohere_api_key = os.getenv("COHERE_API_KEY")  # Replace with your actual API key
# cohere_client = cohere.Client(cohere_api_key)

# def print_industry_data(industry_info):
#     print("\nIndustry Overview:")
#     print(industry_info.get('overview', 'No overview found.'))

#     print("\nKey Offerings:")
#     for offering in industry_info.get('key_offerings', []):
#         print(f"- {offering}")

#     print("\nStrategic Focus Areas:")
#     for focus in industry_info.get('strategic_focus', []):
#         print(f"- {focus}")

# class MarketStandardsAgent:
#     def __init__(self, industry):
#         self.industry = industry
#         self.trends = []
#         self.standards = []

#     def fetch_market_standards(self):
#         try:
#             # Example URL for industry trends & standards
#             url = f"https://example.com/industry/{self.industry.lower()}/trends-standards"
#             response = requests.get(url)
#             response.raise_for_status()  # Ensure we raise an error for bad responses
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Parse trends and standards (customize as per actual data source)
#             self.trends = [trend.get_text() for trend in soup.select(".trend-class")]
#             self.standards = [standard.get_text() for standard in soup.select(".standard-class")]

#             print("Trends and Standards Retrieved Successfully.")
        
#         except Exception as e:
#             print(f"Error fetching market standards: {e}")

#     def analyze_trends(self):
#         return f"Industry Trends for {self.industry}:\n" + "\n".join([f"- {trend}" for trend in self.trends])

#     def analyze_standards(self):
#         return f"Industry Standards for {self.industry}:\n" + "\n".join([f"- {standard}" for standard in self.standards])

# class UseCaseGenerator:
#     def __init__(self, industry_trends, industry_standards):
#         self.industry_trends = industry_trends
#         self.industry_standards = industry_standards
#         self.use_cases = []

#     def generate_use_cases(self):
#         prompt = (f"Based on the following industry trends:\n{self.industry_trends}\n"
#                   f"And industry standards:\n{self.industry_standards}\n"
#                   "Suggest AI, GenAI, LLMs, and ML-based use cases for improving operational efficiency, "
#                   "customer satisfaction, and business processes in the industry.")

#         try:
#             response = cohere_client.generate(
#                 model="command-xlarge",
#                 prompt=prompt,
#                 max_tokens=500,
#                 temperature=0.7,
#                 stop_sequences=["--end--"]
#             )
#             self.use_cases = response.generations[0].text.strip().split('\n')
        
#         except Exception as e:
#             print(f"Error generating use cases: {e}")

#     def display_use_cases(self):
#         print("Suggested AI/ML Use Cases:")
#         for case in self.use_cases:
#             print(f"- {case}")
#         return self.use_cases  # Return use cases for further processing

# class ResourceCollector:
#     def __init__(self, industry, use_cases, keywords, github_token=None):
#         self.industry = industry
#         self.use_cases = use_cases
#         self.keywords = keywords
#         self.datasets = []
#         self.bonus_solutions = []
#         self.github_token = github_token

#     def extract_relevant_keywords(self):
#         relevant_keywords = []
#         for use_case in self.use_cases:
#             words = use_case.split()
#             relevant_keywords.extend(words)
#         return set(relevant_keywords)  # Use a set to avoid duplicates

#     def search_datasets(self):
#         dataset_sources = {
#             "Kaggle": "https://www.kaggle.com/search?q={}",
#             "HuggingFace": "https://huggingface.co/datasets?search={}",
#             "GitHub": "https://api.github.com/search/repositories?q={}+dataset"
#         }

#         relevant_keywords = self.extract_relevant_keywords()  # Keep this as a set for unique keywords
#         relevant_keywords_list = list(relevant_keywords)  # Convert to list for indexing
#         max_requests_per_source = 5  # Limit the number of requests to each source

#         for i, keyword in enumerate(relevant_keywords_list):  # Use index for tracking
#             for source, url in dataset_sources.items():
#                 search_url = url.format(keyword)
#                 headers = {'Authorization': f'token {self.github_token}'} if source == "GitHub" and self.github_token else {}

#                 try:
#                     print(f"Searching datasets for keyword: {keyword} in {source}...")
#                     response = requests.get(search_url, headers=headers if source == "GitHub" else None)
#                     response.raise_for_status()

#                     if source == "GitHub":
#                         results = response.json().get('items', [])[:max_requests_per_source]
#                         for result in results:
#                             title = result['name']
#                             link = result['html_url']
#                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
#                             print(f"Found: [{title}]({link})")  # Print link with title

#                     elif source == "Kaggle":
#                         soup = BeautifulSoup(response.text, 'html.parser')
#                         datasets = soup.select('a.sc-gKsewC')
#                         for dataset in datasets[:max_requests_per_source]:
#                             title = dataset.get_text().strip()
#                             link = f"https://www.kaggle.com{dataset.get('href')}"
#                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
#                             print(f"Found: [{title}]({link})")  # Print link with title

#                     elif source == "HuggingFace":
#                         soup = BeautifulSoup(response.text, 'html.parser')
#                         datasets = soup.select('a.card-link')
#                         for dataset in datasets[:max_requests_per_source]:
#                             title = dataset.get_text().strip()
#                             link = f"https://huggingface.co{dataset.get('href')}"
#                             self.datasets.append(f"**Source**: {source} | **Keyword**: {keyword} | **Dataset**: [{title}]({link})")
#                             print(f"Found: [{title}]({link})")  # Print link with title

#                     print(f"Completed search for {source} with keyword: {keyword}")

#                 except requests.exceptions.RequestException as e:
#                     print(f"Error retrieving data from {source} for keyword '{keyword}': {e}")

#                 # Sleep only after every max_requests_per_source requests
#                 if (i + 1) % max_requests_per_source == 0:
#                     print("Sleeping to avoid overwhelming the server...")
#                     time.sleep(random.uniform(2, 5))  # Reduced sleep duration
#                 else:
#                     time.sleep(random.uniform(1, 3))  # Shorter sleep between individual requests

#     def propose_bonus_solutions(self):
#         self.bonus_solutions = [
#             "1. **Document Search System**: Implement a GenAI-powered document search tool to help employees quickly find relevant information within internal documents, research papers, and clinical guidelines.",
#             "2. **Automated Report Generation**: Use AI to generate reports for healthcare practitioners by analyzing and summarizing patient records, lab results, and treatment plans.",
#             "3. **AI-Powered Customer Service Chatbot**: Deploy a chatbot powered by GenAI to handle patient inquiries, provide appointment scheduling, and answer FAQs, thereby improving customer satisfaction and reducing the workload on staff."
#         ]

#     def save_to_markdown(self, filename='Resource_Assets.md'):
#         with open(filename, 'w') as file:
#             file.write(f"# Resource Asset Collection for {self.industry} Industry\n\n")
#             file.write("## Generated AI/ML Use Cases\n")
#             for i, use_case in enumerate(self.use_cases, start=1):
#                 file.write(f"{i}. {use_case}\n")
#             file.write("\n## Relevant Dataset Resources\n")
#             for dataset in self.datasets:
#                 file.write(f"{dataset}\n")
#             file.write("\n## Suggested GenAI Solutions\n")
#             for solution in self.bonus_solutions:
#                 file.write(f"{solution}\n")

# if __name__ == "__main__":
#     # Industry input
#     industry = input("Enter the industry (e.g., Automotive, Healthcare, Finance, etc.): ")

#     # Fetch and display industry data
#     industry_data = fetch_industry_data(industry)
#     print_industry_data(industry_data)

#     # Get relevant keywords for the industry
#     keywords = industry_data.get('keywords', ["default", "keywords"])  # Default keywords if none found

#     # Define general use cases for any industry
#     use_cases = [
#         f"{industry} Decision Support",
#         f"Predictive Analytics and Operations Optimization in {industry}",
#         f"R&D Enhancement in {industry}",
#         "Chatbots and Virtual Assistants",
#         f"Risk Assessment and Management in {industry}",
#         "Data Analysis and Insights Generation",
#         "Customer Service Automation"
#     ]

#     # Initialize agents
#     market_standards_agent = MarketStandardsAgent(industry)
#     market_standards_agent.fetch_market_standards()
#     industry_trends = market_standards_agent.analyze_trends()
#     industry_standards = market_standards_agent.analyze_standards()

#     # Generate use cases
#     use_case_gen = UseCaseGenerator(industry_trends, industry_standards)
#     use_case_gen.generate_use_cases()
#     use_case_gen.display_use_cases()

#     # Collect resources
#     resource_collector = ResourceCollector(industry, use_cases, keywords, github_token=os.getenv("GITHUB_TOKEN"))
#     resource_collector.search_datasets()
#     resource_collector.propose_bonus_solutions()

#     # Save results to markdown
#     resource_collector.save_to_markdown()

#     print("Resource asset collection completed!")


import streamlit as st
import requests
from bs4 import BeautifulSoup
import cohere
from dotenv import load_dotenv
import os
import time
import random

from industry_research_agent import fetch_industry_data
from resource_collection_agent import ResourceCollector

load_dotenv()

# Initialize Cohere API client
cohere_api_key = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(cohere_api_key)

# Streamlit setup
st.title("AI Use Case and Resource Generator")
st.sidebar.title("Input Industry")

# Industry input
industry = st.sidebar.text_input("Enter the industry (e.g., Automotive, Healthcare, Finance, etc.):", "")

class MarketStandardsAgent:
    def __init__(self, industry):
        self.industry = industry
        self.trends = []
        self.standards = []

    def fetch_market_standards(self):
        try:
            url = f"https://example.com/industry/{self.industry.lower()}/trends-standards"
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            self.trends = [trend.get_text() for trend in soup.select(".trend-class")]
            self.standards = [standard.get_text() for standard in soup.select(".standard-class")]
            return "Market standards retrieved successfully."
        except Exception as e:
            return f"Error fetching market standards: {e}"

class UseCaseGenerator:
    def __init__(self, industry_trends, industry_standards):
        self.industry_trends = industry_trends
        self.industry_standards = industry_standards
        self.use_cases = []

    def generate_use_cases(self):
        prompt = (f"Based on the following industry trends:\n{self.industry_trends}\n"
                  f"And industry standards:\n{self.industry_standards}\n"
                  "Suggest AI, GenAI, LLMs, and ML-based use cases for improving operational efficiency, "
                  "customer satisfaction, and business processes in the industry.")

        try:
            response = cohere_client.generate(
                model="command-xlarge",
                prompt=prompt,
                max_tokens=500,
                temperature=0.7,
                stop_sequences=["--end--"]
            )
            self.use_cases = response.generations[0].text.strip().split('\n')
        except Exception as e:
            st.write(f"Error generating use cases: {e}")

class ResourceCollectorUI:
    def __init__(self, industry, use_cases, keywords, github_token=None):
        self.industry = industry
        self.use_cases = use_cases
        self.keywords = keywords
        self.datasets = []
        self.github_token = github_token

    def extract_relevant_keywords(self):
        relevant_keywords = []
        for use_case in self.use_cases:
            words = use_case.split()
            relevant_keywords.extend(words)
        return set(relevant_keywords)  # Use a set to avoid duplicates

    def search_datasets(self):
        dataset_sources = {
            "Kaggle": "https://www.kaggle.com/search?q={}",
            "HuggingFace": "https://huggingface.co/datasets?search={}",
            "GitHub": "https://api.github.com/search/repositories?q={}+dataset"
        }

        relevant_keywords = self.extract_relevant_keywords()  # Keep this as a set for unique keywords
        relevant_keywords_list = list(relevant_keywords)  # Convert to list for indexing
        max_requests_per_source = 5  # Limit the number of requests to each source

        for i, keyword in enumerate(relevant_keywords_list):  # Use index for tracking
            for source, url in dataset_sources.items():
                search_url = url.format(keyword)
                headers = {'Authorization': f'token {self.github_token}'} if source == "GitHub" and self.github_token else {}

                try:
                    print(f"Searching datasets for keyword: {keyword} in {source}...")
                    response = requests.get(search_url, headers=headers if source == "GitHub" else None)
                    response.raise_for_status()

                    if source == "GitHub":
                        results = response.json().get('items', [])[:max_requests_per_source]
                        for result in results:
                            title = result['name']
                            link = result['html_url']
                            dataset_entry = f"**Source**: {source} | **Keyword**: `{keyword}` | **Dataset**: [{title}]({link})"
                            self.datasets.append(dataset_entry)
                            st.write(dataset_entry)

                    elif source == "Kaggle":
                        soup = BeautifulSoup(response.text, 'html.parser')
                        datasets = soup.select('a.sc-gKsewC')
                        for dataset in datasets[:max_requests_per_source]:
                            title = dataset.get_text().strip()
                            link = f"https://www.kaggle.com{dataset.get('href')}"
                            dataset_entry = f"**Source**: {source} | **Keyword**: `{keyword}` | **Dataset**: [{title}]({link})"
                            self.datasets.append(dataset_entry)
                            st.write(dataset_entry)
                            

                    elif source == "HuggingFace":
                        soup = BeautifulSoup(response.text, 'html.parser')
                        datasets = soup.select('a.card-link')
                        for dataset in datasets[:max_requests_per_source]:
                            title = dataset.get_text().strip()
                            link = f"https://huggingface.co{dataset.get('href')}"
                            dataset_entry = f"**Source**: {source} | **Keyword**: `{keyword}` | **Dataset**: [{title}]({link})"
                            self.datasets.append(dataset_entry)
                            st.write(dataset_entry)

                    print(f"Completed search for {source} with keyword: {keyword}")

                except requests.exceptions.RequestException as e:
                    print(f"Error retrieving data from {source} for keyword '{keyword}': {e}")

                # Sleep to avoid overwhelming the server
                if (i + 1) % max_requests_per_source == 0:
                    print("Sleeping to avoid overwhelming the server...")
                    time.sleep(random.uniform(2, 5))
                else:
                    time.sleep(random.uniform(1, 3))
if industry:
    # Step 1: Fetch industry data
    industry_data = fetch_industry_data(industry)
    st.write("### Industry Overview")
    st.write(industry_data.get('overview', 'No overview available.'))

    # Step 2: Fetch market standards
    market_agent = MarketStandardsAgent(industry)
    market_status = market_agent.fetch_market_standards()
    st.write("### Industry Trends and Standards")
    st.write(market_status)
    st.write("Trends:")
    st.write(market_agent.trends)
    st.write("Standards:")
    st.write(market_agent.standards)

    # Step 3: Generate use cases
    use_case_gen = UseCaseGenerator(market_agent.trends, market_agent.standards)
    use_case_gen.generate_use_cases()
    st.write("### Suggested AI/ML Use Cases")
    st.write(use_case_gen.use_cases)

    # Step 4: Collect resources
    # Collect resources
    keywords = industry_data.get('keywords', [])
    resource_collector = ResourceCollectorUI(industry, use_case_gen.use_cases, keywords, github_token=os.getenv("GITHUB_TOKEN"))
    resource_collector.search_datasets()

    # Display datasets as a Markdown list
    st.write("### Relevant Dataset Resources")
    if resource_collector.datasets:
        for dataset in resource_collector.datasets:
            st.markdown(f"- {dataset}")
    else:
        st.write("No datasets found.")
