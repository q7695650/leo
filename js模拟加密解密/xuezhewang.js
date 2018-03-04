function strEnc(E, u, a, d) {
    var g = E.length;
    var h = "";
    var B, v, s, F, f, l;
    if (u != null && u != "") {
        B = getKeyBytes(u);
        F = B.length
    }
    if (a != null && a != "") {
        v = getKeyBytes(a);
        f = v.length
    }
    if (d != null && d != "") {
        s = getKeyBytes(d);
        l = s.length
    }
    if (g > 0) {
        if (g < 4) {
            var C = strToBt(E);
            var e;
            if (u != null && u != "" && a != null && a != "" && d != null && d != "") {
                var A;
                var q, p, o;
                A = C;
                for (q = 0; q < F; q++) {
                    A = enc(A, B[q])
                }
                for (p = 0; p < f; p++) {
                    A = enc(A, v[p])
                }
                for (o = 0; o < l; o++) {
                    A = enc(A, s[o])
                }
                e = A
            } else {
                if (u != null && u != "" && a != null && a != "") {
                    var A;
                    var q, p;
                    A = C;
                    for (q = 0; q < F; q++) {
                        A = enc(A, B[q])
                    }
                    for (p = 0; p < f; p++) {
                        A = enc(A, v[p])
                    }
                    e = A
                } else {
                    if (u != null && u != "") {
                        var A;
                        var q = 0;
                        A = C;
                        for (q = 0; q < F; q++) {
                            A = enc(A, B[q])
                        }
                        e = A
                    }
                }
            }
            h = bt64ToHex(e)
        } else {
            var t = parseInt(g / 4);
            var r = g % 4;
            var w = 0;
            for (w = 0; w < t; w++) {
                var c = E.substring(w * 4 + 0, w * 4 + 4);
                var D = strToBt(c);
                var e;
                if (u != null && u != "" && a != null && a != "" && d != null && d != "") {
                    var A;
                    var q, p, o;
                    A = D;
                    for (q = 0; q < F; q++) {
                        A = enc(A, B[q])
                    }
                    for (p = 0; p < f; p++) {
                        A = enc(A, v[p])
                    }
                    for (o = 0; o < l; o++) {
                        A = enc(A, s[o])
                    }
                    e = A
                } else {
                    if (u != null && u != "" && a != null && a != "") {
                        var A;
                        var q, p;
                        A = D;
                        for (q = 0; q < F; q++) {
                            A = enc(A, B[q])
                        }
                        for (p = 0; p < f; p++) {
                            A = enc(A, v[p])
                        }
                        e = A
                    } else {
                        if (u != null && u != "") {
                            var A;
                            var q;
                            A = D;
                            for (q = 0; q < F; q++) {
                                A = enc(A, B[q])
                            }
                            e = A
                        }
                    }
                }
                h += bt64ToHex(e)
            }
            if (r > 0) {
                var b = E.substring(t * 4 + 0, g);
                var D = strToBt(b);
                var e;
                if (u != null && u != "" && a != null && a != "" && d != null && d != "") {
                    var A;
                    var q, p, o;
                    A = D;
                    for (q = 0; q < F; q++) {
                        A = enc(A, B[q])
                    }
                    for (p = 0; p < f; p++) {
                        A = enc(A, v[p])
                    }
                    for (o = 0; o < l; o++) {
                        A = enc(A, s[o])
                    }
                    e = A
                } else {
                    if (u != null && u != "" && a != null && a != "") {
                        var A;
                        var q, p;
                        A = D;
                        for (q = 0; q < F; q++) {
                            A = enc(A, B[q])
                        }
                        for (p = 0; p < f; p++) {
                            A = enc(A, v[p])
                        }
                        e = A
                    } else {
                        if (u != null && u != "") {
                            var A;
                            var q;
                            A = D;
                            for (q = 0; q < F; q++) {
                                A = enc(A, B[q])
                            }
                            e = A
                        }
                    }
                }
                h += bt64ToHex(e)
            }
        }
    }
    return h
}

