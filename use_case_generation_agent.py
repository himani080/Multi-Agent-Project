import requests
from bs4 import BeautifulSoup
import cohere

# Initialize Cohere with your API key
cohere_api_key = "7ahNpMhTSQe6lSRAe2SGmpwXmT6weZkqiHQ2ULeV"
cohere_client = cohere.Client(cohere_api_key)

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


# Main Program
if __name__ == "__main__":
    industry = input("Enter the industry (e.g., Automotive, Healthcare): ")
    market_agent = MarketStandardsAgent(industry)
    
    # Step 1: Fetch and analyze trends & standards
    market_agent.fetch_market_standards()
    industry_trends = market_agent.analyze_trends()
    industry_standards = market_agent.analyze_standards()

    print(industry_trends)
    print(industry_standards)

    # Step 2: Generate and display relevant use cases
    use_case_generator = UseCaseGenerator(industry_trends, industry_standards)
    use_case_generator.generate_use_cases()
    use_case_generator.display_use_cases()
