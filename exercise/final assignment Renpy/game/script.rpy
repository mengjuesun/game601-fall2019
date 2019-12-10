# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e0 = Character(" ")
define e1 = Character("Bohu Tang")
define e2 = Character("Autumn")
define e3 = Character("Mother")
define e4 = Character("Officer")
define e5 = Character("Robbers")
define e6 = Character("Lord Ning")
define e7 = Character("Evil Scholar")
define e8 = Character("Doctor")
define e9 = Character("Zhu")
define e10 = Character("Wen")
define e11 = Character ("Servant")
define e12 = Character("Madam Hua")
define e13 = Character("General Hua")
# The game starts here.


label start:

    $ lovepoints = 0

    scene 院落场景 with fade

    play sound "beginning.mp3"

    show 唐伯虎1 at truecenter with dissolve

    # These display lines of dialogue.


    e0 "This man named Bohu Tang, he is a painter, a calligrapher and a poet. People call him the gifted scholar of southeast China."
    e0 "People know him is not only because of his talent, but also because of his passionate: he has eight lovers. However, what he really wants to have is a wife who can understand his talent and value him..."

    hide 唐伯虎1

    stop sound

    e0 "One day, Bohu Tang is reading the poet in the home..."
    show 唐伯虎1 at right
    show 妈妈 at left
    play sound "trouble.mp3"

    e3 "Bohu, bad things happened! Lord Ning's officer came find you"
    e1 "Lord Ning? The brother of the emperor? What he wants from me?"
    e3 "I heard that recently Ning planning to betrayed the emperor, maybe he wants you to join his team."
    e1 "I won't let that happened..."

    menu:
        "To see those people":
             jump meeting

        "Hide in your bedroom":
             jump bedroom

    return


label bedroom:
    scene 监狱 with dissolve
    e0 "These people catch Bohu and send him to jail because he resist Lord Ning's order."
    jump start


label meeting:
    show 唐伯虎1 at right with dissolve
    e1 "If I don't meet them, they may kill us... Let's go mom."

    scene 唐伯虎家门口
    show 军官 at left with dissolve
    e4 "Bohu Tang! Lord Ning wants you to be our staff officer. You must come with us today!"
    show 唐伯虎1 at right with dissolve
    e1 "Officer, thanks for the appreciation of Lord Ning. However, I have a very serious illness and the doctor said I might dead soon..."
    e4 "emmm, that's interesting... Because almost everyone invited by our Lord Ning said that they were sick."
    e4 "Don't worried, Bohu. I brought a doctor and let him see how sick you are!"
    e1 "..."
    hide 军官 with dissolve
    hide 唐伯虎1 with dissolve

    scene 卧室
    show 军官 at left with dissolve
    e4 "Doctor, is Bohu Tang sick?"
    show 医生
    e8 "emmm, looks everything is fine."
    e4 "Oh? Ha ha"
    hide 医生
    hide 军官

    menu:
        "Use your Kong fu to change your pulse":
         jump illness

        "Sophistry situation":
         jump Sophistry

    return

label Sophistry:
    show 唐伯虎1 at right
    e1 "Officer, maybe there is something wrong with your doctor. I really have a serious illness! You must trust me!"
    show 军官 at left
    e4 "No need! You dare to disobey Lord Ning's order, go to prison boy!"
    scene 监狱 with dissolve
    e0 "These people catch Bohu and send him to jail because he resist Lord Ning's order."
    jump start

