import sublime
import sublime_plugin

from Vintageous import plugins
from Vintageous.vi import inputs
from Vintageous.vi import utils
from Vintageous.vi.cmd_defs import ViOperatorDef
from Vintageous.vi.core import ViTextCommandBase
from Vintageous.vi.inputs import input_types
from Vintageous.vi.inputs import parser_def
from Vintageous.vi.search import reverse_search
from Vintageous.vi.utils import modes
from Vintageous.vi.utils import regions_transformer

import re


@plugins.register(seq='<C-.><C-.>', modes=(modes.NORMAL,))
class ViDartOpenCommandPalette(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'show_overlay'
        cmd['action_args'] = {
            'overlay': 'command_palette',
            'text': 'Dart: ',
            }
        return cmd


@plugins.register(seq='<C-S-.><C-S-.>', modes=(modes.NORMAL,))
class ViDartOpenBuildCommandPalette(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'show_overlay'
        cmd['action_args'] = {
            'overlay': 'command_palette',
            'text': 'Build: Dart: ',
            }
        return cmd


@plugins.register(seq='<C-S-.><C-S-.>', modes=(modes.NORMAL,))
class ViDartOpenBuildCommandPalette(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'show_overlay'
        cmd['action_args'] = {
            'overlay': 'command_palette',
            'text': 'Build: Dart: ',
            }
        return cmd


@plugins.register(seq='<C-.><C-cr>', modes=(modes.NORMAL,))
class ViDartSmartRun(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'dart_smart_run'
        cmd['action_args'] = {}
        return cmd


@plugins.register(seq='<C-.><C-S-cr>', modes=(modes.NORMAL,))
class ViDartUpdateSmartRun(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'dart_smart_run'
        cmd['action_args'] = {
            "force_update": True,
        }
        return cmd


@plugins.register(seq='<C-S-.><C-cr>', modes=(modes.NORMAL,))
class ViDartSmartRunSecondary(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'dart_smart_run'
        cmd['action_args'] = {
            "action": "secondary",
        }
        return cmd


@plugins.register(seq='<C-S-.><C-S-cr>', modes=(modes.NORMAL,))
class ViDartSmartRunSecondary(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'dart_smart_run'
        cmd['action_args'] = {
            "action": "secondary",
            "force_update": True,
        }
        return cmd


@plugins.register(seq='<C-.><C-0>', modes=(modes.NORMAL,))
class ViDartStopProcesses(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'dart_smart_run'
        cmd['action_args'] = {
            "kill_only": True,
        }
        return cmd


@plugins.register(seq='<C-.><C-o>', modes=(modes.NORMAL,))
class ViDartShowOutputPanel(ViOperatorDef):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def translate(self, state):
        cmd = {}
        cmd['action'] = 'show_panel'
        cmd['action_args'] = {
            "panel": "output.dart.out",
        }
        return cmd
