import json
file_name = "ItemData.json"
with open(file_name, "r") as openfile:
    item_list = json.load(openfile)


# item_list1 = {"000004": {"type": "customer", "details": ["Benson", "Kyla", "Ahad Ha'am Street 5/22, Haifa"], "location": "address", "value": ""}, "000005": {"type": "customer", "details": ["Singh", "Stacey", "Arlozorov Street 3/32,  Haifa"], "location": "address", "value": ""}, "000006": {"type": "customer", "details": ["Townsend", "Miah", "Ben Gurion Avenue 8/40,  Haifa"], "location": "address", "value": ""}, "000007": {"type": "customer", "details": ["Gallegos", "Lucie", "Ha'Atzma'ut Street‎  12/56,  Haifa"], "location": "address", "value": ""}, "000008": {"type": "customer", "details": ["Gilbert", "Alisha", "HaHagana Street 11/34,  Haifa"], "location": "address", "value": ""}, "000009": {"type": "customer", "details": ["Klein", "Kayleigh", "HaNadiv Avenue‎  5/18,  Haifa"], "location": "address", "value": ""}, "000010": {"type": "customer", "details": ["Rosales", "Haris", "HaNamal Street‎  8/33,  Haifa"], "location": "address", "value": ""}, "000011": {"type": "customer", "details": ["Montes", "Ronan", "Haneviim Street 13/33,  Haifa"], "location": "address", "value": ""}, "000012": {"type": "customer", "details": ["Crane", "Carolyn", "Hassan Shukri Street‎  11/48,  Haifa"], "location": "address", "value": ""}, "000013": {"type": "customer", "details": ["Goodman", "Matteo", "HaZevi Avenue‎  13/41,  Haifa"], "location": "address", "value": ""}, "000014": {"type": "customer", "details": ["O'Brien", "Anas", "HaZiyonut Avenue‎  9/15,  Haifa"], "location": "address", "value": ""}, "000015": {"type": "customer", "details": ["Howell", "Levi", "Herzl Street 5/35,  Haifa"], "location": "address", "value": ""}, "000016": {"type": "customer", "details": ["Thomson", "Amanda", "Jaffa Street 5/1,  Haifa"], "location": "address", "value": ""}, "000017": {"type": "customer", "details": ["Fischer", "Roseanna", "Jerusalem Street 13/32,  Haifa"], "location": "address", "value": ""}, "000018": {"type": "customer", "details": ["Le", "Krishan", "Yitzhak Avenue‎  10/39, Haifa"], "location": "address", "value": ""}, "000019": {"type": "customer", "details": ["Carter", "Cynthia", "Louis Promenade‎  4/58,  Haifa"], "location": "address", "value": ""}, "000020": {"type": "customer", "details": ["Barker", "Woody", "Maale Hashihrur Street‎  3/60,  Haifa"], "location": "address", "value": ""}, "000021": {"type": "customer", "details": ["Villegas", "Henrietta", "Masada Street 7/39,  Haifa"], "location": "address", "value": ""}, "000022": {"type": "customer", "details": ["Bowers", "Ruairi", "Nathanson Street‎  3/38,  Haifa"], "location": "address", "value": ""}, "000023": {"type": "customer", "details": ["Pennington", "Dewey", "Sderot haNassi 3/32,  Haifa"], "location": "address", "value": ""}}
# item_list2 = {"000001": {"type": "library", "details": ["City Library ", "Shivat Zion Street‎  12, Haifa"], "location": "address", "value": ""}, "000002": {"type": "library", "details": ["City Library ", "Sirkin street 14, Kiryat Yam"], "location": "address", "value": ""}, "000003": {"type": "library", "details": ["City Library ", "Yefe Nof street‎  9, Tirat Hacarmel "], "location": "address", "value": ""}}
# item_list3 = {"000024": {"type": "book", "details": ["Don Quixote", "Miguel de Cervantes", "Action & Advetnure", "English", "1983"], "value": "80"}, "000025": {"type": "book", "details": ["The Adventures of Huckleberry Finn", "Mark Twain", "Action & Advetnure", "English", "1990"], "value": "82"}, "000026": {"type": "book", "details": ["The Adventures of Tom Sawyer", "Mark Twain", "Action & Advetnure", "English", "1950"], "value": "113"}, "000027": {"type": "book", "details": ["Treasure Island", "Robert Louis Stevenson", "Action & Advetnure", "English", "2010"], "value": "119"}, "000028": {"type": "book", "details": ["The Call of the Wild", "Jack London", "Action & Advetnure", "English", "2009"], "value": "85"}, "000029": {"type": "book", "details": ["White Fang", "Jack London", "Action & Advetnure", "English", "1943"], "value": "82"}, "000030": {"type": "book", "details": ["Kim", "Rudyard Kipling", "Action & Advetnure", "English", "1854"], "value": "114"}, "000031": {"type": "book", "details": ["Around the World in Eighty Days", "Jules Verne", "Action & Advetnure", "English", "1890"], "value": "81"}, "000032": {"type": "book", "details": ["Robinson Crusoe", "Daniel Defoe", "Action & Advetnure", "English", "1880"], "value": "78"}, "000033": {"type": "book", "details": ["Hatchet", "Gary Paulsen", "Action & Advetnure", "English", "1960"], "value": "98"}, "000034": {"type": "book", "details": ["On the Road", "Jack Kerouac", "Autobiographical", "English", "1983"], "value": "106"}, "000035": {"type": "book", "details": ["The Sorrows of Young Werther", "Johann Wolfgang von Goethe", "Autobiographical", "English", "1990"], "value": "102"}, "000036": {"type": "book", "details": ["Remembrance of Things Past", "Marcel Proust", "Autobiographical", "English", "1950"], "value": "75"}, "000037": {"type": "book", "details": ["Little House on the Prairie", "Laura Ingalls Wilder", "Autobiographical", "English", "2010"], "value": "95"}, "000038": {"type": "book", "details": ["Swann's Way", "Marcel Proust", "Autobiographical", "English", "2009"], "value": "100"}, "000039": {"type": "book", "details": ["On the Banks of Plum Creek", "Laura Ingalls Wilder", "Autobiographical", "English", "1943"], "value": "105"}, "000040": {"type": "book", "details": ["The Long Winter", "Laura Ingalls Wilder", "Autobiographical", "English", "1854"], "value": "103"}, "000041": {"type": "book", "details": ["By the Shores of Silver Lake", "Laura Ingalls Wilder", "Autobiographical", "English", "1890"], "value": "96"}, "000042": {"type": "book", "details": ["Alice's Adventures in Wonderland", "Lewis Carroll", "Fantasy", "English", "1880"], "value": "106"}, "000043": {"type": "book", "details": ["Gulliver's Travels", "Jonathan Swift", "Fantasy", "English", "1960"], "value": "108"}, "000044": {"type": "book", "details": ["The Hobbit, or, There and Back Again", "J.R.R. Tolkien", "Fantasy", "English", "1983"], "value": "100"}, "000045": {"type": "book", "details": ["The Return of the King", "J.R.R. Tolkien", "Fantasy", "English", "1990"], "value": "116"}, "000046": {"type": "book", "details": ["The Wizard of Oz", "L. Frank Baum", "Fantasy", "English", "1950"], "value": "119"}, "000047": {"type": "book", "details": ["The Wind in the Willows", "Kenneth Grahame", "Fantasy", "English", "2010"], "value": "78"}, "000048": {"type": "book", "details": ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", "English", "2009"], "value": "97"}, "000049": {"type": "book", "details": ["The Lion, the Witch, and the Wardrobe", "C.S. Lewis", "Fantasy", "English", "1943"], "value": "94"}, "000050": {"type": "book", "details": ["Peter Pan", "J.M. Barrie", "Fantasy", "English", "1854"], "value": "85"}, "000051": {"type": "book", "details": ["Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fantasy", "English", "1890"], "value": "84"}, "000052": {"type": "book", "details": ["Pride and Prejudice", "Jane Austen", "Romance", "English", "1880"], "value": "85"}, "000053": {"type": "book", "details": ["Jane Eyre", "Charlotte Brontë", "Romance", "English", "1960"], "value": "119"}, "000054": {"type": "book", "details": ["Anna Karenina", "Leo Tolstoy", "Romance", "English", "1983"], "value": "94"}, "000055": {"type": "book", "details": ["Sense and Sensibility", "Jane Austen", "Romance", "English", "1990"], "value": "110"}, "000056": {"type": "book", "details": ["Persuasion", "Jane Austen", "Romance", "English", "1950"], "value": "110"}, "000057": {"type": "book", "details": ["Mansfield Park", "Jane Austen", "Romance", "English", "2010"], "value": "71"}, "000058": {"type": "book", "details": ["Far from the Madding Crowd", "Thomas Hardy", "Romance", "English", "2009"], "value": "70"}, "000059": {"type": "book", "details": ["The Return of the Native", "Thomas Hardy", "Romance", "English", "1943"], "value": "106"}, "000060": {"type": "book", "details": ["Northanger Abbey", "Jane Austen", "Romance", "English", "1854"], "value": "97"}, "000061": {"type": "book", "details": ["Love in the Time of Cholera", "Gabriel García Márquez", "Romance", "English", "1890"], "value": "94"}}


# item_list1.update(item_list2)
# item_list1.update(item_list3)

# print(item_list1)
# with open(file_name, 'w') as outfile:
#     json.dump(item_list1, outfile, sort_keys= True, indent= 4)

# for i in item_list:
#     # if i["type"] == item_type:
#     print(item_list[i]["type"])
    