""" QtEventHandler handles the events from QWidgets """

# !/usr/bin/python3
from itasks_components import ItasksComponent


class QtEventHandler:
    """ QtEventHandler handles the events from QWidgets """

    def __init__(self, itasks_service):
        """
        :param itasks_service: iTasks service
        """
        self.itasks_service = itasks_service

    def button_clicked_event(self, itasks_component: ItasksComponent):
        """
        Button clicked event handler
        :param itasks_component: ItasksComponent which triggered the event
        """
        task_id = itasks_component.task_id
        task_splitted = task_id.split("-")

        action_id = itasks_component.action_id
        instance_no = int(task_splitted[0])
        task_no = int(task_splitted[1])

        self.itasks_service.send_ui_event(
            {
                "instanceNo": instance_no,
                "taskNo": task_no,
                "action": action_id
            }
        )

        # Example of update call
        itasks_component.update(
            x=38,
            y=38,
            width=38,
            height=38,
            text="kaas",
            enabled=False,
            icon="icons/accept.png"
        )

    def textbox_changed_event(self, itasks_component: ItasksComponent):
        """
        Textbox changed event handler
        :param itasks_component: ItasksComponent which triggered the event
        """
        task_id = itasks_component.task_id
        task_splitted = task_id.split("-")

        instance_no = int(task_splitted[0])
        task_no = int(task_splitted[1])

        value = itasks_component.qwidget.text()

        self.itasks_service.send_ui_event(
            {
                "instanceNo": instance_no,
                "taskNo": task_no,
                "edit": "v",
                "value": value
            }
        )
