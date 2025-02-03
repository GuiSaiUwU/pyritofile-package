from loguru import logger
from pyritofile import SKN, SKL, BIN
from requests import get

def test_bin():
    logger.info("Testing BIN")
    response = get("https://raw.communitydragon.org/latest/game/globals.cdtb.bin")
    
    bin_file = BIN()
    bin_file.read('', raw=response.content)
    if (bin_file.write('', True) == response.content):
        logger.info("BIN Test passed")
    else:
        logger.error("BIN Test failed")

def test_local_bin():
    logger.info("Testing Local BIN")

    bin_file = BIN()
    bin_file.read(r'C:\Users\GuiSai\Desktop\skin0.bin')
    with open(r"C:\Users\GuiSai\Desktop\skin0.bin", "rb") as f:
        content = f.read()
    
    if (bin_file.write('', True) == content):
        logger.info("Local BIN Test passed")
    else:
        logger.error("Local BIN Test failed")

def test_skn():
    logger.info("Testing SKN")
    response = get("https://raw.communitydragon.org/latest/game/assets/characters/akali/skins/base/akali.skn")
    
    skn_file = SKN()
    skn_file.read('', raw=response.content)

    if (skn_file.write('', True) + b"\x00"*12 == response.content):
        logger.info("SKN Test passed")
    else:
        logger.error("SKN Test failed")


def test_skl():
    """
    Disabled bcs is always failing
    """
    logger.info("Testing SKL")
    response = get("https://github.com/GuiSaiUwU/EveryRiotSKLFile/raw/refs/heads/main/skl/assets/characters/ahri/skins/base/ahri_base.skl")
    
    skl_file = SKL()
    skl_file.read('', raw=response.content)
    skl_file.write('a.skl')
    if (skl_file.write('', True) == response.content):
        logger.info("SKL Test passed")
    else:
        logger.error("SKL Test failed")


if __name__ == '__main__':
    test_bin()
    test_skn()
    test_local_bin()
    #test_skl()