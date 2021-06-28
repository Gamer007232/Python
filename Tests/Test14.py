print('''
    *                             |>>>                    +
+          *                      |                   *       +
                    |>>>      _  _|_  _   *     |>>>
           *        |        |;| |;| |;|        |                 *
     +          _  _|_  _    \\.    .  /    _  _|_  _       +
 *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|
               \\..      /    ||:+++. |    \\.    .  /           *
      +         \\.  ,  /     ||:+++  |     \\:  .  /
                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *
          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +
                 ||+++ ||.    .     .      . ||+++.|   *
+   *            ||: . ||:.     . .   .  ,   ||:   |               *
         *       ||:   ||:  ,     +       .  ||: , |      +
  *              ||:   ||:.     +++++      . ||:   |         *
     +           ||:   ||.     +++++++  .    ||: . |    +
           +     ||: . ||: ,   +++++++ .  .  ||:   |             +
                 ||: . ||: ,   +++++++ .  .  ||:   |        *
                 ||: . ||: ,   +++++++ .  .  ||:   |

''')
print("Welcome to 'The Dark Castle'")
print("[Mission Objective]: Locate the treasure.")
print("*********************************************")
print("")
print(
    "The gates of the castle open slowly as you approach. The air is thick with fog. The castle sure lives up to its name 'The Dark Castle', it is dark everywhere.  The only light is the torches on the wall that give off just enough light to see the hallway you find yourself in."
)
print("")
input("  (Enter to Continue)")
print("")
print(
    "As you enter the gates, you hear a loud crashing sound. You turn around to realize the gate has now slammed shut behind you.  The only option is to continue forward."
)
print("")
input("  (Enter to Continue)")
print("")
print(
    "You reach the end of the hallway and find yourself in front of 2 old doors that are covered in dust and mold."
)
print("")
input("  (Enter to Continue)")
print("")
print(
    "The only real difference that you can see between the doors is that the door on the RIGHT you can see a light coming from under the door. The door on the LEFT is as dark as the room around you."
)
print("")
input("  (Enter to Continue)")
print("")
print('''
      ______
   ,-' ;  ! `-.
  / :  !  :  . \ 
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
 ''')
print("")
print("*******************************************")
print("")
first_choice = (input("Which door do you enter?\n (Left or Right): ")).lower()
if (first_choice == "right") or (first_choice == "r"):
    print("")
    print("*******************************************")
    print("")
    print(
        "The door seems to be stuck at first. You push on the door, giving it your all.  The door opens slightly, You take a couple steps back and then run full force at the door putting all your weight behind it.  The door slams open against the wall."
    )
    print("")
    input("  (Enter to Continue)")
    print("")
    print(
        "The light is so bright it illuminates the entire room.  But in the back of the room you notice something moving, but can't quite tell what it is. The light is too bright, you can't make out what is moving.  Whatever it is, it is big, and its coming closer."
    )
    print("")
    input("  (Enter to Continue)")
    print("")
    print(
        "You feel the ground shake as this thing walks. Your knees buckle and you fall to the floor. Was it because of the floor shaking or your nerves because this thing looks like a dragon, and it seems to be rather irritated at you.  The sound of the door slamming open must have woken it up."
    )
    print("")
    print("*******************************************")
    print("")
    first_choice_b = (
        input("Do you want to run? or Do you want to fight?\n (Run or Fight): "
              )).lower()
    if (first_choice_b == "run") or (first_choice_b == "r"):
        print("")
        print("*******************************************")
        print("")
        print(
            "You turn around to run. The ground shakes more as the dragon approaches you. You are stumbling your way to the door, your hand reaches out at the doorway."
        )
        print("")
        input("  (Enter to Continue)")
        print("")
        print(
            "The dragon leans down and opens his mouth to start a monsterous stream of fire that immediately overtakes your entire body. You turn to ashes, and the wind blows your ashes through the door, and the door slams shut behind you."
        )
        print("")
        print("☠  You have died!! ☠")
    else:
        print("")
        print("*******************************************")
        print("")
        print("     @xxxx[{:::::::::::::::::::::::>")
        print("")
        print(
            "You are ready to go down swinging.  You reach for your sword, and raise it into the air. The dragon stops walking immediately, and his head tilts to the side as he stares at you with this strange look on his face."
        )
        print("")
        input("  (Enter to Continue)")
        print("")
        print(
            "The dragon leans down and opens his mouth to start a monsterous stream of fire that immediately overtakes your entire body. You turn to ashes, and the wind blows your ashes through the door, and the door slams shut behind you."
        )
        print("")
        print("☠  You have died!! ☠")
