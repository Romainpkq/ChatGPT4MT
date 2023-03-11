import openai


openai.api_key = ''

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-0301',
    messages=[
        {"role": "user",
         "content": 'Please provide the [TGT] translation for the following sentence: ' + line,
         }],
    temperature=0
)
