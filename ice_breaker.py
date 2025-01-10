from dotenv import load_dotenv
import os

from langchain import PromptTemplate
from langchain_openai import ChatOpenAI

information = """Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman known for his key roles in the space company SpaceX and the automotive company Tesla, Inc. He is also known for his ownership of X Corp. (the company that operates the social media platform X, formerly Twitter), and his role in the founding of the Boring Company, xAI, Neuralink, and OpenAI. Musk is the wealthiest individual in the world; as of January 2025, Forbes estimates his net worth to be US$421 billion.[2]

A member of the wealthy South African Musk family, Musk was born in Pretoria and briefly attended the University of Pretoria. At the age of 18 he immigrated to Canada, acquiring its citizenship through his Canadian-born mother, Maye. Two years later, he matriculated at Queen's University in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University but never enrolled in classes, and with his brother Kimbal co-founded the online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In 2002, Musk acquired United States citizenship, and that October eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.
"""

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain!")

    summary_template = """
    given information {information} about a person from I want to you to create:
    1. a short summarry
    2. two interesting facts about them
    """

    summary_prompt_template =  PromptTemplate(input_variables="information", template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)
