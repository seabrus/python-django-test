import datetime
from django.utils import timezone

from django.test import TestCase

from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.template.loader import render_to_string

from . models import Question, Choice
from . views import get_name


def create_question(question_text, days):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_choice(choice_text, question_pk=1, votes=0):
    return Choice.objects.create(choice_text=choice_text, question=Question.objects.get(pk=question_pk), votes=votes)


class NamePageTest(TestCase):
    """ 
    Your-Name page view resolution test
    """
    def test_url_resolves_to_get_name_view(self):
        found = resolve('/dj/your-name/')
        self.assertEqual(found.func, get_name)

    def test_name_page_returns_correct_html(self):
        request = HttpRequest()
        response = get_name(request)
        expected_html = render_to_string('dj/name-form/name.html')
        self.assertEqual(response.content.decode(), expected_html)


class NamePageTestDjangoStyle(TestCase):
    """ 
    Almost the same as above but with Django TestCase functions
    """
    @classmethod
    def setUpTestData(cls):
        """   3 choices are need because choice_pk = 3 is used in the view   """
        create_question(question_text="Question #1", days=-30)
        create_choice(choice_text="Choice #1", question_pk=1)
        create_choice(choice_text="Choice #2", question_pk=1)
        create_choice(choice_text="Choice #3", question_pk=1)


    def test_url_resolves_to_correct_view(self):
        response = self.client.get(reverse('dj:your_name'))
        self.assertEqual(response.resolver_match.func, get_name)

    def test_correct_templates_are_used(self):
        response = self.client.get('/dj/your-name/')
        self.assertTemplateUsed(response, 'dj/name-form/name.html')
        tmpl_names = [tmpl.name for tmpl in response.templates]
        print 'Templates used: ', tmpl_names
        self.assertIn('dj/base.html', tmpl_names) 
        self.assertIn('dj/name-form/name.html', tmpl_names) 
        self.assertIn('dj/name-form/name-form-partial.html', tmpl_names) 

    def test_response_has_correct_html(self):
        response = self.client.get('/dj/your-name/')
        expected_html = render_to_string('dj/name-form/name.html')
        self.assertContains(response, '<h3>InlineFormSet - Choices</h3>', html=True)


    def test_redirects_after_POST(self):
        response = self.client.post(
            reverse('dj:your_name'),
            data = {'your_name': 'Amy Sara', 'date_field': '2015-11-09'}
        )
        self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/dj/thanks/')
        self.assertRedirects(response, '/dj/thanks/')
        print 'Response Content-Type =', response['Content-Type']

    def test_AJAX_POST(self):
        response = self.client.post(
            reverse('dj:your_name'),
            data = {'your_name': 'Amy Sara', 'date_field': '2015-11-09'},
            HTTP_X_REQUESTED_WITH = 'XMLHttpRequest',                        # AJAX request
        )
        self.assertTemplateUsed(response, 'dj/name-form/name-form-partial.html', 'Template used ')
        self.assertEqual(response.status_code, 200)
        #print 'AJAX-response Location =', response['location']
        print 'AJAX-response Content-Type =', response['Content-Type']

"""
>>> MODEL testing example

    saved_list = List.objects.first()
    self.assertEqual(saved_list, list_)

    saved_items = Item.objects.all()
    self.assertEqual(saved_items.count(), 2)

    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    self.assertEqual(first_saved_item.text, 'The first (ever) list item')
    self.assertEqual(first_saved_item.list, list_)
    self.assertEqual(second_saved_item.text, 'Item the second')
    self.assertEqual(second_saved_item.list, list_)
"""


# SOME EXAMPLES
# response = self.client.get( '/lists/%d/' % (list_.id,) )                ---   '/lists/%d/' % (list_.id,)

#self.assertTrue(response.content.startswith(b'<html>'))
#self.assertIn(b'<title>To-Do lists</title>', response.content)
#self.assertTrue(response.content.strip().endswith(b'</html>'))


class NameViewTests(TestCase):
    def setUp(self):
        """   3 choices are need because choice_pk = 3 is used in the view   """
        create_question(question_text="Question #1", days=-30)
        create_choice(choice_text="Choice #1", question_pk=1)
        create_choice(choice_text="Choice #2", question_pk=1)
        create_choice(choice_text="Choice #3", question_pk=1)
 
    def test_inline_formset(self):
        """
        ChoiceInlineFormSet instance should be present in the responce
        """
        response = self.client.get(reverse('dj:your_name'))
        self.assertContains(response, 'Choice text inlineFormSet')
        


'''
class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('dj:dj_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('dj:dj_index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('dj:dj_index'))
        self.assertContains(response, "No polls are available.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('dj:dj_index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('dj:dj_index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        response = self.client.get(reverse('dj:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(question_text='Past Question.',  days=-5)
        response = self.client.get(reverse('dj:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text, status_code=200)

'''
