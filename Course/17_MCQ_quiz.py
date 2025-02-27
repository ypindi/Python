from Question_17 import Question

question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("Hey you got " + str(score) + "/" + str(len(questions)) + " correct.")
    print(f'Hey you got {score}/{len(questions)} as correct.')

run_test(questions)