from django.db import models
import uuid

class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length = 200)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-timestamp', 'title']

class Paragraph(models.Model):
	post_id = models.ForeignKey(Post, related_name='content', on_delete=models.CASCADE)
	content = models.TextField()
	sequence = models.IntegerField()
	
	def __str__(self):
		return self.content[:20]
	
class Comment(models.Model) : 
	para_id = models.ForeignKey(Paragraph, related_name='comment', on_delete=models.CASCADE)
	comment_text = models.TextField()
	timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)

	def __str__(self):
		return self.comment_text[:20]

	class Meta:
		ordering = ['-timestamp']