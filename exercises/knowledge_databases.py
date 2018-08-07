from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(wiki_article, topic, rating):
    Knowledge_object = Knowledge(
        Wiki_article= wiki_article,
        topic=topic,
        rating=rating)
    session.add(Knowledge_object)
    session.commit()

add_article("hhhhhhhh", "hehehe", 0)

def query_all_articles():
	articles = session.query(
		Knowledge).all()
	return articles

print("-------------------------------")
print(query_all_articles())

def query_article_by_topic(topicc):
	return session.query(Knowledge).filter_by(
		topic=topicc).all()

print("-------------------------------")
print(query_article_by_topic("WOW"))


def delete_article_by_topic(topicc):
	session.query(Knowledge).filter_by(
		topic=topicc).all().delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).all().delete()
	session.commit()

def edit_article_rating(threshold):
	a=session.query(Knowledge).all()
	b=[]
	for i in range (len(a)):
		if a[i].rating < threshold:
			b.append(a[i])
	return b
print("------------------------------")
print(edit_article_rating(5))

def query_article_by_primary_key(primaryKey):
	return session.query(Knowledge).filter_by(person_id=primaryKey).first()

print("------------------------------")
print(query_article_by_primary_key(2))

def edit_rating(updated_rating, article_title):
	a=session.query(Knowledge).filter_by(topic=article_title).all()
	for i in a:
		i.rating=updated_rating
	session.commit()

edit_rating("WOW",4,"HHHH")
print("----------------------------")
print(query_all_articles())

def delete_article_by_rating(threshold):
	c=edit_article_rating(threshold)
	for i in c:
		session.delete(i)
	session.commit()

def Top_5_ratings():
	order_by(rating(Knowledge.rating))