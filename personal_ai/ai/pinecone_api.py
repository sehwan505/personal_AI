import openai
import pinecone

openai.api_key = "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"

PINECONE_API_KEY = 'a838ce6a-684a-4779-bf9a-fbdbf2096f91'
PINECONE_API_ENV = 'northamerica-northeast1-gcp'


def loading_previous_answers(prompt: str):
    index_name = 'gpt-answers'
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
    response = index.query(query_embeds, top_k=5, include_metadata=True)
    contexts = [item['metadata']['text'] for item in response['matches']]
    augmented_query = "\n\n---\n\n".join(contexts)+"\n\n-----\n\n"+prompt

    return augmented_query