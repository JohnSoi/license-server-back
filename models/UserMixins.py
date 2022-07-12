from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_mixin, declared_attr


@declarative_mixin
class UserMixins:
    @declared_attr
    def create_user_id(self):
        return Column(Integer, ForeignKey('users.id'))

    @declared_attr
    def update_user_id(self):
        return Column(Integer, ForeignKey('users.id'))

    @declared_attr
    def delete_user_id(self):
        return Column(Integer, ForeignKey('users.id'))

