from django.shortcuts import render, get_object_or_404;
from django.http import HttpResponse, HttpResponseRedirect;
from django.template import loader;
from .models import Question, Choice;
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

# def index(request):
#     # return HttpResponse("My Django app this deepen the Bhishma")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         "latest_question_list":latest_question_list
#     }
#     return HttpResponse(template.render(context, request))


class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #  """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except:
#     #     raise Http404('Question does not exists')
#     question= get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html',{'question':question})
    

class DetailView(generic.DetailView):
        model = Question
        template_name='polls/detail.html'

        def get_queryset(self):
            """
            Excludes any questions that aren't published yet.
            """
            return Question.objects.filter(pub_date__lte=timezone.now())



# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request, 'polls/results.html', {"question":question})
        
class ResultsView(generic.DetailView):
     model=Question
     template_name='polls/results.html'


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question,pk = question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
        # print('-------------')
        # print(request.POST)
        # print('-------------')
    except (KeyError, Choice.DoesNotExist):
        return render(request, 
                      {
                       "question": question,
                       "error_message": 'You did not select a choice'   
                      })
    else:
        
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        

def get_queryset(self):
      """
    Return the last five published questions (not including those set to be
    pub
    """
      return Question.objects.filter(pub_date__lte= timezone.now()).order_by('-pub_date')[:5]