label illness:
    show 医生 at right
    e8 "Waaait! I feel something... Oh my god, Bohu Tang's pulse is very chaotic!"
    show 军官 at left
    e4 "what???"
    hide 医生
    hide 军官
    show 唐伯虎1 at right
    e1 "I told you. I'm very sick now."
    show 医生 at left
    e8 "Bohu Tang, I think maybe you should prepare your funeral now. Goodbye."
    hide 医生
    show 军官 at left
    e4 "Hum! I really shouldn’t be here to waste time, let ’s go soldiers!"
    hide 军官
    e1 "..."
    e1 "(Huh, it's really thrilling)"

    show 妈妈 at left with dissolve
    e3 "Bohu! Kneel!"
    e1 "Mother?"
    e1 "(Kneel)"
    e3 "Do you remember what you promised to you father before he died?"
    e3 "You promised that you will never reveal your kong fu again because it may be discovered by our Tang family's enemies"
    e1 "I know mother, but who are our enemies? You never tell me."
    e3 "Our Tang family's have two enemies. One is general Hua's wife, who is now living in family Hua's mansion. She loved your father when she was young but your father only loves me."
    e1 "..."
    e3 "Another enemy is the person who called Evil Scholar. He and your father used to compete for first place in the Kung Fu Leaderboard. However, your father is beated by Evil Scholar because he used hidden weapons."
    e3 "After that, your father depressed every day until death..."
    e1 "Mother..."
    e1 "Don't worried, I will be careful in the future."
    stop sound
    jump Autumn

label Autumn:
    scene 桥 with fade
    play sound "spring.mp3"
    e0 "Today is the first day of spring. You and your scholar friends are chatting and playing on the bridge."
    show 唐伯虎1 at right
    e1 "We finally have time to meet each other. I have recently painted at home nad I have no time to travel at all. We really should have fun today."
    show 祝枝山 at left
    e9 "Hahahaha, Come on brother Tang. Be honest to us, which lover did you seeing recently?"
    e1 "...No one. They never make me happy anymore, because they only care about material life but never care about the inner."
    show 文征明 at center
    e10 "Don't be depressed my friend. I heard that today family Hua The Hua family is going to the temple. Maybe we should go and see"
    e9 "Yes! I heard it too! And each of Mrs. Hua's four maids is beautiful. Their names are Spring, Summer, Autumn and Winter."
    e9 "Especially Autumn, I heard that she just like an angel from heaven. Besides, she also loves poet and painting."
    e10 "I can't wait! Let's go!"
    e1 "okay,fine..."

    scene 相遇 with fade
    show 秋香 at left with dissolve
    e2 "Don't worried, everyone has foods~"
    e0 "(Poor kids: Thank you... We didn't eat anything for few days...)"
    e2 "Oh... poor kids. I promise to you that I will bring foods here for you often."
    show 唐伯虎1 at right with dissolve
    e1 "excuse me my lady, I just saw you gave foods to these poor kids. May I ask if they are your families?"
    e2 "No sir, I'm not familiar with these kids. I came to temple and I found these kids are begging for foods, so I bought some dumplings for them."
    e1 "...You are really a beautiful girl with a kind heart."
    e2 "(laugh) It's almost evening, I must go now. Farewell, sir."
    e1 "...Farewell, my lady."
    e1 "!!! Can I ask your name?!"
    e2 "My name is Autumn."
    hide 秋香 with dissolve
    e1 "!!!"
    show 祝枝山 at left with dissolve
    show 文征明 at center with dissolve
    e9 "We met so many beautiful girls. What about you Bohu?"
    e1 "......"
    e10 "Bohu?"
    e1 "Oh, I'm sorry I didn't notice you two..."
    e10 "What happenend?"
    e1 "Well... I think I met an angel."
    stop sound
    jump story

label story:

    $ lovepoints = 0

    scene 华府 with fade
    play sound "makeup.mp3"
    e0 "You came to the mansion of Hua familiy."
    menu:
        "Go straight to the door and shout Autumn":
         $ lovepoints -= 10

         show 唐伯虎1 at right
         e0 "(Peng peng peng!!!)"
         e1 "I want to meet lady Autumn! I want to meet lady Autumn!"
         show 武状元 at left
         e11 "Why there always man to bother lady Autumn?!!"
         e1 "..."
         e11 "Catch him brothers, put this guy in the chalet!"
         scene 柴房
         e0 "You are outnumbered and locked in the chalet. You agreed their conditions and they released a few days later."
         e0 "Autumn also heard about your rude behaviors."
         jump Hua

        "Make up first":
         $ lovepoints += 20

         show 唐伯虎2 at right
         show 祝枝山 at left
         e9 "Bohu, this is the mansion of general Hua. I already use many ashes to helped you makeup. Now your cloth is just like poor people's cloth."
         e1 "Thank you Zhu. I will never leave Hua familiy till I married Autumn!"
         hide 祝枝山 with dissolve
         show 秋香 at left with dissolve
         e2 "Are you looking for a job? Wait, I know you, aren't you the man I saw at the temple few days ago? Why did you come here to work?"
         e1 "To be honest, I've already been impoverished and relying on my mother to support me."
         e1 "I felt so ashamed because that day I saw you helped others even if you are just a weak woman, and I'm still relying on my mother even if I'm a young man"
         e1 "That's why I determined that I couldn't live like this anymore, I decided to find a job to support my family."
         e2 "I'm glad you can realize the mistake, everyone commit errors. You can be a servant here later."
         e2 "And, what's your name?"
         e1 "...My name is An"
         jump Hua
    return
    stop sound

