import openai
import pinecone
from util import config
import uuid


openai.api_key = config["OPENAI_KEY"]
PINECONE_API_KEY = config["PINECONE_KEY"]
PINECONE_API_ENV = config["PINECONE_ENV"]


def appending_shots(prompt: str):
    index_name = 'gpt-answers-index'
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=1536, metric='dotproduct')

    index = pinecone.Index(index_name)

    embed_model = "text-embedding-ada-002"
    user_input = "What is deep q learning?"

    embed_query = openai.Embedding.create(
        input=user_input,
        engine=embed_model
    )
    query_embeds = embed_query['data'][0]['embedding']
    response = index.query(query_embeds, top_k=5, include_metadata=True, namespace='langchain-namespace')
    print(response)
    contexts = [f"context:{item['metadata']['text']}\n" for item in response['matches']]
    augmented_query = "\n\n---\n\n".join(contexts)+"\n\n-----\n\n"+prompt
    print(augmented_query)

    return augmented_query

def add_vector(text: str):
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
    index = pinecone.Index('gpt-answers-index')
    
    vectors = [{
                "id": str(uuid.uuid4()),
                "values":get_openai_embedding(text),
                "metadata":{'text': text}
            }]
    
    upsert_response = index.upsert(
        vectors=vectors,
        namespace='langchain-namespace'
    )

def get_openai_embedding(text: str):
    embed_model = "text-embedding-ada-002"
    embed = openai.Embedding.create(
        input=text,
        engine=embed_model
    )
    embeds = embed['data'][0]['embedding']

    if embeds:
        return embeds
    else:
        raise Exception("Request failed with status code: there is no embeds")