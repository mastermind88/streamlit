# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import date, datetime

import streamlit as st
from streamlit import runtime

d1 = st.date_input("Single date", date(1970, 1, 1), min_value=date(1970, 1, 1))
st.write("Value 1:", d1)

d2 = st.date_input("Single datetime", datetime(2019, 7, 6, 21, 15), help="Help text")
st.write("Value 2:", d2)

d3 = st.date_input("Range, no date", [])
st.write("Value 3:", d3)

d4 = st.date_input("Range, one date", [date(2019, 7, 6)])
st.write("Value 4:", d4)

d5 = st.date_input("Range, two dates", [date(2019, 7, 6), date(2019, 7, 8)])
st.write("Value 5:", d5)

d6 = st.date_input("Disabled, no date", [], disabled=True)
st.write("Value 6:", d6)

d7 = st.date_input(
    "Label hidden", datetime(2019, 7, 6, 21, 15), label_visibility="hidden"
)
st.write("Value 7:", d7)

d8 = st.date_input(
    "Label collapsed", datetime(2019, 7, 6, 21, 15), label_visibility="collapsed"
)
st.write("Value 8:", d8)

d9 = st.date_input("Single date with format", date(1970, 1, 1), format="MM-DD-YYYY")
st.write("Value 9:", d9)

d10 = st.date_input(
    "Range, two dates with format",
    [date(2019, 7, 6), date(2019, 7, 8)],
    format="MM/DD/YYYY",
)
st.write("Value 10:", d10)

d11 = st.date_input("Range, no date with format", [], format="DD.MM.YYYY")
st.write("Value 11:", d11)


if runtime.exists():

    def on_change():
        st.session_state.date_input_changed = True
        st.text("Date input changed callback")

    st.date_input(
        "Single date with callback",
        date(1970, 1, 1),
        min_value=date(1970, 1, 1),
        key="date_input12",
        on_change=on_change,
    )
    st.write("Value 12:", st.session_state.date_input12)
    st.write("Date Input Changed:", "date_input_changed" in st.session_state)

d13 = st.date_input("Empty value", value=None)
st.write("Value 13:", d13)
