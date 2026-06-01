# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6013?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6013
- Title: Filipino Veterans Fairness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6013
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-03-21T08:05:59Z
- Update date including text: 2026-03-21T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6013",
    "number": "6013",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Filipino Veterans Fairness Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-21T08:05:59Z",
    "updateDateIncludingText": "2026-03-21T08:05:59Z"
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
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
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
          "date": "2025-11-10T17:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:34:53Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "GU"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "HI"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6013ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6013\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Mullin (for himself, Mr. Moylan , and Mr. Case ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the benefits furnished by the Secretary of Veterans Affairs to certain individuals who served in the forces of the Philippines and the Philippine Scouts.\n#### 1. Short title\nThis Act may be cited as the Filipino Veterans Fairness Act of 2025 .\n#### 2. Improvement of veterans benefits furnished to certain individuals who served in the forces of the Philippines and the Philippine Scouts\n##### (a) Expansion of benefits\nSection 107 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (3) the following new paragraph:\n(4) sections 1541 and 1542 of this title. ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (2) the following new paragraph:\n(3) sections 1541 and 1542 of this title. ; and\n##### (b) Eligibility\nSuch section is further amended by adding at the end the following new subsections:\n(e) (1) In determining the eligibility of the service of an individual under this section, the Secretary shall take into account any alternative documentation regarding such service, including documentation other than the recognized guerrilla rosters stored at the National Personnel Records Center, that the Secretary determines relevant. (2) Not later than March 1 of each year, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report that includes\u2014 (A) the number of individuals applying for benefits pursuant to this section during the previous year; and (B) the number of such individuals that the Secretary approved for benefits. (f) Section 1002(h) of the American Recovery and Reinvestment Act of 2009 (title X of division A of Public Law 111\u20135 ; 123 Stat. 200; 38 U.S.C. 107 note) shall not apply to an individual described in subsection (a) or (b) of this section. .\n##### (c) Effective date\n**(1) In general**\nThe amendments made by this section shall take effect on the date that is 270 days after the date of the enactment of this Act.\n**(2) Applicability**\nNo benefits shall accrue to any person for any period before the effective date of this Act by reason of the amendments made by this section.",
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
        "updateDate": "2025-11-18T16:01:21Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6013ih.xml"
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
      "title": "Filipino Veterans Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T08:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Filipino Veterans Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T08:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the benefits furnished by the Secretary of Veterans Affairs to certain individuals who served in the forces of the Philippines and the Philippine Scouts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T08:33:22Z"
    }
  ]
}
```
