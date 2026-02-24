#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ROS Scanner helper module.

:author Alias Robotics SL (https://aliasrobotics.com)
"""
from aztarna.ros.commons import BaseNodeROS, BaseNodeROS, BaseServiceROS, BaseHostROS, ParameterROS, ActionROS

class ROSHost(BaseHostROS):
    """
    Class for keeping all the attributes of a ROS Node.Extends:class:`aztarna.commons.BaseHostROS`
    """
    def __init__(self, address, port):
        super().__init__()
        self.address = address
        self.port = port
        self.communications = []
        self.services = []
        self.params = []
        self.actions = []

    def __repr__(self):
        if len(self.nodes) == 0:
            return "Address: {}".format(self.address)
        return "Address: {}, Nodes: {}".format(self.address, self.nodes)

class Node(BaseNodeROS):
    """
    Node class, an extension of the BaseNodeROS
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.published_topics = []
        self.subscribed_topics = []
        self.services = []

    def __str__(self):
        return '{} XMLRPCUri: http://{}:{}'.format(self.name, self.address, self.port)

class Topic(BaseNodeROS):
    """
    Topic class, an extension of BaseNodeROS
    """
    def __init__(self, name, topic_type):
        super().__init__()
        self.name = name
        self.type = topic_type

    def __str__(self):
        return self.name + '(Type: ' + self.type + ')'

class Service(BaseServiceROS):
    """
    Service class, an extension of BaseServiceROS
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return '{}'.format(self.name)


class Param(ParameterROS):
    """
    Param class, an extension of ParameterROS
    """
    def __init__(self, name, param_type, value):
        super().__init__()
        self.name = name
        self.type = param_type
        self.value = value

    def __str__(self):
        return '{} (Type: {}, Value: {})'.format(self.name, self.type, self.value)


class Action(ActionROS):
    """
    Action class, an extension of ActionROS
    """
    def __init__(self, name, action_type):
        super().__init__()
        self.name = name
        self.type = action_type

    def __str__(self):
        return '{} (Type: {})'.format(self.name, self.type)
