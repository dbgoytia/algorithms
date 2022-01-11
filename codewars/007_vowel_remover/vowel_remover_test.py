import vowel_remover

def test_shorcut():
    assert vowel_remover.shortcut('hello') == 'hll'
    assert vowel_remover.shortcut('h e l l o') == 'h  l l '
    assert vowel_remover.shortcut('he l lo') == 'h l l'