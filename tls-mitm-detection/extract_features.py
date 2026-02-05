import pyshark
import pandas as pd

pcap_file = "capture/tls_traffic.pcap"

cap = pyshark.FileCapture(pcap_file, display_filter="tls.handshake")

features = []

for pkt in cap:
    try:
        tls = pkt.tls

        record = {
            "tls_version": tls.handshake_version if hasattr(tls, "handshake_version") else 0,
            "cipher_suite": tls.handshake_ciphersuite if hasattr(tls, "handshake_ciphersuite") else 0,
            "cert_length": len(tls.handshake_certificate) if hasattr(tls, "handshake_certificate") else 0,
            "handshake_type": tls.handshake_type,
            "packet_length": int(pkt.length),
            "time_delta": float(pkt.sniff_time.timestamp())
        }

        features.append(record)

    except Exception:
        pass

cap.close()

df = pd.DataFrame(features)
df.to_csv("tls_features.csv", index=False)

print("TLS handshake features extracted successfully.")
