import openai
import argparse

openai.api_key = "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"

p = argparse.ArgumentParser(description="ChatGPT on terminal")
p.add_argument("input", help="Input question")

args = p.parse_args()

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = args.input

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
