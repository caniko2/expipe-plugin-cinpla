from expipe_plugin_cinpla.imports import *
from expipe_plugin_cinpla.scripts import openephys
from . import utils


def attach_to_cli(cli):
    @cli.command('openephys',
                 short_help='Register an open-ephys recording-action to database.')
    @click.argument('openephys-path', type=click.Path(exists=True))
    @click.option('-u', '--user',
                  type=click.STRING,
                  help='The experimenter performing the recording.',
                  )
    @click.option('-d', '--depth',
                  multiple=True,
                  callback=utils.validate_depth,
                  help=(
                    'Alternative "find" to find from surgery or adjustment' +
                    ' or given as <key num depth unit> e.g. ' +
                    '<mecl 0 10 um> (omit <>).'),
                  )
    @click.option('-l', '--location',
                  type=click.STRING,
                  callback=utils.optional_choice,
                  envvar=PAR.POSSIBLE_LOCATIONS,
                  help='The location of the recording, i.e. "room-1-ibv".'
                  )
    @click.option('--session',
                  type=click.STRING,
                  help='Session number, assumed to be in end of filename by default',
                  )
    @click.option('--action-id',
                  type=click.STRING,
                  help=('Desired action id for this action, if none' +
                        ', it is generated from open-ephys-path.'),
                  )
    @click.option('--entity-id',
                  type=click.STRING,
                  help='The id number of the entity.',
                  )
    @click.option('-m', '--message',
                  multiple=True,
                  type=click.STRING,
                  help='Add message, use "text here" for sentences.',
                  )
    @click.option('-t', '--tag',
                  multiple=True,
                  type=click.STRING,
                  callback=utils.optional_choice,
                  envvar=PAR.POSSIBLE_TAGS,
                  help='Add tags to action.',
                  )
    @click.option('--overwrite',
                  is_flag=True,
                  help='Overwrite files and expipe action.',
                  )
    @click.option('--register-depth',
                  is_flag=True,
                  help='Overwrite files and expipe action.',
                  )
    @click.option('--templates',
                  multiple=True,
                  type=click.STRING,
                  help='Which templates to add',
                  )
    def _register_openephys_recording(
        action_id, openephys_path, depth, overwrite, templates,
        entity_id, user, session, location, message, tag, delete_raw_data,
        query_depth_answer, register_depth):
        openephys.register_openephys_recording(
            project=PAR.PROJECT,
            action_id=action_id,
            openephys_path=openephys_path,
            depth=depth,
            overwrite=overwrite,
            templates=templates,
            entity_id=entity_id,
            user=user,
            session=session,
            location=location,
            message=message,
            tag=tag,
            delete_raw_data=None,
            query_depth_answer=None,
            register_depth=register_depth)
