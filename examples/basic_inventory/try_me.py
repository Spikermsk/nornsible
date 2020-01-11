from nornir import InitNornir
from nornir.plugins.tasks import networking


def main():
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(name="c3560")
    agg_result = nr.run(
        task=networking.netmiko_send_command, command_string="show run | i hostname"
    )
    print(agg_result["c3560"].result)


if __name__ == "__main__":
    main()
