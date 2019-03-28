import json 
import jieba.posseg as pseg
from json.decoder import JSONDecodeError
import datetime

'''docs = open('sportsnews.txt')
f2 = labels = open('sports_labels.txt','a')

docs_lines = docs.read().split('\n')

train = []
for doc in docs_lines:
    try:
        text = json.loads(doc)['content']
        print(text)
        if text == "":
            continue
        
        text = text[:100]
        words = pseg.cut(text)
        line0 = [] 
        for w in words:
            if 'x' != w.flag:
                line0.append(w.word)
        train.append(' '.join(line0)) 
        f2.write('5'+'\n')
    except JSONDecodeError as e:
        print(doc+'cuowu')

f1 = open('sports_tests.txt','w')
f1.write('\n'.join(train))
f1.close()'''

class dataProcess():
    def __init__(self,docname):
        self.docname = docname
        

    def process(self):
        train = []
        labels =[] 
        docs = open(self.docname)
        

        docs_lines = docs.read().split('\n')

        train = []
        for doc in docs_lines:
            try:
                text = json.loads(doc)['content']
                label = json.loads(doc)['label']
                print(text)
                if text == "" or text == None:
                    continue
                if len(text) > 100: 
                    text = text[:100]
                words = pseg.cut(text)
                line0 = [] 
                for w in words:
                    if 'x' != w.flag:
                        line0.append(w.word)
                train.append(' '.join(line0))
                labels.append(str(label)) 
                #f2.write(str(label)+'\n')
            except JSONDecodeError as e:
                print(doc+'cuowu')

        f1 = open('testdata/testdata.txt','a')
        f2 = open('testdata/testlabel.txt','a')
        f1.write('\n'.join(train))
        f1.write('\n')
        f2.write('\n'.join(labels))
        f2.write('\n')
        f1.close()
        f2.close()


carD = dataProcess('datasource/carnews{}.txt'.format(str(datetime.date.today())))
carD.process()

entD = dataProcess('datasource/entnews{}.txt'.format(str(datetime.date.today())))
entD.process()

moneyD = dataProcess('datasource/moneynews{}.txt'.format(str(datetime.date.today())))
moneyD.process()

'''fashionD = dataProcess('datasource/fashionnews{}.txt'.format(str(datetime.date.today())))
fashionD.process()'''

healthD = dataProcess('datasource/healthnews{}.txt'.format(str(datetime.date.today())))
healthD.process()

itD = dataProcess('datasource/itnews{}.txt'.format(str(datetime.date.today())))
itD.process()

warD = dataProcess('datasource/warnews{}.txt'.format(str(datetime.date.today())))
warD.process()

sportD = dataProcess('datasource/sportnews{}.txt'.format(str(datetime.date.today())))
sportD.process()

travleD = dataProcess('datasource/travelnews{}.txt'.format(str(datetime.date.today())))
travleD.process()

