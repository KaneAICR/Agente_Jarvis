import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
load_dotenv()

@function_tool
def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

@function_tool
def subtract(a: int, b: int) -> int:
    """Return the difference of two numbers."""
    return a - b

@function_tool
def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b

@function_tool
def divide(a: int, b: int) -> int:
    """Return the quotient of two numbers."""
    return a / b


agent_Profe_de_matematicas = Agent(
    name="Math Tutor",
    instructions="You provide help with math problems. First provide the tool result and then write [+++] and the Explain your reasoning at each step and include examples", 
    model="gpt-4o-mini",
    tools=[add, subtract, multiply, divide]
)



## gui 
if __name__ == "__main__":
    print("=== Tutor de Matemáticas ===")
    print("(para salir escribe 'salir', 'exit' o 'bye')")
    
    while True:
        user_input = input("\nIngresa tu consulta: ")
        
        if user_input.lower() in ["salir", "exit", "bye"]:
            print("¡Hasta pronto!")
            break
            
        
        #usando run
        result = Runner.run_sync(agent_Profe_de_matematicas, user_input)
        print("\nRespuesta del agente:")
        print(result.final_output)