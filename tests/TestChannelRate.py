# TestChannelRate.py
#
# Test the channel rate feature introduced by Richard Harrison.
#
# Copyright (c) 2016 Bertrand Coconnier
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <http://www.gnu.org/licenses/>
#

import os
from JSBSim_utils import JSBSimTestCase, CreateFDM, RunTest, ExecuteUntil


class TestChannelRate(JSBSimTestCase):
    def setUp(self):
        JSBSimTestCase.setUp(self, 'check_cases', 'ground_tests')

    def testChannelRate(self):
        os.environ['JSBSIM_DEBUG'] = str(0)
        fdm = CreateFDM(self.sandbox)
        fdm.load_script(self.sandbox.path_to_jsbsim_file('scripts',
                                                         'systems-rate-test-0.xml'))
        fdm.run_ic()

        ExecuteUntil(fdm, 30.)

        self.assertEqual(fdm['simulation/frame'], fdm['tests/rate-1-v']-1)
        self.assertEqual(int(fdm['simulation/frame']/4),
                         fdm['tests/rate-4'])
        self.assertEqual(fdm['simulation/dt'], fdm['tests/rate-1-dt'])
        self.assertEqual(fdm['simulation/dt']*4, fdm['tests/rate-4-dt'])
        self.assertEqual(fdm['simulation/sim-time-sec'],
                         fdm['tests/rate-1-dt-sum'])
        self.assertAlmostEqual(fdm['simulation/dt'] * fdm['tests/rate-4'] * 4,
                               fdm['tests/rate-4-dt-sum'])

RunTest(TestChannelRate)