# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6000?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6000
- Title: Veterans’ Sentinel Act
- Congress: 119
- Bill type: HR
- Bill number: 6000
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-03-27T08:06:30Z
- Update date including text: 2026-03-27T08:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6000",
    "number": "6000",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Veterans\u2019 Sentinel Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:30Z",
    "updateDateIncludingText": "2026-03-27T08:06:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:38:37Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "KY"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "WI"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "ME"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "NE"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6000ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6000\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Crow (for himself and Mr. Ellzey ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the collection and analysis of data regarding certain suicides by veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Sentinel Act .\n#### 2. Suicides by veterans on property of the Department of Veterans Affairs: collection and analysis of data; working group\n##### (a) Annual reports\nSection 1709B of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraph (2) as subparagraph (3); and\n**(B)**\nby inserting after paragraph (1) the following new paragraph (2):\n(2) The statistical trends and recommendations described in subsection (b). ;\n**(2)**\nby redesignating subsection (b), as amended, as subsection (c); and\n**(3)**\nby inserting after subsection (a) the following new subsection (b):\n(b) On-Campus suicides On an annual basis, the Secretary shall\u2014 (1) evaluate the statistical trends of suicides and attempted suicides by veterans that occur on the property of the Department; and (2) determine recommendations for preventing such suicides and attempted suicides. .\n##### (b) Working group\n**(1) Establishment**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish a working group to collect and analyze data regarding on-campus suicides and attempted on-campus suicides.\n**(2) Methodology**\nIn collecting and analyzing the information under paragraph (1), the working group shall\u2014\n**(A)**\nreview root cause analysis data available to the Secretary regarding all on-campus suicides and attempted on-campus suicides;\n**(B)**\nwith respect to on-campus suicides\u2014\n**(i)**\nanalyze data available to the Secretary under the Behavioral Health Autopsy Program of the Department, including family interviews; and\n**(ii)**\ndocument reasons for any deficiencies in the data collected; and\n**(C)**\nnot less frequently than every 90 days, communicate with the medical centers and field offices of the Department in order to coordinate the collection and review actions of the working group with such actions carried out by the medical centers and field offices.\n**(3) Data collection improvements**\nThe working group shall consider, and may implement for purposes described in paragraph (1), improvements to the processes by which the Secretary collects data regarding on-campus suicides and attempted on-campus suicides in order to unify the disparate sources of such data, including with respect to\u2014\n**(A)**\nmodifying incident reports and other methods to collect data, including both suicide and attempted suicide report fields;\n**(B)**\ndeveloping and ensuring that each source of data relating to on-campus suicides and attempted on-campus suicides includes a specified section for such on-campus incidents; and\n**(C)**\ndeveloping an associated management system to consolidate all relevant data for on-campus suicides and attempted on-campus suicides, including such data from Behavioral Health Autopsy Program assessments, health records of the Department, root cause analyses, incident reports, and other sources of data.\n**(4) Briefings**\nNot later than one year after the date of the enactment of this Act, and annually thereafter during the period of operation under paragraph (6), the Secretary shall provide to the Committees on Veterans\u2019 Affairs of the House of Representatives and Senate a briefing on the progress and findings of the working group established under such paragraph.\n**(5) Report**\nNot later than 30 days after the end of the period of operation under paragraph (6), the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report detailing\u2014\n**(A)**\nthe effectiveness of the working group established under such paragraph; and\n**(B)**\nany recommendations to enhance the data collection and management by the Secretary with respect to on-campus suicides and attempted on-campus suicides, including improvements identified under paragraph (3).\n**(6) Duration**\nThe working group shall operate for a period determined by the Secretary that is not less than two years and not longer than five years.\n**(7) On-campus suicide defined**\nIn this subsection, the term on-campus suicide means a suicide described in section 1709B(b) of title 38, United States Code, as amended by subsection (a).",
      "versionDate": "2025-11-10",
      "versionType": "Introduced in House"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T16:15:00Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6000ih.xml"
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
      "title": "Veterans\u2019 Sentinel Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 Sentinel Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the collection and analysis of data regarding certain suicides by veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:18Z"
    }
  ]
}
```
