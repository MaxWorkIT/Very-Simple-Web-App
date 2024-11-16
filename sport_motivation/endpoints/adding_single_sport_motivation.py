from sport_motivation.models.POSTSportModel import SPostSport

from sport_motivation.patterns.POST_sport_pattern import post_sport_pattern
from main_files.motivation_fake_dbs import sport_mtv

from typing import Annotated

from fastapi import Depends


def adding_single_sport_motivation(
        endpoint_post_data: Annotated[SPostSport, Depends()]
) -> SPostSport | str:
    entered_sport_mtv_id = list(endpoint_post_data)[0][1]

    return post_sport_pattern(pattern_post_data=endpoint_post_data) \
        if (not sport_mtv and entered_sport_mtv_id == 1
            or len(sport_mtv)+1 == entered_sport_mtv_id) \
        else (f"the entered sport_mtv_id ({entered_sport_mtv_id}) "
              f"is already in the database or it is too large")