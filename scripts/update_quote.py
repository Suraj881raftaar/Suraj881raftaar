import random
import datetime

# Curated list of high-quality programming, AI, and exploration quotes
QUOTES = [
    {"quote": "The analytical engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves.", "author": "Ada Lovelace"},
    {"quote": "The question of whether a computer can think is no more interesting than the question of whether a submarine can swim.", "author": "Edsger W. Dijkstra"},
    {"quote": "Computers are useless. They can only give you answers.", "author": "Pablo Picasso"},
    {"quote": "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.", "author": "Stuart Russell & Peter Norvig"},
    {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"quote": "Complexity is the enemy of execution.", "author": "Tony Robbins"},
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Artificial intelligence is growing up fast, as are robots whose ability to manual partner with humans is improving rapidly.", "author": "Stephen Hawking"},
    {"quote": "Intelligence is the ability to adapt to change.", "author": "Stephen Hawking"},
    {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
    {"quote": "A code is like love, write it with support, hope, and absolute trust.", "author": "Anonymous"},
    {"quote": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"quote": "Software is a great combination between artistry and engineering.", "author": "Bill Gates"},
    {"quote": "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it.", "author": "Patrick McKenzie"},
    {"quote": "Live as if you were to die tomorrow. Learn as if you were to live forever.", "author": "Mahatma Gandhi"}
]

def get_daily_quote():
    # Seed with the current day of the year so it changes daily
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    random.seed(day_of_year)
    return random.choice(QUOTES)

def update_readme():
    quote_data = get_daily_quote()
    quote_str = f'\n> **"{quote_data["quote"]}"**\n>\n> *— {quote_data["author"]}*\n'

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "<!-- DAILY-QUOTE:START -->"
    end_tag = "<!-- DAILY-QUOTE:END -->"

    if start_tag in content and end_tag in content:
        parts_before = content.split(start_tag)[0]
        parts_after = content.split(end_tag)[1]
        new_content = parts_before + start_tag + quote_str + end_tag + parts_after

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated the daily quote!")
    else:
        print("Daily quote tags not found in README.md.")

if __name__ == "__main__":
    update_readme()
