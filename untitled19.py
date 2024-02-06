pip install sentence-transformers



pip install faiss-cpu

from langchain.document_loaders import PyPDFLoader

from langchain.text_splitter import CharacterTextSplitter

import os

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub



def loading_dataKnowledge():
    ############################### RAG GETTING ANSWERS FROM KNOWLEDGEBASE ##############################################
    ###############################LOADING DOCUMENT IN DB AND MAKING IT TO VECTOR########################################
    loader = PyPDFLoader("/content/caseD.pdf")
    # loader = PyPDFLoader("/content/The-Field-Guide-to-Data-Science.pdf")
    # !gdown "https://drive.google.com/uc?id=15hUEJQViQDxu_fnJeO_Og1hGqykCmJut&confirm=t"
    data = loader.load()
    documents=data
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    ######################################################################################################################

    ###################################LOADING LOCALY STORD DB############################################################
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
    embeddings = HuggingFaceEmbeddings()
    # db =FAISS.load_local("/content/drive/MyDrive/intel hackathon/db", embeddings)
    db =FAISS.from_documents(docs, embeddings)

    llm=HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta", model_kwargs={"temperature":0.7, "max_length":512}) #USEING ZEPHUR FOR GETING DOMINE KNOWLEDGE WITH TRAINED DATA
    chain = load_qa_chain(llm, chain_type="stuff")
    return db,chain

def response(msg,db):
    docs = db.similarity_search(msg)

    return docs

msg="what is the evidence in the case"+" ? give only relevent answers from documents'"
db,chain=loading_dataKnowledge()

bot_response =chain.run(input_documents=response(msg,db) , question= msg)
print(bot_response)

start_index = bot_response.find("Helpful Answer:")
# print(start_index)
if start_index != -1:
    # Extract the substring after "Helpful Answer:"
    relevant_info = bot_response[start_index + len("Helpful Answer:"):].strip()
    print(relevant_info)
else:
    print("No relevant information found.")
