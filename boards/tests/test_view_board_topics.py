# 作者      : pengcheng
# 创建时间  : 2020/6/8 16:20
from django.test import TestCase
from django.urls import reverse, resolve

from boards.models import Board
from boards.views import board_topics


class BoardTopicsTest(TestCase):
    def setUp(self):
        Board.objects.create(name="Django",description="Django board.")

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics',kwargs={'pk':1})
        respones = self.client.get(url)
        self.assertEquals(respones.status_code,200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics',kwargs={'pk':99})
        respones = self.client.get(url)
        self.assertEquals(respones.status_code,404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func,board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics',kwargs={'pk':1})
        respones = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(respones,'href="{0}"'.format(homepage_url))