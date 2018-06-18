import random

class Findnumber:       #Findnumber라는 클래스를 정의한다.
    def __init__(self):
        self.number = 0
        self.trial = 0

    def new_game(self,limit):
        self.number = random.randint(1, limit)
        self.trial = 0


    def compare(self,num):
        if num>self.number:
            result = "Smaller"
        elif num<self.number:
            result = "Greater"
        elif num==self.number:
            result = "Success"
        self.trial +=1

        return result


    def gettrial(self):
        return self.trial



if __name__ ==  '__main__':
    game = Findnumber()
    game.new_game(100)

    while(1):
        mynumber = int(input("Your guess:"))
        gameresult = game.compare(mynumber)
        print(gameresult)
        if gameresult == "Success":
            print("SUCCESS in",game.gettrial(),"trials")
            break


