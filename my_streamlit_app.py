from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI
from langchain.chains import (
    StuffDocumentsChain, LLMChain, ConversationalRetrievalChain
)
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
import langchain_openai
from langchain.agents.agent_types import AgentType
import langchain_experimental.agents.agent_toolkits
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI
import os
import argparse       
import time  
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA                
from langchain.document_loaders import TextLoader    
from langchain.text_splitter import CharacterTextSplitter 
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import gradio as gr
import glob
import tqdm
from tqdm import tqdm 
from langchain.callbacks.manager import CallbackManager
from langchain import PromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import create_vectorstore_agent
from langchain.agents.agent_toolkits import VectorStoreToolkit
from langchain.agents.agent_toolkits import VectorStoreInfo


os.environ['OPENAI_API_KEY'] = 'xxxxx'  





import os
import glob

large_text_file_path = '/Users/raghavsrivastava/Desktop/full-submission.txt'

output_folder = 'split_files'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
num_chunks = 50  

with open(large_text_file_path, 'r', encoding='utf-8') as file:
    large_text = file.read()

chunk_size = len(large_text) // num_chunks
for i in range(num_chunks):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_chunks - 1 else len(large_text)
    chunk = large_text[start:end]
    part_path = f'{output_folder}/part_{i + 1}.txt'
    with open(part_path, 'w', encoding='utf-8') as part_file:
        part_file.write(chunk)



llm = ChatOpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()

split_folder = 'split_files'
split_files = sorted(glob.glob(f'{split_folder}/*.txt'))[:1]  # Using one file for simplicity
documents = []

# Process the smaller chunks with longer delays to avoid rate limit errors
for part_path in split_files:
    loader = TextLoader(part_path)  # Load the text file
    docs = loader.load_and_split()  # Load and split into document objects
    documents.extend(docs)  # Add to the list of documents
    
    # Add a longer delay between batches to avoid rate limit errors
    time.sleep(30)  # Adjust delay based on rate limit considerations

# Create a vector store from the documents
store = Chroma.from_documents(documents, embeddings, collection_name='sec_filings')

# Create the VectorStoreInfo object
vectorstore_info = VectorStoreInfo(
    name="sec_filings",
    description="A collection of smaller text files from a large 10-K filing",
    vectorstore=store
)

# Create the toolkit from the vectorstore info
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info, llm=llm)

# Create the agent executor
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# Define the chatbot function to run the agent executor
def sec_filing_agent(prompt):
    response = agent_executor.run(prompt)
    return response

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# 🦜🔗 GPT-Based SEC Filing Agent")
    
    with gr.Row():
        # Textbox for user query
        text_input = gr.Textbox(label="Enter your query here", placeholder="Ask anything about the SEC filings")
        
        # Button to submit the query
        submit_btn = gr.Button("Submit")
    
    # Create a chatbot interface to show the response
    chatbot = gr.Chatbot(label="Agent Response")
    
    # Define the submit action to run the agent and update the chatbot
    submit_btn.click(sec_filing_agent, inputs=[text_input], outputs=[chatbot])

# Launch the Gradio application
demo.launch(debug=True, share=True)




