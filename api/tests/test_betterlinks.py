import pytest
from rest_framework import status
from api.models import BetterLink, ProtocolChoices

@pytest.mark.django_db
class TestBetterLinkAPI:
    def test_create_betterlink(self, client):
        c = client()
        long_link = "https://docs.djangoproject.com/en/4.2/intro/tutorial01/"
        c.post("/api/bls/", {'long_link': long_link}, format='json')
        assert BetterLink.objects.count() == 1

    def test_create_betterlink_and_redirect_flow(self, client):
        c = client()
        long_link = "https://docs.djangoproject.com/en/4.2/intro/tutorial01/"
        response = c.post("/api/bls/", {'long_link': long_link}, format='json')
        assert BetterLink.objects.count() == 1
        bl = BetterLink.objects.last()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {'old_link': 'https://docs.djangoproject.com/en/4.2/intro/tutorial01/', 'short_link': f"http://localhost:8000/api/blsr/{bl.short_link}"}

        # test redirect
        response = c.get(f"/api/blsr/{bl.short_link}/")
        assert response.status_code == status.HTTP_302_FOUND
        assert response.url == long_link

    def test_shortlink_already_exists(self, client):
        c = client()
        long_link = "https://docs.djangoproject.com/en/4.2/intro/tutorial01/"
        short_link = "abc1234"

        _ = BetterLink.objects.create(
            old_long_link_proto=ProtocolChoices.HTTPS,
            old_link_url=long_link.split("://")[1],
            short_link=short_link
        )

        response = c.post("/api/bls/", {'long_link': long_link, 'short_link': short_link}, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'short_link' in response.data
        assert response.data['short_link'][0] == 'Short link already exists in the database.'

    def test_bl_list(self, client):
        c = client()
        long_link = "https://docs.djangoproject.com/en/4.2/intro/tutorial01/"
        _ = c.post("/api/bls/", {'long_link': long_link}, format='json')
        assert BetterLink.objects.count() == 1

        last = BetterLink.objects.last()

        response = c.get("/api/bls/")
        assert response.status_code == 200
        assert response.json() == {
            'count': 1,
            'next': None, 
            'previous': None,
            'results': [
                {
                    'old_link': 'https://docs.djangoproject.com/en/4.2/intro/tutorial01/', 
                    'short_link': f'http://localhost:8000/api/blsr/{last.short_link}'
                }
            ]
        }
