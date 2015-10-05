from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import  RequestContext

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from drealtime import iShoutClient
ishout_client = iShoutClient()

@login_required
def home(request):
		
		users = User.objects.exclude(id=request.user.id)

		variables = RequestContext(request, {'users':users})
		return render_to_response ('home.html', variables)


@login_required
def alert(request):
	r = request.GET.get

	ishout_client.emit(

			int(r('user')),
			   'alertchannel',
			   data = {'msg':'Hello Alok, I am at DLF CyberTower'}

		)

return HttpResponseRedirect(reverse('home'))