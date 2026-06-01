# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3051?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3051
- Title: PARTNERS Act
- Congress: 119
- Bill type: S
- Bill number: 3051
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2026-03-09T19:59:36Z
- Update date including text: 2026-03-09T19:59:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3051",
    "number": "3051",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "PARTNERS Act",
    "type": "S",
    "updateDate": "2026-03-09T19:59:36Z",
    "updateDateIncludingText": "2026-03-09T19:59:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-23",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-23",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2025-12-15",
                "committees": {
                  "item": {
                    "name": "Foreign Relations Committee",
                    "systemCode": "ssfr00"
                  }
                },
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Referred to the Committee on Foreign Relations.",
                "type": "IntroReferral"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-12-15",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-12-15",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              }
            ]
          },
          "count": "3"
        },
        "amendedBill": {
          "congress": "119",
          "number": "3051",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "PARTNERS Act",
          "type": "S",
          "updateDateIncludingText": "2026-03-09"
        },
        "chamber": "Senate",
        "congress": "119",
        "cosponsors": {
          "count": "1",
          "countIncludingWithdrawnCosponsors": "1",
          "item": {
            "bioguideId": "K000383",
            "firstName": "Angus",
            "fullName": "Sen. King, Angus S., Jr. [I-ME]",
            "isOriginalCosponsor": "True",
            "lastName": "King",
            "middleName": "S.",
            "party": "I",
            "sponsorshipDate": "2025-12-15",
            "state": "ME"
          }
        },
        "latestAction": {
          "actionDate": "2025-12-15",
          "text": "Referred to the Committee on Foreign Relations."
        },
        "number": "3990",
        "sponsors": {
          "item": {
            "bioguideId": "C001056",
            "firstName": "John",
            "fullName": "Sen. Cornyn, John [R-TX]",
            "lastName": "Cornyn",
            "party": "R",
            "state": "TX"
          }
        },
        "submittedDate": "2025-12-15T05:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2025-12-15T23:49:21Z"
      }
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
          "date": "2025-10-23T19:40:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-10-23",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3051is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3051\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mr. Cornyn (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo build the capacity of the Armed Forces of Mexico to counter the threat posed by transnational criminal organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Partnership for Advancing Regional Training and Narcotics Enforcement Response Strategies Act or the PARTNERS Act .\n#### 2. Building the capacity of the Armed Forces of Mexico to counter the threat posed by transnational criminal organizations\n##### (a) Statement of policy\nIt is the policy of the United States Government to counter the threat posed by transnational criminal organizations, including through military capacity building and security cooperation with the Government of Mexico.\n##### (b) Plan\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense, in consultation with the Secretary of State and with the agreement of the Government of Mexico, shall submit to the appropriate congressional committees a plan for a pilot program under which the Armed Forces of Mexico and the United States Armed Forces will train jointly in the United States on tactics, techniques, and procedures for countering the threat posed by transnational criminal organizations, including through\u2014\n**(1)**\noperations involving the use of rotary-wing aircraft; and\n**(2)**\nin consultation with the appropriate civilian government agencies specializing in countering transnational criminal organizations\u2014\n**(A)**\njoint network analysis;\n**(B)**\ncounter threat financing;\n**(C)**\ncounter illicit trafficking (including narcotics, weapons, and human trafficking, and illicit trafficking in natural resources); and\n**(D)**\nassessments of key nodes of activity of transnational criminal organizations.\n##### (c) Implementation\nNot later than 15 days after the date on which the plan required by subsection (b) is submitted under such subsection, the Secretary of Defense shall begin implementing the pilot program described in the plan.\n##### (d) Definition of appropriate congressional committees\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services, the Committee on Foreign Relations, and the Committee on Appropriations of the Senate; and\n**(2)**\nthe Committee on Armed Services, the Committee on Foreign Affairs, and the Committee on Appropriations of the House of Representatives.",
      "versionDate": "2025-10-23",
      "versionType": "Introduced in Senate"
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
        "name": "International Affairs",
        "updateDate": "2025-11-20T17:24:04Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3051is.xml"
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
      "title": "PARTNERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PARTNERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Partnership for Advancing Regional Training and Narcotics Enforcement Response Strategies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to build the capacity of the armed forces of Mexico to counter the threat posed by transnational criminal organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T03:48:15Z"
    }
  ]
}
```
