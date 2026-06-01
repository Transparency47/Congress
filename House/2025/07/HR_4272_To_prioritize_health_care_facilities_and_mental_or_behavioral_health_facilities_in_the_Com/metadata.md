# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4272
- Title: Prioritizing Rural Hospitals Act
- Congress: 119
- Bill type: HR
- Bill number: 4272
- Origin chamber: House
- Introduced date: 2025-07-02
- Update date: 2026-04-23T08:06:57Z
- Update date including text: 2026-04-23T08:06:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-02: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-07-02: Introduced in House

## Actions

- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-02",
    "latestAction": {
      "actionDate": "2025-07-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4272",
    "number": "4272",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Prioritizing Rural Hospitals Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:06:57Z",
    "updateDateIncludingText": "2026-04-23T08:06:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-02",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-02",
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
          "date": "2025-07-02T13:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "KS"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4272ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4272\nIN THE HOUSE OF REPRESENTATIVES\nJuly 2, 2025 Ms. Underwood (for herself and Mr. Mann ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo prioritize health care facilities and mental or behavioral health facilities in the Community Facilities program for fiscal years 2026 through 2031, and allow loans and grants under the program to be used for medical supplies, increasing telehealth capabilities, supporting staffing needs, or renovating and remodeling closed facilities.\n#### 1. Short title\nThis Act may be cited as the Prioritizing Rural Hospitals Act .\n#### 2. Improving rural health care access\n##### (a) In general\nFor fiscal years 2026 through 2031, in selecting recipients of direct loans or grants for the development of essential community facilities under section 306(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a) ), the Secretary of Agriculture shall give priority to entities eligible for the direct loans or grants to develop\u2014\n**(1)**\nhealth care facilities; or\n**(2)**\nmental or behavioral health facilities, including certified community behavioral health clinics described in section 223 of the Protecting Access to Medicare Act of 2014 ( 42 U.S.C. 1396a note; Public Law 113\u201393 ).\n##### (b) Use of funds\nAn eligible entity referred to in subsection (a) that receives a direct loan or grant pursuant to this section may use the direct loan or grant funds to\u2014\n**(1)**\nprovide medical supplies;\n**(2)**\nincrease telehealth capabilities, including underlying health care information systems;\n**(3)**\nsupport staffing needs, subject to the condition that the eligible entity shall not use more than 25 percent of the direct loan or grant funds for this purpose; or\n**(4)**\nrenovate or remodel closed health care facilities.\n##### (c) Limitation on other reprioritizations\nFor fiscal years 2026 through 2031, the Secretary of Agriculture shall not make any national reprioritizations within the Community Facilities direct loan and grant programs under section 608 of the Rural Development Act of 1972 ( 7 U.S.C. 2204b\u20132 ).",
      "versionDate": "2025-07-02",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-28T14:22:48Z"
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
      "date": "2025-07-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4272ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prioritize health care facilities and mental or behavioral health facilities in the Community Facilities program for fiscal years 2026 through 2031, and allow loans and grants under the program to be used for medical supplies, increasing telehealth capabilities, supporting staffing needs, or renovating and remodeling closed facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:31:26Z"
    },
    {
      "title": "Prioritizing Rural Hospitals Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prioritizing Rural Hospitals Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T04:23:23Z"
    }
  ]
}
```
