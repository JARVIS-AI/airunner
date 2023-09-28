from airunner.data.bootstrap.controlnet_bootstrap_data import controlnet_bootstrap_data
from airunner.data.bootstrap.generator_bootstrap_data import sections_bootstrap_data
from airunner.data.bootstrap.imagefilter_bootstrap_data import imagefilter_bootstrap_data
from airunner.data.bootstrap.model_bootstrap_data import model_bootstrap_data
from airunner.data.bootstrap.pipeline_bootstrap_data import pipeline_bootstrap_data
from airunner.data.bootstrap.prompt_bootstrap_data import prompt_bootstrap_data, style_bootstrap_data, \
    variable_bootstrap_data
from airunner.data.models import ControlnetModel, Pipeline, Document, Settings, PromptGeneratorSetting, \
    GeneratorSetting, SplitterSection, GridSettings, MetadataSettings, PathSettings, MemorySettings, AIModel, \
    ImageFilter, ImageFilterValue, BrushSettings, Prompt, PromptVariable, PromptCategory, PromptOption, \
    PromptVariableCategory, PromptVariableCategoryWeight, PromptStyleCategory, PromptStyle
from airunner.utils import get_session

session = get_session()

# check if database is blank:
if not session.query(Prompt).first():

    # Add Prompt objects
    for prompt_option, data in prompt_bootstrap_data.items():
        category = PromptCategory(name=prompt_option)
        prompt = Prompt(
            name=f"Standard {prompt_option} prompt",
            category=category
        )
        session.add(prompt)
        session.commit()
        prompt_id = prompt.id

        prompt_variables = []
        for category_name, variable_values in data["variables"].items():
            # add prompt category
            cat = session.query(PromptVariableCategory).filter_by(name=category_name).first()
            if not cat:
                cat = PromptVariableCategory(name=category_name)
                session.add(cat)
                session.commit()

            # add prompt variable category weight
            weight = session.query(PromptVariableCategoryWeight).filter_by(
                prompt_category=category,
                variable_category=cat
            ).first()
            if not weight:
                try:
                    weight_value = data["weights"][category_name]
                except KeyError:
                    weight_value = 1.0
                weight = PromptVariableCategoryWeight(
                    prompt_category=category,
                    variable_category=cat,
                    weight=weight_value
                )
                session.add(weight)
                session.commit()

            # add prompt variables
            for var in variable_values:
                session.add(PromptVariable(
                    value=var,
                    prompt_category=category,
                    variable_category=cat
                ))
            session.commit()

        def insert_variables(variables, prev_object=None):
            for option in variables:
                text = option.get("text", None)
                cond = option.get("cond", "")
                else_cond = option.get("else", "")
                next_cond = option.get("next", None)
                or_cond = option.get("or_cond", None)
                prompt_option = PromptOption(
                    text=text,
                    cond=cond,
                    else_cond=else_cond,
                    or_cond=or_cond,
                    prompt_id=prompt_id
                )
                if prev_object:
                    session.add(prompt_option)
                    session.commit()
                    prev_object.next_cond_id = prompt_option.id
                    session.add(prev_object)
                    session.commit()
                    prev_object = prompt_option
                else:
                    session.add(prompt_option)
                    session.commit()
                    prev_object = prompt_option
                if next_cond:
                    prev_object = insert_variables(
                        variables=next_cond,
                        prev_object=prev_object,
                    )
            return prev_object

        insert_variables(data["builder"])

        session.commit()

    for variable_category, data in variable_bootstrap_data.items():
        category = session.query(PromptVariableCategory).filter_by(name=variable_category).first()
        if not category:
            category = PromptVariableCategory(name=variable_category)
            session.add(category)
            session.commit()
        for variable in data:
            session.add(PromptVariable(
                value=variable,
                variable_category=category
            ))
        session.commit()

    # Add PromptStyle objects
    for style_category, data in style_bootstrap_data.items():
        category = PromptStyleCategory(name=style_category, negative_prompt=data["negative_prompt"])
        session.add(category)
        session.commit()
        for style in data["styles"]:
            session.add(PromptStyle(
                name=style,
                style_category=category
            ))
        session.commit()

    # Add ControlnetModel objects
    for name, path in controlnet_bootstrap_data.items():
        session.add(ControlnetModel(name=name, path=path))
    session.commit()


    # Add AIModel objects
    for model_data in model_bootstrap_data:
        session.add(AIModel(**model_data))
    session.commit()


    # Add Pipeline objects
    for pipeline_data in pipeline_bootstrap_data:
        session.add(Pipeline(**pipeline_data))
    session.commit()


    # Add PathSettings objects
    session.add(PathSettings())
    session.commit()


    # Add BrushSettings objects
    session.add(BrushSettings())
    session.commit()


    # Add GridSettings objects
    session.add(GridSettings())
    session.commit()


    # Add MetadataSettings objects
    session.add(MetadataSettings())
    session.commit()


    # Add MemorySettings objects
    session.add(MemorySettings())
    session.commit()


    # Add ImageFilter objects
    for filter in imagefilter_bootstrap_data:
        image_filter = ImageFilter(
            display_name=filter[0],
            name=filter[1],
            filter_class=filter[2]
        )
        for filter_value in filter[3]:
            image_filter.image_filter_values.append(ImageFilterValue(
                name=filter_value[0],
                value=filter_value[1],
                value_type=filter_value[2],
                min_value=filter_value[3] if len(filter_value) > 3 else None,
                max_value=filter_value[4] if len(filter_value) > 4 else None
            ))
        session.add(image_filter)
        session.commit()

    image_filter = session.query(ImageFilter).filter_by(name='color_balance').first()

    # Access its image_filter_values
    filter_values = image_filter.image_filter_values


    # Add Document object
    settings = Settings(nsfw_filter=True)
    settings.prompt_generator_settings.append(
        PromptGeneratorSetting(
            name="Prompt A",
            active=True,
            settings_id=settings.id
        )
    )
    settings.prompt_generator_settings.append(
        PromptGeneratorSetting(
            name="Prompt B",
            settings_id=settings.id
        )
    )
    settings.splitter_sizes.append(SplitterSection(
        name="content_splitter",
        order=0,
        size=390
    ))
    settings.splitter_sizes.append(SplitterSection(
        name="content_splitter",
        order=1,
        size=512
    ))
    settings.splitter_sizes.append(SplitterSection(
        name="content_splitter",
        order=2,
        size=200
    ))
    settings.splitter_sizes.append(SplitterSection(
        name="content_splitter",
        order=3,
        size=64
    ))
    settings.splitter_sizes.append(SplitterSection(
        name="main_splitter",
        order=0,
        size=520
    ))
    settings.splitter_sizes.append(SplitterSection(
        name="main_splitter",
        order=1,
        size=-1
    ))
    session.add(settings)

    settings.brush_settings = session.query(BrushSettings).first()
    settings.path_settings = session.query(PathSettings).first()
    settings.grid_settings = session.query(GridSettings).first()
    settings.metadata_settings = session.query(MetadataSettings).first()
    settings.memory_settings = session.query(MemorySettings).first()

    for section in sections_bootstrap_data:
        for generator_name in sections_bootstrap_data[section]:
            settings.generator_settings.append(GeneratorSetting(
                section=section,
                generator_name=generator_name
            ))

    session.add(Document(
        name="Untitled",
        settings=settings
    ))
    session.commit()
