# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1644?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1644
- Title: Autonomy for Disabled Veterans Act
- Congress: 119
- Bill type: S
- Bill number: 1644
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-02-03T12:03:16Z
- Update date including text: 2026-02-03T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1644",
    "number": "1644",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Autonomy for Disabled Veterans Act",
    "type": "S",
    "updateDate": "2026-02-03T12:03:16Z",
    "updateDateIncludingText": "2026-02-03T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
        "item": [
          {
            "date": "2025-05-07T19:36:09Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-07T19:36:09Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "AR"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1644is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1644\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Ms. Cortez Masto (for herself and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to modify the authority of the Secretary of Veterans Affairs to furnish improvements and structural alterations as part of home health services for disabled veterans.\n#### 1. Short title\nThis Act may be cited as the Autonomy for Disabled Veterans Act .\n#### 2. Modification to authority of Secretary of Veterans Affairs to furnish improvements and structural alterations as part of home health services for disabled veterans\n##### (a) Increase\nParagraph (2) of subsection (a) of section 1717 of title 38, United States Code, is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by inserting in the case of a veteran before the em dash; and\n**(2)**\nby striking subparagraphs (A) and (B) and inserting the following:\n(A) who first applied for benefits under this paragraph for a non-service-connected disability before the date of the enactment of the Autonomy for Disabled Veterans Act and whose disability the Secretary determines is service-connected after such date, $6,800; or (B) who first applied for benefits under this paragraph on or after the date of the enactment of the Autonomy for Disabled Veterans Act , $10,000. .\n##### (b) Adjustment for inflation; cap on benefits\nSuch subsection is further amended\u2014\n**(1)**\nby redesignating paragraph (3) as paragraph (5); and\n**(2)**\nby inserting after paragraph (2) the following new paragraphs:\n(3) On the first day of each fiscal year, the dollar amounts in effect under paragraph (2) shall\u2014 (A) increase by a percentage equal to the percentage by which the residential home cost of construction index established under section 2102(e)(3) of this title increased during the previous fiscal year; or (B) if such index did not increase during such previous fiscal year, remain the same. (4) The Secretary may not furnish more than three improvements or structural alterations under paragraph (2) to a veteran. .\n##### (c) Rule of construction\nA veteran who, before the date of the enactment of this Act, exhausted the eligibility of such veteran for benefits under section 1717 of title 38, United States Code, shall not be entitled to additional benefits under such section by reason of the amendments made by this Act.",
      "versionDate": "2025-05-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:33:29Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1644is.xml"
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
      "title": "Autonomy for Disabled Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Autonomy for Disabled Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to modify the authority of the Secretary of Veterans Affairs to furnish improvements and structural alterations as part of home health services for disabled veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:23Z"
    }
  ]
}
```
