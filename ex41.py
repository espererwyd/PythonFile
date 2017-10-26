import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = [] #定义空列表WORDS

PHRASES = { #定义字典
    "class %%%(%%%):":
      "Make a class named %%% which is-a %%%.",
    "class %%%(object): \n\t def __init__(self,***)":
      "class %%% has a __init__ which takes self and *** parameters.",
    "class %%%(object): \n\t def ***(self, @@@)":
      "class %%% has a funtion named *** which takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From ***, get the *** function and call it with parameters self and @@@",
    "***.*** = '***'":
      "from ***, get the *** attribute and set it to '***'."
}

# do they want to drill phrases first?
if len(sys.argv) == 2 and sys.argv[1] == "english": #如果参数量为2并且第二个参数为english
    Phrase_First = True #将正确赋值Phrase_First
else:
    Phrase_First = False #否则则将错误赋值于Phrase_First

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #开始循环，对于所有文件中的每一列
    WORDS.append(str(word.strip(), encoding = "utf-8")) #将其用utf-8编码方式加入到WORDS列表中


def convert(snippet, phrase): #定义convert函数，输入条件为snippet和phrase
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))] #查找snippet中"%%%"的个数并在WORDS列表中随机获取相同数量的字符，最后将其首字母大写，赋值给class_names
    other_names = random.sample(WORDS, snippet.count("***")) #查找snippet中"***"的个数并随机获取相同数量的字符，赋值给other_names
    results = [] #定义空列表results
    param_names = [] #定义空列表param_names

    for i in range(0, snippet.count("@@@")): #开始循环，i的取值范围：0到"@@@"在snippet中的个数
        param_count = random.randint(1,3) #对param_count进行随机赋值，范围为1到2
        param_names.append(', '.join(random.sample(WORDS, param_count))) #在WORDS列表中随机取param_count个数，之间加入逗号分隔，并添加到param_names列表中

    for sentence in snippet, phrase: #开始循环：对于snippet和phrase中的每一个sentence变量
        result = sentence[:] #切片复制

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) #将class_names中的单词替换result中的"%%%", 一次替换一个
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1) #将other_names中的单词替换result中的"***"，一次替换一个

        # fake parameter list
        for word in param_names:
            result = result.replace("@@@", word, 1) #将param_names中的单词替换result中的"@@@"，一次替换一个

        results.append(result) #将经由上述过程处理过的result加入到results列表中

    return results #返回results列表

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys()) #将dict PHRASES中的所有键组成一个列表，定义为snippets
        random.shuffle(snippets) #随机抽取snippets中的一个，即为PHRASES中的某一个键

        for snippet in snippets: #开始循环,对于snippets列表中的每一个目标snippet
            phrase = PHRASES[snippet] #将PHRASES字典中对应刚刚随机抽取的snippet键所对应值赋予phrase变量
            question, answer = convert(snippet, phrase) #执行convert函数，将convert的返回值results列表赋值给变量question 和 answer
            if Phrase_First:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer} \n\n")
except EOFError: #End-OF-File Error (CTRL-Z-ENTER)
    print(" \nBYE")
