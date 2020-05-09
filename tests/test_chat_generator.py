import numpy as np
import pandas as pd
from datetime import datetime
from whatstk.objects import WhatsAppChat
from whatstk.utils.chat_generator import ChatGenerator


USERS = ['laurent', 'anna', 'lua', 'miquel']


def test_generate_messages():
    cg = ChatGenerator(size=10, users=USERS)
    messages = cg.generate_messages()
    assert(isinstance(messages, (list, np.ndarray)))
    assert(all([isinstance(m, str) for m in messages]))


def test_generate_emojis():
    cg = ChatGenerator(size=10, users=USERS)
    emojis = cg.generate_emojis()
    assert(isinstance(emojis, (list, np.ndarray)))
    assert(all([isinstance(e, str) for e in emojis]))


def test_generate_timestamps_1():
    cg = ChatGenerator(size=10, users=USERS)
    timestamps = cg.generate_timestamps()
    assert(isinstance(timestamps, (list, np.ndarray)))
    assert(all([isinstance(ts, datetime) for ts in timestamps]))


def test_generate_timestamps_2():
    cg = ChatGenerator(size=10, users=USERS)
    timestamps = cg.generate_timestamps(last=datetime.now())
    assert(isinstance(timestamps, (list, np.ndarray)))
    assert(all([isinstance(ts, datetime) for ts in timestamps]))


def test_generate_users():
    cg = ChatGenerator(size=10, users=USERS)
    users = cg.generate_users()
    assert(isinstance(users, (list, np.ndarray)))
    assert(all([isinstance(u, str) for u in users]))


def test_generate_df():
    cg = ChatGenerator(size=10, users=USERS)
    df = cg.generate_df()
    assert(isinstance(df, pd.DataFrame))


def test_generate_1():
    cg = ChatGenerator(size=10, users=USERS)
    chat = cg.generate()
    assert(isinstance(chat, WhatsAppChat))


def test_generate_2():
    cg = ChatGenerator(size=10, users=USERS)
    chat = cg.generate(hformat='%Y-%m-%d, %H:%M - %name:')
    assert(isinstance(chat, WhatsAppChat))


def test_generate_3(tmpdir):
    cg = ChatGenerator(size=10, users=USERS)
    filename = tmpdir.join("export.txt")
    chat = cg.generate(filename=str(filename))
    assert(isinstance(chat, WhatsAppChat))


def test_export(tmpdir):
    cg = ChatGenerator(size=10, users=USERS)
    chat = cg.generate()
    filename = tmpdir.join("export.txt")
    chat = cg.export(chat, str(filename))
