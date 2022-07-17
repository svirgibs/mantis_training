import random
from model.project import Project


def test_delete_project(app):
    app.session.ensure_login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project("New Test Project"))
    old_projects = app.project.get_project_list()
    random_project = random.choice(old_projects)
    app.project.delete_project_by_name(random_project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(random_project)
    assert len(old_projects) == len(new_projects)
    app.session.ensure_logout()
