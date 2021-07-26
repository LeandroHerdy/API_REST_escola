from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import CursoAPIView, AvaliacaoAPIView, CursosAPIView, AvaliacaosAPIView, CursoViewSet, AvaliacaoViewSet


router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes', AvaliacaosAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaosAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/', AvaliacaosAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]
