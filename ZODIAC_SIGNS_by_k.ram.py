def choice():
    ch=input("\n ENTER YES TO CONTINUE AND NO TO EXIT ")
    if (ch=="YES" or ch=="yes" or ch=="Y" or ch=="y"):
        {
            call()
        }
    else:
         print("bye come back later")

print("ZODIAC SIGNS")
def call():
    L1=["1)ARIES","2)TAURUS","3)GEMINI","4)CANCER","5)LEO","6)VIRGO","7)LIBRA","8)SCORPIO","9)SAGITTARIUS","10)CAPRICON","11)AQUARIUS","12)PISCES"]
    for i in range(0,len(L1)):
        print(L1[i])
    L2=["ARIES\nThe time is right to pursue training for a particular skill or finish a degree in a field of interest to you, Aries. ",
        "TAURUS\nYour enthusiasm will be as contagious as your smile today, predicts Ganesha. People will stand charmed by your high spirits.",
        "GEMINI\nThis morning you may feel in a fog, but it should lift around midday.Enjoy the boost of energy that this good news gives you.",
        "CANCER\nIf it's true that you reap what you sow, Cancer, you're in for a great harvest in the coming months.",
        "LEO\nYou're highly esteemed in your profession because of your strong business acumen and no-nonsense approach to problem solving.",
        "VIRGO\nOpportunity may knock for you today from an unlikely source, perhaps total strangers! Use your intuition to follow potential leads.",
        "LIBRA\nExpect to receive interesting communications today, Libra. You might hear from a long-lost friend and have a chance to catch up on the news.",
        "SCORPIO\nYou're in a great position to reap the rewards from all your past hard work, Scorpio.",
        "SAGITTARIUS\n With the current celestial energy, you might be going on a trip, Sagittarius. It may be for business, pleasure, or both.",
        "CAPRICON\nDon't be surprised if money comes from an unlikely source. It could be a surprisingly good return on an investment or a bequest from a relative",
        "AQUARIUS\nThis is a good time to forge new relationships, Aquarius. Be open-minded if someone you know approaches with a proposal. ",
        "PISCES\nYou're feeling your power and strength today, Pisces. You've worked hard to get into good physical shape."]
    x=int(input("ENTER YOUR CHOICE IN GIVEN RANGE:"))
    print(L2[x-1])
    choice()
call()   
        
        
        
