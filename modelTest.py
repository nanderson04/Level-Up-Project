import tensorflow as tf
import numpy as np 

from spamModel.spam_detector import SpamDetector

spam_model = SpamDetector()

results = spam_model.predict(["Hello world", 
                    "As a valued customer, I am pleased to advise you that following recent review of your Mob No. you are awarded with a £1500 Bonus Prize, call 09066364589",
                    "This is definitely not spam",
                    "XXXMobileMovieClub: To use your credit, click the WAP link in the next txt message or click here>> http://wap. xxxmobilemovieclub.com?n=QJKGIGHJJGCBL", 
                    "Funky shark is a real thing", 
                    "WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.",
                    "Ela kano.,il download, come wen ur free..",
                ])

## Indices: 0 - not spam, 1 - spam, 2 - not spam, 3 - spam, 4 - not spam, 5 - spam, 6 - not spam

print(results)