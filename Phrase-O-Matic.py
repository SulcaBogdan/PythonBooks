import random

verbs = ['Leverage', 'Sync', 'Target',
 'Gamify', 'Offline', 'Crowd-sourced',
 '24/7', 'Lean-in', '30,000 foot']

adjectives = ['A/B Tested', 'Freemium',
 'Hyperlocal', 'Siloed', 'B-to-B',
 'Oriented', 'Cloud-based','API-based']

nouns = ['Early Adopter', 'Low-hanging Fruit',
 'Pipeline', 'Splash Page', 'Productivity',
 'Process', 'Tipping Point', 'Paradigm']


count = 0
while count < len(verbs):
    result = random.choice(verbs) + " " + random.choice(adjectives) + " " + random.choice(nouns)
    count += 1
    print(result)



