from ui_generator import components
import json


def create_component(json_component=""):
    json_ding = json.loads(json_component)
    action = getattr(components.Components, json_ding["type"].lower())
    action(json_ding["attributes"])


create_component('{"type": "Icon","attributes": {"hint": "Please enter a single line of text (this value is required)","hint-type": "info","iconCls": "icon-info","marginLeft": 5,"tooltip": "Please enter a single line of text (this value is required)"}}')


