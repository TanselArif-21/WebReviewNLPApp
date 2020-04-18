import WebScraper
import TopicModeling
import string
import random
import os
import Directory

def return_something():
	return 200


def LDA(site, inurl1, inurl2, increment_string1, increment_string2, total_pages, increment,filename=''):
	'''
	Description: This function accepts a dataframe of house prices and a user provided list to predict the sales price for
	df: a data frame
	ls: a list containing the information for a house to predict for
	'''

	#inurl1 = "https://www.tripadvisor.co.uk/Attraction_Review-g190384-d6755801-Reviews"
	#inurl2 = "-The_House_of_Dionysus-Paphos_Paphos_District.html"

	ms = WebScraper.WebScraper(site=site,url1=inurl1,
						  url2=inurl2,increment_string1=increment_string1,increment_string2=increment_string2,
						  total_pages=int(total_pages),increment=int(increment),silent=False)

	ms.fullscraper()

	filePath = Directory.outputPath
	if filename=='':
		for i in range(4):
			filename = filename + random.choice(string.ascii_letters)

	myTopicModel = TopicModeling.TopicModeling(ms.all_reviews)
	
	myTopicModel.ldaFromReviews()
	myTopicModel.generate_wordcloud()
	myTopicModel.saveLDA(os.path.join(filePath,'templates/LDAhtmls',filename + '1' + '.html'))
	myTopicModel.saveWordcloud(os.path.join(filePath,'static',filename + '2' + '.png'))
	
	del myTopicModel

	# # Return the predicted Sale Price
	return None
