import random

def generate_challenge(skill_level):
    challenges = {
        "easy": ["FizzBuzz", "Palindrome Check", "Factorial"],
        "medium": ["Binary Search", "Merge Sort", "Linked List Reversal"],
        "hard": ["Dijkstra's Algorithm", "Knapsack Problem", "Graph Coloring"]
    }
    return random.choice(challenges.get(skill_level.lower(), []))

# Example usage
skill_level = "medium"
challenge = generate_challenge(skill_level)
print(f"Random {skill_level} challenge: {challenge}")
