import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required resources from NLTK
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Define a function for preprocessing a single document
def preprocess_document(text_content):
    # Lowercase the text
    text_content = text_content.lower()

    
    # Tokenize the text
    tokens = word_tokenize(text_content)
    
    # Remove stopwords and non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    
    # Optional: Stem the tokens
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens

# Define a function to process all documents in a directory
def preprocess_documents(directory_path):
    preprocessed_corpus = {}
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    extracted_text = ' '.join(re.findall(r'<TEXT>(.*?)</TEXT>', content, re.DOTALL))
                   
                    if extracted_text:
                        processed_tokens = preprocess_document(extracted_text)
                        preprocessed_corpus[filename] = processed_tokens
                        
                    else:
                        print(f"No <TEXT> tags found in file: {filename}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    
    return preprocessed_corpus

def preprocess_documents_head(directory_path, include_head=False):
    preprocessed_corpus = {}
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    # Extract DOCNO
                    docno = re.search(r'<DOCNO>(.*?)</DOCNO>', content, re.DOTALL)
                    if docno:
                        docno = docno.group(1).strip()

                    # Extract and optionally include HEAD field
                    extracted_text = ' '.join(re.findall(r'<TEXT>(.*?)</TEXT>', content, re.DOTALL))
                    if include_head:
                        extracted_head = ' '.join(re.findall(r'<HEAD>(.*?)</HEAD>', content, re.DOTALL))
                        extracted_text = extracted_head + ' ' + extracted_text

                    if extracted_text:
                        processed_tokens = preprocess_document(extracted_text)
                        preprocessed_corpus[docno] = processed_tokens
                    else:
                        print(f"No <TEXT> or <HEAD> tags found in file: {filename}")
                        
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    
    return preprocessed_corpus

def test():

    directory_path = r'C:\Users\narme\Documents\Winter 2024 Courses\InformationRetrieval\assign1\AP_collection\coll'

    # Preprocess all documents in the specified directory
    corpus = preprocess_documents(directory_path)

    # For demonstration purposes, print the tokens of the first document
    first_doc_tokens = next(iter(corpus.values()))
    print(first_doc_tokens)


