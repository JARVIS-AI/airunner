import os

from airunner.data.models.settings_db_handler import SettingsDBHandler
from airunner.data.models.settings_models import Lora, Embedding

def scan_path_for_lora(base_path) -> bool:
    lora_added = False
    lora_deleted = False

    db_handler = SettingsDBHandler()
    for versionpath, versionnames, versionfiles in os.walk(os.path.expanduser(os.path.join(base_path, "art/models"))):
        version = versionpath.split("/")[-1]
        lora_path = os.path.expanduser(
            os.path.join(
                base_path,
                "art/models",
                version,
                "lora"
            )
        )
        if not os.path.exists(lora_path):
            continue

        session = db_handler.get_db_session()
        existing_lora = session.query(Lora).all()
        for lora in existing_lora:
            if not os.path.exists(lora.path):
                session.delete(lora)
                lora_deleted = True
        for dirpath, dirnames, filenames in os.walk(lora_path):
            for file in filenames:
                if file.endswith(".ckpt") or file.endswith(".safetensors") or file.endswith(".pt"):
                    name = file.replace(".ckpt", "").replace(".safetensors", "").replace(".pt", "")
                    path = os.path.join(dirpath, file)
                    item = db_handler.get_lora_by_name(name)
                    if not item or item.path != path or item.version != version:
                        item = Lora(
                            name=name,
                            path=path,
                            scale=1,
                            enabled=False,
                            loaded=False,
                            trigger_word="",
                            version=version
                        )
                        session.add(item)
                        lora_added = True
        if lora_deleted or lora_added:
            session.commit()
            session.close()
    return lora_deleted or lora_added

def scan_path_for_embeddings(base_path) -> bool:
    embedding_added = False
    embedding_deleted = False
    db_handler = SettingsDBHandler()
    items = []
    for versionpath, versionnames, versionfiles in os.walk(os.path.expanduser(os.path.join(base_path, "art/models"))):
        version = versionpath.split("/")[-1]
        embedding_path = os.path.expanduser(
            os.path.join(
                base_path,
                "art/models",
                version,
                "embeddings"
            )
        )
        if not os.path.exists(embedding_path):
            continue
        session = db_handler.get_db_session()
        existing_embeddings = session.query(Embedding).all()
        for embedding in existing_embeddings:
            if not os.path.exists(embedding.path):
                session.delete(embedding)
                embedding_deleted = True
        for dirpath, dirnames, filenames in os.walk(embedding_path):
            for file in filenames:
                if file.endswith(".ckpt") or file.endswith(".safetensors") or file.endswith(".pt"):
                    name = file.replace(".ckpt", "").replace(".safetensors", "").replace(".pt", "")
                    path = os.path.join(dirpath, file)
                    item = db_handler.get_embedding_by_name(name)
                    if not item or item.path != path or item.version != version:
                        item = Embedding(
                            name=name,
                            path=path,
                            version=version,
                            tags="",
                            active=False,
                            trigger_word=""
                        )
                        session.add(item)
                        embedding_added = True
        if embedding_deleted or embedding_added:
            session.commit()
            session.close()
    return embedding_deleted or embedding_added