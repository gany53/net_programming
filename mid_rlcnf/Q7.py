import socket
import struct
import binascii

class Udphdr:
    def __init__(self, sp, dp, len, cs):
        self.sp = sp
        self.dp = dp
        self.len = len
        self.cs = cs

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!H', self.sp)
        packed += struct.pack('!H', self.dp)
        packed += struct.pack('!H', self.len)
        packed += struct.pack('!H', self.cs)
        return packed
    
def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

    
udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))

# import socket
# import struct
# import binascii

# class Iphdr:
#     def __init__(self, tot_len, protocol, saddr, daddr):
#         self.ver_len = 0x45
#         self.tos = 0
#         self.tot_len = tot_len
#         self.id = 0
#         self.frag_off = 0
#         self.ttl = 127
#         self.protocol = protocol #TCP(6)/UDP(17)
#         self.check = 0
#         self.saddr = socket.inet_aton(saddr)
#         self.daddr = socket.inet_aton(daddr)

#     def pack_Iphdr(self):
#         packed = b''
#         packed += struct.pack('!BBH', self.ver_len, self.tos, self.tot_len)
#         packed += struct.pack('!HH', self.id, self.frag_off)
#         packed += struct.pack('!BBH', self.ttl, self.protocol, self.check)
#         packed += struct.pack('!4s', self.saddr)
#         packed += struct.pack('!4s', self.daddr)
#         return packed
    
# def unpack_Iphdr(buffer):
#     unpacked = struct.unpack('!BBHHHBBH4s4s', buffer[:20])
#     return unpacked
# def getPacketSize(unpacked_ipheader):
#     return unpacked_ipheader[2]
# def getProtocolId(unpacked_ipheader):
#     return unpacked_ipheader[6]
# def getIP(unpacked_ipheader):
#     src_ip = socket.inet_ntoa(unpacked_ipheader[8])
#     dst_ip = socket.inet_ntoa(unpacked_ipheader[9])
#     return (src_ip, dst_ip)
    
# ip = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')
# packed_iphdr = ip.pack_Iphdr()
# print(binascii.b2a_hex(packed_iphdr))

# unpacked_iphdr = unpack_Iphdr(packed_iphdr)
# print(unpacked_iphdr)
# print('Packet size:{} Protocol:{} IP:{}'.format(getPacketSize(unpacked_iphdr), getProtocolId(unpacked_iphdr), getIP(unpacked_iphdr)))