from tests.testLogin import *
from tests.testDashboard import *
from tests.testTimeTracking import *
from tests.testEmployees import *


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Dante_Login))
suite.addTests(loader.loadTestsFromModule(Dante_Dashboard))
suite.addTests(loader.loadTestsFromModule(Dante_TimeTracking))
suite.addTests(loader.loadTestsFromModule(Dante_Employees))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