function strDec(D, t, a, c) {
    var e = D.length;
    var f = "";
    var B, v, q, E, d, h;
    if (t != null && t != "") {
        B = getKeyBytes(t);
        E = B.length
    }
    if (a != null && a != "") {
        v = getKeyBytes(a);
        d = v.length
    }
    if (c != null && c != "") {
        q = getKeyBytes(c);
        h = q.length
    }
    var s = parseInt(e / 16);
    var A = 0;
    for (A = 0; A < s; A++) {
        var b = D.substring(A * 16 + 0, A * 16 + 16);
        var g = hexToBt64(b);
        var C = new Array(64);
        var u = 0;
        for (u = 0; u < 64; u++) {
            C[u] = parseInt(g.substring(u, u + 1))
        }
        var r;
        if (t != null && t != "" && a != null && a != "" && c != null && c != "") {
            var w;
            var p, o, l;
            w = C;
            for (p = h - 1; p >= 0; p--) {
                w = dec(w, q[p])
            }
            for (o = d - 1; o >= 0; o--) {
                w = dec(w, v[o])
            }
            for (l = E - 1; l >= 0; l--) {
                w = dec(w, B[l])
            }
            r = w
        } else {
            if (t != null && t != "" && a != null && a != "") {
                var w;
                var p, o, l;
                w = C;
                for (p = d - 1; p >= 0; p--) {
                    w = dec(w, v[p])
                }
                for (o = E - 1; o >= 0; o--) {
                    w = dec(w, B[o])
                }
                r = w
            } else {
                if (t != null && t != "") {
                    var w;
                    var p, o, l;
                    w = C;
                    for (p = E - 1; p >= 0; p--) {
                        w = dec(w, B[p])
                    }
                    r = w
                }
            }
        }
        f += byteToString(r)
    }
    return f
}

function getKeyBytes(d) {
    var a = new Array();
    var c = d.length;
    var e = parseInt(c / 4);
    var f = c % 4;
    var b = 0;
    for (b = 0; b < e; b++) {
        a[b] = strToBt(d.substring(b * 4 + 0, b * 4 + 4))
    }
    if (f > 0) {
        a[b] = strToBt(d.substring(b * 4 + 0, c))
    }
    return a
}

function strToBt(l) {
    var a = l.length;
    var o = new Array(64);
    if (a < 4) {
        var g = 0,
            f = 0,
            c = 0,
            b = 0;
        for (g = 0; g < a; g++) {
            var e = l.charCodeAt(g);
            for (f = 0; f < 16; f++) {
                var h = 1,
                    d = 0;
                for (d = 15; d > f; d--) {
                    h *= 2
                }
                o[16 * g + f] = parseInt(e / h) % 2
            }
        }
        for (c = a; c < 4; c++) {
            var e = 0;
            for (b = 0; b < 16; b++) {
                var h = 1,
                    d = 0;
                for (d = 15; d > b; d--) {
                    h *= 2
                }
                o[16 * c + b] = parseInt(e / h) % 2
            }
        }
    } else {
        for (g = 0; g < 4; g++) {
            var e = l.charCodeAt(g);
            for (f = 0; f < 16; f++) {
                var h = 1;
                for (d = 15; d > f; d--) {
                    h *= 2
                }
                o[16 * g + f] = parseInt(e / h) % 2
            }
        }
    }
    return o
}

function bt4ToHex(b) {
    var a;
    switch (b) {
        case "0000":
            a = "0";
            break;
        case "0001":
            a = "1";
            break;
        case "0010":
            a = "2";
            break;
        case "0011":
            a = "3";
            break;
        case "0100":
            a = "4";
            break;
        case "0101":
            a = "5";
            break;
        case "0110":
            a = "6";
            break;
        case "0111":
            a = "7";
            break;
        case "1000":
            a = "8";
            break;
        case "1001":
            a = "9";
            break;
        case "1010":
            a = "A";
            break;
        case "1011":
            a = "B";
            break;
        case "1100":
            a = "C";
            break;
        case "1101":
            a = "D";
            break;
        case "1110":
            a = "E";
            break;
        case "1111":
            a = "F";
            break
    }
    return a
}

function hexToBt4(a) {
    var b;
    switch (a) {
        case "0":
            b = "0000";
            break;
        case "1":
            b = "0001";
            break;
        case "2":
            b = "0010";
            break;
        case "3":
            b = "0011";
            break;
        case "4":
            b = "0100";
            break;
        case "5":
            b = "0101";
            break;
        case "6":
            b = "0110";
            break;
        case "7":
            b = "0111";
            break;
        case "8":
            b = "1000";
            break;
        case "9":
            b = "1001";
            break;
        case "A":
            b = "1010";
            break;
        case "B":
            b = "1011";
            break;
        case "C":
            b = "1100";
            break;
        case "D":
            b = "1101";
            break;
        case "E":
            b = "1110";
            break;
        case "F":
            b = "1111";
            break
    }
    return b
}

