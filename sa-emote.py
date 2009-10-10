import smilies
from waveapi import events
from waveapi import model
from waveapi import robot
from waveapi import document

def OnDocumentChanged(properties, context):
  for blip in context.GetBlips():
    UpdateBlip(blip, chop=-1)

def OnBlipSubmitted(properties, context):
  for blip in context.GetBlips():
    UpdateBlip(blip)

def UpdateBlip(blip, chop=0):
  doc = blip.GetDocument()
  doc_text = doc.GetText()
  if chop < 0:
    doc_text = doc_text[:chop]
  
  updates = []
  for text, src in smilies.smilies:
    i = 0
    while doc_text.find(text, i) != -1:
      i = doc_text.find(text, i)
      updates.append((i, text,
                      "http://zeebo-devel.appspot.com/assets/emotes/%s" % src))
      i += len(text)
  
  updates.sort()
  updates.reverse()
  for index, text, src in updates:
    doc.DeleteRange(document.Range(index, index + len(text)))
    doc.InsertElement(index, document.Image(url=src))

if __name__ == '__main__':
  myRobot = robot.Robot('sa-emote', 
      image_url='http://sa-emote.appspot.com/assets/awesome.png',
      version='3',
      profile_url='http://sa-emote.appspot.com/')
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.RegisterHandler(events.DOCUMENT_CHANGED, OnDocumentChanged)
  myRobot.Run()
