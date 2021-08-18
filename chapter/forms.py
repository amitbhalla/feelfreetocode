from django.forms import ModelForm, CharField, Textarea


from chapter.models import TextChapter


class TextChapterForm(ModelForm):
    content = CharField(widget=Textarea)

    class Meta:
        model = TextChapter
        fields = "__all__"
