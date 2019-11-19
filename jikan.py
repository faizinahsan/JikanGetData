import requests
import json

listOfAnime = [11757,34566,2476]
posData = list()
negData = list()

trainDataCount = 0
testDataCount = 0

for idAnime in listOfAnime:
    for i in range(1,11):
        response = requests.get("https://api.jikan.moe/v3/anime/"+str(idAnime)+"/reviews/"+str(i))
        items = response.json()
        reviews = items["reviews"]
        for j in range (0,len(reviews)):
            score = reviews[j]["reviewer"]["scores"]["overall"]
            if score >=7:
                posData.append(reviews[j])
            else:
                negData.append(reviews[j])

    if len(posData) != len(negData):
        # slice data if the data is not the same len
        minDataLen = min(len(posData),len(negData))
        posData = posData[0:minDataLen]
        negData = negData[0:minDataLen]

    trainPosLen = round(len(posData) * 0.7)
    testPosLen = round(len(posData)*0.3)
    trainNegLen = round(len(negData)*0.7)
    testNegLen = round(len(negData)*0.3)
    print(len(posData))
    print(str(trainPosLen)+','+str(testPosLen)+','+str(trainNegLen)+','+str(testNegLen))

    trainPosData = posData[0:trainPosLen]
    testPosData = posData[0:testPosLen]
    trainNegData = negData[0:trainNegLen]
    testNegData = negData[0:testNegLen]
    # The Two Training Data pos or neg is the same len so we use 1 for
    # Training Data
    for i in range(0,len(trainPosData)):
        scorePos = trainPosData[i]["reviewer"]["scores"]["overall"]
        with open("./training/pos/"+str(i+trainDataCount)+"_"+str(scorePos)+".txt","w+",encoding="UTF-8") as f:
            f.write(trainPosData[i]["content"])
        scoreNeg = trainNegData[i]["reviewer"]["scores"]["overall"]
        with open("./training/neg/"+str(i+trainDataCount)+"_"+str(scoreNeg)+".txt","w+",encoding="UTF-8") as f:
            f.write(trainNegData[i]["content"])
    trainDataCount+=len(trainPosData)
    # The Two Test Data pos or neg is the same len so we use 1 for
    # Testing Data
    for i in range(0,len(testPosData)):
        scorePos = trainPosData[i]["reviewer"]["scores"]["overall"]
        with open("./testing/pos/"+str(i+testDataCount)+"_"+str(scorePos)+".txt","w+",encoding="UTF-8") as f:
            f.write(testPosData[i]["content"])
        scoreNeg = testNegData[i]["reviewer"]["scores"]["overall"]
        with open("./testing/neg/"+str(i+testDataCount)+"_"+str(scoreNeg)+".txt","w+",encoding="UTF-8") as f:
            f.write(testNegData[i]["content"])
    testDataCount+=len(testNegData)
    posData.clear()
    negData.clear()
# print(len(scoreList))
# print("Panjang Responses"+str(len(responses)))
# print(responses[0])
# Pengambilan Skor Overall
# responses[index]["reviewer"]["scores"]["overall"]

# for index in range(0,len(responses)):
#     if responses[index]["reviewer"]["scores"]["overall"] > 4:
#         print(responses[index]["reviewer"]["scores"]["overall"])

# Write Data To Text
# score = reviews[2]["reviewer"]["scores"]["overall"]
# line = reviews[2]["content"]
# with open("./textdata/"+str(2)+"_"+str(score)+".txt","w+",encoding="UTF-8") as f:
#     f.write(line)
# # f = open("./textdata/"+str(0)+"_"+str(score)+".txt","w+")
# # f.close()
# print("done")
# Print Content of responses
# print(json.dumps(responses[0]["content"],indent=4,sort_keys=True))
# print(responses)

# print(response['content'])
# print(json.dumps(response.json(),indent=4,sort_keys=True))
# for i in range(1,10):
#  response = requests.get("https://api.jikan.moe/v3/anime/11757/reviews/"+str(i))
#  responses.append(response)
# print(len(responses))
# for i in responses:
#     print(json.dumps(i.json(), indent=4, sort_keys=True))
# print(json.dumps(responses.json(), indent=4, sort_keys=True))
# print(response.status_code)