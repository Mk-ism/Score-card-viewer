from pycricbuzz import Cricbuzz


c=Cricbuzz()

def first():
#fetching match data
        match_data = c.matches()
        #print(match_data)                                                  
        matches = []
        mt_id = []
        status = []
        mtype = []
        mnums = []
        m_srs = []
        for match in match_data:
                matches.append(match['mchdesc'])
                mt_id.append(match['id'])
                m_srs.append(match['srs'])
                mnums.append(match['mnum'])
                mtype.append(match['type'])
                status.append(match['status'])
#fetching data to the screen
        print("All Matches")
        for i,j in enumerate(matches,1):
                print("%d - %s"%(i,j))
#Taking input about matches
        choice = int(input('\nEnter choice : '))
        no_of_matches = len(matches)
        while choice <1 or choice > no_of_matches:
                print('\nNot available choose again')
                choice = int(input('\nEnter choice again: '))
        print('\n')

#getting matchwise data
        matches = matches[choice-1].title()
        m_srs = m_srs[choice-1].title()
        status = status[choice-1].title()
        mtype = mtype[choice-1].title()
        mnums = mnums[choice-1].title()
        mt_id = int(mt_id[choice-1])


#printing data
        print("your choice - " + matches.upper())
        choice = input("Want to know detail(y/n): ")
        if choice == 'y':
                print('\nDetails are:\n')
                print(m_srs)
                print("type: " + mtype)
                print(mnums)
                print("staus_of_match: " + status)
                print('\n')
                return mt_id
        elif choice == 'n':
               return mt_id
        else:
                retry = input("retry y/n : ")
                if(retry == 'y'):
                        return mt_id
                else:
                        return None

def commentary(mt_id):
        Info = c.commentary(mt_id)
        #print(Info)                                                          
        print('\n')
#making dictionary and storing
        commentry ={}
        commentry['commentary'] = Info['commentary']
#Arranging data into string
        strings =''
        for cmntry in enumerate(commentry['commentary']):
        	strings += "{}\n\n".format(cmntry)
        return (strings)


def Score(mt_id):
        Info = c.livescore(mt_id)
        #print(Info)                                                         
        print('\n\n')
#making dictionary and storing
        score = {}
        score['matchinfo'] = "{}, {}".format(Info['matchinfo']['mnum'],Info['matchinfo']['mchdesc'])
        score['status'] = "{}, {}".format(Info['matchinfo']['mchstate'].title(),Info['matchinfo']['status'])
        score['bowling'] = Info['bowling']
        score['batting'] = Info['batting']
#Arranging data into string
        strings = ''
        strings += score['matchinfo'] + '\n' + score['status'] + '\n\n'
        strings += score['batting']['team'] + '\n'
#team1        
        for scr in reversed(score['batting']['score']):
        	strings += "{} :- {}/{} in {} overs\n".format(scr['desc'],scr['runs'],scr['wickets'],scr['overs']) 
        for b in reversed(score['batting']['batsman']):
        	strings += "{} : {}({}) \n".format(b['name'].strip('*'),b['runs'],b['balls'])
#team2
        strings += "\n" + score['bowling']['team'] + '\n'
        for scr in reversed(score['bowling']['score']):
        	strings += "{} :- {}/{} in {} overs\n".format(scr['desc'],scr['runs'],scr['wickets'],scr['overs']) 
        for b in reversed(score['bowling']['bowler']):
                strings += "{} : {}/{} \n".format(b['name'].strip('*'),b['wickets'],b['runs'])
	
        return (strings)



def scorecard(mt_id):
        Info = c.scorecard(mt_id)
        #print(Info)                                                    
        print("\n")
#making dictionary and storing
        score_card = {}
        score_card['matchinfo'] = "{}, {}".format(Info['matchinfo']['mnum'],Info['matchinfo']['mchdesc'])
        score_card['status'] = "{}, {}".format(Info['matchinfo']['mchstate'].title(),Info['matchinfo']['status'])
        score_card['scorecard'] = Info['scorecard']
#Arranging data into string
        strings = ''
        strings += score_card['matchinfo'] + '\n' + score_card['status'] + '\n\n'
        strings +='*'*35 +'\n\n'
        for scr in reversed(score_card['scorecard']):
        	strings += "{} {}\n{}/{} in {} overs\n\n".format(scr['batteam'],scr['inngdesc'],scr['runs'],scr['wickets'],scr['overs'])
        	strings += "Batting\n"
        	strings += "{:<17} {:<3} {:<3} {:<3} {}\n\n".format('Name','R','B','4','6')
        	for b in scr['batcard']:
        		strings += "{:<17} {:<3} {:<3} {:<3} {}\n{}\n\n".format(b['name'], b['runs'], b['balls'], b['fours'], b['six'], b['dismissal'])
        	strings +="-"*35 +"\n\n"
        	strings += "Bowling\n"
        	strings += "{:<17} {:<5} {:<3} {:<3} {}\n\n".format('Name','O','M','R','W')
        	for b in scr['bowlcard']:
        		strings += "{:<17} {:<5} {:<3} {:<3} {}\n\n".format(b['name'], b['overs'], b['maidens'], b['runs'], b['wickets'])
        	strings +='*'*35 +'\n\n'
        return (strings)

                        

def main():
    print("*"*10 + "  Live cricket match detail Extractor  " + "*"*10)
    print('\n')
    print("*"*15 + 'By Mayank Kumar'+"*"*15)
    print('\n')
#Match Info   
    mt_id = first()
    print("What do you want to know")
    print('1. Live Score')
    print('2. Full Score Card')
    print('3. Commentary')
#getting what to know
    numb = int(input("Enter your choice: "))

    if(numb == 1):
        again = 'y'
        while again == 'y':
            print('\n\n')
            print(Score(int(mt_id)))
            again = input('\n\nDo you want to refresh(y/n):  ')
            if(again=='y'):
                print(Score(int(mt_id)))
            else:
                T_y = input("Thank you")

    elif(numb == 2):
        again = 'y'
        while again == 'y':
            print('\n\n')
            print(scorecard(int(mt_id)))
            again = input('\n\nDo you want to refresh(y/n):  ')
            if(again=='y'):
                print(scorecard(int(mt_id)))
            else:
                T_y = input("Thank you")

    elif(numb == 3):
        again = 'y'
        while again == 'y':
            print("\n\n")
            print(commentary(mt_id))
            again = input('\n\nDo you want to refresh(y/n):  ')
            if(again=='y'):
                print(commentary(mt_id))
            else:
                T_y = input("Thank you")
            
    else:
            print("\n\n")
            again = input('\n\nDo you want to choose again(y/n):  ')
            if(again=='y'):
                first()
            else:
                T_y = input("Thank you") 


if __name__ == '__main__':
 	main()



