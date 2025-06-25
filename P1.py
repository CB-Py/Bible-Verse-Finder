import json
def read_verse_file():
    with open('verses.json','r') as file:
        data = json.load(file)
        return data

def  bible_verse_finder():
    topic=['love','strength','peace','hope','grace']
    topic_verse = read_verse_file()
    while True:
        print('\n---Bible Verse Topic---')
        for x in topic:
            print(f'Topic: {x}')
            
        choice = input('\nEnter the name of topic (type "exit" to leave):')
        
        
        if choice == "exit":
            print('You have exited the system, have a blessed day ahead')
            break
        
        else:
            if choice in topic_verse:
                print(f'\nVerses on {choice.capitalize()}:')
                for verse in topic_verse[choice]:
                    readable_verse  = verse.replace("_"," ")
                    print(f'- {readable_verse}')
        
        
        

if __name__ == "__main__":
    bible_verse_finder()
    
    
    
    