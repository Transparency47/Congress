# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1665
- Title: OATH Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1665
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-03-19T11:03:26Z
- Update date including text: 2026-03-19T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1665",
    "number": "1665",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "OATH Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:26Z",
    "updateDateIncludingText": "2026-03-19T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
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
            "date": "2026-03-18T20:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:10Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-07T21:33:57Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1665is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1665\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Blumenthal introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to ensure veterans of secrecy oath programs receive the full benefits they have earned, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Obligations to Aberdeen\u2019s Trusted Heroes Act of 2025 or the OATH Act of 2025 .\n#### 2. Definition of secrecy oath program\nSection 5100 of title 38, United States Code, is amended by adding at the end the following new paragraph:\n(3) The term secrecy oath program means a United States Government program in which participants are required to sign a non-disclosure agreement preventing the disclosure of any information regarding the program under penalty of court-martial or criminal punishment. .\n#### 3. Notice to veterans of secrecy oath programs regarding benefits\n##### (a) Notice required\n**(1) In general**\nSection 6303 of title 38, United States Code, is amended\u2014\n**(A)**\nby redesignating subsections (c), (d), and (e) as subsections (d), (e), and (f), respectively; and\n**(B)**\nby inserting after subsection (b) the following new subsection (c):\n(c) Notice to veterans of secrecy oath programs (1) Not later than 90 days after the date on which participants in a secrecy oath program are released from the oath taken under such program, the Secretary shall\u2014 (A) identify the veterans who participated in the program; (B) notify each such veteran of all benefits and services under laws administered by the Department for which the veteran may be eligible; and (C) distribute the information described in subsection (d)(1) as required by such subsection. (2) If the Secretary identifies any veterans who are entitled to notice under paragraph (1) and did not receive such notice, the Secretary shall, not later than 90 days after the date of any such identification\u2014 (A) notify each such veteran of all benefits and services under laws administered by the Department for which the veteran may be eligible; and (B) distribute the information described in subsection (d)(1) as required by such subsection. (3) In this subsection, the term secrecy oath program has the meaning given that term in section 5100 of this title. .\n**(2) Conforming amendments**\nSection 6303 of such title is further amended\u2014\n**(A)**\nin subsection (a), by striking through (d) and inserting through (e) ; and\n**(B)**\nin subsection (e), as redesignated by subsection (a)(1)(A), by striking subsections (b) and (c) and inserting subsections (b), (c), and (d) .\n##### (b) Edgewood Arsenal program\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nidentify the veterans who participated in the secrecy oath program at Edgewood Arsenal at Aberdeen Proving Ground, Maryland, at any time during the period beginning on January 1, 1948, and ending on December 31, 1975;\n**(2)**\nnotify each such veteran of all benefits and services under laws administered by the Department of Veterans Affairs for which the veteran may be eligible; and\n**(3)**\ndistribute the information described in section 6303(d)(1) of title 38, United States Code, as amended by subsection (a), as required by such section.\n#### 4. Effective dates of awards of disability compensation for participants in secrecy oath programs\nSection 5110(b) of title 38, United States Code, is amended by adding at the end the following new paragraph:\n(5) (A) The effective date of an award of disability compensation to a veteran described in subparagraph (B) shall be the day following the date of the veteran\u2019s discharge or release. (B) A veteran described in this subparagraph is a veteran who\u2014 (i) participated in the secrecy oath program at Edgewood Arsenal at Aberdeen Proving Ground, Maryland, at any time during the period beginning on January 1, 1948, and ending on December 31, 1975; or (ii) participated in any other secrecy oath program not described in clause (i). .",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Maryland",
            "updateDate": "2025-12-12T21:05:37Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2025-12-12T21:05:29Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-12-12T21:05:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:31:27Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1665is.xml"
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
      "title": "OATH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "OATH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Obligations to Aberdeen\u2019s Trusted Heroes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to ensure veterans of secrecy oath programs receive the full benefits they have earned, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:23Z"
    }
  ]
}
```
