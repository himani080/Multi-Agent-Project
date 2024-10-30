from industry_research_agent import fetch_industry_data
from resource_collection_agent import ResourceCollector
import requests
from bs4 import BeautifulSoup
import cohere
from dotenv import load_dotenv
import os
load_dotenv()


# Initialize Cohere with your API key
cohere_api_key = os.getenv("COHERE_API_KEY")  # Replace with your actual API key
cohere_client = cohere.Client(cohere_api_key)

def print_industry_data(industry_info):
    print("\nIndustry Overview:")
    print(industry_info.get('overview', 'No overview found.'))

    print("\nKey Offerings:")
    for offering in industry_info.get('key_offerings', []):
        print(f"- {offering}")

    print("\nStrategic Focus Areas:")
    for focus in industry_info.get('strategic_focus', []):
        print(f"- {focus}")

class MarketStandardsAgent:
    def __init__(self, industry):
        self.industry = industry
        self.trends = []
        self.standards = []

    def fetch_market_standards(self):
        try:
            # Example URL for industry trends & standards
            url = f"https://example.com/industry/{self.industry.lower()}/trends-standards"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Parse trends and standards (customize as per actual data source)
            self.trends = [trend.get_text() for trend in soup.select(".trend-class")]
            self.standards = [standard.get_text() for standard in soup.select(".standard-class")]

            print("Trends and Standards Retrieved Successfully.")
        
        except Exception as e:
            print(f"Error fetching market standards: {e}")

    def analyze_trends(self):
        analysis = f"Industry Trends for {self.industry}:\n"
        for trend in self.trends:
            analysis += f"- {trend}\n"
        return analysis

    def analyze_standards(self):
        standards_analysis = f"Industry Standards for {self.industry}:\n"
        for standard in self.standards:
            standards_analysis += f"- {standard}\n"
        return standards_analysis


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
                model="command-xlarge",  # Updated model name
                prompt=prompt,
                max_tokens=500,
                temperature=0.7,
                stop_sequences=["--end--"]
            )
            self.use_cases = response.generations[0].text.strip().split('\n')
        
        except Exception as e:
            print(f"Error generating use cases: {e}")

    def display_use_cases(self):
        print("Suggested AI/ML Use Cases:")
        for case in self.use_cases:
            print(f"- {case}")


if __name__ == "__main__":
    # Industry input
    industry = input("Enter the industry (e.g., Automotive, Healthcare, Finance, etc.): ")

    # Fetch and display industry data
    industry_data = fetch_industry_data(industry)
    print_industry_data(industry_data)

    # Get relevant keywords for the industry
    keywords = industry_data.get('keywords', ["default", "keywords"])  # Default keywords if none found

    # Define general use cases for any industry
    use_cases = [
        f"{industry} Decision Support",
        f"Predictive Analytics and Operations Optimization in {industry}",
        f"R&D Enhancement in {industry}",
        "Chatbots and Virtual Assistants",
        f"Risk Assessment and Management in {industry}",
        "Data Analysis and Monitoring",
        "Personalized Services and Customer Support",
        "Fraud Detection and Cybersecurity"
    ]

    # Collect resources and propose bonus solutions
    github_token = os.getenv("GITHUB_TOKEN")  # Replace with your actual GitHub token
    collector = ResourceCollector(industry, use_cases, keywords, github_token=github_token)
    collector.search_datasets()
    collector.propose_bonus_solutions()
    collector.save_to_markdown(filename=f"{industry}_Resource_Assets.md")

    print(f"{industry} Resource Assets saved to '{industry}_Resource_Assets.md'.")

    # Step 1: Fetch and analyze trends & standards
    market_agent = MarketStandardsAgent(industry)
    market_agent.fetch_market_standards()
    industry_trends = market_agent.analyze_trends()
    industry_standards = market_agent.analyze_standards()

    # Step 2: Generate relevant use cases based on trends and standards
    use_case_generator = UseCaseGenerator(industry_trends, industry_standards)
    use_case_generator.generate_use_cases()
    
    # Step 3: Display the suggested use cases
    use_case_generator.display_use_cases()
