from chatgpt_wrapper import ChatGPT
from flask import Flask, request, jsonify

app = Flask(__name__)
chat_gpt = ChatGPT()


@app.route("/chatgpt/question", methods=["POST"])
def question():
    args = request.args
    prompt = request.json
    question = prompt["question"]

    if args.get("debug", default=False, type=bool):
        print("ChatGPT Question Received...")
        print(f"ChatGPT Question is: {question}")

    response = chat_gpt.ask(question)

    if args.get("debug", default=False, type=bool):
        print("ChatGPT Response Received...")
        print(f"ChatGPT Response is: {response}")

    return response


@app.route("/chatgpt/status", methods=["GET"])
def status():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(threaded=False)
