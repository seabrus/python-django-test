"""
#from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#from django.template import RequestContext, loader

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('dj/index.html')
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    context = {'latest_question_list': latest_question_list}
    #return HttpResponse(template.render(context))
    return render(request, 'dj/index.html', context)


def detail(request, question_id):
    """ """try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """ """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'dj/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'dj/results.html', {'question': question})
"""
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'dj/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'dj/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'dj/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'dj/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('dj:results', args=(p.id,)))


from django import forms
from django.contrib import messages

from .models import Question
from .forms import NameForm, QuestionForm

def get_name(request):
    AjaxFormSet = forms.modelformset_factory(Question, form=QuestionForm)

    # if this is a POST request
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if 'your_name' in request.POST:
            form = NameForm(request.POST)
            ajax_formset = AjaxFormSet()

            # check whether it's valid:
            if form.is_valid():
                return HttpResponseRedirect('/dj/thanks/')
            else:
                # Display a list of valid data 
                for clean_prop in form.cleaned_data:
                    messages.add_message(request, messages.INFO, clean_prop + ' = ' + unicode(form.cleaned_data[ clean_prop ]))   
                                                                                                                # str() -- raises UnicodeEncodeError for russian letters
                    #messages.add_message(request, messages.INFO, clean_prop + ' = ' + form.cleaned_data[ clean_prop ])     # no error, too
                # Prepare error fields
                for prop in NameForm.base_fields:   #for prop in form.fields:
                    if prop in form.errors:
                        form.fields[ prop ].widget = getattr(forms, form.fields[ prop ].widget_type)( attrs={'class': 'form-control field-has-error'} )
                            #e.g.: forms.TextInput( attrs={'class': 'form-control field-has-error'} )

        else:
            form = NameForm()
            ajax_formset = AjaxFormSet(request.POST, request.FILES)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        ajax_formset = AjaxFormSet()
        #ajax_form = QuestionForm( instance=Question.objects.get(pk=3) )

    return render(request, 'dj/name-form/name.html', {'form': form, 'ajax_formset': ajax_formset})
    #return render(request, 'dj/name-form/name.html', {'form': form, 'ajax_form': ajax_form})



"""
            for prop in dir(NameForm):
                if not prop.startswith('__') and not callable(getattr(NameForm, prop)):
                    print prop
                    if prop in form.errors and prop == 'your_name':
                        form.fields[ prop ].widget = forms.TextInput( attrs={'class': 'form-control field-has-error'} )

            if 'your_name' in form.errors:
                form.fields['your_name'].widget = forms.TextInput( attrs={'class': 'form-control field-has-error'} )
            if 'date_field' in form.errors:
                form.fields['date_field'].widget = forms.DateInput( attrs={'class': 'form-control field-has-error'} )
"""


