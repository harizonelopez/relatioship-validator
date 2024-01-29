# Dev_@ladinh production
# Relationship validator program developed by DNI, the program basically entails entering your data and the program to determine whether you are fit to go

def net_worth():
    net_worth = int(input("\nQtn. What's your net worth? {in 100,000s} \n   Ans-> "))
    if net_worth == 0:
        print("\n   You need to be serious with yourself plus your life. Can you strive for a better future.")
        play_again()
        
    elif net_worth <= 10000:
        print("     That's shocking and not bringing any hapiness. Tafuta pesa bna $$$$")
        partner_info()
            
    elif net_worth <= 50000:
        print("    You are far away behind, This your net worth can only cater for a date without enjiying the luxury with your m-heart. *lol**")
        partner_info()
        
    elif net_worth <= 100000:
        print("    It seems that you can do it so continue focusing to make more, I'm impressed with you pall, cheeers....")
        partner_info()
        
    elif net_worth > 100000:
        print("   Congrats and you deserve an applause. I think we can be business associates.\n   Remember to always keep the assets at a higher ratio than the liabilities.")
        partner_info()
        
    elif net_worth == "":
        print("     !!ERROR!! You need to enter your net worth accordingly and in figures.")
        play_again()
        
    else:
        print("     !!ERROR!! You need to enter your net worth accordingly and in figures.")
        play_again()

def user_agreement():
    print("**User Agreements and Legal Terms**")
    user_answer = input("Qtn. Do you agree with the user legal terms and laws? {yes or no} \n    Ans-> ").lower()
    if user_answer == "yes":
        print("\n   It was a pleasure spending with you,\n   Welcome next time to the simple hook-up platform programm.\n")
        
    elif user_answer == "no":
        print("\n   !!ERROR!! You have to agree with the user legal terms and laws.\n")
    
    elif user_answer == "":
        print("\n   !!ERROR!! Respond only with the options provided for you.\n")
        play_again()
        
    else:
        print("\n   !!ERROR!! Respond only with the options provided for you.\n")
        play_again()
    
def partner_info():
    print("\nQtn. Please describe the type of a partner you may want to be with in your whole entire life untill God separates either of you or both apart.")
    answer = input("   Ans-> ").lower()
    if answer == "":
        print("\n   !!ERROR!! You need to enter the description in the entry field above.")
        play_again()
        
    elif len(answer) < 5:
        print("\n   !!ERROR!! The length of your description should exceed 5 characters.")
        play_again()
        
    else:
        print(f"\n  Wow {answer} is a nice and cool partner description, Your prayers are heard by J.A.R.V.I.S\n")
       user_agreement()
       
def car_ownership():
    print("\n    It's now time to know what you own in your life.")
    car_ownership =  input("Qtn. Do you own a car in your life? {yes or no} \n   Ans-> ").lower()
    if car_ownership == "yes":
        print("     That's awesome and cool, It seems you are stinking rich. Wish you the best.")
        house_ownership()
        
    elif car_ownership == "no":
        print("\n   It's cool pall, all is awesome. Hope one day you will own yours in life.")
        house_ownership()
        
    elif car_ownership == "":
        print("     !!ERROR!! You need to respond to the question correctly using the options given.")
        play_again()
        
    else:
        print("     !!ERROR!! You need to respond to the question correctly using the options given.")
        play_again()
        
def house_ownership():
    house_ownership = input("\nQtn. Do you have a house?\n  Ans-> ").lower()
    if house_ownership == "yes":
        print("     That's amazing and wonderfull. \n   In this life, that's the basic need you have to be with at first hand, big up(:")
        net_worth()
        
    elif house_ownership == "no":
        print("     It's shocking to hear that but all is cool,\n   I know that's the next thing in your mind to own after geting your soulmate -^-^-")
        net_worth()
        
    elif house_ownership == "":
        print("     !!ERROR!! It's simple, You either have a house or not,,")
        play_again()
        
    else:
        print("     !!ERROR!! It's simple, You either have a house or not,,")
        play_again()

def kids():
    kids_number = int(input("\nQtn. How many kids do you have?\n    Ans-> "))
    if kids_number == 1:
        gender = input("Qtn. What is the gender? {male or female} \n    Ans-> ").lower()
        if gender == "male":
            kid_name = input("\nQtn. What's the name of your little king?\n    Ans-> ").lower()
            if kid_name == "":
                print("\n   !!ERROR!! You need to enter the name of the kid, Try again.")
                play_again()
        
            else:
                if kid_name in ["kevo","brayo","dax","mark","stano","samson"]:
                    print(f"    Oops!! {kid_name} seems to be of a player name, You need to take caution with him carefully.")
                    car_ownership()
                    
                else:
                    print(f"\n  Oh!!, {kid_name} is a nice name and I wish him the best in his life.")
                    car_ownership()
                    
        elif gender == "female":
            kid_name = input("\nQtn. What's the name of your young princess?\n   Ans-> ").lower()
            if kid_name == "":
                print("\n   !ERROR!! You need to enter the name of the baby girl, Try again.")
                play_again()
                
            else:
                if kid_name in ["mercy","lucy","vee","sharon","shee","susan"]:
                    print(f"    Oops!! {kid_name} seems to be of a player name, You need to take caution with her carefully.")
                    car_ownership()
                    
                else:
                    print(f"\n  Oh!!, {kid_name} is a nice name and I wish her the best in her life as she natures up.")
                    car_ownership()
        else:
            print("     You need to enter the correct gender of the kid")
            play_again()
    
    elif kids_number >= 2:
        boys = int(input("\nQtn. How many male kids do you have?\n   Ans-> "))
        girls = int(input("\nQtn. How many female kids do you have?\n   Ans-> "))
        if boys == 0:
            print("     You have to enter the number of male kids you have, Try again")
            play_again()
            
        if girls == 0:
           print("     You have to enter the number of female kids you have, Try again")
           play_again()
        
        else:
            print(f"    Hurray!! {boys} boys and {girls} girls is a great achievement in life.\n    Hope that you will get a partner whom will take good care of you plus your beautifull little angels.")
            car_ownership()
            
    elif kids_number == 0:
        print("     All is cool pall.\n     That's amazing for the start, I hope all will be cool.")
        car_ownership()
    
    elif kids_number == "":
        print("!!ERROR!!, Use figures when entering the kids_number")
        play_again()
        
    else:
        print("     !!ERROR!!.\n     Kid(s) number required.")
        play_again()

