import expipe_plugin_cinpla
from expipecli.utils.plugin import IPlugin
from expipe_plugin_cinpla.imports import *
from . import adjust
from . import axona as AX
from . import misc
from . import openephys as OE
from . import entity
from . import surgery


class CinplaPlugin(IPlugin):
    def attach_to_cli(self, cli):
        @cli.group(short_help='Tools for registering.')
        @click.help_option('-h', '--help')
        @click.pass_context
        def register(ctx):
            pass

        @cli.group(short_help='Tools for processing.')
        @click.help_option('-h', '--help')
        @click.pass_context
        def process(ctx):
            pass

        misc.attach_to_cli(cli)
        adjust.attach_to_cli(cli)
        surgery.attach_to_cli(register)
        entity.attach_to_cli(register)
        OE.attach_to_register(register)
        OE.attach_to_process(process)
        AX.attach_to_cli(register)
