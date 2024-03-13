import turtle
import pandas


def get_mouse_cor(x, y):
    if len(cities_dict["Coordinates"]) >= 81:
        return
    new_dict = {"x": x, "y": y}
    cities_dict["Coordinates"].append(new_dict)


cities = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin",
          "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa",
          "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum",
          "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkâri", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir",
          "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli",
          "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş",
          "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Sivas",
          "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"]
cities_dict = {
    "Cities": cities,
    "Coordinates": []
}
count = 0
screen = turtle.Screen()
screen.setup(width=1200, height=600)
screen.title("Guess Turkish Cities")
image = "turkish_map.gif"
screen.addshape(image)
turtle.shape(image)

turtle.onclick(get_mouse_cor)
turtle.mainloop()

while True:
    if len(cities_dict["Coordinates"]) >= 81:
        break
    cities_dict["Coordinates"].append({"x": 0, "y": 0})

#pandas.DataFrame(cities_dict).to_csv("cities_with_coordinates.csv")
