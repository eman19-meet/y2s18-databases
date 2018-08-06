from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'Knowledge'
	person_id= Column(Integer, primary_key=True)
	Wiki_article= Column(String) 
	topic=Column(String)
	rating=Column(Integer)

	def __repr__(self):
		if self.rating>=7:
			return("{} . If you want to learn about : {} , you should look at the Wikipedia article called : {} , "
					"We gave this article a rating of:  {} out of 10!").format(self.person_id ,self.topic, self.Wiki_article, self.rating)
		else:
			return("{} . If you want to learn about : {} , you should look at the Wikipedia article called : {} , "
					"We gave this article a rating of:  {} out of 10! "
					"Unfortunately, this article does not have a better rating. Maybe, this is an article that should be"
					"replaced soon!.").format(self.person_id ,self.topic,  self.Wiki_article, self.rating)

a1= Knowledge(person_id=1, Wiki_article="blablabla", topic="WOW", rating=10)
a2= Knowledge(person_id=2, Wiki_article="hahaha", topic="YAHOO", rating=3)

print(a1)
print("----------------------------")
print(a2)
