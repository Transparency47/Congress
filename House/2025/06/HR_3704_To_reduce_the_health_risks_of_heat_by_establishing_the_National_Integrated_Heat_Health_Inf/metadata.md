# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3704
- Title: Coordinated Federal Response to Extreme Heat Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3704
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2025-12-05T21:48:04Z
- Update date including text: 2025-12-05T21:48:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3704",
    "number": "3704",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000381",
        "district": "3",
        "firstName": "Yassamin",
        "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
        "lastName": "Ansari",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Coordinated Federal Response to Extreme Heat Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:48:04Z",
    "updateDateIncludingText": "2025-12-05T21:48:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-06-04T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-04T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MO"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "OR"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MI"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NV"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "WA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "OH"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "RI"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MD"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "DC"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "AZ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NV"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "GA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "FL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "PA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "IL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3704ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3704\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Ms. Ansari (for herself, Mr. Bell , Ms. Dexter , Mrs. Dingell , Mrs. Foushee , Mr. Garcia of California , Mr. Horsford , Ms. Jayapal , Mr. Landsman , Mr. Liccardo , Mr. Magaziner , Mrs. McClain Delaney , Mrs. McIver , Mr. Mullin , Ms. Norton , Ms. Rivas , Mr. Stanton , Ms. Titus , Mrs. Watson Coleman , Mr. Whitesides , Ms. Williams of Georgia , Ms. Wilson of Florida , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reduce the health risks of heat by establishing the National Integrated Heat Health Information System within the National Oceanic and Atmospheric Administration and the National Integrated Heat Health Information System Interagency Committee to improve extreme heat preparedness, planning, and response, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Coordinated Federal Response to Extreme Heat Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Extreme heat**\nThe term extreme heat means heat that substantially exceeds local temperature norms in terms of any combination of the following:\n**(A)**\nDuration.\n**(B)**\nIntensity.\n**(C)**\nSeason length.\n**(D)**\nFrequency.\n**(2) Heat**\nThe term heat means any combination of the atmospheric parameters associated with modulating human thermoregulation, such as air temperature, humidity, solar exposure, and wind speed.\n**(3) Heat event**\nThe term heat event means an occurrence of extreme heat of 2 days or more that may have heat-health implications.\n**(4) Heat-health**\nThe term heat-health means health effects to humans from heat, during or outside of heat events, including from vulnerability and exposure, or the risk of such effects.\n**(5) Planning**\nThe term planning means activities performed across timescales (including days, weeks, months, years, and decades) with scenario-based, probabilistic or deterministic information to identify and take actions to proactively mitigate heat-health risks.\n**(6) Preparedness**\nThe term preparedness means activities performed across timescales with decision support tools to manage risk in advance of a heat event and increased ambient temperature.\n**(7) Tribal government**\nThe term Tribal government means the recognized governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of enactment of this Act pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ).\n#### 3. National Integrated Heat Health Information System Interagency Committee\n##### (a) Establishment of committee\nThere is established within the National Oceanic and Atmospheric Administration an interagency committee, to be known as the National Integrated Heat Health Information System Interagency Committee (in this section referred to as the Committee ).\n##### (b) Purpose\nThe Committee shall coordinate agencies represented on the Committee to execute, as appropriate, activities across such agencies to ensure a united Federal approach to reducing health risks from heat.\n##### (c) Membership\n**(1) In general**\nIn order to carry out and achieve the purpose described in subsection (b), the Committee shall include the following:\n**(A)**\nThe Director of the National Integrated Heat Health Information System.\n**(B)**\nNot fewer than 1 representative from each of the following:\n**(i)**\nFrom the Department of Commerce, the following:\n**(I)**\nFrom the National Oceanic and Atmospheric Administration, the following:\n**(aa)**\nThe National Weather Service.\n**(bb)**\nThe Office of Oceanic and Atmospheric Research.\n**(cc)**\nThe National Environmental Satellite, Data, and Information Service.\n**(II)**\nThe National Institute of Standards and Technology.\n**(III)**\nThe Bureau of the Census.\n**(ii)**\nFrom the Department of Health and Human Services, the following:\n**(I)**\nThe Centers for Disease Control and Prevention, including the National Institute for Occupational Safety and Health.\n**(II)**\nThe Office of the Assistant Secretary of Health and Human Services for Preparedness and Response.\n**(III)**\nThe Substance Abuse and Mental Health Services Administration.\n**(IV)**\nThe National Institutes of Health.\n**(V)**\nThe Indian Health Service.\n**(iii)**\nFrom the Department of the Interior, the following:\n**(I)**\nThe Bureau of Indian Affairs.\n**(II)**\nThe Bureau of Land Management.\n**(III)**\nThe National Park Service.\n**(IV)**\nThe Office of Hawaiian Relations.\n**(iv)**\nFrom the Environmental Protection Agency, the following:\n**(I)**\nThe Office of Air and Radiation, if the Administrator of the Environmental Protection Agency determines appropriate.\n**(II)**\nThe Office of Research and Development, if the Administrator determines appropriate.\n**(III)**\nThe Office of International and Tribal Affairs.\n**(v)**\nThe Federal Emergency Management Agency.\n**(vi)**\nThe Department of Defense.\n**(vii)**\nThe Department of Agriculture.\n**(viii)**\nThe Department of Housing and Urban Development.\n**(ix)**\nThe Department of Transportation.\n**(x)**\nThe Department of Energy.\n**(xi)**\nThe Department of Labor, including the Occupational Safety and Health Administration.\n**(xii)**\nThe Department of Veteran Affairs.\n**(xiii)**\nThe Department of Education.\n**(xiv)**\nThe Department of State.\n**(xv)**\nThe United States Agency for International Development.\n**(xvi)**\nSuch other Federal agencies as the Under Secretary of Commerce for Oceans and Atmosphere considers appropriate.\n**(2) Selection of representatives**\nThe head of an agency specified in paragraph (1)(B) shall, in appointing representatives of the agency to the Committee, select representatives who have expertise in areas relevant to the responsibilities of the Committee, such as weather prediction, health impacts, behavioral science, public health hazard preparedness and response, or mental health services.\n**(3) Co-chairs**\n**(A) In general**\nThe members of the Committee shall select 3 individuals from among such members to serve as co-chairs of the Committee, subject to the approval of the Under Secretary of Commerce for Oceans and Atmosphere.\n**(B) Selection**\n**(i) Initial selection**\nOf the co-chairs first selected, one shall be from the National Oceanic and Atmospheric Administration, one shall be from the Department of Health and Human Services, and one shall be from the Federal Emergency Management Agency.\n**(ii) Subsequent selection**\nSubsequent co-chairs shall be selected from among the members of the Committee, except the National Oceanic and Atmospheric Administration shall have the opportunity to maintain a co-chair position.\n**(C) Terms**\nEach co-chair shall serve for a term of not more than 5 years.\n**(D) Responsibilities of co-chairs**\nThe co-chairs of the Committee shall, in consultation with the Director of the National Integrated Heat Health Information System\u2014\n**(i)**\ndetermine the agenda of the Committee, in consultation with other members of the Committee;\n**(ii)**\ndirect the work of the Committee; and\n**(iii)**\nconvene meetings of the Committee not less frequently than once each fiscal quarter.\n##### (d) Responsibilities of Committee\nThe Committee shall coordinate an integrated, Federal Government-wide approach to reducing health risks and impacts of heat, including by\u2014\n**(1)**\ndeveloping the strategic plan required by subsection (e);\n**(2)**\ncoordinating across Federal agencies on heat-health communication, engagement, research, service delivery, and workforce development; and\n**(3)**\nbuilding capacity and partnerships with Federal and non-Federal entities.\n##### (e) Strategic plan\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Committee shall submit to Congress and make available on a public website a 5-year strategic plan that outlines the goals and projects of the Committee, including how the Committee will improve coordination and integration of interagency Federal capacity and capabilities to address health risks of heat, including\u2014\n**(A)**\na strategy for improving and coordinating existing Federal data collection and data management to include sharing of data and statistics on heat-related illnesses and mortalities and other impacts to inform heat-related activities;\n**(B)**\na strategy for improving and coordinating Federal activities to understand user gaps and needs, conduct research, foster innovative solutions, and provide actionable information and services; and\n**(C)**\nmechanisms for financing heat planning and preparedness within such agencies as the Committee considers appropriate.\n**(2) Implementation**\nThe head of an agency represented on the Committee may implement the portions of the strategic plan required by paragraph (1) that are relevant to that agency.\n**(3) Updates**\nNot later than 5 years after the submission of the strategic plan required by paragraph (1), and every 5 years thereafter, the Committee shall brief Congress on an update of the plan, which shall include progress made toward goals outlined in the previous plan and new priorities that emerge.\n##### (f) Consultation\nIn carrying out the responsibilities of the Committee, the Committee shall consult with relevant\u2014\n**(1)**\nregional, State, Tribal, and local governments;\n**(2)**\ninternational organizations and partners;\n**(3)**\nresearch institutions;\n**(4)**\nnongovernmental organizations and associations;\n**(5)**\nmedical experts with expertise in emergency response; and\n**(6)**\nenvironmental health, economic or business development, or other stakeholders.\n#### 4. National Integrated Heat Health Information System\n##### (a) Establishment\nThe Under Secretary of Commerce for Oceans and Atmosphere shall establish within the National Oceanic and Atmospheric Administration a system, to be known as the National Integrated Heat Health Information System (NIHHIS) (in this section referred to as the System ).\n##### (b) Purpose\nThe purpose of the System is to reduce heat-related impacts by\u2014\n**(1)**\nimproving the delivery of data, information, forecasts, warnings, predictions, and projections related to temperature and extreme heat and related impacts;\n**(2)**\nthrough the Office of Oceanic and Atmospheric Research, developing science-based solutions and tools to improve impact-based decision support services for heat impacts to human life, property, and the United States economy; and\n**(3)**\nsupporting a research program on heat health, in coordination with the agencies represented on the National Integrated Heat Health Information System Interagency Committee.\n##### (c) Data management\n**(1) Availability**\nThe data and metadata associated with the System shall be fully and openly available, within the legal right to redistribute, in accordance with chapter 31 of title 44, United States Code (commonly known as the Federal Records Act of 1950 ), and the Federal Evidence-Based Policymaking Act of 2018 ( Public Law 115\u2013435 ; 132 Stat. 5529) and the amendments made by that Act, to maximize use of such data to support the goals of the System.\n**(2) National Centers for Environmental Information**\n**(A) In general**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall manage, maintain, and steward archival data and metadata associated with the System within the National Centers for Environmental Information.\n**(B) Warning coordination meteorologist**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall designate at least one warning coordination meteorologist, as described in section 405 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8545 ), at the National Centers for Environmental Information.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated to the National Oceanic and Atmospheric Administration to carry out sections 3 and 4, including for any administrative costs for the National Integrated Heat Health Information System Interagency Committee and the National Integrated Heat Health Information System, $5,000,000 for each of fiscal years 2025 through 2029.",
      "versionDate": "2025-06-04",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-06",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Natural Resources, Energy and Commerce, and Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3816",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Weather Act Reauthorization Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-29",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "325",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Coordinated Federal Response to Extreme Heat Act of 2025",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-23T14:10:03Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3704ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Coordinated Federal Response to Extreme Heat Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:07Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Coordinated Federal Response to Extreme Heat Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reduce the health risks of heat by establishing the National Integrated Heat Health Information System within the National Oceanic and Atmospheric Administration and the National Integrated Heat Health Information System Interagency Committee to improve extreme heat preparedness, planning, and response, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:23Z"
    }
  ]
}
```
