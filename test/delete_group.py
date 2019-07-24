
def test_delete_group(app):

    if len (app.group.get_group_list()) == 0:
        app.group.add_new_group("my group")
    old_list = app.group.get_group_list()
    app.group.delete_group("New_group")
    new_list = app.group.get_group_list()
    old_list.remove("my group")
    assert sorted(old_list) == sorted(new_list)