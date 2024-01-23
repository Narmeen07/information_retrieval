from collections import defaultdict

def build_inverted_index(corpus):
    '''
    Uses a default dict for fast processing of tokens

    '''
    inverted_index = defaultdict(set)

    for doc_id, tokens in corpus.items():
        try:
            for token in tokens:
                inverted_index[token].add(doc_id)
        except Exception as e:
            print(f"Error processing document {doc_id}: {e}")

    # Convert sets to lists for the final output, if required
    for token in inverted_index:
        inverted_index[token] = list(inverted_index[token])

    return inverted_index

'''
def build_inverted_index(corpus):
    inverted_index = {}

    for doc_id, tokens in corpus.items():
        try:
            for token in tokens:
                if token not in inverted_index:
                    inverted_index[token] = set()
                inverted_index[token].add(doc_id)
        except Exception as e:
            print(f"Error processing document {doc_id}: {e}")

    for token in inverted_index:
        inverted_index[token] = list(inverted_index[token])

    return inverted_index
'''
def print_first_few_entries(inverted_index, limit=5):
    for i, (token, doc_ids) in enumerate(inverted_index.items()):
        print(f"Token: {token}, Document IDs: {doc_ids}")
        if i >= limit - 1:
            break

