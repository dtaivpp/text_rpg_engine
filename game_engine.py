import sys,time,random
import pickle 

def slow_type(t):
    typing_speed = 75 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')


def get_input(valid_input: list):
  while True:
    user_entered = input()
    if user_entered not in valid_input:
      print("Invalid input. Please use one \
              of the following inputs:\n")
      print(valid_input)
      user_entered = None
    else:
      return user_entered


def display_page_text(lines: list):
  for line in lines:
    slow_type(line)
    # Make the user press enter to see the next line
    get_input([""])


def get_response(options: list):
  for index, option in enumerate(options):
    print(str(index) + ". " + option[0])
  
  valid_inputs = [str(num) for num in range(len(options))]

  option_index = int(get_input(valid_inputs))

  return options[option_index][1]


def story_flow(story: dict):
  curr_page = 1

  while curr_page != None:
    page = story.get(curr_page, None)
    
    if page == None:
      curr_page = None
      break

    display_page_text(page['Text'])
    
    if len(page['Options']) == 0:
      curr_page = None
      break

    curr_page = get_response(page['Options'])
   
if __name__=='__main__':
    story = {}
    with open('chapter1.ch', 'rb') as chapter:
 
        story = pickle.load(chapter)

    story_flow(story)