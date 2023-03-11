import openai


openai.api_key = ''

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-0301',
    messages=[
        {"role": "system", "content": "You are a machine translation system that "
                                      "translates sentences in the [DOM] domain."},
        {"role": "user",
         "content": 'Please provide the [TGT] translation for the following sentence: ' + line,
         }],
    temperature=0
)

print(completion.choices[0]["message"]["content"])