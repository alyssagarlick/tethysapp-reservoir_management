# This python script tells the app how to navigate between html pages. When you want to add a new page to the app, create an html page,
# refer to it in the url_maps function here, and add a link to the new page in the base.html

#This is also where you put the information, icon, color, etc of the app itself.

from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class ReservoirManagement(TethysAppBase):
    """
    Tethys app class for Dam Inventory.
    """

    name = 'Herramientas de Operaciones de los Embalses'
    index = 'reservoir_management:home'
    icon = 'reservoir_management/images/droplets.png'
    package = 'reservoir_management'
    root_url = 'reservoir-management'
    color = '#01AEBF'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='reservoir-management',
                controller='reservoir_management.controllers.home'
            ),
            UrlMap(name='reportar',
                   url='reservoir-management/reportar',
                   controller='reservoir_management.controllers.reportar'
                   ),
            UrlMap(
                name='sabana_yegua',
                url='reservoir-management/sabana_yegua',
                controller='reservoir_management.controllers.sabana_yegua'
            ),
            UrlMap(
                name='hatillo',
                url='reservoir-management/hatillo',
                controller='reservoir_management.controllers.hatillo'
            ),
            UrlMap(
                name='maguaca',
                url='reservoir-management/maguaca',
                controller='reservoir_management.controllers.maguaca'
            ),
            UrlMap(
                name='chacuey',
                url='reservoir-management/chacuey',
                controller='reservoir_management.controllers.chacuey'
            ),
            UrlMap(
                name='jiguey',
                url='reservoir-management/jiguey',
                controller='reservoir_management.controllers.jiguey'
            ),
            UrlMap(
                name='moncion',
                url='reservoir-management/moncion',
                controller='reservoir_management.controllers.moncion'
            ),
            UrlMap(
                name='pinalito',
                url='reservoir-management/pinalito',
                controller='reservoir_management.controllers.pinalito'
            ),
            UrlMap(
                name='rincon',
                url='reservoir-management/rincon',
                controller='reservoir_management.controllers.rincon'
            ),
            UrlMap(
                name='sabaneta',
                url='reservoir-management/sabaneta',
                controller='reservoir_management.controllers.sabaneta'
            ),
            UrlMap(
                name='tavera_bao',
                url='reservoir-management/tavera_bao',
                controller='reservoir_management.controllers.tavera_bao'
            ),
            UrlMap(
                name='valdesia',
                url='reservoir-management/valdesia',
                controller='reservoir_management.controllers.valdesia'
            ),
        )

        return url_maps


    #These are the setting to connect to the geoserver (where the shapefiles are stored). You will also have to connect in tethys environment
    def spatial_dataset_service_settings(self):
        """
        Example spatial_dataset_service_settings method.
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name='main_geoserver',
                description='spatial dataset service for app to use',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

        return sds_settings
