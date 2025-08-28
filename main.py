from algorithm import InputHandler

while True:
    inp = input("Enter a number, name, or array (e.g., [1,2,3]) or 'exit' to quit: ")
    if inp.lower() == 'exit':
        print("Goodbye!")
        break
    processor = InputHandler(inp)
    processor.process_inpt()