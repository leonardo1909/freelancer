from rest_framework import status
from rest_framework.test import APITestCase


class TestCPF_CNPJ(APITestCase):

    def test_exemples(self):
        '''
            Test:
                - Test freelancer example.
            Expected Result:
                - It expect the result shown on the
                readme.
        '''
        data = {
            'freelance': {
                'id': 42,
                'user': {
                    'firstName': 'Hunter',
                    'lastName': 'Moore',
                    'jobTitle': 'Fullstack JS Developer'
                },
                'status': 'new',
                'retribution': 650,
                'availabilityDate': '2018-06-13T00:00:00+01:00',
                'professionalExperiences': [
                    {
                        'id': 4,
                        'companyName': 'Okuneva, Kerluke and Strosin',
                        'startDate': '2016-01-01T00:00:00+01:00',
                        'endDate': '2018-05-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 241,
                                'name': 'React'
                            },
                            {
                                'id': 270,
                                'name': 'Node.js'
                            },
                            {
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 54,
                        'companyName': 'Hayes - Veum',
                        'startDate': '2014-01-01T00:00:00+01:00',
                        'endDate': '2016-09-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 470,
                                'name': 'MySQL'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            },
                            {
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 80,
                        'companyName': 'Harber, Kirlin and Thompson',
                        'startDate': '2013-05-01T00:00:00+01:00',
                        'endDate': '2014-07-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 370,
                                'name': 'Javascript'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            }
                        ]
                    }
                ]
            }
        }

        response = self.client.post(
            '/frelancer/experience/',
            data,
            format='json'
        )

        expected_response = {
            'freelance': {
                'id': 42,
                'computedSkills': [
                    {
                        'id': 241,
                        'name': 'React',
                        'durationInMonths': 28
                    },
                    {
                        'id': 270,
                        'name': 'Node.js',
                        'durationInMonths': 28
                    },
                    {
                        'id': 370,
                        'name': 'Javascript',
                        'durationInMonths': 60
                    },
                    {
                        'id': 400,
                        'name': 'Java',
                        'durationInMonths': 40
                    },
                    {
                        'id': 470,
                        'name': 'MySQL',
                        'durationInMonths': 32
                    }
                ]
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_experience_start_date_equal(self):
        '''
            Test:
                - Test freelancer that have two experiences with
                at least one same technology and both started at the same date.
            Expected Result:
                - As the both started at the same date, the comom technology
                experience with shorter duration won't be considered.
        '''
        data = {
            'freelance': {
                'id': 42,
                'user': {
                    'firstName': 'Hunter',
                    'lastName': 'Moore',
                    'jobTitle': 'Fullstack JS Developer'
                },
                'status': 'new',
                'retribution': 650,
                'availabilityDate': '2018-06-13T00:00:00+01:00',
                'professionalExperiences': [
                    {
                        'id': 4,
                        'companyName': 'Okuneva, Kerluke and Strosin',
                        'startDate': '2016-01-01T00:00:00+01:00',
                        'endDate': '2018-05-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 241,
                                'name': 'React'
                            },
                            {
                                'id': 270,
                                'name': 'Node.js'
                            },
                            {
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 54,
                        'companyName': 'Hayes - Veum',
                        'startDate': '2016-01-01T00:00:00+01:00',
                        'endDate': '2016-09-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 470,
                                'name': 'MySQL'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            },
                            {
                                #this Javascript experience won't be counted.
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 80,
                        'companyName': 'Harber, Kirlin and Thompson',
                        'startDate': '2013-05-01T00:00:00+01:00',
                        'endDate': '2014-07-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 370,
                                'name': 'Javascript'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            }
                        ]
                    }
                ]
            }
        }

        response = self.client.post(
            '/frelancer/experience/',
            data,
            format='json'
        )

        expected_response = {
            'freelance': {
                'id': 42,
                'computedSkills': [
                    {
                        'id': 241,
                        'name': 'React',
                        'durationInMonths': 28
                    },
                    {
                        'id': 270,
                        'name': 'Node.js',
                        'durationInMonths': 28
                    },
                    {
                        'id': 370,
                        'name': 'Javascript',
                        'durationInMonths': 42
                    },
                    {
                        'id': 400,
                        'name': 'Java',
                        'durationInMonths': 22
                    },
                    {
                        'id': 470,
                        'name': 'MySQL',
                        'durationInMonths': 8
                    }
                ]
            }
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_invalid_payload(self):
        '''
            Test:
                - Test an invalid freelance payload.
                - The key "freelance" are miswritten.
            Expected Result:
                - The endpoint must return 422 status code.
        '''
        data = {
            'frelance': {
                'id': 42,
                'user': {
                    'firstName': 'Hunter',
                    'lastName': 'Moore',
                    'jobTitle': 'Fullstack JS Developer'
                },
                'status': 'new',
                'retribution': 650,
                'availabilityDate': '2018-06-13T00:00:00+01:00',
                'professionalExperiences': [
                    {
                        'id': 4,
                        'companyName': 'Okuneva, Kerluke and Strosin',
                        'startDate': '2016-01-01T00:00:00+01:00',
                        'endDate': '2018-05-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 241,
                                'name': 'React'
                            },
                            {
                                'id': 270,
                                'name': 'Node.js'
                            },
                            {
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 54,
                        'companyName': 'Hayes - Veum',
                        'startDate': '2016-01-01T00:00:00+01:00',
                        'endDate': '2016-09-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 470,
                                'name': 'MySQL'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            },
                            {
                                #this Javascript experience won't be counted.
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 80,
                        'companyName': 'Harber, Kirlin and Thompson',
                        'startDate': '2013-05-01T00:00:00+01:00',
                        'endDate': '2014-07-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 370,
                                'name': 'Javascript'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            }
                        ]
                    }
                ]
            }
        }

        response = self.client.post(
            '/frelancer/experience/',
            data,
            format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    def test_invalid_experience_start_date(self):
        '''
            Test:
                - Test an invalid freelance experience start date.
                - The date must start with the first day of the month.
            Expected Result:
                - The endpoint must return 422 status code.
        '''
        data = {
            'freelance': {
                'id': 42,
                'user': {
                    'firstName': 'Hunter',
                    'lastName': 'Moore',
                    'jobTitle': 'Fullstack JS Developer'
                },
                'status': 'new',
                'retribution': 650,
                'availabilityDate': '2018-06-13T00:00:00+01:00',
                'professionalExperiences': [
                    {
                        'id': 4,
                        'companyName': 'Okuneva, Kerluke and Strosin',
                        'startDate': '2016-01-05T00:00:00+01:00',
                        'endDate': '2018-05-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 241,
                                'name': 'React'
                            },
                            {
                                'id': 270,
                                'name': 'Node.js'
                            },
                            {
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 54,
                        'companyName': 'Hayes - Veum',
                        'startDate': '2016-01-01T00:00:00+01:00',
                        'endDate': '2016-09-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 470,
                                'name': 'MySQL'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            },
                            {
                                #this Javascript experience won't be counted.
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 80,
                        'companyName': 'Harber, Kirlin and Thompson',
                        'startDate': '2013-05-01T00:00:00+01:00',
                        'endDate': '2014-07-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 370,
                                'name': 'Javascript'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            }
                        ]
                    }
                ]
            }
        }

        response = self.client.post(
            '/frelancer/experience/',
            data,
            format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    def test_experience_invalid_date(self):
        '''
            Test:
                - Test validation for an invalid date
            Expected Result:
                - The endpoint must return 422 status code.
        '''
        data = {
            'freelance': {
                'id': 42,
                'user': {
                    'firstName': 'Hunter',
                    'lastName': 'Moore',
                    'jobTitle': 'Fullstack JS Developer'
                },
                'status': 'new',
                'retribution': 650,
                'availabilityDate': '2018-06-13T00:00:00+01:00',
                'professionalExperiences': [
                    {
                        'id': 4,
                        'companyName': 'Okuneva, Kerluke and Strosin',
                        'startDate': '2016-13-05T00:00:00+01:00',
                        'endDate': '2018-05-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 241,
                                'name': 'React'
                            },
                            {
                                'id': 270,
                                'name': 'Node.js'
                            },
                            {
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 54,
                        'companyName': 'Hayes - Veum',
                        'startDate': '2016-01-01T00:00:00+01:00',
                        'endDate': '2016-09-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 470,
                                'name': 'MySQL'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            },
                            {
                                'id': 370,
                                'name': 'Javascript'
                            }
                        ]
                    },
                    {
                        'id': 80,
                        'companyName': 'Harber, Kirlin and Thompson',
                        'startDate': '2013-05-01T00:00:00+01:00',
                        'endDate': '2014-07-01T00:00:00+01:00',
                        'skills': [
                            {
                                'id': 370,
                                'name': 'Javascript'
                            },
                            {
                                'id': 400,
                                'name': 'Java'
                            }
                        ]
                    }
                ]
            }
        }

        response = self.client.post(
            '/frelancer/experience/',
            data,
            format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_422_UNPROCESSABLE_ENTITY
        )
