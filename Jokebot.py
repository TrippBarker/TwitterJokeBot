import openai

openai.api_key_path = '<OPENAI API KEY PATH GOES HERE>'
model_engine = "text-davinci-003"

def promptGPT(userPrompt):
    indoctronation = "Prompt: You are an AI bot that provides a user with a witty joke when asked for one. If a joke is not asked for, you are to act confused and provide a random joke instead of responding appropriately. Please respond to the following request: " + userPrompt
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = indoctronation,
        max_tokens = 30,
        n = 1,
        stop = None,
        temperature = 1,
    )
    return completion.choices[0].text



print(promptGPT("tell me a joke"))