from logging import exception
from werkzeug import cached_property
import markdown
import yaml


class Post(object):
    post_delimeter = '---'
    def __init__(self,path):
        self.path = path
        self._initialize_metadata_()

    def _initialize_metadata_(self):
        content = ''
        with open(self.path, 'r') as fin:
            for line in fin:
                if not line.strip():
                    break
                content += line
                self.__dict__.update(yaml.load(content))



    @cached_property
    def html(self):
        # --- is delimeter for the post.
        with open(self.path,'r') as fin:
            content = fin.read().split(self.post_delimeter,1)[1].strip()
        return markdown.markdown(content)
