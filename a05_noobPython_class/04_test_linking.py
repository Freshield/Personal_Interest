import tensorflow as tf

print(type(tf.train.AdamOptimizer()))

class Mouth(object):

    word = 'say '

    @classmethod
    def say(cls,some):
        print(cls.word + some)

class Body(object):

    mouth = Mouth()


class People:

    body = Body()
    name = 'lol'



People.body.mouth.say('hello')