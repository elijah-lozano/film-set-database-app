
#from .env.py import *
import mysql.connector
import time

entities = ("ACTOR","CHOOSES_STORY", "DIRECTOR", "DIRECTS",
            "FILM", "FILMS", "FINANCIER", "FUNDS", "HIRES", 
            "INSTRUCTS", "MEMBER", "PERFORMS_IN", "PITCHES_TO",
            "PRODUCER")


def main():

    movie_db = mysql.connector.connect(
            host = "127.0.0.1",
            user="root",
            password="hidden",
            database ="movie_db"
    )

    cursor = movie_db.cursor()

    print("\n\n---------- Elijah Lozano's Project: Movie Database ----------\n\n")

    for entity in entities:
        print("Selecting all from "+entity+" (select * from "+entity+")\n")
        select_all(cursor, entity)
        print("\n")



    while True:
        
        print("1. Report the film crew members' name and salary that were hired on 2015/05/15 and have a salary higher than $53,000.\n")
        print("2. Report the movie title and film crew members' names who worked on the same film (It: Chapter 2) and were hired on the same day.\n")
        print("3. Report the producer name and phone number who chose the story for the films that Tom Holland performed in.\n")
        print("4. Report movie titles and actors who perfomed in them.\n")
        print("5. Report the director names and film titles of directors who directed a horror film.\n")
        print("6. Insert an actor named 'Actor Man'\n")
        print("7. Update 'Actor Man' salary and agent name.\n")
        print("8. Delete actor 'Actor Man'\n")


        print("Type 'exit' to exit program.\n")

        user_select = input("Choose a query or type exit to leave: ")
        
        if user_select == "1":
            query1(cursor)
            continue

        elif user_select == "2":
            query2(cursor)
            continue

        elif user_select == "3":
            query3(cursor)
            continue
        
        elif user_select == "4":
            query4(cursor)
            continue

        elif user_select == "5":
            query5(cursor)
            continue

        elif user_select == "6":
            insert_actor(cursor, "\'2223334444\'", "\'Actor Man\'", "\'2009-10-09\'", "\'Gersh\'", 150000)
            continue

        elif user_select == "7":
            update_actor(cursor)
            continue

        elif user_select == "8":
            delete_actor(cursor)
            continue

        elif user_select == "exit":
            print("Goodbye.\n")
            break
        

def query1(cursor):
    
    print("\n-------------------------------------------------------------\n")
    print("You chose: Report the film crew members' name and salary that were hired on 2015/05/15 and have a salary higher than $53,000.\n")
    query = "select M.fullName, M.salary from MEMBER M where dateHired='2015-05-15' group by salary having salary > 53000"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    result = cursor.fetchall()
    
    print("Report generated: \n")
    
    for x in result:
        print(x)
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)

def query2(cursor):
    
    print("\n-------------------------------------------------------------\n")
    print("You chose: Report the movie title and film crew members' names who worked on the same film and were hired on the same day.\n")
    query = "select F.title, Z.memName from FILM F, FILMS Z where F.filmNum=Z.filmNum and Z.filmNum=2 and Z.memName IN (select fullName from MEMBER where dateHired='2015-05-15')"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    result = cursor.fetchall()
    
    print("Report generated: \n")
    
    for x in result:
        print(x)
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)

def query3(cursor):
    
    print("\n-------------------------------------------------------------\n")
    print("You chose: Report the producer name and phone number who chose the story for the films that Tom Holland performed in.\n")
    query = "select C.proName, C.proPhoneNum, F.title from CHOOSES_STORY C, FILM F where C.filmNum IN (select P.filmNum from PERFORMS_IN P, ACTOR A where P.filmNum=F.filmNum and P.actorName='Tom Holland')"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    result = cursor.fetchall()
    
    print("Report generated: \n")
    
    for x in result:
        print(x)
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)
    

def query4(cursor):
    
    print("\n-------------------------------------------------------------\n")
    print("You chose: Report movie titles and actors who perfomed in them.\n")
    query = "select F.title, P.actorName from PERFORMS_IN P JOIN FILM F ON P.filmNum=F.filmNum"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    result = cursor.fetchall()
    
    print("Report generated: \n")
    
    for x in result:
        print(x)
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)


def query5(cursor):
    
    print("\n-------------------------------------------------------------\n")
    print("You chose: Report the director names and film titles of directors who directed a horror film.\n")
    query = "select X.dirName, F.title from DIRECTS X, FILM F where F.genre='Horror' and X.filmNum=F.filmNum"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    result = cursor.fetchall()
    
    print("Report generated: \n")
    
    for x in result:
        print(x)
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)


def select_all(cursor, entity):

    query = "select * from "+entity
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    for x in result:
        print(x)

def insert_actor(cursor, phone, name, date, agent_name, salary):
    print("\n-------------------------------------------------------------\n")
    print("You chose: Insert new actor\n")
    query = "insert into actor (phoneNum, fullName, dateHired, agentName, salary) values("+phone+", "+name+", "+date+", "+agent_name+", "+str(salary)+")"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    #result = cursor.fetchall()
    
    print("Report generated: \n")
    
    select_all(cursor, "actor")
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)

def update_actor(cursor):
    print("\n-------------------------------------------------------------\n")
    print("You chose: Update actor salary and agent name\n")
    query = "update actor set salary=550000, agentName=\'Heena Jathore\' where fullName=\'Actor Man\'"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    #result = cursor.fetchall()
    
    print("Report generated: \n")
    
    select_all(cursor, "actor")
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)


def delete_actor(cursor):
    print("\n-------------------------------------------------------------\n")
    print("You chose: Delete actor 'Actor Man'\n")
    query = "delete from actor where fullName=\'Actor Man\'"
    print("Running query: "+query+"\n")

    cursor.execute(query)
    #result = cursor.fetchall()
    
    print("Report generated: \n")
    
    select_all(cursor, "actor")
    
    print("\nSleeping...\n-------------------------------------------------------------\n")
    time.sleep(8)




if __name__ == "__main__":
    main()