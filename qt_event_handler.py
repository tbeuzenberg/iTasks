""" QtEventHandler handles the events from QWidgets """

# !/usr/bin/python3
from itasks import ItasksService
from itasks_components import ItasksComponent


class QtEventHandler:
    """ QtEventHandler handles the events from QWidgets """

    @staticmethod
    def button_clicked_event(itasks_component: ItasksComponent):
        """
        Button clicked event handler
        :param itasks_component: ItasksComponent which triggered the event
        """
        itasks_service = ItasksService()

        task_id = itasks_component.task_id
        task_splitted = task_id.split("-")

        action_id = itasks_component.action_id
        instance_no = int(task_splitted[0])
        task_no = int(task_splitted[1])

        itasks_service.send_ui_event(
            {
                "instanceNo": instance_no,
                "taskNo": task_no,
                "action": action_id
            }
        )

        # Example of update call
        # itasks_component.update(
        #     [
        #         {"name": "x", "value": 38},
        #         {"name": "y", "value": 38},
        #         {"name": "width", "value": 38},
        #         {"name": "height", "value": 38},
        #         {"name": "text", "value": "kaas"},
        #         {"name": "enabled", "value": False},
        #         {"name": "icon", "value": "icons/accept.png"}
        #     ]
        # )

    @staticmethod
    def textbox_changed_event(itasks_component: ItasksComponent):
        """
        Textbox changed event handler
        :param itasks_component: ItasksComponent which triggered the event
        """
        itasks_service = ItasksService()

        task_id = itasks_component.task_id
        task_splitted = task_id.split("-")

        editor_id = itasks_component.editor_id
        instance_no = int(task_splitted[0])
        task_no = int(task_splitted[1])

        value = itasks_component.qwidget.text()

        itasks_service.send_ui_event(
            {
                "instanceNo": instance_no,
                "taskNo": task_no,
                "edit": editor_id,
                "value": value
            }
        )