function byteToString(d) {
    var c = "";
    for (i = 0; i < 4; i++) {
        var b = 0;
        for (j = 0; j < 16; j++) {
            var a = 1;
            for (m = 15; m > j; m--) {
                a *= 2
            }
            b += d[16 * i + j] * a
        }
        if (b != 0) {
            c += String.fromCharCode(b)
        }
    }
    return c
}

function bt64ToHex(c) {
    var b = "";
    for (i = 0; i < 16; i++) {
        var a = "";
        for (j = 0; j < 4; j++) {
            a += c[i * 4 + j]
        }
        b += bt4ToHex(a)
    }
    return b
}

function hexToBt64(a) {
    var b = "";
    for (i = 0; i < 16; i++) {
        b += hexToBt4(a.substring(i, i + 1))
    }
    return b
}

function enc(b, q) {
    var t = generateKeys(q);
    var p = initPermute(b);
    var c = new Array(32);
    var s = new Array(32);
    var g = new Array(32);
    var o = 0,
        l = 0,
        h = 0,
        f = 0,
        e = 0;
    for (h = 0; h < 32; h++) {
        c[h] = p[h];
        s[h] = p[32 + h]
    }
    for (o = 0; o < 16; o++) {
        for (l = 0; l < 32; l++) {
            g[l] = c[l];
            c[l] = s[l]
        }
        var r = new Array(48);
        for (f = 0; f < 48; f++) {
            r[f] = t[o][f]
        }
        var a = xor(pPermute(sBoxPermute(xor(expandPermute(s), r))), g);
        for (e = 0; e < 32; e++) {
            s[e] = a[e]
        }
    }
    var d = new Array(64);
    for (o = 0; o < 32; o++) {
        d[o] = s[o];
        d[32 + o] = c[o]
    }
    return finallyPermute(d)
}

function dec(b, q) {
    var t = generateKeys(q);
    var p = initPermute(b);
    var c = new Array(32);
    var s = new Array(32);
    var g = new Array(32);
    var o = 0,
        l = 0,
        h = 0,
        f = 0,
        e = 0;
    for (h = 0; h < 32; h++) {
        c[h] = p[h];
        s[h] = p[32 + h]
    }
    for (o = 15; o >= 0; o--) {
        for (l = 0; l < 32; l++) {
            g[l] = c[l];
            c[l] = s[l]
        }
        var r = new Array(48);
        for (f = 0; f < 48; f++) {
            r[f] = t[o][f]
        }
        var a = xor(pPermute(sBoxPermute(xor(expandPermute(s), r))), g);
        for (e = 0; e < 32; e++) {
            s[e] = a[e]
        }
    }
    var d = new Array(64);
    for (o = 0; o < 32; o++) {
        d[o] = s[o];
        d[32 + o] = c[o]
    }
    return finallyPermute(d)
}

function initPermute(b) {
    var a = new Array(64);
    for (i = 0, m = 1, n = 0; i < 4; i++, m += 2, n += 2) {
        for (j = 7, k = 0; j >= 0; j--, k++) {
            a[i * 8 + k] = b[j * 8 + m];
            a[i * 8 + k + 32] = b[j * 8 + n]
        }
    }
    return a
}

function expandPermute(a) {
    var b = new Array(48);
    for (i = 0; i < 8; i++) {
        if (i == 0) {
            b[i * 6 + 0] = a[31]
        } else {
            b[i * 6 + 0] = a[i * 4 - 1]
        }
        b[i * 6 + 1] = a[i * 4 + 0];
        b[i * 6 + 2] = a[i * 4 + 1];
        b[i * 6 + 3] = a[i * 4 + 2];
        b[i * 6 + 4] = a[i * 4 + 3];
        if (i == 7) {
            b[i * 6 + 5] = a[0]
        } else {
            b[i * 6 + 5] = a[i * 4 + 4]
        }
    }
    return b
}

function xor(c, b) {
    var a = new Array(c.length);
    for (i = 0; i < c.length; i++) {
        a[i] = c[i] ^ b[i]
    }
    return a
}

