import threading

from airunner.data.models import AIModel
from airunner.utils import get_session
from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.model_manager.templates.import_ui import Ui_import_model_widget
from airunner.aihandler.download_civitai import DownloadCivitAI

class ImportWidget(BaseWidget):
    widget_class_ = Ui_import_model_widget
    model_widgets = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_import_form()

    def action_clicked_button_import(self):
        self.show_model_select_form()

    def action_clicked_button_download(self):
        self.show_download_form()

    def action_clicked_button_cancel(self):
        self.show_import_form()

    def show_import_form(self):
        self.ui.import_form.show()
        self.ui.model_select_form.hide()
        self.ui.download_form.hide()

    def show_model_select_form(self):
        print("SHOW MODEL SELECT FORM")
        self.ui.import_form.hide()
        self.ui.model_select_form.show()
        self.ui.download_form.hide()
        self.import_models()

    def show_download_form(self):
        self.ui.import_form.hide()
        self.ui.model_select_form.hide()
        self.ui.download_form.show()
        self.download_model()
    
    def download_model(self):
        print("DOWNLOAD MODEL")
        self.download_civit_ai = DownloadCivitAI()

        # get value from import_widget.model_choices
        download_url, file, model_version = self.ui.model_choices.currentData()
        size_kb = file["sizeKB"]

        model_data = self.current_model_data
        name = model_data["name"] + " " + model_version["name"]
        
        model_version_name = model_version["name"]
        categories = self.settings_manager.model_categories
        actions = self.settings_manager.pipeline_actions
        category = "stablediffusion"
        pipeline_action = "txt2img"
        if "inpaint" in model_version_name:
            pipeline_action = "outpaint"
        diffuser_model_version = model_version["baseModel"]
        pipeline_class = self.settings_manager.get_pipeline_classname(pipeline_action, diffuser_model_version, category)
        diffuser_model_versions = self.settings_manager.model_versions
        file_path = self.download_path(file, diffuser_model_version)  # path is the download path of the model

        print("Name", name)
        print("Path", file_path)
        print("Branch", "main")
        print("Version", diffuser_model_version)
        print("Category", category)
        print("Pipeline Action", pipeline_action)


        session = get_session()
        model_exists = session.query(AIModel).filter_by(
            name=name,
            path=file_path,
            branch="main",
            version=diffuser_model_version,
            category=category,
            pipeline_action=pipeline_action,
        ).first()
        if not model_exists:
            new_model = AIModel(
                name=name,
                path=file_path,
                branch="main",
                version=diffuser_model_version,
                category=category,
                pipeline_action=pipeline_action,
                enabled=True,
                is_default=False
            )
            session.add(new_model)
            session.commit()
        
        print("starting download")
        self.download_model_thread(download_url, file_path, size_kb)
        # self.thread = threading.Thread(target=self.download_model_thread, args=(download_url, file_path, size_kb))
        # self.thread.start()

    def download_model_thread(self, download_url, file_path, size_kb):
        self.download_civit_ai.download_model(download_url, file_path, size_kb, self.download_callback)

    def download_callback(self, current_size, total_size):
        current_size = int(current_size / total_size * 100)
        self.ui.download_progress_bar.setValue(current_size)
        if current_size >= total_size:
            self.reset_form()
            self.settings_manager.add_model(self.current_model_data)
            self.show_items_in_scrollarea()
    
    def import_models(self):
        url = self.ui.import_url.text()
        print("IMPORT MODELS")
        try:
            model_id = url.split("/")[4]
        except IndexError:
            return

        data = DownloadCivitAI.get_json(model_id)
        self.current_model_data = data
        self.is_civitai = "civitai.com" in url
        model_name = data["name"]
        model_versions = data["modelVersions"]
        self.ui.model_choices.clear()
        for model_version in model_versions:
            version_name = model_version["name"]
            download_url = model_version["downloadUrl"]
            sd_model_version = model_version["baseModel"]
            files = model_version["files"]
            # try:
            #     url = file["url"]
            # except KeyError:
            #     url = ""
            download_choice = f"{model_name} - {version_name} - {sd_model_version}"
            for file in files:
                self.ui.model_choices.addItem(
                    download_choice, 
                    (download_url, file, model_version)
                )

        self.ui.model_choices.currentIndexChanged.connect(self.model_version_changed)

        self.ui.name.setText(self.current_model_data["name"])
        if not self.current_model_data["nsfw"]:
            self.ui.nsfw_label.hide()
        else:
            self.ui.nsfw_label.show()
        
        if "creator" in self.current_model_data and "username" in self.current_model_data["creator"]:
            self.ui.creator.setText(
                f"By {self.current_model_data['creator']['username']}"
            )
        else:
            self.ui.creator.setText("")

        #self.current_model_object.url = url

        self.set_model_form_data()
    
    def model_version_changed(self, index):
        self.set_model_form_data()
    
    def download_path(self, file, version):
        path = self.settings_manager.path_settings.model_base_path
        file_name = file["name"]
        return f"{path}/{version}/{file_name}"

    def set_model_form_data(self):
        try:
            download_url, file, model_version = self.ui.model_choices.currentData()
        except TypeError:
            return
        model_version_name = model_version["name"]

        categories = self.settings_manager.model_categories
        actions = self.settings_manager.pipeline_actions
        category = "stablediffusion"
        pipeline_action = "txt2img"
        if "inpaint" in model_version_name:
            pipeline_action = "outpaint"
        diffuser_model_version = model_version["baseModel"]
        pipeline_class = self.settings_manager.get_pipeline_classname(pipeline_action, diffuser_model_version, category)
        diffuser_model_versions = self.settings_manager.model_versions
        path = self.download_path(file, diffuser_model_version)  # path is the download path of the model

        self.ui.model_form.set_model_form_data(
            categories, 
            actions, 
            diffuser_model_versions, 
            category, 
            pipeline_action, 
            pipeline_class, 
            diffuser_model_version, 
            path, 
            self.current_model_data["name"],
            model_data=self.current_model_data
        )

        if self.is_civitai:
            self.ui.model_form.ui.branch_label.hide()
            self.ui.model_form.ui.branch_line_edit.hide()