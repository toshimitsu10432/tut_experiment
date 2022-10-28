pre_e = 0
sum_e = 0
# 比例利得K_p, 積分利得K_i, エラー値e, 制御周期dt
def pid(K_p, K_i, e, dt):
    sum_e += e*dt
    p = K_p*e
    i = K_i*sum_e
    d = K_p*(abs(pre_e-e)/dt)
    pre_e = e
    return p + i + d