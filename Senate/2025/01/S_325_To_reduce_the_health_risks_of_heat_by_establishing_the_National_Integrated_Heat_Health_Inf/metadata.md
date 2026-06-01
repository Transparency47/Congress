# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/325?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/325
- Title: Coordinated Federal Response to Extreme Heat Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 325
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-04-10T16:23:01Z
- Update date including text: 2026-04-10T16:23:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/325",
    "number": "325",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Coordinated Federal Response to Extreme Heat Act of 2025",
    "type": "S",
    "updateDate": "2026-04-10T16:23:01Z",
    "updateDateIncludingText": "2026-04-10T16:23:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-01-30T00:11:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s325is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 325\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Markey (for himself, Mr. Padilla , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo reduce the health risks of heat by establishing the National Integrated Heat Health Information System within the National Oceanic and Atmospheric Administration and the National Integrated Heat Health Information System Interagency Committee to improve extreme heat preparedness, planning, and response, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Coordinated Federal Response to Extreme Heat Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Extreme heat**\nThe term extreme heat means heat that substantially exceeds local temperature norms in terms of any combination of the following:\n**(A)**\nDuration.\n**(B)**\nIntensity.\n**(C)**\nSeason length.\n**(D)**\nFrequency.\n**(2) Heat**\nThe term heat means any combination of the atmospheric parameters associated with modulating human thermoregulation, such as air temperature, humidity, solar exposure, and wind speed.\n**(3) Heat event**\nThe term heat event means an occurrence of extreme heat of 2 days or more that may have heat-health implications.\n**(4) Heat-health**\nThe term heat-health means health effects to humans from heat, during or outside of heat events, including from vulnerability and exposure, or the risk of such effects.\n**(5) Planning**\nThe term planning means activities performed across timescales (including days, weeks, months, years, and decades) with scenario-based, probabilistic or deterministic information to identify and take actions to proactively mitigate heat-health risks.\n**(6) Preparedness**\nThe term preparedness means activities performed across timescales with decision support tools to manage risk in advance of a heat event and increased ambient temperature.\n**(7) Tribal government**\nThe term Tribal government means the recognized governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of enactment of this Act pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ).\n#### 3. National Integrated Heat Health Information System Interagency Committee\n##### (a) Establishment of committee\nThere is established within the National Oceanic and Atmospheric Administration an interagency committee, to be known as the National Integrated Heat Health Information System Interagency Committee (in this section referred to as the Committee ).\n##### (b) Purpose\nThe Committee shall coordinate agencies represented on the Committee to execute, as appropriate, activities across such agencies to ensure a united Federal approach to reducing health risks from heat.\n##### (c) Membership\n**(1) In general**\nIn order to carry out and achieve the purpose described in subsection (b), the Committee shall include the following:\n**(A)**\nThe Director of the National Integrated Heat Health Information System.\n**(B)**\nNot fewer than 1 representative from each of the following:\n**(i)**\nFrom the Department of Commerce, the following:\n**(I)**\nFrom the National Oceanic and Atmospheric Administration, the following:\n**(aa)**\nThe National Weather Service.\n**(bb)**\nThe Office of Oceanic and Atmospheric Research.\n**(cc)**\nThe National Environmental Satellite, Data, and Information Service.\n**(II)**\nThe National Institute of Standards and Technology.\n**(III)**\nThe Bureau of the Census.\n**(ii)**\nFrom the Department of Health and Human Services, the following:\n**(I)**\nThe Centers for Disease Control and Prevention, including the National Institute for Occupational Safety and Health.\n**(II)**\nThe Office of the Assistant Secretary of Health and Human Services for Preparedness and Response.\n**(III)**\nThe Substance Abuse and Mental Health Services Administration.\n**(IV)**\nThe National Institutes of Health.\n**(V)**\nThe Indian Health Service.\n**(iii)**\nFrom the Department of the Interior, the following:\n**(I)**\nThe Bureau of Indian Affairs.\n**(II)**\nThe Bureau of Land Management.\n**(III)**\nThe National Park Service.\n**(IV)**\nThe Office of Hawaiian Relations.\n**(iv)**\nFrom the Environmental Protection Agency, the following:\n**(I)**\nThe Office of Air and Radiation, if the Administrator of the Environmental Protection Agency determines appropriate.\n**(II)**\nThe Office of Research and Development, if the Administrator determines appropriate.\n**(III)**\nThe Office of International and Tribal Affairs.\n**(v)**\nThe Federal Emergency Management Agency.\n**(vi)**\nThe Department of Defense.\n**(vii)**\nThe Department of Agriculture.\n**(viii)**\nThe Department of Housing and Urban Development.\n**(ix)**\nThe Department of Transportation.\n**(x)**\nThe Department of Energy.\n**(xi)**\nThe Department of Labor, including the Occupational Safety and Health Administration.\n**(xii)**\nThe Department of Veteran Affairs.\n**(xiii)**\nThe Department of Education.\n**(xiv)**\nThe Department of State.\n**(xv)**\nThe United States Agency for International Development.\n**(xvi)**\nSuch other Federal agencies as the Under Secretary of Commerce for Oceans and Atmosphere considers appropriate.\n**(2) Selection of representatives**\nThe head of an agency specified in paragraph (1)(B) shall, in appointing representatives of the agency to the Committee, select representatives who have expertise in areas relevant to the responsibilities of the Committee, such as weather prediction, health impacts, behavioral science, public health hazard preparedness and response, or mental health services.\n**(3) Co-chairs**\n**(A) In general**\nThe members of the Committee shall select 3 individuals from among such members to serve as co-chairs of the Committee, subject to the approval of the Under Secretary of Commerce for Oceans and Atmosphere.\n**(B) Selection**\n**(i) Initial selection**\nOf the co-chairs first selected, one shall be from the National Oceanic and Atmospheric Administration, one shall be from the Department of Health and Human Services, and one shall be from the Federal Emergency Management Agency.\n**(ii) Subsequent selection**\nSubsequent co-chairs shall be selected from among the members of the Committee, except the National Oceanic and Atmospheric Administration shall have the opportunity to maintain a co-chair position.\n**(C) Terms**\nEach co-chair shall serve for a term of not more than 5 years.\n**(D) Responsibilities of co-chairs**\nThe co-chairs of the Committee shall, in consultation with the Director of the National Integrated Heat Health Information System\u2014\n**(i)**\ndetermine the agenda of the Committee, in consultation with other members of the Committee;\n**(ii)**\ndirect the work of the Committee; and\n**(iii)**\nconvene meetings of the Committee not less frequently than once each fiscal quarter.\n##### (d) Responsibilities of Committee\nThe Committee shall coordinate an integrated, Federal Government-wide approach to reducing health risks and impacts of heat, including by\u2014\n**(1)**\ndeveloping the strategic plan required by subsection (e);\n**(2)**\ncoordinating across Federal agencies on heat-health communication, engagement, research, service delivery, and workforce development; and\n**(3)**\nbuilding capacity and partnerships with Federal and non-Federal entities.\n##### (e) Strategic plan\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Committee shall submit to Congress and make available on a public website a 5-year strategic plan that outlines the goals and projects of the Committee, including how the Committee will improve coordination and integration of interagency Federal capacity and capabilities to address health risks of heat, including\u2014\n**(A)**\na strategy for improving and coordinating existing Federal data collection and data management to include sharing of data and statistics on heat-related illnesses and mortalities and other impacts to inform heat-related activities;\n**(B)**\na strategy for improving and coordinating Federal activities to understand user gaps and needs, conduct research, foster innovative solutions, and provide actionable information and services; and\n**(C)**\nmechanisms for financing heat planning and preparedness within such agencies as the Committee considers appropriate.\n**(2) Implementation**\nThe head of an agency represented on the Committee may implement the portions of the strategic plan required by paragraph (1) that are relevant to that agency.\n**(3) Updates**\nNot later than 5 years after the submission of the strategic plan required by paragraph (1), and every 5 years thereafter, the Committee shall brief Congress on an update of the plan, which shall include progress made toward goals outlined in the previous plan and new priorities that emerge.\n##### (f) Consultation\nIn carrying out the responsibilities of the Committee, the Committee shall consult with relevant\u2014\n**(1)**\nregional, State, Tribal, and local governments;\n**(2)**\ninternational organizations and partners;\n**(3)**\nresearch institutions;\n**(4)**\nnongovernmental organizations and associations;\n**(5)**\nmedical experts with expertise in emergency response; and\n**(6)**\nenvironmental health, economic or business development, or other stakeholders.\n#### 4. National Integrated Heat Health Information System\n##### (a) Establishment\nThe Under Secretary of Commerce for Oceans and Atmosphere shall establish within the National Oceanic and Atmospheric Administration a system, to be known as the National Integrated Heat Health Information System (NIHHIS) (in this section referred to as the System ).\n##### (b) Purpose\nThe purpose of the System is to reduce heat-related impacts by\u2014\n**(1)**\nimproving the delivery of data, information, forecasts, warnings, predictions, and projections related to temperature and extreme heat and related impacts;\n**(2)**\nthrough the Office of Oceanic and Atmospheric Research, developing science-based solutions and tools to improve impact-based decision support services for heat impacts to human life, property, and the United States economy; and\n**(3)**\nsupporting a research program on heat health, in coordination with the agencies represented on the National Integrated Heat Health Information System Interagency Committee.\n##### (c) Data management\n**(1) Availability**\nThe data and metadata associated with the System shall be fully and openly available, within the legal right to redistribute, in accordance with chapter 31 of title 44, United States Code (commonly known as the Federal Records Act of 1950 ), and the Federal Evidence-Based Policymaking Act of 2018 ( Public Law 115\u2013435 ; 132 Stat. 5529) and the amendments made by that Act, to maximize use of such data to support the goals of the System.\n**(2) National Centers for Environmental Information**\n**(A) In general**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall manage, maintain, and steward archival data and metadata associated with the System within the National Centers for Environmental Information.\n**(B) Warning coordination meteorologist**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall designate at least one warning coordination meteorologist, as described in section 405 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8545 ), at the National Centers for Environmental Information.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated to the National Oceanic and Atmospheric Administration to carry out sections 3 and 4, including for any administrative costs for the National Integrated Heat Health Information System Interagency Committee and the National Integrated Heat Health Information System, $5,000,000 for each of fiscal years 2025 through 2029.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-04",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3704",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Coordinated Federal Response to Extreme Heat Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Air quality",
            "updateDate": "2025-04-04T19:27:42Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2025-04-04T19:27:49Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-04-04T19:30:15Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-04T19:28:36Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-10T16:23:01Z"
          },
          {
            "name": "Department of Commerce",
            "updateDate": "2025-04-04T19:28:16Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2025-04-04T19:27:37Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-04-04T19:28:25Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-04T19:29:08Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-04-04T19:30:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-07T14:28:00Z"
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
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s325is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-03-05T05:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Coordinated Federal Response to Extreme Heat Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reduce health risks of heat by establishing the National Integrated Heat Health Information System within the National Oceanic and Atmospheric Administration and the National Integrated Heat Health Information System Interagency Committee to improve extreme heat preparedness, planning, and response, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:57Z"
    }
  ]
}
```
