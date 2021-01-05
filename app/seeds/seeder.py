# pylint: disable=line-too-long,too-many-locals,broad-except,too-many-statements
"""This module run seeds"""
from .seed_user import seeds as user_seed

class Seeds:
    """This class run seeds"""
    def __init__(self, db, modules):
        self.session = db.session
        self.modules = modules

    def run(self):
        """This method run seeds"""
        
        user = self.modules.user.model.User

        try:
            users = user_seed(user)

        except Exception as error:
            print(error)

        try:
            print("Getting Started First Seeds ...")
            self.session.add_all(users)
            print("Successfully inserted data from First Seed")
        except Exception as error:
            self.session.rollback()
            print(f"Error: {error}")
            raise
        else:
            self.session.commit()

        self.session.close()
