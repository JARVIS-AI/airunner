# revision identifiers, used by Alembic.
import sqlalchemy

from airunner.aihandler.models import settings_models
from airunner.data.bootstrap.controlnet_bootstrap_data import controlnet_bootstrap_data
from airunner.data.bootstrap.font_settings_bootstrap_data import font_settings_bootstrap_data
from airunner.data.bootstrap.model_bootstrap_data import model_bootstrap_data
from airunner.data.bootstrap.pipeline_bootstrap_data import pipeline_bootstrap_data
from airunner.data.bootstrap.prompt_templates_bootstrap_data import prompt_templates_bootstrap_data
from airunner.settings import SCHEDULER_CLASSES, DEFAULT_SHORTCUTS

revision = '1ee2a000c0d1'
down_revision = 'fafbef6dbccb'
branch_labels = None
depends_on = None

from alembic import op

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(settings_models.ApplicationSettings.__tablename__,
                    *settings_models.ApplicationSettings.__table__.columns)
    op.create_table(settings_models.ActiveGridSettings.__tablename__,
                    *settings_models.ActiveGridSettings.__table__.columns)
    op.create_table(settings_models.CanvasSettings.__tablename__,
                    *settings_models.CanvasSettings.__table__.columns)
    op.create_table(settings_models.ControlnetSettings.__tablename__,
                    *settings_models.ControlnetSettings.__table__.columns)
    op.create_table(settings_models.ImageToImageSettings.__tablename__,
                    *settings_models.ImageToImageSettings.__table__.columns)
    op.create_table(settings_models.OutpaintSettings.__tablename__,
                    *settings_models.OutpaintSettings.__table__.columns)
    op.create_table(settings_models.DrawingPadSettings.__tablename__,
                    *settings_models.DrawingPadSettings.__table__.columns)
    op.create_table(settings_models.MetadataSettings.__tablename__,
                    *settings_models.MetadataSettings.__table__.columns)
    op.create_table(settings_models.GeneratorSettings.__tablename__,
                    *settings_models.GeneratorSettings.__table__.columns)
    op.create_table(settings_models.ControlnetImageSettings.__tablename__,
                    *settings_models.ControlnetImageSettings.__table__.columns)
    op.create_table(settings_models.TTSSettings.__tablename__,
                    *settings_models.TTSSettings.__table__.columns)
    op.create_table(settings_models.SpeechT5Settings.__tablename__,
                    *settings_models.SpeechT5Settings.__table__.columns)
    op.create_table(settings_models.EspeakSettings.__tablename__,
                    *settings_models.EspeakSettings.__table__.columns)
    op.create_table(settings_models.STTSettings.__tablename__,
                    *settings_models.STTSettings.__table__.columns)
    op.create_table(settings_models.Schedulers.__tablename__,
                    *settings_models.Schedulers.__table__.columns)
    op.create_table(settings_models.TranslationSettings.__tablename__,
                    *settings_models.TranslationSettings.__table__.columns)
    op.create_table(settings_models.LLMGeneratorSettings.__tablename__,
                    *settings_models.LLMGeneratorSettings.__table__.columns)
    op.create_table(settings_models.BrushSettings.__tablename__,
                    *settings_models.BrushSettings.__table__.columns)
    op.create_table(settings_models.GridSettings.__tablename__,
                    *settings_models.GridSettings.__table__.columns)
    op.create_table(settings_models.PathSettings.__tablename__,
                    *settings_models.PathSettings.__table__.columns)
    op.create_table(settings_models.MemorySettings.__tablename__,
                    *settings_models.MemorySettings.__table__.columns)
    op.create_table(settings_models.Chatbot.__tablename__,
                    *settings_models.Chatbot.__table__.columns)
    op.create_table(settings_models.TargetFiles.__tablename__,
                    *settings_models.TargetFiles.__table__.columns)
    op.create_table(settings_models.TargetDirectories.__tablename__,
                    *settings_models.TargetDirectories.__table__.columns)
    op.create_table(settings_models.AIModels.__tablename__,
                    *settings_models.AIModels.__table__.columns)
    op.create_table(settings_models.ShortcutKeys.__tablename__,
                    *settings_models.ShortcutKeys.__table__.columns)
    op.create_table(settings_models.Lora.__tablename__,
                    *settings_models.Lora.__table__.columns)
    op.create_table(settings_models.SavedPrompt.__tablename__,
                    *settings_models.SavedPrompt.__table__.columns)
    op.create_table(settings_models.Embedding.__tablename__,
                    *settings_models.Embedding.__table__.columns)
    op.create_table(settings_models.PromptTemplate.__tablename__,
                    *settings_models.PromptTemplate.__table__.columns)
    op.create_table(settings_models.ControlnetModel.__tablename__,
                    *settings_models.ControlnetModel.__table__.columns)
    op.create_table(settings_models.FontSetting.__tablename__,
                    *settings_models.FontSetting.__table__.columns)
    op.create_table(settings_models.PipelineModel.__tablename__,
                    *settings_models.PipelineModel.__table__.columns)

    set_default_values(settings_models.ApplicationSettings)
    set_default_values(settings_models.ActiveGridSettings)
    set_default_values(settings_models.CanvasSettings)
    set_default_values(settings_models.ControlnetSettings)
    set_default_values(settings_models.ImageToImageSettings)
    set_default_values(settings_models.OutpaintSettings)
    set_default_values(settings_models.DrawingPadSettings)
    set_default_values(settings_models.MetadataSettings)
    set_default_values(settings_models.GeneratorSettings)
    set_default_values(settings_models.ControlnetImageSettings)
    set_default_values(settings_models.TTSSettings)
    set_default_values(settings_models.SpeechT5Settings)
    set_default_values(settings_models.EspeakSettings)
    set_default_values(settings_models.STTSettings)
    set_default_values(settings_models.Schedulers)
    set_default_values(settings_models.TranslationSettings)
    set_default_values(settings_models.LLMGeneratorSettings)
    set_default_values(settings_models.BrushSettings)
    set_default_values(settings_models.GridSettings)
    set_default_values(settings_models.PathSettings)
    set_default_values(settings_models.MemorySettings)
    set_default_values(settings_models.Chatbot)
    set_default_values(settings_models.TargetFiles)
    set_default_values(settings_models.TargetDirectories)
    set_default_ai_models()
    set_default_schedulers()
    set_default_shortcut_keys()
    set_default_prompt_templates()
    set_default_controlnet_models()
    set_default_font_settings()
    set_default_pipeline_values()

    # ### end Alembic commands ###

