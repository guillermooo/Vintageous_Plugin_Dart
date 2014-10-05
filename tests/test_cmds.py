import sublime

import unittest

from Vintageous.state import State
from Vintageous.vi.utils import modes


TESTS = ()

# =============================================================
# you need to edit this test; it won't work like this
# =============================================================
class Test_sample(unittest.TestCase):
    def testAll_InternalNormalMode(self):
        for (i, data) in enumerate(TESTS):

            self.write('dog cat turkey')
            self.clear_sel()
            self.add_sel(self.R(4))
            self.state.mode = modes.INTERNAL_NORMAL

            motion = {}
            motion['motion'] = '_vi_e'
            motion['motion_args'] = {'mode': modes.INTERNAL_NORMAL, 'count': 1}

            surround_with, expected = data
            self.view.run_command('_vi_plug_ys', {'mode': modes.INTERNAL_NORMAL,
                                                   'surround_with': surround_with,
                                                   'motion': motion})

            actual = self.view.substr(self.R(0, self.view.size()))
            self.assertEqual(actual, expected, 'failed at {0}'.format(i))

            self.erase_all()
