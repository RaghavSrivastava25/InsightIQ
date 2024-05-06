# InsightIQ

# InsightIQ Bot - Financial Insights from SEC Filings Using RAG

Welcome to InsightIQ Bot! This repository contains a sophisticated bot designed to analyze and extract insights from 10K filings, providing users with valuable information about a company's financial performance, strategies, risks, and more.

## Overview

InsightIQ Bot is an AI-powered tool that uses RAG to analyze large financial documents like 10K filings. It offers an intuitive interface for users to interact with the bot and ask questions, generating insights and summaries from the data. The bot can handle complex queries and is designed to be both user-friendly and efficient.

## Features

- **Automated Analysis**: InsightIQ Bot can process and analyze 10K filings to extract key insights.
- **Interactive Interface**: Users can interact with the bot through a simple chat-based interface.
- **Natural Language Processing**: The bot uses advanced NLP techniques to understand and respond to user queries.
- **Customizable**: The bot's responses and behavior can be customized to suit specific needs.
- **Open Source**: This project is open source, allowing developers to contribute and extend its capabilities.


## What I've Done

- **Data Collection**: Using the `sec-edgar-downloader` Python library, we downloaded SEC filings for Apple, Google, and Microsoft from 1995 to 2023. These filings were organized into corresponding folders and saved for further processing.
  
- **Data Preparation**: Given the large size of the SEC filings (some reaching 14 MB), we split them into 50 smaller text files to facilitate processing. This step ensured we could handle the data efficiently without encountering rate limit errors.
  
- **Vector Database Creation**: Using OpenAI GPT embeddings, we implemented Retrieval Augmented Generation (RAG) to extract relevant information from the filings. Each of the 50 smaller text files was converted into embeddings and stored in a vector database using ChromaDB.
  
- **Query Retrieval and Similarity Search**: The embeddings in the vector database allow for similarity-based search and retrieval. This capability enables the retrieval of specific information from the filings based on user queries.
  
- **Gradio Web App**: To create a user-friendly interface, we deployed a chat agent through a Gradio-based web application. This app allows users to interact with the data and ask questions, receiving relevant insights in response.

## How It Works

The project uses OpenAI GPT embeddings to generate vector representations of the SEC filings. When a user asks a question, the chat agent performs a similarity search in the vector database to retrieve relevant information. This approach enables efficient and accurate retrieval of insights from the large dataset of SEC filings.

## Deployment

To deploy the project and start using the chat agent, follow these steps:

1. Clone this repository to your local environment.
2. Install the necessary dependencies as outlined in `requirements.txt`.
3. Launch the Gradio-based web app to interact with the chat agent.
4. Ask questions and explore the insights derived from the SEC filings.

## Contributions and Feedback

Contributions to the project are welcome! If you have suggestions for improvements or would like to contribute code, please open a pull request or submit an issue. We're open to feedback and look forward to enhancing the project's capabilities.

## License and Contact

This project is licensed under the MIT License. For more information, please refer to the `LICENSE` file. If you have any questions or need assistance, please reach out through the project's GitHub issues page.

Thank you for exploring this project! We hope you find it useful for extracting insights from SEC filings.


## Demo Video 

https://www.veed.io/view/35d198e9-8351-4ff1-9cca-9138c6daa7ca?panel=share
