from random import randrange


def test_delete_group(app):
    if len (app.group.get_group_list()) <= 1:
         app.group.add_new_group("my group")
    old_list = app.group.get_group_list()
    index = randrange(len(old_list))
    app.group.delete_group(index)
    del old_list[index]
    new_list = app.group.get_group_list()
    assert len(old_list) == len(new_list)
    assert sorted(old_list) == sorted(new_list)