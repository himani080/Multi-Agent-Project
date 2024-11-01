# # import requests
# # from bs4 import BeautifulSoup

# # def fetch_industry_data(industry):
# #     industry_info = {}

# #     # Define Wikipedia URLs for known industries
# #     urls = {
# #         'healthcare': "https://en.wikipedia.org/wiki/Healthcare",
# #         'automotive': "https://en.wikipedia.org/wiki/Automotive_industry",
# #         'finance': "https://en.wikipedia.org/wiki/Finance",
# #         'manufacturing': "https://en.wikipedia.org/wiki/Manufacturing",
# #         'retail': "https://en.wikipedia.org/wiki/Retail"
# #     }

# #     # Attempt to fetch industry data
# #     overview_url = urls.get(industry.lower())
    
# #     if overview_url:
# #         try:
# #             headers = {
# #                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# #             }
# #             response = requests.get(overview_url, headers=headers)
# #             response.raise_for_status()

# #             soup = BeautifulSoup(response.text, 'html.parser')

# #             # Extracting the industry overview
# #             paragraphs = soup.find('div', class_='mw-parser-output').find_all('p')
# #             industry_info['overview'] = ' '.join([para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True)])

# #             # General extraction for offerings and focus areas
# #             industry_info['key_offerings'] = []
# #             industry_info['strategic_focus'] = []

# #             # Find all headers to locate relevant sections
# #             headers = soup.find_all(['h2', 'h3'])
# #             capturing_offerings = False
# #             capturing_focus = False

# #             for header in headers:
# #                 header_text = header.get_text(strip=True).lower()
                
# #                 # Detect if we are in the offerings or focus areas section
# #                 if 'key offerings' in header_text or 'offerings' in header_text:
# #                     capturing_offerings = True
# #                     capturing_focus = False
# #                 elif 'strategic focus' in header_text or 'focus' in header_text:
# #                     capturing_focus = True
# #                     capturing_offerings = False
# #                 else:
# #                     capturing_offerings = capturing_focus = False
                
# #                 # Extracting list items if capturing is active
# #                 next_sibling = header.find_next_sibling()
# #                 while next_sibling:
# #                     if next_sibling.name == 'ul':
# #                         if capturing_offerings:
# #                             industry_info['key_offerings'] += [li.get_text(strip=True) for li in next_sibling.find_all('li')]
# #                         if capturing_focus:
# #                             industry_info['strategic_focus'] += [li.get_text(strip=True) for li in next_sibling.find_all('li')]
# #                         break
# #                     elif next_sibling.name in ['h2', 'h3']:
# #                         break  # Stop capturing when hitting another header
# #                     next_sibling = next_sibling.find_next_sibling()

# #             # If no offerings or focus found, try to get all list items on the page
# #             if not industry_info['key_offerings']:
# #                 all_lists = soup.find_all('ul')
# #                 for ul in all_lists:
# #                     items = [li.get_text(strip=True) for li in ul.find_all('li')]
# #                     if items:
# #                         industry_info['key_offerings'].extend(items)

# #             if not industry_info['strategic_focus']:
# #                 all_lists = soup.find_all('ul')
# #                 for ul in all_lists:
# #                     items = [li.get_text(strip=True) for li in ul.find_all('li')]
# #                     if items:
# #                         industry_info['strategic_focus'].extend(items)

# #         except Exception as e:
# #             print(f"Error fetching data from {overview_url}: {e}")
# #             industry_info['overview'] = "Failed to retrieve overview."
# #             industry_info['key_offerings'] = ["Failed to retrieve offerings."]
# #             industry_info['strategic_focus'] = ["Failed to retrieve focus areas."]
# #     else:
# #         industry_info['overview'] = "No overview found for this industry."
# #         industry_info['key_offerings'] = ["No offerings found for this industry."]
# #         industry_info['strategic_focus'] = ["No focus areas found for this industry."]

# #     return industry_info

# import requests
# from bs4 import BeautifulSoup

# def fetch_industry_data(industry):
#     industry_info = {}

#     # Define Wikipedia URLs for known industries
#     urls = {
#         'healthcare': "https://en.wikipedia.org/wiki/Healthcare",
#         'automotive': "https://en.wikipedia.org/wiki/Automotive_industry",
#         'finance': "https://en.wikipedia.org/wiki/Finance",
#         'manufacturing': "https://en.wikipedia.org/wiki/Manufacturing",
#         'retail': "https://en.wikipedia.org/wiki/Retail"
#     }

#     # Attempt to fetch industry data
#     overview_url = urls.get(industry.lower())
    
#     if overview_url:
#         try:
#             headers = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
#             }
#             response = requests.get(overview_url, headers=headers)
#             response.raise_for_status()

#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Extracting the industry overview
#             paragraphs = soup.find('div', class_='mw-parser-output').find_all('p')
#             industry_info['overview'] = ' '.join([para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True)])

#             # Initialize lists for key offerings and strategic focus
#             industry_info['key_offerings'] = []
#             industry_info['strategic_focus'] = []

