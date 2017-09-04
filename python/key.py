import bitcoin

# 秘密鍵の作成

valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decoded_private_key < bitcoin.N

print ("秘密鍵(hex): ", private_key)
print ("秘密鍵(decimal): ", decoded_private_key)

# 秘密鍵を WIF フォーマットに変換

wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print("秘密鍵(WIF): ", wif_encoded_private_key)

# "01" suffix を圧縮された秘密鍵を示すものとして追加
compressed_private_key = private_key + '01'
print("圧縮された秘密鍵(hex): ", compressed_private_key)

# 圧縮された公開鍵からWIF フォーマットを生成(WIF圧縮)
wif_compressed_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
print("秘密鍵(WIF圧縮)", wif_compressed_private_key)

# 公開鍵を作成
public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
print("公開鍵(x,y)座標: ", public_key)

# hexエンコード, prefix は04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
print("公開鍵(hex): ", hex_encoded_public_key)

# 公開鍵圧縮、prefix をy座標の偶数奇数で変更する
(public_key_x, public_key_y) = public_key
if (public_key_y % 2) == 0:
    compressed_prefix = '02'
else:
    compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
print("圧縮された公開鍵(hex): ", hex_compressed_public_key)

# 公開鍵からビットコインアドレスを生成
print("ビットコインアドレス(b58check): ", bitcoin.pubkey_to_address(public_key))

# 圧縮されたビットコインアドレスを圧縮された公開鍵から生成
print("圧縮されたビットコインアドレス(b58check): ", bitcoin.pubkey_to_address(hex_compressed_public_key))
