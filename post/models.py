from django.db import models

# Create your models here.
STATUS_FIELDS =[
    ('draft','Draft'),
    ('published','Published'),
]


class Category(models.Model):
    title =models.CharField(max_length=150 ,verbose_name='Title')
    slug = models.SlugField(max_length=150 , unique=True,allow_unicode=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Tag(models.Model):
    title =models.CharField(max_length=50 ,verbose_name='Title')
    slug = models.SlugField(max_length=150 , unique=True ,allow_unicode=True)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    def __str__(self):
        return self.title


class Post(models.Model):
    title =models.CharField(max_length=255 ,verbose_name='Title')
    status = models.CharField(max_length=20, choices= STATUS_FIELDS , default='draft' ,verbose_name='Status')
    created_date = models.DateTimeField(verbose_name='Created')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category')
    picture =models.ImageField(upload_to='uploads/%Y/%m/%d',null =True ,blank=True, verbose_name='Picture')
    content = models.TextField(verbose_name='Content')
    author = models.CharField(max_length=20,default='홍길동',verbose_name='Created by')
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True,allow_unicode=True)
    objects = models.Manager()
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return self.title
