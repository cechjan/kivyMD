from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget
import json

person_list = [{"name": "Karel Nový", "state": "CZE"},
               {"name": "Ivan Hrozný", "state": "RUS"},
               {"name": "John Walker", "state": "USA"}]


class MyItem(TwoLineAvatarListItem):
    def __init__(self, name, state, gender, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = name
        self.secondary_text = state
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=f"images/{gender}.png")
        self.add_widget(ImageLeftWidget(source=f"images/{state}.jpg"))
        self.add_widget(self.image)

    # def on_press(self):
    #     print(self.text)
    #
    # def on_touch_down(self, touch):
    #     print(touch)
    #     self.image.source = "images/blue.png"
    #
    # def on_touch_up(self, touch):
    #     print(touch)
    #     self.image.source = "images/green.png"


class Persons(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Persons, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        # for person in person_list:
        #     list.add_widget(MyItem(name=person['name'], state=person['state']))
        with open("modules/person.json", encoding="utf-8") as f:
            data = json.load(f)
            for person in data["person"]:
                list.add_widget(MyItem(name=person['name'], state=person['state'], gender=person['gender']))
        scrollview.add_widget(list)
        self.add_widget(scrollview)
