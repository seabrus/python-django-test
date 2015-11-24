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

# EXAMPLES
#self.assertTrue(response.content.startswith(b'<html>'))
#self.assertIn(b'<title>To-Do lists</title>', response.content)
#self.assertTrue(response.content.strip().endswith(b'</html>'))


class NameViewTests(TestCase):
    def setUp(self):
        """
        3 choices are need because choice_pk = 3 is used in the view
        """
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
