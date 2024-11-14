import os


def main(**kwargs):
    import action_build_oomp
    import action_build_release

    action_build_oomp.main(**kwargs)
    action_build_release.main(**kwargs)





if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)