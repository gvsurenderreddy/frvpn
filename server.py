import argparse
import pytun
import channel
import udplink

parser = argparse.ArgumentParser()
parser.add_argument('--tun', metavar='name')
parser.add_argument('addr')

args = parser.parse_args()

tun = pytun.TunTapDevice(**dict(name=args.tun)
                         if args.tun else {})

ch = channel.ChannelServer()
ch.server_loop(file=tun,
               addr=udplink.parse_addr(args.addr))