#             # Find all list items in the content
#             all_lists = soup.find_all('ul')
#             for ul in all_lists:
#                 items = [li.get_text(strip=True) for li in ul.find_all('li')]
#                 for item in items:
#                     # Basic keyword detection for offerings and focus areas
#                     if any(keyword in item.lower() for keyword in [
#                         'vehicle', 'service', 'manufacturing', 'technology', 'innovation', 
#                         'sustainability', 'electric', 'autonomous', 'safety', 'mobility']):
#                         industry_info['key_offerings'].append(item)

#                     if any(keyword in item.lower() for keyword in [
#                         'focus', 'strategy', 'customer', 'partnership', 'experience', 
#                         'global', 'expansion', 'cost', 'regulatory']):
#                         industry_info['strategic_focus'].append(item)

#             # Provide fallback messages if no offerings or focus found
#             if not industry_info['key_offerings']:
#                 industry_info['key_offerings'].append("No specific offerings found.")

#             if not industry_info['strategic_focus']:
#                 industry_info['strategic_focus'].append("No specific focus areas found.")

#         except requests.RequestException as e:
#             industry_info['overview'] = "Failed to retrieve overview."
#             industry_info['key_offerings'] = ["Failed to retrieve offerings."]
#             industry_info['strategic_focus'] = ["Failed to retrieve focus areas."]
#             print(f"Request error: {e}")
#         except Exception as e:
#             industry_info['overview'] = "Failed to retrieve overview due to an unexpected error."
#             industry_info['key_offerings'] = ["Failed to retrieve offerings due to an unexpected error."]
#             industry_info['strategic_focus'] = ["Failed to retrieve focus areas due to an unexpected error."]
#             print(f"Unexpected error: {e}")
#     else:
#         industry_info['overview'] = "No overview found for this industry."
#         industry_info['key_offerings'] = ["No offerings found for this industry."]
#         industry_info['strategic_focus'] = ["No focus areas found for this industry."]

#     return industry_info

# # Example usage
# automotive_data = fetch_industry_data('automotive')
# print(automotive_data)

import requests
from bs4 import BeautifulSoup

def fetch_industry_data(industry):
    industry_info = {}

    # Define Wikipedia URLs for known industries
    urls = {
        'healthcare': "https://en.wikipedia.org/wiki/Healthcare",
        'automotive': "https://en.wikipedia.org/wiki/Automotive_industry",
        'finance': "https://en.wikipedia.org/wiki/Finance",
        'manufacturing': "https://en.wikipedia.org/wiki/Manufacturing",
        'retail': "https://en.wikipedia.org/wiki/Retail"
    }

    # Attempt to fetch industry data
    overview_url = urls.get(industry.lower())
    
    if overview_url:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            response = requests.get(overview_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Extracting the industry overview
            paragraphs = soup.find('div', class_='mw-parser-output').find_all('p')
            industry_info['overview'] = ' '.join([para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True)])

            # Initialize lists for key offerings and strategic focus
            industry_info['key_offerings'] = []
            industry_info['strategic_focus'] = []

            # Find all list items in the content
            all_lists = soup.find_all('ul')
            for ul in all_lists:
                items = [li.get_text(strip=True) for li in ul.find_all('li')]
                for item in items:
                    # Use the industry name to check for relevant offerings and focus areas
                    if industry.lower() in item.lower():
                        industry_info['key_offerings'].append(item)

                    if any(keyword in item.lower() for keyword in [
                        'focus', 'strategy', 'customer', 'partnership', 'experience', 
                        'global', 'expansion', 'cost', 'regulatory']):
                        industry_info['strategic_focus'].append(item)

            # Provide fallback messages if no offerings or focus found
            if not industry_info['key_offerings']:
                industry_info['key_offerings'].append("No specific offerings found.")

            if not industry_info['strategic_focus']:
                industry_info['strategic_focus'].append("No specific focus areas found.")

        except requests.RequestException as e:
            industry_info['overview'] = "Failed to retrieve overview."
            industry_info['key_offerings'] = ["Failed to retrieve offerings."]
            industry_info['strategic_focus'] = ["Failed to retrieve focus areas."]
            print(f"Request error: {e}")
        except Exception as e:
            industry_info['overview'] = "Failed to retrieve overview due to an unexpected error."
            industry_info['key_offerings'] = ["Failed to retrieve offerings due to an unexpected error."]
            industry_info['strategic_focus'] = ["Failed to retrieve focus areas due to an unexpected error."]
            print(f"Unexpected error: {e}")
    else:
        industry_info['overview'] = "No overview found for this industry."
        industry_info['key_offerings'] = ["No offerings found for this industry."]
        industry_info['strategic_focus'] = ["No focus areas found for this industry."]

    return industry_info

# # Example usage
# if __name__ == "__main__":
#     industry_input = input("Enter the industry (e.g., Healthcare, Automotive, Finance, etc.): ")
#     industry_data = fetch_industry_data(industry_input)
#     print(industry_data)
