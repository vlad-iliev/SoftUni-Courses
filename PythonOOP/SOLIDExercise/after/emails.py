from abc import ABC, abstractmethod
class IContent:
    def __init__(self,content):
        self.content = content
        self.content_type = None


class MyContent(IContent):
    def __init__(self,content):
        super().__init__(content)
        self.content_type = 'MyML'



class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.content_type = None
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content:MyContent):
        if content.content_type == 'MyML':
            self.__content = '\n'.join(['<myML>', content.content, '</myML>'])
        else:
            self.__content = content.content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


email = Email('IM')

email.set_sender('qmal')

email.set_receiver('james')

content = MyContent('Hello, there!')

email.set_content(content)

print(email)