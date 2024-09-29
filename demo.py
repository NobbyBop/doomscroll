import google.generativeai as genai
import os
import datetime

genai.configure(api_key=os.environ["GEMINI"])
model = genai.GenerativeModel("gemini-1.5-flash")

user_info = "I am a 21 year old man who enjoys art and music. I play the guitar and like drawing."
user_interests = ["guitar", "running", "drawing", "reading", "writing poetry"]
user_achievements = []
suggestions = []
# This is an example of a task.
# achievement = {"desc":"Here is a description of a task I completed.",
#                "date": datetime.datetime.now()}


if __name__ == "__main__":
    print("ANTI-DOOMSCROLL APP - Terminal Edition")
    end = False
    while(not end):
        print("MENU\n1. About Me\n2. My Interests\n3. My Achievements\n4. Get An Idea!\n5.Quit")
        option = input("> ").strip()
        while(option not in ("1", "2", "3", "4", "5")):
            print(f"Invalid option '{option}'. Valid options are [1], [2], [3], [4], [5].")
            option = input("> ").strip()

        # About Me
        if(option == "1"):
            print(f"Your bio: {user_info}\n[ENTER] to return, [C] to modify.")
            option = input("> ").strip()
            while(option not in ("", "c", "C")):
                print(f"Invalid option '{option}'. Valid options are [ENTER] and [C].")
                option = input("> ").strip()
            if(option in ("c", "C")):
                print("Type your new info, and press [ENTER] when done.")
                user_info = input("> ")
            continue

        # Get An Idea!
        elif(option == "4"):
            prompt = "Your response will be a one-sentence prompt to the user to complete a task with the goal of avoiding doomscrolling and doing something fulfilling.\n" +\
                                              f"The user has the following bio: {user_info}\n"+\
                                              f"The user has the following interests: {user_interests}\n" +\
                                              f"The user has already completed the following tasks: {user_achievements}\n"+\
                                              "Please follow the instructions below in generating your prompt:\n"+\
                                              "1. Do not give the user a task they have already completed in the last 30 days.\n" +\
                                              "2. Use the user's bio and interests to create a task that encourages exploration and aligns with their interests.\n" +\
                                              "3. Generate a task that is immediately achievable and does not require excessive purchases.\n"+\
                                              "4. Provide a specific, straightforward task with no room for re-interpretation or compound steps.\n"+\
                                              "5. Avoid mentioning scrolling or similar behaviors in the response."
            print("Stop doomscrolling! Try this instead:")
            response = model.generate_content(prompt)
            idea = response.text
            print(idea)
            ideas = [idea]
            changes = []
            print("What do you think? [Y] or [N]")
            option = input("> ").strip()
            while option not in ("y", "Y", "n", "N"):
                print(f"Invalid option '{option}'. Valid options are [Y] and [N].")
                option = input("> ").strip()
            while option in ("n", "N"):
                print("What would make this idea better?")
                changes.append( input("> ").strip())
                response = model.generate_content(prompt + f"6. In response to {ideas}, the user has suggested {changes}. Adhere to these suggestions as your top priority.")
                print("Stop doomscrolling! Try this instead:")
                idea = response.text
                print(idea)
                ideas.append(idea)
                print("What do you think? [Y] or [N]")
                option = input("> ").strip()
        
        #Quit
        elif(option == "5"):
            print("Goodbye. Stay off your phone!")
            end = True
            continue
        else:
            print("Not implemented yet!")
            
