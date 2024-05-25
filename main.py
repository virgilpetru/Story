import sys

print('''                  (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\ 
                            (_)                 /  \  /\ 
                    ________[_]________      /\/    \/  \ 
           /\      /\        ______    \    /   /\/\  /\/\ 
          /  \    //_\       \    /\    \  /\/\/    \/    \ 
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \ 
 /\/\/\/       //_______\       \|__|      \ 
/      \      /XXXXXXXXXX\                  \ 
        \    /_I_II  I__I_\__________________\ 
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~''')
print("Welcome to the Cabin in the Woods! ")
print("Your goal is to find the treasure. ")
print("""Your adventure started a few hours ago
and you've lost your map on the difficult road.""")
print("You are now deep into the Enchanted forest")
print("""   
 ^  ^  ^   ^           ^  ^   ^  ^  ^   ^  ^
/|\/|\/|\ /|\         /|\/|\ /|\/|\/|\ /|\/|\ 
/|\/|\/|\ /|\         /|\/|\ /|\/|\/|\ /|\/|\ 
/|\/|\/|\ /|\         /|\/|\ /|\/|\/|\ /|\/|\ """)
forest = input("You see that your path is dividing in two. Where are you heading now? Left or Right? ").lower()
if forest !="left":
    print("You bumped into the hungry trolls, they are going to enjoy you as dinner. GAME OVER!")
    print(""" 
       ,/`|;V\.;
     ,\;`~\,;\;`\,
    /;|\_|,\~/`,\/;,
   `\`/;`\,`;`|;\`\ ' 
   ;|V`,;'|'/'`/'/| \ 
   `/;'|`\V'/;\,\_V/
    `;|\, |;`,_|_,'
       `,`\_\/;'
          \;`/     _____________
        \ \| |    |  WARNING!   |
        _oo| |    |SOME TROLLS! |
        `\.| |    |_____________|
 ---....__/  `\,____  |    |
      _,-'     `-   ""|---.|...""")
    sys.exit()
print("The path you follow takes you to a river but you need to cross it, over here you have to choose: ")
river = input("You can 'take the boat' next to the dock or you can try to 'swim' across ").lower()
if river != "take the boat":
    print("You decided to swim, but the water is full of ferocious crocodiles. GAME OVER!")
    sys.exit()
print("""The boat takes you safely to the other side of the river,
     _
    /|\ 
   /_|_\ 
 ____|____
 \_o_o_o_/
~~ |     ~~~~~
you walk a few steps and you
see the cabin in the woods, but be careful, it is not an ordinary one, it is a magic cabin,
be careful with your next moves!""")
cabin = input("""You are in front of the cabin, but it has 3 front doors. Which one do you choose?
Brown, Green or Black?""" ).lower();
if cabin == "brown":
    print("You choose the wrong door, the witch catches you in a trap. GAME OVER!")
    sys.exit()
elif cabin == "green":
    print("You choose the wrong door, you entered a room full of beasts. GAME OVER!")
    sys.exit()
elif cabin == "black":
    print ("CONGRATULATIONS! The door you picked opens to a room full of gold. You find the treasure!")
    print("""
              .-=========-.
              \ '-=====-' /
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\ """)
else:
    print("GAME OVER!")
