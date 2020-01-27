import pickle

story = {
    1: {
      'Text': [
            "Hello there..",
            "I bet you werent exepecting to hear from me so soon...",
            "...you seem a little confused do you know who I am?"
        ],
      'Options': [
          ("Yeah of course!", 2),
          ("I'm sorry I dont", 3)
        ]
    },
    2: {    
        'Text': [
            "Go figure.. a fall like that couldn't get through your thick skull",
            "Not to mention how could you forget me your best friend Jeff"
        ],
        'Options': [
          ("What did I hit my head on?", 4),
          ("Really?", 5)
        ]
    },
    3: {
        'Text': [
            "I guess that makes sense you really hit your head hard there...",
            "I'm your best friend. Jeff.. You and I were just on a mission"
        ],
        'Options': [
          ("What did I hit my head on?", 4),
          ("Really?", 5)
        ]
    },
    4: {
      'Text': [
            "You fell off that cliff over there.",
            "Heck of a fall really..."
        ],
      'Options': []
    },
    5: {
      'Text': [
            "Yeah man it was crazy",
            "Never seen a man fall off a cliff like that before..."
        ],
      'Options': []
    }
}

with open('chapter1.ch', 'wb') as chapter:
  pickle.dump(story, chapter)
