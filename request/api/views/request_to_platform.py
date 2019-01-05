import requests
import json
from agri_platform.settings import PLATFORM_URL
from request.models import MyUser
from request.utils.login_required import login_required

Plt_url = PLATFORM_URL


class Auth:
    def __init__(self):
        self.url_auth = Plt_url + "/auth"

    def login(self, username, password, remember):
        raw_data = {"username": username, "password": password, "remember": remember}
        json_login = json.dumps(raw_data)

        try:
            response = requests.post(self.url_auth + "/login", data=json_login)
            if response.status_code == 200:
                token = {'access_token': response.json()['access_token'],
                         'refresh_token': response.json()['refresh_token']}
                return token

            else:
                return "try again"
        except:
            return "Error => Auth:login() "

    def refresh(self, access_token, refresh_token):
        header = {"Authorization": "Bearer " + access_token}
        raw_data = {"token": refresh_token}
        json_refresh = json.dumps(raw_data)

        try:
            response = requests.post(self.url_auth + "/refresh", data=json_refresh, headers=header)
            if response.status_code == 200:
                token = {'access_token': response.json()['access_token'],
                         'refresh_token': response.json()['refresh_token']}
                return token

            else:
                return "try again"
        except:
            return "Error => Auth:refresh() "


class Projects:
    def __init__(self, token):
        self.url_projects = Plt_url + "/projects"
        self.access_token = token["access_token"]
        self.refresh_token = token["refresh_token"]

    def get_projects(self):
        header = {"Authorization": "Bearer " + self.access_token}

        try:
            response = requests.get(self.url_projects, headers=header)

            # Successful
            print(response.status_code)
            if response.status_code == 200:
                return response.json()

            # Unauthorized

            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                print(u.access_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()
                print(u.access_token)
                return Projects(token_new).get_projects()

            else:
                return "Error1 => Projects:get_projects() "

        except:
            return "Error2 => Projects:get_projects() "

    def get_project_detail(self, id):
        header = {"Authorization": "Bearer " + self.access_token}

        try:
            response = requests.get(self.url_projects + "/" + id, headers=header)

            # Successful
            if response.status_code == 200:
                return response.json()

            # Unauthorized
            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()

                return Projects(token_new).get_project_detail(id)


            else:
                return "Error1 => Projects:get_project_detail()"

        except:
            return "Error2 => Projects:get_project_detail() "

    def create_project(self, name, additionalProp=None):
        header = {"Authorization": "Bearer " + self.access_token}

        new_proj = {"name": name, "envs": additionalProp}
        json_proj = json.dumps(new_proj)

        try:
            response = requests.post(self.url_projects, data=json_proj, headers=header)

            # Successful
            if response.status_code == 200:
                return response.json()

            # Unauthorized
            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()

                return Projects(token_new).create_project(name, additionalProp)

            else:
                return "Error1 => Projects:create_project()"

        except:
            return "Error2 => Projects:create_project() "


class Things:
    def __init__(self, token):
        self.url_things = Plt_url + "/projects"
        self.access_token = token["access_token"]
        self.refresh_token = token["refresh_token"]

    def get_project_things(self, id_project):
        header = {"Authorization": "Bearer " + self.access_token}

        try:
            response = requests.get(self.url_things + "/%s/things" % id_project, headers=header)

            # Successful
            if response.status_code == 200:
                return response.json()

            # Unauthorized
            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()

                return Things(token_new).get_project_things(id_project)

            else:
                return "Error1 => Projects:get_project_things()"

        except:
            return "Error2 => Projects:get_project_things() "

    def get_thing_data(self, id_project, id_thing):
        header = {"Authorization": "Bearer " + self.access_token}

        try:
            response = requests.get(self.url_things + "/%s/things/%s" % (id_project, id_thing), headers=header)

            # Successful
            if response.status_code == 200:
                return response.json()

            # Unauthorized
            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()

                return Things(token_new).get_thing_data(id_project, id_thing)

            else:
                return response.status_code

        except:
            return "Error2 => Things:get_thing_data() "

    def add_thing(self, id_project, thing_data):
        # thing_data format =>
        # {
        #   "name": "0000000000000073",
        #   "model": "aolab",
        #   "location": {
        #     "lat": 35.807657,
        #     "long": 51.398408
        #   }
        # }

        header = {"Authorization": "Bearer " + self.access_token}

        json_thing = json.dumps(thing_data)

        try:
            response = requests.post(self.url_things + "/%s/things" % id_project, data=json_thing, headers=header)

            # Successful
            if response.status_code == 200:
                return response.json()

            # Unauthorized
            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()

                return Things(token_new).add_thing(id_project, thing_data)

            else:
                return "Error1 => Projects:add_thing()"

        except:
            return "Error2 => Projects:add_thing() "


class Data:
    def __init__(self, token, project_id, thing_id):
        self.url_data = Plt_url + "/projects%s/things/%s/queries/" % project_id, thing_id
        self.access_token = token["access_token"]
        self.refresh_token = token["refresh_token"]
        self.project_id = project_id
        self.thing_id = thing_id

    def fetch_data_in_time_range(self, time_range_aset):
        # Time range format : {
        #   "range": {
        #     "from": "2018-12-26T06:29:53.414Z",
        #     "to": "2018-12-26T06:29:53.414Z"
        #   },
        #   "type": "number",
        #   "target": "string"
        # }

        header = {"Authorization": "Bearer " + self.access_token}

        json_query = json.dumps(time_range_aset)

        try:
            response = requests.post(self.url_data + "fetch", data=json_query, headers=header)

            # Successful
            if response.status_code == 200:
                return response.json()

            # Unauthorized
            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()

                return Data(token_new, self.project_id, self.thing_id).fetch_data_in_time_range(time_range_aset)

            else:
                return "Error1 => Data:fetch_data_in_time_range()"

        except:
            return "Error2 => Data:fetch_data_in_time_range()"

    def get_recent_data(self, assset):
        # {
        #   "asset": "string",
        #   "limit": 0,
        #   "offset": 0
        # }

        header = {"Authorization": "Bearer " + self.access_token}

        json_query = json.dumps(assset)

        try:
            response = requests.post(self.url_data + "recently", data=json_query, headers=header)

            # Successful
            if response.status_code == 200:
                return response.json()

            # Unauthorized
            elif response.status_code == 401:
                u = MyUser.objects.get(access_token=self.access_token, refresh_token=self.refresh_token)
                token_new = Auth().refresh(self.access_token, self.refresh_token)
                print(token_new)
                u.access_token = token_new.get('access_token')
                u.refresh_token = token_new.get('refresh_token')
                u.save()

                return Data(token_new, self.project_id, self.thing_id).fetch_data_in_time_range(assset)

            else:
                return "Error1 => Data:fetch_data_in_time_range()"

        except:
            return "Error2 => Data:fetch_data_in_time_range()"
