from tethys_sdk.base import TethysAppBase, url_map_maker


class SpatialDataViewer(TethysAppBase):
    """
    Tethys app class for Spatial Data Viewer.
    """

    name = 'Spatial Data Viewer'
    index = 'spatial_data_viewer:home'
    icon = 'spatial_data_viewer/images/icon.gif'
    package = 'spatial_data_viewer'
    root_url = 'spatial-data-viewer'
    color = '#2980b9'
    description = '&quot;This app allows users to preview HydroShare Geographic Feature and Raster Resources.&quot;'
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