label Hua:
    scene 华府院子 with fade
    play sound "garden.mp3"
    e0 "You become a servant of family Hua, now you have more chance to meet Autumn."
    show 秋香 at left with dissolve
    e2 "This poet is so beautiful..."
    show 唐伯虎3 at right with dissolve
    e1 "Hi Autumn, what're you doing?"
    e2 "An~ I am reading Bohu Tang's poems. He is the poet I admire most. Do you know him?"
    menu:
        "I don't know him":
         $ lovepoints += 10
         e1 "emmm... I don't know this guy. Anyway, take a break Autumn. Let's fly a kite!"
         jump night

        "I know him":
         $ lovepoints += 20
         e1 "Yes, I know him. He is also a famous painter. I also have his painting, Bamboo In A Spring Thunderstorm."
         e2 "Wow An, You do know him! Can I see the painting?"
         e1 "Here it is."
         show 竹子画 at truecenter with dissolve
         e2 "...What an amazing painting..."
         e1 "It is. I never want to sell this painting because Bohu Tang is also my favourite scholar and I valued his work so much."
         e2 "(She seems very happy)"
         jump night

    return
    stop sound

label night:
    scene 夜路 with fade
    play sound "Night.mp3"
    e0 "This evening..."
    show 唐伯虎3 at right with dissolve
    e1 "(walking) Ha, cool nights are best for walking~~"
    e0 "(Noise)"
    show 强盗 at left
    e5 "Stop! Boy! Who are you?"
    e1 "!!! (robbers?) Don't hit me brothers! I'm just a servant of family Hua."
    e5 "We are the most vicious robbers in this area and we want to rob Autumn as our leader's new wife!"
    e5 "Now, you have two choices. One is lead us to Autumn's room, another is killed by us."
    e1 "(I can't show my Kong Fu now and they are too many people, I must wait for chance)"
    e1 "Okay brothers, I will show you the road."
    e1 "Let me trick her out of the house so there is no sounds."
    e5 "emmm... Okay, but be fast!"
    hide 强盗
    hide 唐伯虎3

    scene 秋香卧室
    show 秋香 at left
    e2 "(singing)"
    show 唐伯虎3 at right
    e1 "Autumn!"
    e2 "!!!An? You scared me!"
    e1 "I'm sorry, but there's no time to explain. You must leave now! Quickly! Use the window!"
    e2 "What happened?? Why?!"
    hide 唐伯虎3
    show 秋香 at right
    show 强盗 at left
    e5 "Hahahha! Go with us Autumn. You're really a beauty~~"
    e2 "Who are you?! What you want?"
    e5 "Our boss wants to invite you to be his wife!"
    e0 "   (Robbers catch Autumn)   "
    e2 "!!! Help!!!"
    stop sound
    hide 秋香
    menu:
        "Beat those robbers":
         $ lovepoints += 20
         show 唐伯虎3 at right
         e1 "(Use a wooden stick)Stop you bastards! Don't you want to take Autumn away!"
         jump misunderstanding

        "Wait for your chance":
         $ lovepoints -= 10
         jump misunderstanding

    return

