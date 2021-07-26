from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_Kargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação precisa estar entra 1 e 5.')


class CursoSerializar(serializers.ModelSerializer):
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    avaliacao = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacao = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacao',
            'media_avaliacao'
        )

    def get_media_avaliacao(self, obj):
        media = obj.avaliacao.aggregate(Avg('avaliacao')).get('avaliacao_avg')
        if media is None:
            return 0
        return round(media * 2) / 2
