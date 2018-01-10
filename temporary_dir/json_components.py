# pylint: skip-file
# pylint: disable-all
"""
This is just an easy file so you don't have to search up the JSON for different components.
There's more components to add, coming later.
"""


def get_palindrome():
    return '{"instance":4,"change":{"type":"replace","definition":{"type":"Panel","attributes":{"height":"flex","width":"flex"},"children":[{"type":"Container","attributes":{},"children":[{"type":"Container","attributes":{"height":"wrap","marginBottom":10,"marginLeft":5,"marginRight":5,"marginTop":5,"minWidth":"wrap","width":"flex"},"children":[{"type":"TextView","attributes":{"value":"Enter a palindrome"}}]},{"type":"Container","attributes":{"direction":"horizontal","height":"wrap","marginBottom":2,"marginLeft":4,"marginRight":4,"marginTop":2,"valign":"middle","width":"flex"},"children":[{"type":"TextField","attributes":{"editorId":"v","hint":"Please enter a single line of text (this value is required)","hint-type":"info","mode":"enter","optional":false,"taskId":"4-1","value":null}},{"type":"Icon","attributes":{"hint":"Please enter a single line of text (this value is required)","hint-type":"info","iconCls":"icon-info","marginLeft":5,"tooltip":"Please enter a single line of text (this value is required)"}}]}]},{"type":"ButtonBar","attributes":{},"children":[{"type":"Button","attributes":{"actionId":"Ok","enabled":false,"iconCls":"icon-ok","taskId":"4-0","text":"Ok","value":"Ok"}},{"type":"Button","attributes":{"actionId":"Cancel","enabled":true,"iconCls":"icon-cancel","taskId":"4-0","text":"Cancel","value":"Cancel"}}]}]}}}'


def get_button(enabled=True, height=100, width=200):
    enabled = "true" if enabled else "false"
    return '{"type": "Button","attributes": {"actionId": "Ok","enabled": ' + enabled + ', "height": ' + str(height) + ', "width": ' + str(width) + ', "iconCls": "icon-ok","taskId": "4-0","text": "Ok","value": "Ok"}}'


def get_icon():
    return '{"type": "Icon","attributes": {"hint": "Please enter a single line of text (this value is required)","hint-type": "info","iconCls": "icon-info","marginLeft": 5,"tooltip": "Please enter a single line of text (this value is required)"}}'

def get_textfield():
    return '{"type": "TextField","attributes": {"editorId": "v","hint": "Please enter a single line of text (this value is required)","hint-type": "info","mode": "enter","optional": false,"taskId": "4-1","value": null}}'


def get_buttonbar_two_buttons():
    return '{"type": "ButtonBar","attributes": {},"children": [{"type": "Button","attributes": {"actionId": "Ok","enabled": false,"iconCls": "icon-ok","taskId": "4-0","text": "Ok","value": "Ok"}},{"type": "Button","attributes": {"actionId": "Cancel","enabled": true,"iconCls": "icon-cancel","taskId": "4-0","text": "Cancel","value": "Cancel"}}]}'


def get_buttonbar():
    return '{"type": "ButtonBar","attributes": {},"children": []}'


def get_change():
    return '{"instance":3,"change":{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[0,"change",{"type":"change","attributes":[{"name":"title","value":"Palindrome"}],"children":[]}]]}]]}]]}]]}}'


"""
Example of a replace JSON:
{"instance":4,"change":{"type":"replace","definition":{"type":"Panel","attributes":{"height":"flex","width":"flex"},"children":[{"type":"Container","attributes":{},"children":[{"type":"Container","attributes":{"height":"wrap","marginBottom":10,"marginLeft":5,"marginRight":5,"marginTop":5,"minWidth":"wrap","width":"flex"},"children":[{"type":"TextView","attributes":{"value":"Enter a palindrome"}}]},{"type":"Container","attributes":{"direction":"horizontal","height":"wrap","marginBottom":2,"marginLeft":4,"marginRight":4,"marginTop":2,"valign":"middle","width":"flex"},"children":[{"type":"TextField","attributes":{"editorId":"v","hint":"Please enter a single line of text (this value is required)","hint-type":"info","mode":"enter","optional":false,"taskId":"4-1","value":null}},{"type":"Icon","attributes":{"hint":"Please enter a single line of text (this value is required)","hint-type":"info","iconCls":"icon-info","marginLeft":5,"tooltip":"Please enter a single line of text (this value is required)"}}]}]},{"type":"ButtonBar","attributes":{},"children":[{"type":"Button","attributes":{"actionId":"Ok","enabled":false,"iconCls":"icon-ok","taskId":"4-0","text":"Ok","value":"Ok"}},{"type":"Button","attributes":{"actionId":"Cancel","enabled":true,"iconCls":"icon-cancel","taskId":"4-0","text":"Cancel","value":"Cancel"}}]}]}}}

Example of a change JSON:
{"instance":3,"change":{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[0,"change",{"type":"change","attributes":[{"name":"title","value":"Palindrome"}],"children":[]}]]}]]}]]}]]}}
"""
