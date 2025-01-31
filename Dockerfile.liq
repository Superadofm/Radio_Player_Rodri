FROM savonet/liquidsoap:latest

COPY autodj.liq /autodj.liq

CMD ["liquidsoap", "/autodj.liq"]
