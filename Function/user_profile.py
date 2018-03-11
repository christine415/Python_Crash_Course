# **user_profile creates an empty dictionary called user_profile
def build_profile(first, last, **user_profile):
    '''Build a dictionary containing everything we know about the user.'''
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for k, v in user_profile.items():
        profile[k] = v
    return profile

profile = build_profile("Albert", "Eistein", location="princeton", field="physics")
print(profile)