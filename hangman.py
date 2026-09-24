import random
words = ["python", "computer", "programming", "developer", "keyboard"]
word = random.choice(words)
guessed_letters = []
max_wrong_guesses = 6
wrong_guesses = 0
display_word = ["_"] * len(word)
print("================================")
print("       🎮 HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print(f"You have {max_wrong_guesses} incorrect guesses.\n")
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses)
    print()
    guess = input("Enter a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!\n")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("❌ Wrong guess!\n")

if "_" not in display_word:
    print("================================")
    print("🎉 CONGRATULATIONS!")
    print("You guessed the word:", word)
    print("================================")

else:
    print("================================")
    print("😢 GAME OVER!")
    print("The correct word was:", word)
    print("================================")