label misunderstanding:
    hide 唐伯虎3
    show 武状元 at right
    e11 "Who is making the noise?!"
    e11 "You robbers! None of you can run out of this house!"
    hide 武状元
    hide 强盗
    e0 "(After a while, you and this servant caught these robbers)"
    scene 大厅
    show 秋香 at right
    e2 "Madam!"
    show 华夫人 at left with dissolve
    e12 "I already know what happened. Don't worried Autumn, I will punish those robbers."
    e2 "...Thank you madam"
    hide 秋香 with dissolve
    e12 "However, I really want to ask how did those robbers slip into our house?"
    show 武状元 at right with dissolve
    e11 "... I'm so sorry madam. Oh! I saw An with them!"
    hide 武状元
    show 唐伯虎3 at right
    e1 "What???"
    e12 "In that case, get him to jail too!"
    hide 唐伯虎3
    show 秋香 at right
    e2 "Wait madam! An is the one who tried to warn me and help me to escape, and he also fought with those robbers."
    e2 "I think they caught him first. He is not a bad guy."
    hide 秋香
    show 唐伯虎3 at right
    e1 "it's my duty to protect ladies, espically you, Autumn."
    e12 "Alright, since Autumn said everything, I'll let you go. Thank you An."
    e1 "It's my pleasure, madam"

    scene 大厅 with fade
    play sound "Lord Ning.mp3"
    e0 "One afternoon..."
    show 华太师 at right
    show 武状元 at left with dissolve
    e11 "Madam! Lord Ning comes!"
    hide 武状元
    e13 "What he wants..."
    show 华夫人 at center with dissolve
    e12 "He must wants to borrow your soldiers. Be careful, don't let him find excuses to embarrass you."
    hide 华夫人
    show 宁王 at left with dissolve
    e6 "Hahahahhahahaha, general Hua and madam Hua, long time no see!"
    e13 "Lord Ning, we are so honored that you be here."
    e6 "General, I heard that you always love paintings, today I came here to send you a painting of Bohu Tang."
    e13 "Thank you my lord, but..."
    e6 "You're welcome! Evil scholar, show them the painting!"
    e13 "..."
    hide 宁王
    show 夺命书生 at left
    e7 "General, madam, please enjoy!"
    hide 夺命书生
    show 假画 at truecenter
    show 宁王 at left
    e6 "Gneral, you took my gift, I think it means you agree my terms about military!"
    hide 假画 with dissolve
    e13 "What? It's nonsense!"
    e6 "I'm nonsense?! How dare you! Maybe you live long enough, general Hua!"
    show 唐伯虎3 at center
    e1 "Wait my Lord! I noticed that your painting of Bohu Tang seems like a fake. You can't fool our general with a fake picture!"
    e13 "An?!"
    e6 "Who are you, boy?!"
    e1 "I'm just a servant, but I know paintings since I was a little boy. I'm sure that painting is a fake one!"
    e1 "Because we always have a real painting of Bohu Tang in this manison!"
    e13 "!!!"
    e6 "!!!"
    e6 "Okay, then take the painting out and let us enjoy it! If your painting is real, I'll never bother you again, but if you lies... I'll send you all to hell!"
    e1 "Deal, my lord! Autumn, come with me to the study room."
    stop sound

    scene 书房
    play sound "painting.mp3"
    show 唐伯虎3 at right with dissolve
    show 秋香 at left with dissolve
    e2 "An! What are you doing! Why you said we have Bohu Tang's painting?!"
    menu:
        "Take out your fan painting":
         $ lovepoints += 10
         e2 "The fan painting? You sure you're going to use this?"
         e1 "Yes, I will use everything to save you all"
         jump realpainting

        "Paint a new one right now":
         $ lovepoints += 20
         e1 "(Painting...)"
         e2 "Do you listen to me?! You did a terrible disaster, we are all going to die... "
         e2 "Now there's no one outside, maybe you should go. Just run away, An, as far as you can!"
         show 真画 at truecenter
         e2 "!!!!!"
         e2 "You draw this? In such a short time?"
         e1 "I have been selling fake paintings of Bohu Tang for a while. I should have cheated them."
         e1 "Let's go!"
         e2 "..."
         jump realpainting
    return

