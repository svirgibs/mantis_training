from model.project import Project


def test_create_project(app):
    app.session.ensure_login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.create(Project(name="New project 3"))
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    app.session.ensure_logout()
