from QABase import QABase

db = QABase("postgresql://postgres@localhost/QA")


def test_db_connection():
    names = db.db_connection()
    assert len(names) == 5


def test_select_from_group_student():
    inf = db.get_info_group_student()
    assert len(inf) == 676


def test_select_from_subject():
    inf = db.get_info_subject()
    assert len(inf) == db.count_from_subject()


def test_insert_into_subject():
    subject_id = 2
    subject_title = "Химия"
    count = db.count_from_subject()
    db.insert_into_subject(subject_id, subject_title)
    assert len(db.get_info_subject()) == count + 1

    db.delete_from_subject(subject_id)


def test_update_subject_title():
    subject_id = 100
    subject_title = "English"
    new_subject_title = "Биология"
    db.insert_into_subject(subject_id, subject_title)
    db.update_subject_title(new_subject_title, subject_id)
    body = db.get_info_subject_by_subject_id(subject_id)
    assert body[0]["subject_title"] == new_subject_title

    db.delete_from_subject(subject_id)


def test_update_subject_id():
    subject_title = "Химия"
    subject_id = 124
    new_subject_id = 126
    db.insert_into_subject(subject_id, subject_title)
    db.update_subject_id(new_subject_id, subject_title)
    body = db.get_info_subject_by_subject_title(subject_title)
    assert body[0]["subject_id"] == new_subject_id

    db.delete_from_subject(new_subject_id)


def test_delete_from_subject():
    subject_id = 15
    subject_title = "Chemy"
    db.insert_into_subject(subject_id, subject_title)
    count = db.count_from_subject()
    db.delete_from_subject(subject_id)
    assert len(db.get_info_subject()) == count - 1