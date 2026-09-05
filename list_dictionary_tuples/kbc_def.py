# ==========================================
# 📊 GAME DATA CONFIGURATION
# ==========================================
QUESTIONS = [
    "\nWhich of these planets in our solar system is closest to the Sun?\nA) Venus\nB) Earth\nC) Mercury\nD) Mars",
    "\nIn the epic Ramayana, whose wife was Sita?\nA) Lakshmana\nB) Rama\nC) Bharata\nD) Shatrughna",
    "\nWhich organ in the human body is responsible for pumping blood?\nA) Lungs\nB) Liver\nC) Brain\nD) Heart",
    "\nWhich of these sports does Virat Kohli play?\nA) Football\nB) Cricket\nC) Badminton\nD) Hockey",
    "\nWhat is the national currency of India?\nA) Dollar\nB) Euro\nC) Rupee\nD) Yen",
    "\nWhich is the largest state in India by geographical area?\nA) Madhya Pradesh\nB) Maharashtra\nC) Rajasthan\nD) Uttar Pradesh",
    "\nWho was the first woman Prime Minister of India?\nA) Pratibha Patil\nB) Indira Gandhi\nC) Sarojini Naidu\nD) Sucheta Kripalani",
    "\nWhich chemical element is represented by the symbol 'O' on the periodic table?\nA) Osmium\nB) Gold\nC) Oxygen\nD) Hydrogen",
    "\nIn which city would you find the historical monument 'Charminar'?\nA) Hyderabad\nB) Bengaluru\nC) Chennai\nD) Mysuru",
    "\nWhich animal is known to have three hearts?\nA) Shark\nB) Whale\nC) Octopus\nD) Dolphin",
    "\nWhich of these Indian monuments was designed by the British architect Edwin Lutyens?\nA) Gateway of India\nB) India Gate\nC) Victoria Memorial\nD) Taj Mahal Palace Hotel",
    "\nWho was the first Indian to win a Nobel Prize?\nA) C. V. Raman\nB) Rabindranath Tagore\nC) Mother Teresa\nD) Har Gobind Khorana",
    "\nWhich mountain range separates the Indian subcontinent from the Tibetan Plateau?\nA) Western Ghats\nB) Aravalli Range\nC) Himalayas\nD) Satpura Range",
    "\nIn 1915, from which country did Mahatma Gandhi permanently return to India?\nA) United Kingdom\nB) South Africa\nC) USA\nD) Mauritius",
    "\nWhich gas is most abundant in the Earth's atmosphere?\nA) Oxygen\nB) Carbon Dioxide\nC) Nitrogen\nD) Hydrogen"
]

ANSWERS = [
    "C) Mercury", "B) Rama", "D) Heart", "B) Cricket", "C) Rupee", 
    "C) Rajasthan", "B) Indira Gandhi", "C) Oxygen", "A) Hyderabad", "C) Octopus", 
    "B) India Gate", "B) Rabindranath Tagore", "C) Himalayas", "B) South Africa", "C) Nitrogen"
]

MONEY_TIERS = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

# ==========================================
# 🛠️ FUNCTION DEFINITIONS
# ==========================================

def greet_user():
    """Handles the game intro and gets the player's name."""
    print("\nDeviyon aur sajjano, namaskar! Main Amitabh Bachchan swagat karta hoon aap sabhi ka Kaun Banega Crorepati mein!")
    player_name = input("Game start karne se pahle kripaya apna name bataye: ")
    print(f"\n{player_name.title()} Ji, bahut bahut swagat hai aapka hamare show me. Chaliye game start karte hain. Wish you all the best !")
    print("=" * 100)
    return player_name.title()


def get_valid_input(question_text, money_tier):
    """Prompts user for input and ensures they type a valid option."""
    while True:
        print("_" * 100)
        user_choice = input(f"The next question for {money_tier} Rs. is -{question_text}\nType your answer (A/B/C/D and press enter to lock): ").upper()
        
        if user_choice in ("A", "B", "C", "D"):
            return user_choice
        else:
            print("Invalid input! Please choose among A/B/C/D only.")


def play_kbc():
    """Main game coordinator managing rounds, scoring, and endgame states."""
    name = greet_user()
    money_collected = 0
    answers_option_only = [ans[0] for ans in ANSWERS]
    
    # Pack data using zip for clean iterative pairing
    game_round = zip(QUESTIONS, ANSWERS, answers_option_only, MONEY_TIERS)
    
    for question, full_answer, correct_option, tier in game_round:
        # Pass data into input-handler function
        user_answer = get_valid_input(question, tier)
        
        if user_answer == correct_option:        
            money_collected = tier
            if money_collected == 10000000:
                print(f"\nBravo! You have successfully won {tier} Rs. Congratulations on becoming a Crorepati. We wish you a bright and rich future ahead.")
                break
            print(f"\nThat is correct answer.\nCongratulations! You have successfully won {money_collected} Rs. Get ready for the next round")
        else:
            print(f"\nAlas! This is not the right answer.\nThe right answer is {full_answer}.\nYou have won {money_collected} Rs. so far and your journey ends here.\nWe wish you a bright future ahead.")
            break

    print(f"\nThank you for playing, {name}!")


# ==========================================
# 🚀 EXECUTION START
# ==========================================
if __name__ == "__main__":
    play_kbc()
