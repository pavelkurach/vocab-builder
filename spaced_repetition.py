from types import MappingProxyType


class SpacedRepetition:
    buckets = MappingProxyType({
        0: 0,
        1: 1,
        2: 3,
        3: 7,
        4: 14,
        5: 30,
    })

    states = ('Forgot', 'OK', 'Recalled easily')

    @staticmethod
    def spaced_repetition_scheduler(bucket: int, state: str) -> int:
        """
        Get new bucket number and repetion interval
        :param bucket: current bucket
        :param state: recall success/failure
        :return: new bucket number
        """
        if not bucket in SpacedRepetition.buckets.keys():
            raise ValueError('Bucket number is incorrect.')

        if state == SpacedRepetition.states[0]:
            return 0
        elif state == SpacedRepetition.states[1]:
            return min(bucket + 1, list(SpacedRepetition.buckets.keys())[-1])
        elif state == SpacedRepetition.states[2]:
            return min(bucket + 2, list(SpacedRepetition.buckets.keys())[-1])
        else:
            raise ValueError('State is incorrect.')