# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2933?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2933
- Title: Protect National Service Act
- Congress: 119
- Bill type: HR
- Bill number: 2933
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2026-04-14T08:05:29Z
- Update date including text: 2026-04-14T08:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2933",
    "number": "2933",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Protect National Service Act",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:29Z",
    "updateDateIncludingText": "2026-04-14T08:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:37:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "NE"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CO"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "MI"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OH"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2933ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2933\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Ms. Houlahan introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo prohibit the use of funds to eliminate the Corporation for National and Community Service.\n#### 1. Short title\nThis Act may be cited as the Protect National Service Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nA recent study from Voices for National Service found that every $1 in Federal taxes invested in AmeriCorps and Senior Corps returns $17.30 to society.\n**(2)**\nOver the last 30 years, more than 900,000 Americans have served as AmeriCorps members, contributing more than 1,200,000,000 hours of service to their communities and accounting for a value of more than $38,000,000,000 across every United States State and United States Territory.\n**(3)**\nThe statute first authorizing the agency, and subsequent reform efforts, have received strong bipartisan support over multiple decades, including from Presidential administrations of both parties.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nany reform or reorganization of the Corporation for National and Community Service should be done\u2014\n**(A)**\nin accordance with existing laws;\n**(B)**\nin a manner that maintains the United States support for national service;\n**(C)**\nin a manner that allows the National Service Trust to continue to meet all of its obligations to participants in AmeriCorps; and\n**(D)**\nin a manner that maintains the Federal Government\u2019s active role in meeting unmet human, educational, environmental, and public safety needs, as well as in renewing the ethic of civic responsibility by encouraging citizens to participate in national service programs; and\n**(2)**\nonly an act of Congress can eliminate the Corporation for National and Community Service as a Government corporation, as defined in section 103 of title 5, United States Code.\n#### 3. Prohibition of funds to eliminate the Corporation for National and Community Service\n##### (a) In general\nConsistent with section 1413 of the Omnibus Consolidated and Emergency Supplemental Appropriations Act of 1999 ( 22 U.S.C. 6563 ), no Federal funds appropriated or otherwise made available by the American Relief Act, 2025 ( Public Law 118\u2013158 ) or any other or prior appropriations Act may be made available to eliminate the status of the Corporation for National and Community Service as a Government corporation, as defined in section 103 of title 5, United States Code.\n##### (b) Rule of construction\nNothing in this section shall be construed to indicate that the elimination, dismantlement, or subsummation of the Corporation for National and Community Service is permissible under existing law.\n##### (c) Certification\nNot later than 30 days after the date of enactment of this act, and annually for 5 years thereafter, the Chief Executive Officer of the Corporation for National and Community Service shall certify to the appropriate Committees compliance with this section.\n##### (d) Appropriate Committees of Congress Defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Education and Workforce of the House of Representatives; and\n**(2)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate.",
      "versionDate": "2025-04-17",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-29T14:58:33Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2933ih.xml"
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
      "title": "Protect National Service Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect National Service Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of funds to eliminate the Corporation for National and Community Service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:33Z"
    }
  ]
}
```