else:
    print("")
    print("*******************************************")
    print("")
    print(
        "The door opens easily and you enter a dark room. You feel your way into the room and you find a table.  The table has a lantern."
    )
    print("")
    input("  (Enter to Continue)")
    print("")
    print(
        "You fumble through your bag looking for a match.  As you light the lantern you realize how big the room is, and as you glance around the room, you notice a large figure on the floor.  It isn't moving, but it is gigantic."
    )
    print("")
    input("  (Enter to Continue)")
    print("")
    print(
        "As you approach the giant figure the light from the lantern reveals blood stains scattered all over the floor.  You lift the lantern up a bit higher as you are walking and you see that the large figure is actually a dead dragon."
    )
    print("")
    input("  (Enter to Continue)")
    print("")
    print(
        "A sense of relief rushes over you as you are happy that it isn't alive at least. Fighting a live dragon would have been a little intense.  You see this very dim light at the end of the room, so you walk towards it."
    )
    print("")
    input("  (Enter to Continue)")
    print("")
    print(
        "As you are walking you don't see any other doors. But as you approach the dim light, your lantern's light reveals a bookcase, and behind it is a set of stairs that go up, and a set of stairs that go down."
    )
    print("")
    print("*******************************************")
    print("")
    second_choice = (input(
        "Do you want to go Up? or Do you want to go Down?\n (Up or Down): ")
                     ).lower()
    if (second_choice == "down"):
        print("")
        print("*******************************************")
        print("")
        print(
            "You start walking down the stairs holding your lantern out in front of you. You reach the bottom of the stairs, and step onto the floor.  As you do you notice that this room is more like ruins.  The place is falling apart."
        )
        print("")
        input("  (Enter to Continue)")
        print("")
        print(
            "You turn around quickly and start making your way back up the stairs as fast as you can, but the steps are giving way as you step on them.  You make it up just a few steps and the entire room with the stairs crumble beneath you and you fall into the merky water below."
        )
        print("")
        input("  (Enter to Continue)")
        print("")
        print(
            "A family of aligators sees you fall into the water and starts heading your direction, so you turn around to start swimming to the closest shore.  As you turn around you see the gator you didn't notice before.  He's right in front of you now."
        )
        print("")
        print(
            "The gator opens his mouth and grabs onto you and drags you under the water.  You struggle but you can't breathe."
        )
        print("")
        print("☠  You have drowned!! ☠")
    else:
        print("")
        print("*******************************************")
        print("")
        print(
            "You start up the stairs holding your lantern out in front of you.  The stairs wind around and around while you continue up and up.  As you reach the top you enter into the tower chamber of the castle."
        )
        print("")
        input("  (Enter to Continue)")
        print("")
        print(
            "The room is so bright and beautiful.  The room is decorated so elegantly with multi-colored drapes and ribbons.  The wall sparkles with gems that are embeded inside the entire wall of the room."
        )
        print("")
        input("  (Enter to Continue)")
        print("")
        print(
            "There are 3 golden chests in the middle of the room. Around the chests on the floor is writing that is engraved into the floor."
        )
        print("")
        input("  (Enter to Continue)")
        print("")
        print("     'Here lay three chests made of gold'")
        print("     'Only one chest does a treasure it hold'")
        print("")
        print("     'Choose wisely or perish'")
        print("     'Only one can you cherish'")
        print("")
        print("")
        print("")
        print("*******************************************")
        print("")
        third_choice = (
            input("Which chest do you want to open?\n (Left | Center | Right) "
                  )).lower()
        print("")
        print("*******************************************")
        print("")
        if (third_choice == "right") or (third_choice == "r"):
            print("")
            print(
                "You open the chest, and you see the treasure that you have been searching for from the beginning. You have Won!!!! Congrats!!!  Thank you for playing :) "
            )
        elif (third_choice == "left") or (third_choice == "l"):
            print("")
            print(
                "You open the chest, and out rushes a green mist.  The mist fills the room almost immediately, and you find yourself gasping for air in the midst of poisonous gas."
            )
            print("")
            print("☠  You have died!! ☠")
        else:
            print("")
            print(
                "You open the chest, and multiple snake heads pop up and dance around for a moment.  The middle snake lashes out and strikes at you, you swing your sword to cut off its head, but the other two snakes bite your arm in the process."
            )
            print("")
            print("☠  You have died!! ☠")