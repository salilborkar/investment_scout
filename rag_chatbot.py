
#about_sandiego.py

import ollama

# loading the dataset

dataset=[]
with open('about_sandiego.txt','r') as f:
	dataset=f.readlines()
	print(f" {len(dataset)} entries")

#add data to vector db

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

vector_db=[]

#adding data chunks to the vector db

def add_chunks2db(chunk):
	embedding=ollama.embed(model=EMBEDDING_MODEL,input=chunk)['embeddings'][0]
	vector_db.append((chunk,embedding))

for i,chunk in enumerate(dataset):
	add_chunks2db(chunk)
	print(f"{i+1}/{len(dataset)} chunk added")

#find similarity in words

def cosine_similarity(a,b):
	dot_product=sum([x*y for x,y in zip(a,b)])
	normA=sum([x**2 for x in a]) ** 0.5
	normB=sum([x**2 for x in b]) ** 0.5
	return dot_product/(normA*normB)

def retrieve(query,top_n=3):
	query_embedding=ollama.embed(model=EMBEDDING_MODEL,input=query)['embeddings'][0]
	#temporarily store (chunk,similarity) pairs
	similarities=[]

	for chunk,embedding in vector_db:
		similarity=cosine_similarity(query_embedding,embedding)
		similarities.append((chunk,similarity))
	#sorting similarity in descending order - higher similarity mean more chunks that are relevant
	similarities.sort(key=lambda x:x[1],reverse=True)
	#return top n similar chunks
	return similarities[:top_n]

#chatbot

input_query=input('Ask me a question about San Diego: ')
retrieved_kb=retrieve(input_query)
print('Retrieved knowledge: ')
for chunk, similarity in retrieved_kb:
	print(f' - (similarity: {similarity:.2f}) {chunk}')

instruction_prompt = f'''use the following pieces of context to answer the question only {'\n'.join([f' - {chunk}' for chunk,similarity in retrieved_kb])}'''

print(f" instruction prompt: {instruction_prompt}")

stream=ollama.chat(model=LANGUAGE_MODEL,messages=[
	{'role':'system','content': instruction_prompt},
	{'role':'system','content': input_query},
	],
	stream=True,
	)
#printing the response from chatbot in real-time
print('Chatbot response: ')
for chunk in stream:
	print(chunk['message']['content'],end='',flush=True)
