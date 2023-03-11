import openai


openai.api_key = ''

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-0301',
    messages=[
        {"role": "system", "content": "You are a machine translation system."},
        {"role": "user",
         "content": '[SRC]: [S_1] [TGT]: [T_1]\n'
                    '[SRC]: [S_2] [TGT]: [T_2]\n'
                    '[SRC]: [S_3] [TGT]: [T_3]\n'
                    '[SRC]: ' + line + ' [TGT]: ',
         }],
    temperature=0
)

print(completion.choices[0]["message"]["content"])