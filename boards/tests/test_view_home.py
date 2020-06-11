# 作者      : pengcheng
# 创建时间  : 2020/6/8 16:20
from django.test import TestCase
from django.urls import resolve, reverse

from boards.models import Board
from boards.views import BoardListView


class HomeTest(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django',description='Django board.')
        url = reverse('home')
        self.respones = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.respones.status_code,200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class,BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics',kwargs={'pk':self.board.pk})
        self.assertContains(self.respones,'href="{0}"'.format(board_topics_url))