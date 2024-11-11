import unittest
from credit_card_validator import credit_card_validator


class TestFunc(unittest.TestCase):
    def test_len_empty_string(self):
        "test for an empty string - error guessing"
        card = ''
        self.assertFalse(credit_card_validator(card))

    def test_should_pass_AE(self):
        "test valid ae w valid checksum - partition"
        card = '343456789012341'
        self.assertTrue(credit_card_validator(card))

    def test_should_pass_AE_invcs(self):
        "test valid ae but invalid checksum - partition"
        card = '343456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_should_pass_V(self):
        "test valid visa w valid checksum - partition"
        card = '4343456789012343'
        self.assertTrue(credit_card_validator(card))

    def test_should_pass_V_invcs(self):
        "test valid visa but invalid checksum - partition"
        card = '4343456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_should_pass_MC(self):
        "test valid mc w valid checksum - partition"
        card = '5143456789012342'
        self.assertTrue(credit_card_validator(card))

    def test_should_pass_MC_invcs(self):
        "test valid mc but invalid checksum - partition"
        card = '5143456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_len_14_invcs(self):
        "test for a length of 14 - boundary testing"
        card = '42345678901234'
        self.assertFalse(credit_card_validator(card))

    def test_len_14(self):
        "test for a length of 14 - boundary testing"
        card = '42345678901231'
        self.assertFalse(credit_card_validator(card))

    def test_len_17(self):
        "test for a length of 17 - boundary testing"
        card = '42345678901234566'
        self.assertFalse(credit_card_validator(card))

    def test_len_17_invcs(self):
        "test for a length of 17 invalid checksum- boundary testing"
        card = '42345678901234567'
        self.assertFalse(credit_card_validator(card))

    def test_one_char_string(self):
        "test for a single character string - error guessing"
        card = '1'
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_false(self):
        "test to validate luhn algorithm - error guessing "
        card = "4234567890123457"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_0(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830360"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_1(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830361"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_2(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830362"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_3(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830363"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_4(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830364"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_5(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830365"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_6(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830356"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_7(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830367"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_8(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830368"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_9(self):
        "test to validate luhn algorithm - error guessing "
        card = "4532015112830369"
        self.assertFalse(credit_card_validator(card))

    def test_luhn_algo_true2(self):
        "test to validate if luhn algo works w repeat value - error guessing"
        card = "4111111111111111"
        self.assertTrue(credit_card_validator(card))

    def test_v_len_14(self):
        "test visa that is too short - boundary testing"
        card = '42345678901231'
        self.assertFalse(credit_card_validator(card))

    def test_v_len_14_invcs(self):
        "test visa that is too short, invalid checksum - boundary testing"
        card = '42345678901234'
        self.assertFalse(credit_card_validator(card))

    def test_v_len_15(self):
        "test visa that is too short - boundary testing"
        card = '423456789012344'
        self.assertFalse(credit_card_validator(card))

    def test_v_len_15_invcs(self):
        "test visa that is too short invalid check sum- boundary testing"
        card = '423456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_v_first_lower(self):
        "test visa with incorrect first digit lower bound - boundary testing"
        card = "3234567890123458"
        self.assertFalse(credit_card_validator(card))

    def test_v_first_lower_invcs(self):
        "test visa with incorrect first digit lower bound - boundary testing"
        card = "3234567890123456"
        self.assertFalse(credit_card_validator(card))

    def test_v_first_lower_true(self):
        "test visa with correct first digit lower bound - partition testing"
        card = "4234567890123456"
        self.assertTrue(credit_card_validator(card))

    def test_v_first_lower_true_invcs(self):
        "test visa with correct first digit lower bound - partition testing"
        card = "4234567890123457"
        self.assertFalse(credit_card_validator(card))

    def test_v_first_upper(self):
        "test visa with incorrect first digit upper bound - boundary testing"
        card = "5034567890123455"
        self.assertFalse(credit_card_validator(card))

    def test_v_first_upper_invcs(self):
        "test visa with incorrect first digit upper bound - boundary testing"
        card = "5034567890123456"
        self.assertFalse(credit_card_validator(card))

    def test_v_len_17(self):
        "test visa that is too long - boundary testing"
        card = '42345678901234889'
        self.assertFalse(credit_card_validator(card))

    def test_v_len_17_invcs(self):
        "test visa that is too long, bad checksum - boundary testing"
        card = '42345678901234888'
        self.assertFalse(credit_card_validator(card))

    def test_v_leading_zero_true(self):
        "testing with a leading 0 good checksum - partition"
        card = "0043456789012344"
        self.assertTrue(credit_card_validator(card))

    def test_v_leading_zero_fail(self):
        "testing with a leading 0 bad checksum - partition"
        card = "0033456789012345"
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_15(self):
        "test mc with correct starting digit but too short by one - partition"
        card = '5143456789012342'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_15_invcs(self):
        "test mc with correct starting digit but too short by one - partition"
        card = '5143456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_15_pt2(self):
        "test mc with correct starting digits but too short by one - partition"
        card = '2222456789012343'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_15_pt2_invcs(self):
        "test mc with correct starting digits but too short by one - partition"
        card = '2222456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_14(self):
        "test mc with correct starting digit but too short by two - partition"
        card = '514345678901230'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_14_invcs(self):
        "test mc with correct starting digit but too short by two - partition"
        card = '514345678901231'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_17(self):
        "test mc with correct starting digit but too long - partition"
        card = '514345678901234564'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_17_invcs(self):
        "test mc with correct starting digit but too long - partition"
        card = '514345678901234567'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_17_two_series(self):
        "test mc with correct starting digit but too long - partition"
        card = '22214567890123452'
        self.assertFalse(credit_card_validator(card))

    def test_mc_len_17_two_series_invcs(self):
        "test mc with correct starting digit but too long - partition"
        card = '22214567890123459'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_upper(self):
        "test mc with incorrect first digit but right length - partition"
        card = '6143456789012340'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_upper_invcs(self):
        "test mc with incorrect first digit but right length - partition"
        card = '6143456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_lower(self):
        "test mc with incorrect first digit but right length -  partition"
        card = '3143456789012347'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_lower_invcs(self):
        "test mc with incorrect first digit but right length -  partition"
        card = '3143456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_lower(self):
        "test mc with incorrect second digit but right length - partition"
        card = '5043456789012343'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_lower_invcs(self):
        "test mc with incorrect second digit but right length - partition"
        card = '5043456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_lower_true(self):
        "test mc with correct second lower digit  - partition"
        card = '5121567890123459'
        self.assertTrue(credit_card_validator(card))

    def test_mc_second_lower_true_invcs(self):
        "test mc with correct second lower digit  - partition"
        card = '5121567890123456'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_upper_true(self):
        "test mc with correct second upper digit - partition"
        card = '5520567890123456'
        self.assertTrue(credit_card_validator(card))

    def test_mc_second_upper_true_invcs(self):
        "test mc with correct second upper digit - partition"
        card = '5520567890123459'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_upper(self):
        "test mc with incorrect second digit but right length -  partition"
        card = '5643456789012347'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_upper_invcs(self):
        "test mc with incorrect second digit but right length -  partition"
        card = '5643456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_lower(self):
        "test mc with incorrect fourth digit but right length - partition"
        card = '2220456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_lower_invcs(self):
        "test mc with incorrect fourth digit but right length - partition"
        card = '2220456789012347'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_lower_true(self):
        "test mc with correct fourth digit to test inclusivity - partition"
        card = '2221567890123455'
        self.assertTrue(credit_card_validator(card))

    def test_mc_fourth_lower_true_invcs(self):
        "test mc with correct fourth digit to test inclusivity - partition"
        card = '2221567890123457'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_lower_true2(self):
        "test mc with correct fourth digit  - partition"
        card = '2222567890123454'
        self.assertTrue(credit_card_validator(card))

    def test_mc_fourth_lower_true2_invcs(self):
        "test mc with correct fourth digit  - partition"
        card = '2222567890123457'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_upper(self):
        "test mc with incorrect fourth digit, right length - partition"
        card = '2721456789012349'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_upper_invcs(self):
        "test mc with incorrect fourth digit, right length - partition"
        card = '2721456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_upper2(self):
        "test mc with incorrect fourth digit, right length - partition"
        card = '2723456789012347'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_upper2_invcs(self):
        "test mc with incorrect fourth digit, right length - partition"
        card = '2723456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_upper_true(self):
        "test mc with correct fourth digit to test inclusivity - partition"
        card = '2720456789012340'
        self.assertTrue(credit_card_validator(card))

    def test_mc_fourth_upper_true_invcs(self):
        "test mc with correct fourth digit to test inclusivity - partition"
        card = '2720456789012348'
        self.assertFalse(credit_card_validator(card))

    def test_mc_fourth_upper_true2(self):
        "test mc with correct fourth digit  - partition"
        card = '2719456789012343'
        self.assertTrue(credit_card_validator(card))

    def test_mc_fourth_upper_true2_invcs(self):
        "test mc with correct fourth digit  - partition"
        card = '2719456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_third_lower(self):
        "test mc with incorrect third digit lower bound - partition"
        card = '2211456789012346'
        self.assertFalse(credit_card_validator(card))

    def test_mc_third_lower_invcs(self):
        "test mc with incorrect third digit lower bound - partition"
        card = '2211456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_third_upper(self):
        "test mc with incorrect third digit upper bound - partition"
        card = '2730456789012348'
        self.assertFalse(credit_card_validator(card))

    def test_mc_third_upper_invcs(self):
        "test mc with incorrect third digit upper bound - partition"
        card = '2730456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_lower_two_series(self):
        "test mc with incorrect second digit lower bound - partition"
        card = '2121456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_lower_two_series_invcs(self):
        "test mc with incorrect second digit lower bound - partition"
        card = '2121456789012347'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_upper_two_series(self):
        "test mc with incorrect second digit upper bound - partition"
        card = '2820456789012341'
        self.assertFalse(credit_card_validator(card))

    def test_mc_second_upper_two_series_invcs(self):
        "test mc with incorrect second digit upper bound - partition"
        card = '2820456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_lower_long_two_series(self):
        "test mc with incorrect first digit, 2 series - partition"
        card = '1221456789012346'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_lower_long_two_series_invcs(self):
        "test mc with incorrect first digit, 2 series - partition"
        card = '1221456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_upper_long_two_series(self):
        "test mc with incorrect first digit , 2 series - partition"
        card = '3720456789012348'
        self.assertFalse(credit_card_validator(card))

    def test_mc_first_upper_long_two_series_invcs(self):
        "test mc with incorrect first digit , 2 series - partition"
        card = '3720456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_ae_len_14(self):
        "test ae with correct starting but too short - partition"
        card = '34345678901231'
        self.assertFalse(credit_card_validator(card))

    def test_ae_len_14_invcs(self):
        "test ae with correct starting but too short - partition"
        card = '34345678901234'
        self.assertFalse(credit_card_validator(card))

    def test_ae_len_14_first_digit(self):
        "test american express with incorrect starting digit - partition"
        card = '443456789012340'
        self.assertFalse(credit_card_validator(card))

    def test_ae_len_14_first_digit_invcs(self):
        "test american express with incorrect starting digit - partition"
        card = '443456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_ae_len_16(self):
        "test ae with correct starting digit but too long - partition"
        card = '3434567890123456'
        self.assertFalse(credit_card_validator(card))

    def test_ae_len_16_invcs(self):
        "test ae with correct starting digit but too long - partition"
        card = '3434567890123459'
        self.assertFalse(credit_card_validator(card))

    def test_ae_first_lower(self):
        "test american express with incorrect lower first digit - partition"
        card = '243456789012342'
        self.assertFalse(credit_card_validator(card))

    def test_ae_first_lower_invcs(self):
        "test american express with incorrect lower first digit - partition"
        card = '243456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_ae_first_upper(self):
        "test american express with incorrect lower first digit - partition"
        card = '443456789012340'
        self.assertFalse(credit_card_validator(card))

    def test_ae_first_upper_invcs(self):
        "test american express with incorrect lower first digit - partition"
        card = '443456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_ae_second_lower(self):
        "test american express with wrong second digit lower - partition"
        card = '333456789012343'
        self.assertFalse(credit_card_validator(card))

    def test_ae_second_lower_invcs(self):
        "test american express with wrong second digit lower - partition"
        card = '333456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_ae_second_upper(self):
        "test american express with wrong second digit lower - partition"
        card = '383456789012342'
        self.assertFalse(credit_card_validator(card))

    def test_ae_second_upper_invcs(self):
        "test american express with wrong second digit lower - partition"
        card = '383456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_ae_middle_one(self):
        "test ae with wrong second digit middle value - partition"
        card = '353456789012348'
        self.assertFalse(credit_card_validator(card))

    def test_ae_middle_one_invcs(self):
        "test ae with wrong second digit middle value - partition"
        card = '353456789012345'
        self.assertFalse(credit_card_validator(card))

    def test_ae_middle_two(self):
        "test ae with wrong second digit middle value - partition"
        card = '363456789012346'
        self.assertFalse(credit_card_validator(card))

    def test_ae_middle_two_invcs(self):
        "test ae with wrong second digit middle value - partition"
        card = '363456789012345'
        self.assertFalse(credit_card_validator(card))


if __name__ == '__main__':
    unittest.main()
