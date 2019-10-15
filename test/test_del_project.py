from model.project import Project
import random

def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.add_project(Project(name="test add"))
    old_projects = app.soap.get_project_list("administrator", "root")
    project = random.choice(old_projects)
    app.project.del_project(project)
    new_projects = app.soap.get_project_list("administrator", "root")
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
