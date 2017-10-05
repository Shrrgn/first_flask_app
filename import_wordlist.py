
import mmh3
import sqlite3

#dbname = "sowpods.db"
#filename = "sowpods.txt"


def work_with_file(filename,dbname):
	conn = sqlite3.connect(dbname)
	print("File...")
	c = conn.cursor()
	with open(filename) as f:
		for word in f:
			
			if not (word == '' or len(list(word)) != 1):
				word = word.lower()[:-2]  
				hash_1, hash_lang = hashing(word)
				c.execute('''INSERT OR IGNORE INTO word_hash_list (word,hash,hash_lang) 
							VALUES (?, ?, ?)''', (word, hash_1, hash_lang))
			else:
				continue


	print("File closed...")
	conn.commit()
	conn.close()
	print("DB closed...")
	

def hashing(word, mode = None, lang = "en-"):
	if mode == None:
		return (mmh3.hash(word), mmh3.hash(word + lang))
	#if mode == 64:
		#return (mmh3.hash64(word), mmh3.hash64(lang + word))
	if mode == 128:
		return (str(mmh3.hash128(word)), str(mmh3.hash128(lang + word)))

'''
def check_word(word):
	return word if word.isalpha() and word != ''
'''
def create_table(dbname):
	print("Openning table...")
	conn = sqlite3.connect(dbname)
	c = conn.cursor()
	c.execute('''create table word_hash_list(
					word_id integer primary key autoincrement,
					word text unique,
					hash text,
					hash_lang text);''')
	
	conn.close()
	print("Closing table...")

def find_collision(dbname):
	print("Finding collisions...\n")
	conn = sqlite3.connect(dbname)

	print("Collisions for hash:")
	cursor = conn.execute('''SELECT word, count(hash) 
								FROM word_hash_list
								GROUP BY hash
								HAVING count(hash) > 1;''')
	for row in cursor:
		print("Word: {}".format(row[0]))
		print("Count: {}".format(row[1]))

	print("\nCollisions for hash_lang:")

	cursor = conn.execute('''SELECT word, count(hash_lang) 
								FROM word_hash_list
								GROUP BY hash_lang
								HAVING count(hash_lang) > 1;''')
	for row in cursor:
		print("Word: {}".format(row[0]))
		print("Count: {}".format(row[1]))

	print("End of collisions...\n")


def main():
	print("Start...")
	create_table(dbname)
	work_with_file(filename,dbname)
	find_collision(dbname)
	print("Done...")

if __name__ == "__main__":
	main()