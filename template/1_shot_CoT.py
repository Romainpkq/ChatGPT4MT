import openai


openai.api_key = ''

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-0301',
    messages=[
        {"role": "system", "content": "You are a machine translation system."},
        {"role": "user",
         "content": 'Please provide the German translation for the following sentence step by step and then provide the complete sentence: '
                    'That said, expect to be out of breath, and take care in the steeper portions, '
                    'especially when wet, as it can become dangerous quickly.\n'
                    '1. That said - 据说 2. expect - 据说 3. to be - 会 4. out of breath - 喘不过气来 5. and - 还有 6. take care - 小心谨慎 '
                    '7. in the steeper portions - 在陡峭的地方 8. especially - 特别 9. when wet - 天气潮湿的时候 10. become - 变得 11. dangerous - 危险 12. quickly - 很快 '
                    'The complete sentence in Chinese is: 据说会让人喘不过气来，还有在陡峭的地方要小心谨慎，特别是天气潮湿时，情况有可能很快变得很危险。\n'
                    'Please provide the German translation for the following sentence step by step and '
                    'then provide the complete sentence: ' + line},
    ],
    temperature=0
)