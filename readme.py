import ollama

def readme(content):
    response = ollama.chat(model='llama3', messages=[
        {
        'role': 'system',
        'content': 'You will be provided with one (or multiple) coding script(s) and your goal will be to write a short text (a few lines) to explain the potential use cases of this project (not use of individual files but of the project as a whole) and why it is useful.' 
        },
        {
        'role': 'user',
        'content': content
        }, 
    ])
    rme = response['message']['content']
    return(rme)