import os


def main(**kwargs):
    import action_oomp_create_parts
    import action_build_oomp
    import action_build_release

    action_oomp_create_parts.main(**kwargs)
    action_build_oomp.main(**kwargs)
    action_build_release.main(**kwargs)





if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)