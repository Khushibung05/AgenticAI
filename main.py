# main.py

from agent import OfficeAgent

agent = OfficeAgent()

print("=" * 50)
print("SMART OFFICE ASSISTANT")
print("=" * 50)
print("Type 'exit' to quit")
print()

while True:

    query = input("You: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    try:

        answer = agent.run(query)

        print("\nAssistant:")
        print(answer)

    except Exception as e:

        print("\nError:")
        print(e)