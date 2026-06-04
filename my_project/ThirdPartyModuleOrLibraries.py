# Java Maven:
# <dependency>groupId/artifactId/version</dependency>

# Before using we need to install the packages using Python pip:
# pip install requests            # HTTP library
# pip install pandas              # Data analysis
# pip install numpy               # Numerical computing
# pip install langchain           # LangChain for AI (you know this!)
# pip install spring-ai           # (hypothetical)



# After installing, just import and use!
import requests

response = requests.get("https://api.github.com")
print(response.status_code)     # 200
print(response.json())          # Print the JSON response