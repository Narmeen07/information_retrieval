from preprocessing import preprocess_documents_head
from indexing import build_inverted_index, print_first_few_entries

def main():
    # Specify the directory containing your documents
    # Use a raw string for the path to handle backslashes appropriately
    directory_path = r'C:\Users\narme\Documents\Winter 2024 Courses\InformationRetrieval\assign1\AP_collection\coll'

    corpus = preprocess_documents_head(directory_path, include_head=True)
    first_doc_tokens = next(iter(corpus.values()))
    #print(first_doc_tokens)

    #Build the inverted index
    inverted_index = build_inverted_index(corpus)
    print_first_few_entries(inverted_index)

    # Further processing or saving the index to a file, etc.
    # ...

if __name__ == "__main__":
    main()