function sBoxPermute(c) {
    var a = new Array(32);
    var e = "";
    var r = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ];
    var q = [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ];
    var p = [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ];
    var o = [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ];
    var l = [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ];
    var h = [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ];
    var g = [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ];
    var f = [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ];
    for (m = 0; m < 8; m++) {
        var d = 0,
            b = 0;
        d = c[m * 6 + 0] * 2 + c[m * 6 + 5];
        b = c[m * 6 + 1] * 2 * 2 * 2 + c[m * 6 + 2] * 2 * 2 + c[m * 6 + 3] * 2 + c[m * 6 + 4];
        switch (m) {
            case 0:
                e = getBoxBinary(r[d][b]);
                break;
            case 1:
                e = getBoxBinary(q[d][b]);
                break;
            case 2:
                e = getBoxBinary(p[d][b]);
                break;
            case 3:
                e = getBoxBinary(o[d][b]);
                break;
            case 4:
                e = getBoxBinary(l[d][b]);
                break;
            case 5:
                e = getBoxBinary(h[d][b]);
                break;
            case 6:
                e = getBoxBinary(g[d][b]);
                break;
            case 7:
                e = getBoxBinary(f[d][b]);
                break
        }
        a[m * 4 + 0] = parseInt(e.substring(0, 1));
        a[m * 4 + 1] = parseInt(e.substring(1, 2));
        a[m * 4 + 2] = parseInt(e.substring(2, 3));
        a[m * 4 + 3] = parseInt(e.substring(3, 4))
    }
    return a
}

function pPermute(b) {
    var a = new Array(32);
    a[0] = b[15];
    a[1] = b[6];
    a[2] = b[19];
    a[3] = b[20];
    a[4] = b[28];
    a[5] = b[11];
    a[6] = b[27];
    a[7] = b[16];
    a[8] = b[0];
    a[9] = b[14];
    a[10] = b[22];
    a[11] = b[25];
    a[12] = b[4];
    a[13] = b[17];
    a[14] = b[30];
    a[15] = b[9];
    a[16] = b[1];
    a[17] = b[7];
    a[18] = b[23];
    a[19] = b[13];
    a[20] = b[31];
    a[21] = b[26];
    a[22] = b[2];
    a[23] = b[8];
    a[24] = b[18];
    a[25] = b[12];
    a[26] = b[29];
    a[27] = b[5];
    a[28] = b[21];
    a[29] = b[10];
    a[30] = b[3];
    a[31] = b[24];
    return a
}

function finallyPermute(a) {
    var b = new Array(64);
    b[0] = a[39];
    b[1] = a[7];
    b[2] = a[47];
    b[3] = a[15];
    b[4] = a[55];
    b[5] = a[23];
    b[6] = a[63];
    b[7] = a[31];
    b[8] = a[38];
    b[9] = a[6];
    b[10] = a[46];
    b[11] = a[14];
    b[12] = a[54];
    b[13] = a[22];
    b[14] = a[62];
    b[15] = a[30];
    b[16] = a[37];
    b[17] = a[5];
    b[18] = a[45];
    b[19] = a[13];
    b[20] = a[53];
    b[21] = a[21];
    b[22] = a[61];
    b[23] = a[29];
    b[24] = a[36];
    b[25] = a[4];
    b[26] = a[44];
    b[27] = a[12];
    b[28] = a[52];
    b[29] = a[20];
    b[30] = a[60];
    b[31] = a[28];
    b[32] = a[35];
    b[33] = a[3];
    b[34] = a[43];
    b[35] = a[11];
    b[36] = a[51];
    b[37] = a[19];
    b[38] = a[59];
    b[39] = a[27];
    b[40] = a[34];
    b[41] = a[2];
    b[42] = a[42];
    b[43] = a[10];
    b[44] = a[50];
    b[45] = a[18];
    b[46] = a[58];
    b[47] = a[26];
    b[48] = a[33];
    b[49] = a[1];
    b[50] = a[41];
    b[51] = a[9];
    b[52] = a[49];
    b[53] = a[17];
    b[54] = a[57];
    b[55] = a[25];
    b[56] = a[32];
    b[57] = a[0];
    b[58] = a[40];
    b[59] = a[8];
    b[60] = a[48];
    b[61] = a[16];
    b[62] = a[56];
    b[63] = a[24];
    return b
}

function getBoxBinary(a) {
    var b = "";
    switch (a) {
        case 0:
            b = "0000";
            break;
        case 1:
            b = "0001";
            break;
        case 2:
            b = "0010";
            break;
        case 3:
            b = "0011";
            break;
        case 4:
            b = "0100";
            break;
        case 5:
            b = "0101";
            break;
        case 6:
            b = "0110";
            break;
        case 7:
            b = "0111";
            break;
        case 8:
            b = "1000";
            break;
        case 9:
            b = "1001";
            break;
        case 10:
            b = "1010";
            break;
        case 11:
            b = "1011";
            break;
        case 12:
            b = "1100";
            break;
        case 13:
            b = "1101";
            break;
        case 14:
            b = "1110";
            break;
        case 15:
            b = "1111";
            break
    }
    return b
}