def single(): 
    gender = input("\nQtn. What's your gender?{male or female}\n    Ans-> ").lower()
    if gender == "male":
        duration = int(input("\nQtn. How long have you been single niggah (yrs)?\n  Ans-> "))
        if duration <= 1:
            print("\n   Oops! sorry man, you seem to have been heartbroken recently. \nWhat was the core cause of your break-up with your 'm-verified'?.")
            asnwer = input("-> ")
            print("\n   That was so touchy bro all will be fine, remember we men we don't force relationships.")
            kids()

        elif duration <= 3:
            print("\n   Congrats buddy, for that all period you have been sterile in zero dock quarantine!! Salute you buddy.\n   It seems things din't go as you expected with your partner. I hope all will be fine.")
            kids()

        elif duration > 3:
            print("\n   Hey man, I'm sorry I can't help you  because it seems you can't heal from your previous relationship.")
            kids()
 
        else:
            print("\n   Oopss!!! You have to enter the duration you have been single!!")
            play_again()
             
    elif gender == "female":
        duration = int(input("\nQtn. How long have you been single niggah (yrs)?\n  Ans-> "))
        if duration <= 1:
            print("\n   Oops! sorry lady, someone seem to have broken your heart recently. What did your man lacked in you that he dumped you as beautifull as you are?")
            asnwer = input("-> ")
            print("\n   That was so touchy 'siz' all will be fine, I have hopes that by the end you will grip with your hands one of the niggahs whom are on the hunt as you.")
            kids()
    
        elif duration <= 3:
            print("\n   That's amazing, bcz to get a lady being single for that period is not a joke. Big Up :)")   
            kids()

        elif duration > 3:
            print("\n   Heyyyy, I'm shoked to hear that but its cool, don't give up.")
            kids()

        else:
            print("\n   Oopss!!! You have to enter the duration you have been single!!")
            play_again()
    else:
        print("\n   Go to hell!! We don't deel with any form of gayism or lesbianism here, You either be a man or a woman.")    
        play_again()

def married():
    gender = input("\nQtn. What is your gender?{male or female}\nAns-> ")
    if gender == "female":
        print("\n   So you are the ladies whom keeps on cheeting to their husbands and \n   afterwards when you get dumped you complain how irresponsible your men are. \n  Shame on you, you are nolonger needed here as this platform is for the single.\n   May GOD struck you with lightening as you are in the process of cheating.\n")
        quit()
        
    elif gender == "male":
        print("\n   You are right and free to go, coz you were permitted to do so by GOD.")
        kids()
        
    else:
        print("\n   Go to hell!! We don't deal with any form of homosexuality here, You either be a man or a woman.")
        quit()
    
def Status():
    print("\nQtn. What's your relationship status? {single or married}")
    answer = input("    Ans-> ").lower()
    if answer == "single":
        single()
        
    elif answer == "married":
        married()
    
    else:
        print("\n   !!ERROR!! Status is required\n")
        Welcome_screen()
    
def play_again():
    print("   You have either completed the validation process\n   or you may have defiled the system protocols and rules governing the programm logic and flow hence leading to program termination.")
    answer = input("Qtn. Do you wish to run the program logic again? {yes or no}\n    Ans-> ").lower()
    if answer == "yes":
        Welcome_screen()
        
    else:
        print("    Cool, You are welcomed again next time, I hope you anjoyed navigating through the program...:)\n")
        quit()
        
def Welcome_screen():
    name_size = 2
    My_name = []
    
    print("\n***Welcome To The Relationship Validator Programme***")
    print("        Enjoy yourself and make yourself cool\n")
    
    print("Qtn. Enter your identity details.")
    firstName = input("  First name: ").lower()  
    lastName = input("  Last name: ").lower()        
   
    if  firstName == "":
        print("\n   You must enter your first name for you to continue, Try again.\n")
        play_again()
        
    elif lastName == "":
        print("\n   You must enter your last name for you to continue, Try again.\n")
        play_again()
        
    elif firstName in ["dan","den","mike","shantel","sharon","shiro","vee","hary","mish","vayo","pamela","kevo","brayo","kevin","brian","stanley","stano","irene","godfrey","gladys","ben","jane","janet","jux"]:
        print(f"    Oops! {firstName}, the name seems to be that of a player somehow, you can try again!")
        play_again()
        
    elif lastName in ["dan","den","mike","shantel","sharon","shiro","vee","hary","mish","vayo","pamela","kevo","brayo","kevin","brian","stanley","stano","irene","godfrey","gladys","ben","jane","janet","jux"]:
        print(f"    Oops! {lastName}, the name seems to be that of a player somehow, you can try again!")
        play_again()
            
    else:
        print(f"\n  {firstName} {lastName}, such a nice name, all is cool and you can continue with your validation")
        Status()
        
        
Welcome_screen()

