from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def handle_PacketIn(event):
    packet = event.parsed
    
    # Verificando se é um pacote IPv4
    if packet.type == packet.IP_TYPE:
        log.info('\nIPv4 Packet:')
        log.info("Protocolo: %s", "TCP" if packet.payload.protocol == packet.payload.TCP_PROTOCOL else "UDP")
        log.info("IP origem: %s", packet.payload.srcip)
        log.info("IP destino: %s", packet.payload.dstip)
        log.info("MAC origem: %s", packet.src)
        log.info("MAC destino: %s", packet.dst)
        
        # Verificando o protocolo do pacote IPv4
        if packet.payload.protocol == packet.payload.TCP_PROTOCOL:
            log.info("Porta de origem: %s", packet.payload.payload.srcport)
            log.info("Porta de destino: %s", packet.payload.payload.dstport)
        elif packet.payload.protocol == packet.payload.UDP_PROTOCOL:
            log.info("Porta de origem: %s", packet.payload.payload.srcport)
            log.info("Porta de destino: %s", packet.payload.payload.dstport)
    
    # Acessando a VLAN TCI da entrada da tabela de fluxo
    vlan_tci = packet.find('vlan').vid if packet.find('vlan') is not None else 0x0000
    log.info("VLAN: %s", vlan_tci)

def launch():
    core.openflow.addListenerByName("PacketIn", handle_PacketIn)


