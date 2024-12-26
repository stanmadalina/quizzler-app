import requests

main_endpoint = "https://opentdb.com/api.php"

parameters = {
    "amount": 12,
    "type": "boolean"
}

response = requests.get(url=main_endpoint, params=parameters)
# print(response.text)

data = response.json()

questions = data["results"]

question_data = []
for i in questions:
    question = i["question"]
    answer = i["correct_answer"]
    question_data.append({"question": question, "correct_answer": answer})
