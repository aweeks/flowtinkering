import sys
import re
from datetime import *
from collections import namedtuple

Flow = namedtuple( 'Flow', ['start_datetime', 'duration', 'protocol', 'src_ip', 'src_port', 'dst_ip', 'dst_port', 'num_packets', 'num_bytes', 'num_flows'] )

with open(sys.argv[1], 'r') as f:
    flow_lines = f.readlines()

flows = list()
#                          date time       duration   proto    src_ip  src_port         dst_ip dst_port n_pkts n_bytes  n_flows
flow_re = re.compile('([\d-]* [\d:\.]*)\s*([\d\.]*)\s*(\S*)\s*([\d\.]*)\:(\d*)\s*->\s*([\d\.]*)\:(\d*)\s*(\d*)\s*(\d*)\s*(\d*)')

def parse_flow(flow_str):
    match = flow_re.match(flow_str)
    try:
        groups = match.groups()
        #print groups
        return Flow(datetime.strptime(groups[0], '%Y-%m-%d %H:%M:%S.%f'),  # start_datetime
                    timedelta(seconds=float(groups[1])),                   # duration
                    groups[2],                                             # protocol
                    groups[3],                                             # src_ip
                    int(groups[4]),                                        # src_port
                    groups[5],                                             # dst_ip
                    int(groups[6]),                                        # dst_port
                    int(groups[7]),                                        # num_packets
                    int(groups[8]),                                        # num_bytes
                    int(groups[9]) )                                       # num_flows
    except Exception:
        return None

for line in flow_lines:
    parsed = parse_flow(line)
    if parsed:
        flows.append(parsed)

for f in flows[0:10]:
    print f
