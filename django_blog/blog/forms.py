from django import forms
from django.forms import widgets
from .models import Tag

# Custom Tag Widget
class TagWidget(widgets.CheckboxSelectMultiple):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = Tag.objects.all()  # Get all the tags from the database
        super().__init__(*args, **kwargs)

# Post Form (For Creating and Editing Posts)
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by('name'),  # Sort tags alphabetically
        required=False,  # Allow posts without tags
        widget=TagWidget(),  # Using the custom TagWidget here
        label="Select Tags"
    )

    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter the title of the post'}),
        label='Post Title'
    )
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write the content of your post here'}),
        label='Post Content'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include the 'tags' field
