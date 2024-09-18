import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Conversation, Message, Summary

class AgentDatabaseHandler:
    def __init__(self, db_path=os.path.expanduser(
        os.path.join(
            "~/.airunner",
            "data",
            "agent_history.db"
        )
    )):
        self.db_path = db_path
        self.engine = create_engine(f'sqlite:///{self.db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.conversation_id = None

    def get_db_session(self):
        return self.Session()

    def load_history_from_db(self, conversation_id):
        with self.get_db_session() as session:
            messages = session.query(Message).filter_by(conversation_id=conversation_id).order_by(Message.timestamp).all()
            return [
                {
                    "role": message.role,
                    "content": message.content,
                    "name": message.name,
                    "is_bot": message.is_bot,
                    "timestamp": message.timestamp,
                    "conversation_id": message.conversation_id
                } for message in messages
            ]

    def add_message_to_history(self, content, role, name, is_bot, conversation_id):
        timestamp = datetime.datetime.now()  # Ensure timestamp is a datetime object
        with self.get_db_session() as session:
            message = Message(
                role=role,
                content=content,
                name=name,
                is_bot=is_bot,
                timestamp=timestamp,
                conversation_id=conversation_id
            )
            session.add(message)
            session.commit()

    def create_conversation(self):
        with self.get_db_session() as session:
            conversation = Conversation(
                timestamp=datetime.datetime.utcnow(),
                title=""
            )
            session.add(conversation)
            session.commit()
            return conversation.id

    def add_summary(self, content, conversation_id):
        timestamp = datetime.datetime.now()  # Ensure timestamp is a datetime object
        with self.get_db_session() as session:
            summary = Summary(
                content=content,
                timestamp=timestamp,
                conversation_id=conversation_id
            )
            session.add(summary)
            session.commit()

    def create_conversation_with_messages(self, messages):
        conversation_id = self.create_conversation()
        for message in messages:
            self.add_message_to_history(
                content=message["content"],
                role=message["role"],
                name=message["name"],
                is_bot=message["is_bot"],
                conversation_id=conversation_id
            )
        return conversation_id

    def get_all_conversations(self):
        with self.get_db_session() as session:
            return session.query(Conversation).all()
