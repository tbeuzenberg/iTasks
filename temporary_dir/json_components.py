# pylint: skip-file
# pylint: disable-all
"""
This is just an easy file so you don't have to search up the JSON for different components.
There's more components to add, coming later.
"""


def get_palindrome():
    return '{"instance":4,"change":{"type":"replace","definition":{"type":"Panel","attributes":{"height":"flex","width":"flex"},"children":[{"type":"Container","attributes":{},"children":[{"type":"Container","attributes":{"height":"wrap","marginBottom":10,"marginLeft":5,"marginRight":5,"marginTop":5,"minWidth":"wrap","width":"flex"},"children":[{"type":"TextView","attributes":{"value":"Enter a palindrome"}}]},{"type":"Container","attributes":{"direction":"horizontal","height":"wrap","marginBottom":2,"marginLeft":4,"marginRight":4,"marginTop":2,"valign":"middle","width":"flex"},"children":[{"type":"TextField","attributes":{"editorId":"v","hint":"Please enter a single line of text (this value is required)","hint-type":"info","mode":"enter","optional":false,"taskId":"2-1","value":null}},{"type":"Icon","attributes":{"hint":"Please enter a single line of text (this value is required)","hint-type":"info","iconCls":"icon-info","marginLeft":5,"tooltip":"Please enter a single line of text (this value is required)"}}]}]},{"type":"ButtonBar","attributes":{},"children":[{"type":"Button","attributes":{"actionId":"Ok","enabled":false,"iconCls":"icon-ok","taskId":"2-0","text":"Ok","value":"Ok"}},{"type":"Button","attributes":{"actionId":"Cancel","enabled":true,"iconCls":"icon-cancel","taskId":"2-0","text":"Cancel","value":"Cancel"}}]}]}}}'


def get_button(enabled=True, height=100, width=200):
    enabled = "true" if enabled else "false"
    return '{"type": "Button","attributes": {"actionId": "Ok","enabled": ' + enabled + ', "height": ' + str(height) + ', "width": ' + str(width) + ', "iconCls": "icon-ok","taskId": "2-0","text": "Ok","value": "Ok"}}'


def get_icon():
    return '{"type": "Icon","attributes": {"hint": "Please enter a single line of text (this value is required)","hint-type": "info","iconCls": "icon-info","marginLeft": 5,"tooltip": "Please enter a single line of text (this value is required)"}}'


def get_textfield(height=100, width=200, x=0, y=0):
    return '{"type": "TextField","attributes": {"editorId": "v", "x": ' + str(x) + ', "y": ' + str(y) + ', "height": ' + str(height) + ', "width": ' + str(width) + ',"hint": "Please enter a single line of text (this value is required)","hint-type": "info","mode": "enter","optional": false,"taskId": "2-1","value": null}}'


def get_buttonbar_two_buttons():
    return '{"type": "ButtonBar","attributes": {},"children": [{"type": "Button","attributes": {"actionId": "Ok","enabled": false,"iconCls": "icon-ok","taskId": "2-0","text": "Ok","value": "Ok"}},{"type": "Button","attributes": {"actionId": "Cancel","enabled": true,"iconCls": "icon-cancel","taskId": "2-0","text": "Cancel","value": "Cancel"}}]}'


def get_buttonbar():
    return '{"type": "ButtonBar","attributes": {},"children": []}'


def get_itasks_layout(json):
    return '{"instance":4,"change":{"type":"replace","definition":' + json + '}}'


def get_change():
    return '{"instance":4,"change":{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[0,"change",{"type":"change","attributes":[{"name":"title","value":"Palindrome"}],"children":[]}]]}]]}]]}]]}}'


def get_change_and_replace():
    return '{"instance":3,"change":{"type":"change","attributes":[],"children":[[1,"change",{"type": "replace","definition": {"type": "Panel", "attributes": {"height": "flex", "width": "flex"}, "children":[{"type": "Button","attributes": {"actionId": "Ok","enabled": false,"iconCls": "icon-ok","taskId": "2-0","text": "Ok","value": "Ok"}},{"type": "Button","attributes": {"actionId": "Cancel","enabled": true,"iconCls": "icon-cancel","taskId": "2-0","text": "Cancel","value": "Cancel"}}]}}],[2,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[0,"change",{"type":"change","attributes":[{"name":"title","value":"Palindrome"}],"children":[]}]]}]]}]]}]]}}'


"""
Example of a replace JSON:
{"instance":4,"change":{"type":"replace","definition":{"type":"Panel","attributes":{"height":"flex","width":"flex"},"children":[{"type":"Container","attributes":{},"children":[{"type":"Container","attributes":{"height":"wrap","marginBottom":10,"marginLeft":5,"marginRight":5,"marginTop":5,"minWidth":"wrap","width":"flex"},"children":[{"type":"TextView","attributes":{"value":"Enter a palindrome"}}]},{"type":"Container","attributes":{"direction":"horizontal","height":"wrap","marginBottom":2,"marginLeft":4,"marginRight":4,"marginTop":2,"valign":"middle","width":"flex"},"children":[{"type":"TextField","attributes":{"editorId":"v","hint":"Please enter a single line of text (this value is required)","hint-type":"info","mode":"enter","optional":false,"taskId":"2-1","value":null}},{"type":"Icon","attributes":{"hint":"Please enter a single line of text (this value is required)","hint-type":"info","iconCls":"icon-info","marginLeft":5,"tooltip":"Please enter a single line of text (this value is required)"}}]}]},{"type":"ButtonBar","attributes":{},"children":[{"type":"Button","attributes":{"actionId":"Ok","enabled":false,"iconCls":"icon-ok","taskId":"2-0","text":"Ok","value":"Ok"}},{"type":"Button","attributes":{"actionId":"Cancel","enabled":true,"iconCls":"icon-cancel","taskId":"2-0","text":"Cancel","value":"Cancel"}}]}]}}}

Example of a change JSON:
{"instance":3,"change":{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[1,"change",{"type":"change","attributes":[],"children":[[0,"change",{"type":"change","attributes":[{"name":"title","value":"Palindrome"}],"children":[]}]]}]]}]]}]]}}
"""


"""
def recursive():
    generator = UIGenerator(QApplication(sys.argv))

    generator.read_itasks_json_instruction(get_palindrome())

    sys.exit(generator.application.exec_())


def direct_component():
    generator = UIGenerator(QApplication(sys.argv))

    mw = QMainWindow()
    mw.setGeometry(0, 0, 200, 600)

    generator.add_instance_tree(instance_id=1, itasks_component=mw)

    btn3 = get_button(width=50, height=500, enabled=False)
    btn2 = get_button(width=150, height=200, enabled=False)
    btn1 = get_button(width=150, height=500)
    tb = get_textfield(height=25, width=175, x=10, y=550)

    generator.add_component_to_widget(
        instance_id=1,
        location=[0],
        json_component=btn1
    )

    generator.add_component_to_widget(
        instance_id=1,
        location=[2],
        json_component=btn2
    )

    generator.add_component_to_widget(
        instance_id=1,
        location=[0, 2],
        json_component=btn3
    )

    generator.add_component_to_widget(
        instance_id=1,
        location=[3],
        json_component=tb
    )

    generator.get_widget(1).show()
    sys.exit(generator.application.exec_())

def application():
    app = Application(
        application=QApplication(sys.argv),
        main_window=QMainWindow()
    )

    app.handle_instruction(get_palindrome())

    app.main_window.show()
    app.instance_trees.get(4).print()

    sys.exit(app.qt_application.exec_())
    """