label realpainting:
    scene 大厅 with fade
    show 唐伯虎3 at right
    show 宁王 at left
    show 真画 at truecenter
    e1 "this is a real painting of Bohu Tang"
    e6 "... Evil scholar! Come and see!"
    hide 真画
    show 夺命书生 at center
    e7 "..."
    e7 "My lord, it is a real painting of Bohu Tang."
    e6 "What?!!!"
    e1 "I told you. So, please leave now, my lord."
    e7 "...Alright, I remember you, boy."
    hide 夺命书生
    hide 宁王
    stop sound

    show 华夫人 at left with dissolve
    show 秋香 at center with dissolve
    e1 "Madam?"
    e12 "It's you! Bohu Tang!"
    e2 "!!!"
    e1 "I'm not!"
    e12 "Come on! Stop lying! I should have found out. I can never forget this face."
    e12 "Servant! Take him to the chalet!"
    e2 "Madam please! He saved us after all..."
    e12 "Shout up Autumn! Family Tang is always our enemy!"
    e2 "..."
    e1 "Don't worried Autumn!"
    hide 华夫人
    hide 秋香
    hide 唐伯虎3

    scene 柴房 with fade
    e0 "You were held here for two days..."
    show 唐伯虎3 at right
    play sound "evil scholar.mp3"
    e0 "   (Noise)   "
    show 秋香 at left
    e2 "Bohu! Evil Scholar breaks in and he hurts general Hua! He said it is the punishment from Lord Ning."
    e1 "What? Rlease me Autumn! I will go to there soon. You need to take care of others now."

    scene 大厅 with dissolve
    show 夺命书生 at left
    show 华太师 at right
    e7 "Hahahahha! You weak people are not worth living!"
    e13 "You..."
    e7 "Let me send you to hell, old man."
    stop sound
    hide 华太师
    show 唐伯虎1 at right
    play sound "hero.mp3"
    e1 "Evil scholar! Today is your death!"
    e7 "Oh? That young servant."
    e1 "Open your eyes, you bastard! You beat my father with a hidden weapon years ago, but can you beat me now?"
    e7 "It ’s you! Son of that old bastard! No wonder I look familiar!"
    e1 "Stop talking nonsense!"
    hide 唐伯虎1
    hide 夺命书生
    e0 "After a long fight, your spear finally stuck in the chest of a Evil Scholar..."
    show 夺命书生 at left with dissolve
    show 唐伯虎1 at right with dissolve
    e7 "......you little bastard...I will..."
    e7 "(Died)"
    hide 夺命书生
    e1 "Father, can you see it? I have revenge for you."

    show 华夫人 at left with dissolve
    show 秋香 at center with dissolve
    e2 "Bohu! Thank you!"
    e2 "(She hugs you)"
    e12 "Bohu Tang. I know we had some history in the past, but it is between me and your father."
    e12 "Today, you use your own actions to show that you are a very good young man and a forever friend of family Hua. So, what reward do you want?"
    e1 "Well... I..."
    e12 "I know what you think~ You love Autumn, right? Then I will marry her to you!"
    e2 "Madam~~"
    e12 "Bohu Tang, would you like to marry Autumn now or spend more time with her then decide?"
    stop sound
    menu:
        "I can't wait, I will marry her now!":
         $ lovepoints += 20
         jump ending

        "Maybe it's good for us to wait spend more time together.":
         $ lovepoints += 10
         jump ending

    return

label ending:
    if lovepoints >= 80:
         scene 结婚 with fade
         play sound "ending1.mp3"
         show 唐伯虎1 at right with dissolve
         show 秋香结婚 at left with dissolve
         e0 "You successfully married Autumn in the end and live a happy life ever since"
         jump end

    if lovepoints < 80:
         scene 华府院子 with fade
         play sound "ending2.mp3"
         show 秋香 at left with dissolve
         show 唐伯虎1 at right with dissolve
         e0 "Although Autumn wants to marry you, but she also think it is good for both of you to know more about each other."
         e0 "You two draw and read poems every day. As time goes by, she is more like your best friend. You think you finally found someone who understands you."
         jump end

label end:
    scene 结束
    stop sound
