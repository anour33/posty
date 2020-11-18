class post:

    def __init__(self,name,image,content) :
        self.name = name
        self.image = image
        self.content = content


post1 = post(name="Yaser",image="img_url",content="je suis Yaser ,et ceci est un exemple de post ")
post2 = post(name="Mohamed",image="img_url",content="je suis Mohamed,et ceci est un exemple de post ")
post3 = post(name="Sara",image="img_url",content="je suis Sara ,et ceci est un exemple de post ")

print(post1.name,"\n",post1.content)
print(post2.name,"\n",post2.content)
print(post3.name,"\n",post3.content)
