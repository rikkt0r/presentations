#!/usr/bin/python3

import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

keys = ["app_name", "replaces_id", "app_icon", "summary", "body", "actions", "hints", "expire_timeout"]


def print_notification(bus, message):
    args = message.get_args_list()
    if len(args) == 8:
        notification = dict([(keys[i], args[i]) for i in range(8)])
        print(f'{notification["app_name"]} :::: {notification["summary"]} - {notification["body"]}')
    else:
        print("Unparsable", args)


if __name__ == "__main__":
    loop = DBusGMainLoop(set_as_default=True)
    session_bus = dbus.SessionBus()
    session_bus.add_match_string(
        "type='method_call',interface='org.freedesktop.Notifications',member='Notify',eavesdrop=true")
    session_bus.add_message_filter(print_notification)
    GLib.MainLoop().run()
