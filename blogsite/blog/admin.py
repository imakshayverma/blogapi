from django.contrib import admin

# Register your models here.
from .models import Post, Paragraph, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'timestamp']
	list_filter = ['title', 'timestamp']
	search_fields = ['title']
	class Meta:
		model = Post

class ParagraphAdmin(admin.ModelAdmin):
	list_display = ['post_id','content', 'sequence']
	list_filter = ['post_id','content',]
	search_fields = ['content']
	class Meta:
		model = Paragraph

class CommentAdmin(admin.ModelAdmin):
	list_display = ['para_id','comment_text',]
	list_filter = ['para_id','comment_text']
	search_fields = ['comment_text']
	class Meta:
		model = Comment

admin.site.register(Post, PostAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Comment, CommentAdmin)