require 'yaml'

CONFIG = YAML.load_file(File.join(File.dirname(__FILE__), 'config.yml'))

Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  config.vm.define CONFIG['server']['name'] do |cfg|
    cfg.vm.box = CONFIG['server']['box']
    cfg.vm.network "public_network", ip: CONFIG['server']['ip']
    cfg.vm.hostname = CONFIG['server']['hostname']
    
    cfg.vm.provider "virtualbox" do |v|
      v.memory = CONFIG['server']['memory']
      v.cpus = CONFIG['server']['cpu']
      v.name = CONFIG['server']['name']
    end

    # ssh 비밀번호인증 활성화
    cfg.vm.provision "shell", inline: <<-SCRIPT
      sed -i -e 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
      systemctl restart sshd
    SCRIPT

    # install loki, promtail, grafana
    cfg.vm.provision "shell", inline: <<-SCRIPT
      apt-get update
      apt-get install -y vim net-tools wget

      # loki
      # reference: https://github.com/grafana/loki/releases/
      curl -O -L "https://github.com/grafana/loki/releases/download/v2.4.1/loki-linux-amd64.zip"
      unzip "loki-linux-amd64.zip"
      chmod a+x "loki-linux-amd64"
      wget https://raw.githubusercontent.com/grafana/loki/master/cmd/loki/loki-local-config.yaml

      # promtail
      # reference: https://github.com/grafana/loki/releases/
      curl -O -L https://github.com/grafana/loki/releases/download/v2.4.1/promtail-linux-amd64.zip
      unzip "promtail-linux-amd64.zip"
      chmod a+x "promtail-linux-amd64"
      wget https://raw.githubusercontent.com/grafana/loki/main/clients/cmd/promtail/promtail-local-config.yaml

      # grafana
      # reference: https://grafana.com/docs/grafana/latest/installation/debian/
      # reference: https://grafana.com/grafana/download?platform=linux
      wget https://dl.grafana.com/enterprise/release/grafana-enterprise-8.3.0.linux-amd64.tar.gz
      tar -zxvf grafana-enterprise-8.3.0.linux-amd64.tar.gz
    SCRIPT
  end
end