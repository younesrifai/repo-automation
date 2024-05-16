import ollama

def desc(content):
    response = ollama.chat(model='llama3', messages=[
        {
        'role': 'system',
        'content': 'You will be provided with a python script and your goal will be to summarize in one sentence what it does.' 
        },
        {
        'role': 'user',
        'content': content
        }, 
    ])
    description = response['message']['content']
    return(description)