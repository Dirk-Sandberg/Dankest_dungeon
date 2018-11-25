import sys,time,select
'''
class User():
        def __init__(self):
                self.health = 100
                self.counter = 100
user = User()
'''
def show_target(user,enemy):
        anidle = 0.0
        wind(user)
        os.system('clear')
        display_arrow(user)
        print user.aimer
        print str(enemy.name) + ' has ' + str(enemy.health) + ' health. '
        center = [0,3]
        windtime = 2
        print ''
        print ''
        print '[return] Shoot the arrow! '
        
        while enemy.health > 0:
                time.sleep(0.01)

                incoming = select.select([sys.stdin],[],[],0.0)[0]
                if len(incoming) > 0: # shot the arrow
                        anidle = 0.0
                        aline = sys.stdin.readline()

                        # user takes damage
                        print 'You shot the arrow at ' + str(user.aimer) + '!'
                        dist = distance(user.aimer,center)
                        if dist < 1:
                                print 'Bullseye!'
                                enemy.lose_health(51) # crit damage
                                time.sleep(2)
                                if enemy.health <= 0:
                                        finish_practice(user)
                        if dist >= 1 and dist <= 1.5:
                                print 'Grazing shot. '
                                enemy.lose_health(26)
                                time.sleep(2)
                                if enemy.health <= 0:
                                        finish_practice(user)
                        if dist > 1.5:
                                print 'You missed the target completely. '
                                time.sleep(2)
                        #print 'User lost health. '
                        #user.counter -= 51
                        #testfun(user)
                        break

                anidle += 0.01
                if anidle > windtime: # time expired to shoot arrow
                        
                        print 'User did not lose health. '
                        testfun(user)
                        break

def testtest(user):
        an_idle = 0.0
        windtime = 2
        time.sleep(0.01)
        incoming = select.select([sys.stdin],[],[],0.0)[0]
        if len(incoming) > 0:
                an_idle = 0.0
                aline = sys.stdin.readline()
                print 'User took damage'
                user.health -= 51
                print user.health
                testtest(user)
        an_idle += 0.01
        if an_idle > windtime:
                print 'User did not take damage'
                print user.health
                testtest(user)
while user.health > 0:
        testtest(user)
print 'User has totally died'


''' OLD SHOW_TARGET
'''
def show_target(user,enemy):
    if user.haybailchamp == False:
        wind(user)
        os.system('clear')
        display_arrow(user)
        print user.aimer
        print str(enemy.name) + ' has ' + str(enemy.health) + ' health. '
        center = [0,3]
        windtime = 2 #np.random.rand()
        #thread = threading.Timer(windtime,show_target, [user,enemy])
        #thread.start()
        print ''
        print ''
        print '[return] Shoot the arrow! (Only press once, please.)'
        time.sleep(2)
        
        i = []
        i, o, e = select.select( [sys.stdin], [], [], windtime )
        #a = sys.stdin.readline()
        if (i): #(i) received user input
            #i = []

            #print 'I AM I', i
            #shoot = sys.stdin.readline().strip()
            print 'You shot the arrow! at '+ str(user.aimer)
            #thread.cancel()
            dist = distance(user.aimer,center)
            print 'Distance from center: ', dist
            if dist < 1:
                print 'Bullseye! '
                enemy.lose_health(51) # crit damage
                time.sleep(2)
                if enemy.health <= 0:
                    finish_practice(user)
                    return
                return
                #show_target(user,enemy)
            if dist  >=1 and dist <= 1.5:
                print 'Grazing shot '
                enemy.lose_health(26) # mild hit damage
                time.sleep(2) # TIME
                if enemy.health <= 0:
                    finish_practice(user)
                    return
                return
                #show_target(user,enemy)
            #i = ''
            if dist > 1.5:
                print 'You missed the target COMPLETELY. '
                time.sleep(2) # TIME
                return
                #show_target(user,enemy)
        else: # user input timed out
            print 'k'
            #return
            #show_target(user,enemy)
'''
            '''
        if shoot == '': #got [return] from user
            print 'You shot the arrow! at '+ str(user.aimer)
            #thread.cancel()
            dist = distance(user.aimer,center)
            print 'Distance from center: ', dist
            if dist < 1:
                print 'Bullseye! '
                enemy.lose_health(101) # crit damage
                #time.sleep(2)
                if enemy.health <= 0:
                    finish_practice(user)
                    return
                show_target(user,enemy)
            if dist  >=1 and dist <= 1.5:
                print 'Grazing shot '
                enemy.lose_health(101) # mild hit damage
                #time.sleep(2)
                if enemy.health <= 0:
                    finish_practice(user)
                    return
                show_target(user,enemy)
            if dist > 1.5:
                print 'You missed the target'
                #time.sleep(2)
                show_target(user,enemy)
            '''
        '''    
        if enemy.health <= 0: # end the show_target loop
            user.haybailchamp=True
            print 'haybailchamp?' + str(user.haybailchamp)
            didigethere()
        '''
'''
