from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class SpatialDataViewer(TethysAppBase):
    """
    Tethys app class for Spatial Data Viewer.
    """

    name = 'Spatial Data Viewer'
    index = 'spatial_data_viewer:home'
    icon = 'spatial_data_viewer/images/cuahsi_logo.png'
    package = 'spatial_data_viewer'
    root_url = 'spatial-data-viewer'
    color = '#008080'
    description = 'This app allows users to preview HydroShare Geographic Feature and Raster Resources.'
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
                url='spatial-data-viewer',
                controller='spatial_data_viewer.controllers.home'
            ),
        )

        return url_maps

    def spatial_dataset_service_settings(self):
        """
        Defines spatial dataset service settings
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name='hs-apps-dev_geoserver',
                description='GeoServer to be used for temporarily mounting user lcoal data.',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
            SpatialDatasetServiceSetting(
                name='hydroshare_geoserver',
                description='GeoServer used by HydroShare to publish resources.',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

        return sds_settings
