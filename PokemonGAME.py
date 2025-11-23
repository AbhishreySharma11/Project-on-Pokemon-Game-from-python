import os, json, random, time

class Pokemon:
    def __init__(self,n,h,a,d):
        self.n=n;self.mh=h;self.ch=h;self.a=a;self.d=d
    def dead(self):return self.ch<=0
    def fullheal(self):self.ch=self.mh
    def __repr__(self):
        p=int(self.ch/self.mh*100)
        s="Healthy"if p>50 else"Hurt"if p>20 else"Critical"
        return f"{self.n} ({s}) — {self.ch}/{self.mh} HP | Atk {self.a} Def {self.d}"

    @staticmethod
    def wild():
        return Pokemon(*random.choice([
            ("Charmander",50,12,8),("Bulbasaur",55,10,10),
            ("Squirtle",52,11,9),("Pikachu",48,13,7),
            ("Rattata",40,14,5),("Pidgey",45,9,6)
        ]))

class Trainer:
    def __init__(self,name,skip=False):
        self.name = name.strip().title() or "Ash"
        self.p = None if skip else self.choose()

    def choose(self):
        s=[("Charmander",52,12,9),("Bulbasaur",55,10,11),
           ("Squirtle",54,11,12),("Pikachu",50,14,8)]
        print("\nPick your starter:\n")
        for i,x in enumerate(s,1):print(f"  {i}. {x[0]}")
        while True:
            try:
                c = int(input("\n> "))-1
                if 0<=c<4:
                    print(f"\nYou chose {s[c][0]}! Let's go!\n")
                    time.sleep(0.7)
                    return Pokemon(*s[c])
            except:
                print("  type a number 1-4")
                continue

def dmg(att,defe):
    return max(1,att.a-defe.d+random.randint(-2,3))

def battle(me,wild):
    print(f"\nA wild {wild.n} appeared!\n")
    time.sleep(1)
    print(f"Go {me.n}!\n")
    r=0
    while me.ch>0 and wild.ch>0:
        r+=1
        print(f"Round {r}")
        if random.random()<0.5:
            damage = dmg(me,wild)
            wild.ch -= damage
            print(f"{me.n} hits for {damage}!")
        else:
            damage = dmg(wild,me)
            me.ch -= damage
            print(f"Wild {wild.n} hits for {damage}!")
        print(me)
        print(f"Wild {wild.n}: {wild.ch}/{wild.mh} HP\n")
        time.sleep(1)
    print("="*45)
    if me.ch>0:
        print("You won!")
        me.fullheal()
    else:
        print("You blacked out...")
    print("="*45,"\n")

SAVE="pokegame.json"

def save(t):
    try:
        with open(SAVE,"w")as f:
            json.dump({"name":t.name,"p":{"n":t.p.n,"ch":t.p.ch,"mh":t.p.mh,"a":t.p.a,"d":t.p.d}},f)
        print("saved")
    except:
        print("couldn't save")

def load():
    if not os.path.exists(SAVE):return None
    try:
        with open(SAVE)as f:
            d=json.load(f)
        t=Trainer(d["name"],skip=True)
        p=d["p"]
        t.p=Pokemon(p["n"],p["mh"],p["a"],p["d"])
        t.p.ch=p["ch"]
        print(f"welcome back {t.name}\n")
        return t
    except:
        return None

def cls():
    os.system("cls"if os.name=="nt"else"clear")

def main():
    cls()
    print("Pokémon Terminal Edition\n")
    player = load()
    if not player:
        name=input("Trainer name: ")
        player=Trainer(name)
    while True:
        print(f"{player.name}'s Pokémon:")
        print(player.p,"\n")
        print("1. Wild battle")
        print("2. Status")
        print("3. Save")
        print("4. Quit")
        c=input("\n> ").strip()
        if c=="1":
            battle(player.p,Pokemon.wild())
        elif c=="2":
            print("\n",player.p,"\n")
        elif c=="3":
            save(player)
        elif c=="4":
            print("\nbye")
            break
        else:
            print("??")
        time.sleep(0.4)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nlater")