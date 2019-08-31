from django.test import TestCase
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    
    def test_all_articles_page_is_default(self):
        # self.client.get is used to fake a url request
        page = self.client.get("/articles/")
        # testing the status code
        self.assertEqual(page.status_code, 200)
        # testing that the correct template was rendered
        self.assertTemplateUsed(page, "index.html")
    
    
    def test_redirect_from_write(self):
        """
        If someone enters the url to render write.html they should be redirected.
        301 is the HTTPS redirect code.
        """
        page = self.client.get("/articles/write")
        self.assertEqual(page.status_code, 301)


    


    