def set_default_prompt_templates():
    values = []
    for template in prompt_templates_bootstrap_data:
        values.append(template)
    op.bulk_insert(
        settings_models.PromptTemplate.__table__,
        values
    )

def set_default_controlnet_models():
    values = []
    for template in controlnet_bootstrap_data:
        values.append(template)
    op.bulk_insert(
        settings_models.ControlnetModel.__table__,
        values
    )

def set_default_ai_models():
    values = []
    for model in model_bootstrap_data:
        values.append(model)
    op.bulk_insert(
        settings_models.AIModels.__table__,
        values
    )

def set_default_schedulers():
    op.bulk_insert(
        settings_models.Schedulers.__table__,
        SCHEDULER_CLASSES
    )


def set_default_values(model_name_):
    default_values = {}
    for column in model_name_.__table__.columns:
        if column.default is not None:
            default_values[column.name] = column.default.arg
    op.bulk_insert(
        model_name_.__table__,
        [default_values]
    )

def set_default_shortcut_keys():
    op.bulk_insert(
        settings_models.ShortcutKeys.__table__,
        DEFAULT_SHORTCUTS
    )

def set_default_font_settings():
    for font_setting in font_settings_bootstrap_data:
        op.bulk_insert(
            settings_models.FontSetting.__table__,
            [font_setting]
        )

def set_default_pipeline_values():
    for pipeline in pipeline_bootstrap_data:
        op.bulk_insert(
            settings_models.PipelineModel.__table__,
            [pipeline]
        )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.drop_table('application_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('translation_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('espeak_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('tts_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('schedulers')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('stt_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('speech_t5_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('controlnet_image_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('generator_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('metadata_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('drawing_pad_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('outpaint_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('image_to_image_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('controlnet_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('canvas_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('active_grid_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('translation_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('llm_generator_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('scheduler_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('brush_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('grid_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('path_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('memory_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('chatbots')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('target_files')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('target_directories')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('aimodels')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('shortcut_keys')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('lora')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('saved_prompts')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('embeddings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('prompt_templates')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('controlnet_models')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('font_settings')
    except sqlalchemy.exc.OperationalError:
        pass
    try:
        op.drop_table('pipeline_models')
    except sqlalchemy.exc.OperationalError:
        pass
    # ### end Alembic commands ###
