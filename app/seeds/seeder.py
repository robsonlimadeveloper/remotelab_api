# pylint: disable=line-too-long,too-many-locals,broad-except,too-many-statements
"""This module run seeds"""
from .seed_user import seeds as user_seed
from .seed_experiment import seeds as experiment_seed
from .seed_user_type import seeds as user_type_seed
from .seed_institute import seeds as institute_seed
from .seed_discipline_type import seeds as discipline_type_seed

class Seeds:
    """This class run seeds"""
    def __init__(self, db, modules):
        self.session = db.session
        self.modules = modules

    def run(self):
        """This method run seeds"""

        user = self.modules.user.model.User
        experiment = self.modules.experiment.model.Experiment
        user_type = self.modules.user_type.model.UserType
        institute = self.modules.institute.model.Institute
        discipline_type = self.modules.discipline_type.model.DisciplineType

        try:
            discipline_types = discipline_type_seed(discipline_type)
            institutes = institute_seed(institute)
            experiments = experiment_seed(experiment)
            user_types = user_type_seed(user_type)
            users = user_seed(user)

        except Exception as error:
            print(error)
        try:
            print("Getting Started First Seeds ...")
            
            self.session.add_all(users)
            self.session.add_all(institutes)
            self.session.add_all(user_types)
            self.session.add_all(experiments)
            self.session.add_all(discipline_types)

            print("Successfully inserted data from First Seed")
        except Exception as error:
            self.session.rollback()
            print(f"Error: {error}")
            raise
        else:
            self.session.commit()

        self.session.close()
