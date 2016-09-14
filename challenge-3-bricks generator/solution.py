from itertools import permutations


def inversions(tile, tiles):
    return [
        tile > following_tile and following_tile != 0
        for following_tile in tiles[tiles.index(tile)+1:]
    ].count(True)


def is_solvable(tiles, size):
    inversions_count = sum(inversions(x, tiles) for x in tiles)
    blank_tile_row = tiles.index(0) // size
    if size % 2 == 1 and inversions_count % 2 == 0:
        return True
    if size % 2 == 0 and inversions_count % 2 != blank_tile_row % 2:
        return True
    return False


def solvable_tiles(size=3):
    tiles = permutations(range(size * size), size * size)

    return (
        tuple((tile[i * size: i * size + size]) for i in range(size))
        for tile in tiles
        if is_solvable(tile, size)
    )