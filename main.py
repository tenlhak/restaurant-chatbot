import os
import json
from dotenv import load_dotenv
from src.bot import RestaurantBot

def save_conversation_outcome(outcome):
    """Save conversation outcomes to JSON files."""
    if outcome['order_id']:
        print(f"\nOrder confirmed! Your order ID is: {outcome['order_id']}")
        with open(f"order_{outcome['order_id']}.json", "w") as f:
            json.dump(outcome['order_details'], f, indent=2)
            
    if outcome['reservation_id']:
        print(f"\nReservation confirmed! Your reservation ID is: {outcome['reservation_id']}")
        with open(f"reservation_{outcome['reservation_id']}.json", "w") as f:
            json.dump(outcome['reservation_details'], f, indent=2)

def main():
    """Main function to run the restaurant chatbot."""
    # Load environment variables
    load_dotenv()
    
    # Initialize bot with menu
    menu_path = os.path.join('data', 'menu.txt')
    if not os.path.exists(menu_path):
        print(f"Error: Menu file not found at {menu_path}")
        return
        
    try:
        bot = RestaurantBot(menu_path)
    except Exception as e:
        print(f"Error initializing bot: {str(e)}")
        return

    # Welcome message
    print("Welcome to Fuji Grill! 🍱")
    print("How can I assist you today?")
    print("(Type 'bye' or 'quit' to end the conversation)")
    
    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
                print("\nAssistant: Thank you for choosing Fuji Grill! Have a great day! 👋")
                
                # Process final conversation outcome
                outcome = bot.process_conversation_outcome()
                save_conversation_outcome(outcome)
                break
            
            # Get bot response
            response = bot.handle_message(user_input)
            print("\nAssistant:", response)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! Thank you for visiting Fuji Grill! 👋")
            break
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again or contact support if the issue persists.")

if __name__ == "__main__":
    main()
