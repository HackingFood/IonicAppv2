import bs4 as BeautifulSoup
Soup = BeautifulSoup.BeautifulSoup
from pymongo import MongoClient as MongClient


import requests

sites =  []

sites.append("https://www.yelp.com/menu/culinary-dropout-austin/antipasti-menu")
sites.append("https://www.yelp.com/menu/jewhungry-austin")
sites.append("https://www.yelp.com/menu/saffron-austin-2")
sites.append("https://www.yelp.com/menu/the-hightower-austin/main-menu")



mylist = []
rest = ["Culinary Dropout","Jew Hungry","Saffron Austin","The High Tower"]
addr = ["11721 Rock Rose Ste 100 Austin, TX 78758", "1209 E 7th St Austin, TX 78702", "3616 Far W Blvd Ste 113 Austin, TX 78731","3808 South Congress Ave Austin, TX 78704"]
picsLinks =[]
picsLinks.append("https://imgoat.com/uploads/c4b761a28b/156180.jpg")
picsLinks.append("https://imgoat.com/uploads/c4b761a28b/156182.jpg")
picsLinks.append("https://imgoat.com/uploads/c4b761a28b/156184.jpg")
picsLinks.append("https://imgoat.com/uploads/c4b761a28b/156185.jpg")



sites2 = []
rest2 = []
addr2 = []
typeOf = []
picLinks2 =[]
myList2 = []

sites2.append("https://www.yelp.com/menu/taco-shack-austin-5?osq=Taco+Shack")
rest2.append("Austin Taco Shack")
addr2.append("402 Brazos St Austin, TX 78701")
typeOf.append("fiesta-taco-salads")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156157.png")

sites2.append("https://www.yelp.com/menu/torchys-tacos-austin-4?osq=Torchy%27s+Tacos")
rest2.append("Torchy's Tacos")
addr2.append("2801 Guadalupe St Ste 5-B Austin, TX 78705")
typeOf.append("breakfast-tacos")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156156.jpg")


'''
sites2.append("https://www.yelp.com/menu/pueblo-viejo-austin")
rest2.append("Pueblo Viejo")
addr2.append("502 Brushy St Austin, TX 78702")
typeOf.append("specialty-tacos")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156158.jpg")
'''

sites2.append("https://www.yelp.com/menu/burger-bar-on-congress-austin/burger-bar")
rest2.append("Austin Burger Bar")
addr2.append("JW Marriott Austin 110 E 2 St Austin, TX 78701 Downtown")
typeOf.append("burgers")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156159.jpg")

'''
sites2.append("https://www.yelp.com/menu/hopdoddy-burger-bar-austin?osq=Hopdoddy+Burger+Bar")
rest2.append("Hop Doddy Burger Bar")
addr2.append("1400 S Congress Ave Ste A190 Austin, TX 78704")
typeOf.append("burgers")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156159.jpg")
'''


sites2.append("https://www.yelp.com/menu/shake-shack-austin?osq=burger")
rest2.append("Shake Shack")
addr2.append("1100 S Lamar Ste 2100 Austin, TX 78704")
typeOf.append("burgers")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156176.jpg")


sites2.append("https://www.yelp.com/menu/mango-8-austin")
rest2.append("Mango 8")
addr2.append("705 W 24th St Ste A Austin, TX 78705")
typeOf.append("classic-teas")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156177.jpg")


sites2.append("https://www.yelp.com/menu/mango-mango-dessert-austin-4")
rest2.append("Magno Mango")
addr2.append("2222 Rio Grande St Ste C120 Austin, TX 78705")
typeOf.append("hot-tea")
picLinks2.append("https://imgoat.com/uploads/c4b761a28b/156178.jpg")



k = 0;

for site in sites2:


    print(site)
    resta = rest2[k]
    addra = addr2[k]
    food = typeOf[k]
    pic = picLinks2[k]
    k = k+1
    r = requests.get(site)
    data = r.text
    soup = Soup(data,'html.parser')
    div = soup.find(id=food)
    print("DIV" + str(div))
    x = div.find_next('h4')
    print(x.text.strip())
    x = x.text.strip()
    y = div.find_next(class_="menu-item-price-amount")
    print(y)
    y = y.text.strip()
    print(y)
    tempList = [x,y,[x,typeOf],resta,addra,pic]
    myList2.append(tempList)






k = 0
for site in sites:

    resta = rest[k]
    addra = addr[k]
    pic = picsLinks[k]
    k = k +1
    r = requests.get(site)
    data = r.text
    soup = Soup(data, 'html.parser')

    divs = soup.findAll(class_='menu-item')
    for div in divs:
        x = div.find('h4')
        print(x.text.strip())
        y = div.find(class_="menu-item-price-amount")
        print(y.text.strip())
        y = y.text.strip()
        y = y[1:]
        templist = [x.text.strip(), y, [x.text.strip()], resta, addra,pic]
        mylist.append(templist)





client = MongClient("mongodb://admin:Foodhacking!@hackingfood-shard-00-00-1vijt.azure.mongodb.net:27017,hackingfood-shard-00-01-1vijt.azure.mongodb.net:27017,hackingfood-shard-00-02-1vijt.azure.mongodb.net:27017/test?ssl=true&replicaSet=HackingFood-shard-0&authSource=admin&retryWrites=true")
db=client.business





database = client['hackFood']
collection = database['sampleData']

for item in mylist:
    collection.insert({"tags": item[2], "price": item[1], "name": item[0], "restaurant": item[3], "address": item[4], "pic":item[5]})

for item in myList2:
    collection.insert({"tags": item[2], "price": item[1], "name": item[0], "restaurant": item[3], "address": item[4], "pic":item[5]})







