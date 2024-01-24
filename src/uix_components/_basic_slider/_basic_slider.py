import uix
from uix.elements import slider, border, input, row, text

uix.html.add_script("slider","""
    event_handlers["init-slider"] = function(id, value, event_name) {
        document.getElementById(value.sliderID).addEventListener("input", function(e) {
            document.getElementById(value.inputID).value = e.target.value;
        });
        document.getElementById(value.inputID).addEventListener("change", function(e) {
            document.getElementById(value.sliderID).value = e.target.value;
        });
    };
""",False)
uix.html.add_css("basic_slider_css","""
.basic-slider {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    flex-direction: column;
    gap: 5px;
    }
""")
class basic_slider(uix.Element):
    def __init__(self,name, id = None, min = 0, max = 100, value = 50, step = 1,callback = None):
        super().__init__("",id = id)
        self.sliderID = id + "-slider"
        self.inputID = id + "-input"
        self.callback = callback
        self.cls("basic-slider")
        with self:
            with row().cls("wall hall").style("justify-content","space-between"):
                text(name)
                input(type="number", id = self.inputID, value = value).style("width","30px;").on("change", self.on_slider_change)
            with row():
                slider(id = self.sliderID, min=min, max=max, value=value, step=step).on("change", self.on_slider_change).style("width","100%")

    def on_slider_change(self,ctx, id, value):
        if self.callback:
            self.callback(ctx, id, value)
       
    def init(self):
        print("basic_slider init")
        self.session.queue_for_send("init-slider", {"sliderID": self.sliderID, "inputID": self.inputID},"init-slider")
 
title = "Basic Slider"
 
description = """
 #basic_slider(name, id, min, max, value, step, callback)
 1. Slider elementinin içerisinde input elementi eklenerek oluşturulan bir componenttir.
    | attr          | desc                                                          |
    | :------------ | :------------------------------------------------------------ |
    | name          | Slider Componentinin name'i input'un önünde yazar             |
    | id            | Slider Componentinin id'si                                    |
    | min           | Slider Componentinin minimum değeri                           |
    | max           | Slider Componentinin maksimum değeri                          |
    | value         | Slider Componentinin başlangıç değeri                         |
    | step          | Slider Componentinin artış değeri                             |
    | callback      | Slider Componentinin değeri değiştiğinde çağırılacak fonksiyon|
 """
 
sample = """
     def basic_slider_example():
        return basic_slider(name="Deneme", id = "mySlider", callback = lambda ctx, id, value: print(f"Slider {id} changed to: {value}"))
     """