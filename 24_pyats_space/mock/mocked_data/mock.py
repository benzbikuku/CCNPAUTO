from genie.testbed import load
tb = load('/home/benz/CCNPAUTO/24_pyats_space/mock/mocked_data/mock.yaml')
dev = tb.devices['nx-osv-1']
dev.connect()