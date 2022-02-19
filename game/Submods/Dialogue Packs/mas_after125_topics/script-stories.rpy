init 5 python:
    addEvent(
        Event(
            persistent._mas_story_database,
            eventlabel="mas_story_mindthegap",
            prompt="Mind the Gap",
            category=[mas_stories.TYPE_NORMAL],
            unlocked=True
        ),
        code="STY"
    )

label mas_story_mindthegap:
    call mas_story_begin
    m 3eud "实际上，这是一个发生在2013年英国伦敦的真实故事."
    m 2dkd "故事开始于一个叫玛格丽特.麦克拉姆的女人，在火车的堤防站中间哭泣。"
    m 2ekd "当别人走近她询问她为什么哭泣时，她问工作人员“声音”去了哪里."
    m 7ekd "她澄清说，她指的是每列火车到达时播放的提示音，警告乘客“小心站台间隙”."
    m 1eka "工作人员向她保证，提示音没有消失，只是在电台升级到新的数字系统时更新到了新的录音."
    m 1tkc "尽管如此，这个解释似乎并没有让她平静下来。{w=0.3}“那个声音，”她解释道，“是我丈夫.”"
    m 1eud "她的丈夫奥斯瓦尔德·劳伦斯（Oswald Laurence）是一位从未成名的演员，他录制了《北线》的所有提示音."
    m 2dkc "奥斯瓦尔德五年前去世了."
    m 2ekc "他们彼此深爱着，他的死使她悲痛万分."
    m 2euc "但有一件事，{w=0.2}在那五年里，{w=0.2}帮助她继续前进."
    m 7eka "每天，当她在上班的路上，她都能在车站听到他的声音.{w=0.3}有时，她会逗留在那里坐下，只是为了听他说那些简短的话."
    m 2dkc "但现在..."
    m 2dkd "工作人员向她表示歉意，但不知道他们是否有权使用旧配音.{w=0.3}他们告诉她，如果找到了，他们会联系她."
    m 7eud "事实证明，许多在该电视台工作的人都有同情心，希望玛格丽特能再多享受一段时间宝贵的记忆."
    m 7ekb "因此，尽管更新档案中的旧记录需要额外的调试才能与当前的系统配合使用，但他们还是让它正常工作了."
    m 3eua "一天，玛格丽特每天上下班时，站台上响起了一个熟悉的声音."
    m 1fkb "“注意空隙，”奥斯瓦尔德说."
    m 1dku "..."
    m 3eka "我说这是一个真实的故事，事实证明，你仍然可以在堤岸站听到那段古老的录音."
    m 3ekb "这是人类善良的一个很好的例子.{w=0.3}恢复一段短得多、质量低得多的录音，员工们不会有多大收获."
    m 1fka "但他们知道失去一个人是什么感觉，知道这让每一张照片、每一段记忆变得多么珍贵."
    m 1dku "这表明人们可以仅仅出于同情和爱而做出不可思议的事情."
    m 1ekbla "这个故事提醒我要珍惜每一刻，不要把我们在一起的任何时间都视为理所当然."
    m 1dkblu "我会永远珍惜你，[player]."
    return
