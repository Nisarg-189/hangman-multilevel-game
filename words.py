easy_words = [
    "apple", "ball", "cat", "dog", "fish",
    "green", "house", "phone", "water"
]

medium_words = [
    "python", "coding", "laptop", "rocket",
    "hangman", "project", "variable"
]

hard_words = [
    "psychology", "xylophone", "architect",
    "parliament", "synchronise", "microscope"
]


def get_difficulty():
    difficulty = input("Enter difficulty (easy / medium / hard) :   ").lower().strip()

    if difficulty in ["easy", "medium", "hard"]:
        return difficulty
    
    else:
        print("❌ Invalid option!!  Choose : (easy / medium / hard)")


def get_words(difficulty):

    if difficulty == "easy":
        return easy_words
    elif difficulty == "medium":
        return medium_words
    elif difficulty == "hard":
        return hard_words