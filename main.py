# SchooloGPT by team Chipos
# Submission for 2024 SHS Hackathon
# Programmed by Victor P.


# Set things up
from openai import OpenAI
import json

client = OpenAI()


# Parse Options
def parse(f):
    fileObj = open(f)
    file = json.load(fileObj)
    fileObj.close()
    return file


# Load data
data = parse("config.json")
allowExamples = data["allowExamples"]
aiBlacklist = data["aiBlacklist"]
blacklistedWords = data["blacklistedWords"]
if aiBlacklist == False:
    blacklist = blacklistedWords
# Get question
q = str(input("Ask me a question: "))
q = q.lower()

# Main
if allowExamples == True and aiBlacklist == True:
    model = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a model that can provide general advice, but refuses to answer questions relating to school assignments. Instead, you will give a random example of the topic you were asked about",
            },
            {"role": "user", "content": f"{q}"},
        ],
    )
    print(model.choices[0].message.content)
elif allowExamples == True and aiBlacklist == False:
    model = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a model that provides general advice.",
            },
            {"role": "user", "content": f"{q}"},
        ],
    )
    x = 0
    blacklisted = 0
    q = q.split()
    for y in q:
        if q[int(x)] in blacklist:
            blacklisted += 1
        x += 1
    if blacklisted <= 1:
        print(model.choices[0].message.content)
    else:
        print('I cannot help you with schoolwork, but here is an example.')
        print('What would you like help with?')
        q = input('')
        model = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a model that provides general advice.",
                },
                {
                    "role": "user",
                    "content": f"generate and explain a random examples of {q}.",
                },
            ],
        )
    print(model.choices[0].message.content)


elif allowExamples == False and aiBlacklist == True:
    model = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a model that can provide general advice, but refuses to answer questions relating to school assignments.",
            },
            {"role": "user", "content": f"{q}"},
        ],
    )
    print(model.choices[0].message.content)
else:
    model = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a model that provides general advice.",
            },
            {"role": "user", "content": f"{q}"},
        ],
    )
    x = 0
    blacklisted = 0
    q = q.split()
    for y in q:
        if q[int(x)] in blacklist:
            blacklisted += 1
        x += 1
    if blacklisted <= 1:
        print(model.choices[0].message.content)
    else:
        print('I cannot help you with schoolwork.')
input("Press enter to exit")
