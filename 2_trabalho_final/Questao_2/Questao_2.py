# Código usado/executado dentro da VM para criar a topologia utilizada na questão 2;

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class topologia_questao_2(Topo):

    def build(self):

        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")
        s7 = self.addSwitch("s7")

        h1 = self.addHost("h1", ip="10.0.0.1/24", mac="00:00:00:00:00:01")
        h2 = self.addHost("h2", ip="10.0.0.2/24", mac="00:00:00:00:00:02")
        h3 = self.addHost("h3", ip="10.0.0.3/24", mac="00:00:00:00:00:03")
        h4 = self.addHost("h4", ip="10.0.0.4/24", mac="00:00:00:00:00:04")
        h5 = self.addHost("h5", ip="10.0.0.5/24", mac="00:00:00:00:00:05")
        h6 = self.addHost("h6", ip="10.0.0.6/24", mac="00:00:00:00:00:06")

        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s7)

        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s7)
        self.addLink(h5, s7)
        self.addLink(h6, s7)


def executar_topologia():
    topo = topologia_questao_2()

    net = Mininet(
        topo=topo,
        controller=None,
        switch=OVSSwitch
    )

    net.start()

    print("\nTopologia inicializada.")
    print("Controlador manual: controller=None")

    CLI(net)

    net.stop()


topos = {"questao2": topologia_questao_2}


if __name__ == "__main__":
    setLogLevel("info")
    executar_topologia()
    