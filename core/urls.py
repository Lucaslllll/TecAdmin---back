from rest_framework import routers
from .api import (TechayUserViewSet, GraphSiteViewSet, SocialNetworkingViewSet,
PlanViewSet, UserClientViewSet, AddressViewSet, GraphTeamViewSet,
NotificationViewSet, VoteViewSet, VideoViewSet, CollectViewSet)

router = routers.DefaultRouter()

router.register('api/techay_user', TechayUserViewSet, 'techay_user')
router.register('api/graph_site', GraphSiteViewSet, 'graph_site')
router.register('api/social_networking', SocialNetworkingViewSet, 'social_networking')
router.register('api/plan', PlanViewSet, 'plan')
router.register('api/user_client', UserClientViewSet, 'user_client')
router.register('api/address', AddressViewSet, 'address')
router.register('api/graph_team', GraphTeamViewSet, 'graph_team')
router.register('api/notification', NotificationViewSet, 'notification')
router.register('api/vote', VoteViewSet, 'vote')
router.register('api/video', VideoViewSet, 'video')
router.register('api/collect', CollectViewSet, 'collect')







urlpatterns = router.urls