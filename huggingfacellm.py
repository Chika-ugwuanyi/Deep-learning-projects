from langchain_classic.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

# Load document
loader = TextLoader("webpages_text.txt", encoding="utf-8")
documents = loader.load()

# Split document
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
texts = text_splitter.split_documents(documents)

# Create Hugging Face embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
docsearch = Chroma.from_documents(
    documents=texts,
    embedding=embeddings
)

# Create Hugging Face model
llm = HuggingFacePipeline.from_model_id(
    model_id="distilgpt2",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "temperature":0.7
        
    }
)

# Create Retrieval QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever()
)

# Ask question
query = "What is the cost of your data science course?"
response = qa.invoke({"query": query})

print(response["result"])