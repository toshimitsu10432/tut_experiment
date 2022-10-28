pre_e = 0
sum_e = 0
# 比例利得K_p, 積分利得K_i, 微分利得K_d,エラー値e, 制御周期dt
def pid(K_p, K_i, K_d, e, dt):
    sum_e += e*dt
    p = K_p*e
    i = K_i*sum_e
    d = K_d*(e-pre_e/dt)
    pre_e = e
    return p + i + d
