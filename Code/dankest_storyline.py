#!/usr/local/bin/python
#Erik Sandberg
#Dankest Dungeon story line
import os
import time
from dungeon_functions import clear

def p(): # press a key
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print ''
    print 'Press [return] to continue.'
    key = raw_input()
    clear()

def archery_intro():
    clear()
    print "Your superboots run out of juice, but fortunately you're safe now. "
    archery()
    p()
    print 'Up ahead a ways you see a small archery range.'
    archery1()
    p()
    print 'A robot greets you. *beep bop*'
    archery2()
    p()
    print '*beep* Hello, traveler. No one has come to visit me for many years. '
    archery2()
    p()
    print  "*boop* I would love to make a new friend. *bop*"
    archery3()
    p()

    
    choice = ''
    while choice == '' or choice == '1' or choice == '2':
        clear()
        print "Perhaps I could invite you to play robo boogie?"
        archery2()
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
        print ''
        print '[1] What is robo boogie? '
        print '[2] What is your name? '
        print '[3] Of course! '
        #p()
        choice = raw_input()
        if choice == '1':
            clear()
            print 'Robo boogie is what humans call "archery", I *boop* believe.'
            archery2()
            p()
        if choice == '2':
            clear()
            print 'My name is "beep"! '
            archery3()
            p()
        if choice == '3':
            clear()
            print '*BEEP BOOP* YAY!'
            archery3()
            p()
            print "I'll teach you how, friendly friend! "
            archery3()
            p()
            print 'Just press the [return] button to shoot the arrow. '
            archery3()
            p()
            print 'The wind is blowing strong today though... It might be hard to aim. '
            archery3()
            p()
            print 'Try to hit the bullseye or spots just around it! '
            archery3()
            p()
        
def archery():
    print ''
    print '        '
    print ' \o/    '
    print '  |     '
    print '_/ l____'
    print ''
    print ''
    print ''
    print ''
def archery1():
    print ''
    print '                    """      """      """      '
    print ' \o/               " . "    " . "    " . "     '
    print '  |                "   "    "   "    "   "     '
    print '_/ l________________"A"______"A"______"A"______'
    print ''
    print ''
    print ''
    print ''
def archery2():
    print ''
    print '      o         o      '
    print '       \       /       '
    print '        -"""""-        '
    print '      /         \      '
    print '     { [?]  [?]  }     '
    print '     |    __     |     '
    print '      H         H      '
    print '       ^---A---^       '
     
def archery3():
    print ''
    print '      o         o      '
    print '       \       /       '
    print '        -"""""-        '
    print '      /         \      '
    print '     { [^]  [^]  }     '
    print '     | . \__/ .  |     '
    print '      H         H      '
    print '       ^---A---^       '





























    
def building():
    print '                         '
    print ' ______________          '
    print '[ ^     .     .]         '
    print '[ .         ~  ]         '
    print '[      []   ___]         '
    print '[      .   |   |         '
    print '[   .      |  .|         '
    print '[_________.|___|         '

def building2():
    print ' ______________          '
    print '[ ^     .     .]         '
    print '[ .         ~  ]         '
    print '[      []   ___]         '
    print '[      .  /|o  |         '
    print '[   .    |./|\ |         '
    print '[________|_|/l_|         '
def building3():
    print '          ~~~~     ~~                  ~~   \ /  '
    print ' ______________             ~~~            - o - '
    print '[ ^     .     .]    ~                       / \  '
    print '[ .         ~  ]                 ~~              '
    print '[      []   ___]                                 '
    print '[      .  /|   |  o7                             '
    print '[   .    |.|   | /|                              '
    print '[________|_|___|./ lv  , . .   V.  , _   .  i    '
def building4():
    print '          ~~~~     ~~                  ~~   \ /  '
    print ' ______________             ~~~            - o - '
    print '[ ^     .     .]    ]~                      / \  '
    print '[ .         ~  O                 ~~              '
    print '[      []   __/0\  --                            '
    print '[      .  /| /000\                         o     '
    print '[   .    |.|  / l   |-                   /|\     '
    print '[________|_|_/   l   _-  , . .   V.  ,   / l.  i '    
def outside_intro():
    clear()
    building()
    p()
    print 'You burst open the dungeon door. A beam of light hits your face.'
    building2()
    p()
    print "You shield your eyes from the harsh sun. You've made it outside. "
    building3()
    p()
    print 'Suddenly, you hear a thunderous crash from the dungeon. A giant has smashed through the wall! '
    building4()
    p()
    print "You're on the run!"
    building4()
    p()
    

def intro():
    clear()
    print 'Ouch... my head really hurts...'
    print ''
    print ''
    p()
    print 'God, what even happened?'
    print ''
    print ''
    p()
    print 'Where the hell am I?'
    print ''
    print ''
    p()
    print 'Last thing I remember was... '
    print ''
    print ''
    p()
    print 'Last thing I remember was... '
    print 'Damn. '
    print ''
    p()
    print 'Last thing I remember was... '
    print 'Damn. '
    print '.'
    p()
    print 'Last thing I remember was... '
    print 'Damn. '
    print '..'
    p()
    print 'Last thing I remember was... '
    print 'Damn. '    
    print '...'
    p()
    print 'I remember! I was walking back from the cliffs.'
    cliffs()
    p()
    print 'But a giant hole in the ground had been covered up!'
    cliffs()
    p()
    print 'I fell through it... but how far down did I go?'
    cliffs2()
    p()
    print 'Best I can remember - really far. '
    cliffs3()
    p()
    print ''
    p()
    print "And now I'm here. God knows where."
    p()
    print "It's a little chilly down here... "
    p()
    print '... and dank. '
    p()
    print 'The floor is tile. Feels like some sort of dungeon.'
    p()
    print '"The dank dungeon".'
    p()
    print 'Hehehe.. '
    p()
    print 'Oooh! The "Dankest dungeon".'
    p()
    print "Yeah, yeah. That's got a nice ring to it. "
    p()
    print 'I suppose I should light a match, huh? '
    p()
    time.sleep(2)
    print ' --->  T H E   D A N K E S T   D U N G E O N  <---'
    time.sleep(3)

def cliffs():
    print '                                   o   '
    print '                                   /|\ '
    print '____________________________._._.__l|  '
    print '       .               .    {   }    ] '
    print '                 .          {   }    ] '
    print '                      .     {   }    ] '
    print '      .                     {   }    ] '
    print '            @               {   }    ] '
    print '                    .       {   }    ] '
    print '               .            {   }    ] '
    print '       v                    {   }    ] '
    print '                 ..         {   }    ] '
def cliffs2():
    print '                                " @$%! "         '
    print '                             \o/         '
    print '____________________________. | .____  '
    print '                            {/ \}    ] '
    print '        ~          .        {   }    ] '
    print '       .                 .  {   }    ] '
    print '                    v       {   }    ] '
    print '              .             {   }    ] '
    print '     .                .     {   }    ] '
    print '                 .          {   }    ] '
    print '         .                  {   }    ] '    
def cliffs3():
    print '                                       '
    print '                                       '
    print '____________________________.   .____  '
    print '        .                   {   }    ] '
    print '   .          .      o      {   }    ] '
    print '   .     (                  {   }    ] '
    print '                 .      ;   {   }    ] '
    print '          .                 {   }    ] '
    print '                            {   }    ] '
    print '   .               .        {\o/}    ] '
    print '                            { | }    ] '    
