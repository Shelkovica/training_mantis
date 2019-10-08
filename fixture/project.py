from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        self.open_manage_page()
        if not(wd.current_url.endswith("manage_proj_page.php") and len(wd.find_elements_by_link_text("Manage Projects")) > 0):
            wd.find_element_by_link_text("Manage Projects").click()

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_overview_page.php") and len(
                wd.find_elements_by_link_text("Site Information") > 0)):
            wd.find_element_by_link_text("Manage").click()

    def get_project_list(self):
        wd = self.app.wd
        if self.project_cache is None:
            self.open_projects_page()
            self.project_cache=[]
            for row in wd.find_elements_by_xpath('//a[contains(@href, "?project_id")]'):
                name = row.text
                id = str(row.get_attribute("href"))[70:]
                self.project_cache.append(Project(name=name, id=id))
        return list(self.project_cache)

    def add_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.app.wd.implicitly_wait(1)
      #  wd.find_element_by_link_text("Manage Projects")
        self.project_cache = None
        self.return_to_home_page()

    def del_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_name("project_id").text
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_xpath("//div[@align='center']/hr").text
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.app.wd.implicitly_wait(1)
        self.project_cache = None
        self.return_to_home_page()


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("my_view_page.php") and len(wd.find_element_by_link_text("Unassigned")) > 0):
            wd.find_element_by_link_text("My View").click()
