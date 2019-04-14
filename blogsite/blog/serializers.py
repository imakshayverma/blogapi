from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
	Post, 
	Paragraph, 
	Comment
	)

class ParagraphSerializer(ModelSerializer):
	class Meta:
		model = Paragraph
		fields = [
			'id',
			'content', 
			'sequence'
		]

class CommentSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = [
            'comment_text',
            'timestamp',
			]

class ParagraphWithCommentsSerializer(ModelSerializer):
	comment = CommentSerializer(many=True)
	class Meta:
		model = Paragraph
		fields = [
			'id',
			'content', 
			'sequence',
			'comment'
		]


class PostListSerializer(ModelSerializer):
	content = ParagraphSerializer(many=True)
	class Meta:
	    model = Post
	    fields = [
	    	'id',
	        'title',
	        'content',
	        'timestamp',
		]


class PostSerializer(ModelSerializer):
	content = serializers.CharField() 
	class Meta:
		model = Post
		fields = [
            'title',
            'timestamp',
            'content'
		]

	def create(self, validated_data):
		"""
		Explicit definition to add respective objects to their respective models - Post and Paragraph.
		"""
		para_data = validated_data.pop('content')
		post = Post.objects.create(**validated_data)
		para_counter = 0
		for para  in para_data.split('\n\n'):
			if len(para.strip('\n')) > 0:
				para_counter += 1
				Paragraph.objects.create(post_id = post, content = para.strip('\n'), sequence=para_counter)
		return post


class PostShowSerializer(ModelSerializer):
	content = ParagraphWithCommentsSerializer(many=True)
	class Meta:
		model = Post
		fields = [
			'id',
		    'title',
		    'timestamp',
		    'content',
		]