function generateKeys(c) {
    var e = new Array(56);
    var f = new Array();
    f[0] = new Array();
    f[1] = new Array();
    f[2] = new Array();
    f[3] = new Array();
    f[4] = new Array();
    f[5] = new Array();
    f[6] = new Array();
    f[7] = new Array();
    f[8] = new Array();
    f[9] = new Array();
    f[10] = new Array();
    f[11] = new Array();
    f[12] = new Array();
    f[13] = new Array();
    f[14] = new Array();
    f[15] = new Array();
    var a = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1];
    for (d = 0; d < 7; d++) {
        for (j = 0, k = 7; j < 8; j++, k--) {
            e[d * 8 + j] = c[8 * k + d]
        }
    }
    var d = 0;
    for (d = 0; d < 16; d++) {
        var h = 0;
        var b = 0;
        for (j = 0; j < a[d]; j++) {
            h = e[0];
            b = e[28];
            for (k = 0; k < 27; k++) {
                e[k] = e[k + 1];
                e[28 + k] = e[29 + k]
            }
            e[27] = h;
            e[55] = b
        }
        var g = new Array(48);
        g[0] = e[13];
        g[1] = e[16];
        g[2] = e[10];
        g[3] = e[23];
        g[4] = e[0];
        g[5] = e[4];
        g[6] = e[2];
        g[7] = e[27];
        g[8] = e[14];
        g[9] = e[5];
        g[10] = e[20];
        g[11] = e[9];
        g[12] = e[22];
        g[13] = e[18];
        g[14] = e[11];
        g[15] = e[3];
        g[16] = e[25];
        g[17] = e[7];
        g[18] = e[15];
        g[19] = e[6];
        g[20] = e[26];
        g[21] = e[19];
        g[22] = e[12];
        g[23] = e[1];
        g[24] = e[40];
        g[25] = e[51];
        g[26] = e[30];
        g[27] = e[36];
        g[28] = e[46];
        g[29] = e[54];
        g[30] = e[29];
        g[31] = e[39];
        g[32] = e[50];
        g[33] = e[44];
        g[34] = e[32];
        g[35] = e[47];
        g[36] = e[43];
        g[37] = e[48];
        g[38] = e[38];
        g[39] = e[55];
        g[40] = e[33];
        g[41] = e[52];
        g[42] = e[45];
        g[43] = e[41];
        g[44] = e[49];
        g[45] = e[35];
        g[46] = e[28];
        g[47] = e[31];
        switch (d) {
            case 0:
                for (m = 0; m < 48; m++) {
                    f[0][m] = g[m]
                }
                break;
            case 1:
                for (m = 0; m < 48; m++) {
                    f[1][m] = g[m]
                }
                break;
            case 2:
                for (m = 0; m < 48; m++) {
                    f[2][m] = g[m]
                }
                break;
            case 3:
                for (m = 0; m < 48; m++) {
                    f[3][m] = g[m]
                }
                break;
            case 4:
                for (m = 0; m < 48; m++) {
                    f[4][m] = g[m]
                }
                break;
            case 5:
                for (m = 0; m < 48; m++) {
                    f[5][m] = g[m]
                }
                break;
            case 6:
                for (m = 0; m < 48; m++) {
                    f[6][m] = g[m]
                }
                break;
            case 7:
                for (m = 0; m < 48; m++) {
                    f[7][m] = g[m]
                }
                break;
            case 8:
                for (m = 0; m < 48; m++) {
                    f[8][m] = g[m]
                }
                break;
            case 9:
                for (m = 0; m < 48; m++) {
                    f[9][m] = g[m]
                }
                break;
            case 10:
                for (m = 0; m < 48; m++) {
                    f[10][m] = g[m]
                }
                break;
            case 11:
                for (m = 0; m < 48; m++) {
                    f[11][m] = g[m]
                }
                break;
            case 12:
                for (m = 0; m < 48; m++) {
                    f[12][m] = g[m]
                }
                break;
            case 13:
                for (m = 0; m < 48; m++) {
                    f[13][m] = g[m]
                }
                break;
            case 14:
                for (m = 0; m < 48; m++) {
                    f[14][m] = g[m]
                }
                break;
            case 15:
                for (m = 0; m < 48; m++) {
                    f[15][m] = g[m]
                }
                break
        }
    }
    return f
};