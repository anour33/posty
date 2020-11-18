class model:

    def __init__(self,logo,name,image,new,edit,delet,post) :
        self.logo = logo
        self.name = name
        self.image = image
        self.new = new
        self.edit = edit
        self.delet = delet
        self.post = post


model1 = model(logo="logo",name="Yaser",image="img_url",new="new",edit="edit", delet="delet",post="je suis Yaser ,et ceci est un exemple de post ")
model2 = model(logo="logo",name="Mohamed",image="img_url",new="new",edit="edit", delet="delet",post="je suis Mohamed,et ceci est un exemple de post ")
model3 = model(logo="logo",name="Sara",image="img_url",new="new",edit="edit", delet="delet",post="je suis Sara ,et ceci est un exemple de post ")

print(model1.name,"\n",model1.post)
print(model2.name,"\n",model2.post)
print(model3.name,"\n",model3.post)
