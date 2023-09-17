import openai
import pandas as pd
from csv import writer

with open("apiKey.txt") as f:
    lines = f.read().splitlines()

openai.api_key = lines[0]

dataFrame = pd.read_csv("questions_new.csv")
# dataFrame.drop(["rating", "date", "variation"], axis=1)

model_engine = "text-davinci-003"

with open('answers_new.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(["answers"])
    f_object.close()

count = 0
for row in dataFrame["questions"]:
    # Set up the model and prompt
    responseList = []
    prompt = f'{row}'
    print(prompt)

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text.split("\n\n")
    # print(response)
    for item in response:
        # str = ''
        # if item == "":
        #     continue
        # if ": " in item:
        #     str += item.split(": ")[1]
        with open('answers_new.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([item])
            f_object.close()
    # responseList.append(row)
    # responseList.append(response)
    # with open('AlexaCombinedReviews.csv', 'a') as f_object:
    #     writer_object = writer(f_object)
    #     writer_object.writerow(responseList)
    #     f_object.close()
    print(count)
    count += 1

#
# def convert(string_):
#     prompt = f'paraphrase the following: {string_}'
#     try:
#         completion = openai.Completion.create(
#             engine=model_engine,
#             prompt=prompt,
#             max_tokens=1024,
#             n=1,
#             stop=None,
#             temperature=0.5)
#         return completion.choices[0].text
#     except:
#         return ""
#

# dataFrame["paraphrased reviews"] = dataFrame['verified_reviews'].apply(convert)
# dataFrame.to_csv("AlexaCombinedReviews.csv", index=False)
