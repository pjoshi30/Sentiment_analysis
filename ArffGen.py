TopWords = {}

def genTopWords():
    count = 0
    file = open("/preetam/NLP/Assignment2/twitterdata.2009.05.25.c/sortedTable.txt")
    for i in range(0, 5000):
        line = file.readline();
        tmp = line.strip().split(" ")
        TopWords[tmp[0]] = count
        count = count + 1
    file.close()
    return True


def genHeaderARFF():
    file_ARFF = open("/preetam/NLP/Assignment2/twitterdata.2009.05.25.c/baseline.arff","w")
    file_ARFF.write("@relation sentiment_baseline\n")
    for var in TopWords.keys():
        temp = "@attribute "+var+" {0,1}"
        file_ARFF.write(temp)
        file_ARFF.write("\n")
    file_ARFF.write("@attribute Sentiment {0,4}")
    file_ARFF.write("\n")
    file_ARFF.write("@data")
    file_ARFF.write("\n")
    file_ARFF.close()
    return True

def genDataSegment():
    file = open("/preetam/NLP/Assignment2/twitterdata.2009.05.25.c/train.40000.2009.05.25")
    file_ARFF = open("/preetam/NLP/Assignment2/twitterdata.2009.05.25.c/baseline.arff","a")
    while 1:
        line = file.readline()
        if not line:
            break
        tmp = line.strip().split(" ")
        tmp1 = tmp[0].split(";;")
        Sentiment = tmp1[0]
        temp = "{"
        TopWord_map = {}
        for var in tmp:
            if TopWords.has_key(var):
                if not TopWord_map.has_key(TopWords[var]):
                    TopWord_map[TopWords[var]] = 1
        TopWord_Array = TopWord_map.keys()
        TopWord_Array.sort()
        for gvar in TopWord_Array:
            temp = temp + str(gvar)+" "+"1, "
        last = len(TopWords)
        #last = last + 1
        temp = temp + str(last) + " "+Sentiment+"}"
        file_ARFF.write(temp)
        file_ARFF.write("\n")
    file.close()
    file_ARFF.close()
    return True

if __name__=="__main__":
    #Calculate the top 5000 frequent words
    genTopWords()
    #Generate the ARFF file with header first
    genHeaderARFF()
    #and then the data segment..
    genDataSegment()

    
