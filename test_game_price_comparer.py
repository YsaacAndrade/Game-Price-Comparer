import game_price_comparer as project
import pytest


def test_search_type():
    ## TEST FOR WRONG TYPE ##
    with pytest.raises(ValueError) as error_type:
        test_type = project.Search("wrong", "game")
    assert str(error_type.value) == "Invalid type!"

    ## TEST FOR 0 CHARS GAME-NAME ##
    with pytest.raises(ValueError) as error_name:
        test_name = project.Search("game", "")
    assert str(error_name.value) == "Invalid name!"

    ## TEST FOR MAXIMUM OF CHARS ##
    with pytest.raises(ValueError) as error_long_name:
        wrong_edge_object = project.Search("game", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    assert str(error_long_name.value) == "Invalid name!"

    ## TEST WITH RIGHT DLC-TYPE AND GAME-NAME ##
    right_object_dlc = project.Search("dlc", "The last of us part i left behind")
    assert right_object_dlc.type == "dlc"
    assert right_object_dlc.name == "The last of us part i left behind"

    ## TEST WITH RIGHT GAME-TYPE AND GAME NAME ##
    right_object_game = project.Search("game", "Minecraft Dungeon")
    assert right_object_game.type == "game"
    assert right_object_game.name == "Minecraft Dungeon"

    ## TEST WITH CAPITALIZED TYPE-GAME ##
    capitalized_type = project.Search("GaMe", "Minecraft Dungeons")
    assert capitalized_type.type == "game"
    assert capitalized_type.name == "Minecraft Dungeons"

    ## TEST WITH CAPITALIZED TYPE-DLC ##
    capitalized_type = project.Search("dLc", "The last of us part i left behind")
    assert capitalized_type.type == "dlc"
    assert capitalized_type.name == "The last of us part i left behind"


def test_confirm_result():
    ## INPUT OF NOTHING ##
    with pytest.raises(SystemExit) as error_value:
        project.confirm_result("")
    assert str(error_value.value) == "No results :("

    ## INPUT OF INT VALUES ##
    with pytest.raises(SystemExit) as error_value_int:
        project.confirm_result(123)
    assert str(error_value_int.value) == "Error with the results. Please, Try again"

    ## INPUT OF FLOAT VALUES ##
    with pytest.raises(SystemExit) as error_value_float:
        project.confirm_result(1.23)
    assert str(error_value_float.value) == "Error with the results. Please, Try again"

def test_get_url():
    ## TEST WITH 0 CHAR ON NAME ##
    with pytest.raises(SystemExit) as error_name:
        project.get_url("dlc", "", "your_api_key")
    assert str(error_name.value) == "Error. Please, Try again!"

    ## TEST WITH 0 CHAR ON TYPE ##
    with pytest.raises(SystemExit) as error_type:
        project.get_url("", "The last of us part i", "your_api_key")
    assert str(error_type.value) == "Error. Please, Try again!"

    ## TEST WITH LEN(TYPE) < 4 ##
    with pytest.raises(SystemExit) as more_than_four:
        project.get_url("gaame", "Minecraft Dungeons", "your_api_key")
    assert str(more_than_four.value) == "Error. Please, Try again!"

    ## TEST WITH ALL CORRECT ##
    assert project.get_url("game", "Minecraft Dungeons", "your_api_key") == "https://api.isthereanydeal.com/games/search/v1?key=your_api_key&id=018d937f&title=Minecraft Dungeons&type=game"
