import random
# or
# from random import randint

class Train:

  def __init__(self, trainNo): # current class object reference self
    self.trainNo = trainNo
  
  def getBook(self, fro, to):
    print(f"your train number: {self.trainNo} from {fro} to {to}")
  
  def getStatus(self):
    print(f"TrainNo: {self.trainNo} is running on time")

  def getFareInfo(self, fro, to):
    print(f"fare of the train: {self.trainNo} from {fro} to {to} price {random.randint(222, 555)}")
    # print(f"fare of the train: {self.trainNo} from {fro} to {to} price {randint(222, 555)}") we already import randint from random

infoTrain = Train(24879)

infoTrain.getFareInfo("kolkata", "bangalore")
infoTrain.getStatus()
infoTrain.getBook("kolkata", "bangalore")