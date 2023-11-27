# Welcome MADS Students to the Chat With U.S. Chronic Disease Data Project 🚀

## Introduction
Welcome to the repository! 🤖 In this GitHub, we embark on a journey to create chatbots powered by Large Language Models, specifically the GPT-4 model, using the Gradio library interface. The main goal of this project is to engage in what we term "Chat With Data." The innovation of GPTs has helped businesses think outside the box in developing chatbots based on their own data, powered by LLMs. This approach is undoubtedly superior to creating a basic NLP solution. The evolution of LLMs has significantly contributed to the fields of Data Science, Machine Learning, and Software Development. Industries should start leveraging such models to empower their domains. Our dataset, sourced from CDC's Division of Population Health, provides a comprehensive set of 124 indicators, enabling uniform definition, collection, and reporting of chronic disease data. Feel free to use any data you prefer for chatting, experiment with parameters and functions to achieve the optimal solution, and enjoy conversing with your data.

### Dataset Overview
The dataset is structured with 124 indicators in the column ["Questions"], classified under 17 health topics. Each question is answered across various Stratification categories and data value types. The dataset, in long format, covers state and national levels from 2008 to 2020, with some values presented as averages over a range of years, as indicated in the YearStart and YearEnd columns.

Data Source: https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi

## Getting Started

### 1. Download the GitHub Code
Clone or download the GitHub code to your local machine. 📥

### 2. Data Loading & Preprocessing
Open the "Data Loading & Preprocessing" notebook and run the provided notebook. This step ensures that the dataset is loaded correctly.

### 3. Explore Different Approaches
Explore different approaches in the provided notebooks. Run the requirements.txt file to install necessary libraries and dependencies. In the notebook, add your OpenAI/AzureOpenAI API credentials as needed. 🧠

#### - PandasAgentLangChainChatbot
This notebook demonstrates how to use agents to interact with a Pandas DataFrame, optimized for question answering. The PandasAgent reads the dataframe, executes Python code, and provides answers in a chat format using the Gradio Chatbot Interface.

You can check its documentation here: https://python.langchain.com/docs/integrations/toolkits/pandas

Chatbot Sample:
![Alt text](PandasAgentLangChainChatbot/Screenshot1.PNG)

#### - Retrieval Augmented Generation (RAG) using LangChain
Explore challenges with RAG and its optimal use with text data rather than a simple dataframe. Interact with the Chronic disease data using the RAG-LangChain file and Gradio interface.

Here is how RAG works (source: https://blog.langchain.dev/espilla-x-langchain-retrieval-augmented-generation-rag-in-llm-powered-question-answering-pipelines/)
![Alt text](RAG-Langchain/ExplainRAG.png)

You can check its documentation here: https://python.langchain.com/docs/use_cases/question_answering/

#### - LamaIndex Approach
Discover an alternative approach using GPT-4, initializing the LamaIndex agent, and prompting the GPT for answers. Similar to PandasAgent, it involves coding and returns answers.

### 4. Evaluation
Compare different approaches with evaluation questions provided in the evaluation notebook. Evaluate answers obtained by each method and assess their performance.

## Conclusion
This repository introduces new approaches, showcasing the power of Large Language Models (GPT-4) in enabling dynamic interactions with your data. There's room for further development, such as finetuning function parameters, creating custom agents, improving evaluation methods, and enhancing dataset preprocessing.

Enjoy exploring the possibilities and happy coding! 🎉
