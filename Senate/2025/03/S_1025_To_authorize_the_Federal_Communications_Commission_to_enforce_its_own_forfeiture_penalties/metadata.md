# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1025?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1025
- Title: FCC Legal Enforcement Act
- Congress: 119
- Bill type: S
- Bill number: 1025
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-01-14T16:47:17Z
- Update date including text: 2026-01-14T16:47:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1025",
    "number": "1025",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Lujan, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "FCC Legal Enforcement Act",
    "type": "S",
    "updateDate": "2026-01-14T16:47:17Z",
    "updateDateIncludingText": "2026-01-14T16:47:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T16:48:03Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "HI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1025is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1025\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Luj\u00e1n (for himself, Mr. Blumenthal , Mr. Welch , Mr. Schatz , Mr. Durbin , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo authorize the Federal Communications Commission to enforce its own forfeiture penalties with respect to violations of restrictions on the use of telephone equipment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FCC Legal Enforcement Act .\n#### 2. Enforcement of forfeiture penalties by Federal Communications Commission\n##### (a) In general\nTitle V of the Communications Act of 1934 ( 47 U.S.C. 501 et seq. ) is amended\u2014\n**(1)**\nin section 503(b)(3)(B) ( 47 U.S.C. 503(b)(3)(B) ), by striking In such action, and inserting the following: If, during the 120-day period beginning on the date of a referral of an unpaid forfeiture penalty imposed for a violation of section 227 (relating to restrictions on the use of telephone equipment), the Attorney General does not commence an action to recover the amount assessed, the Commission may commence and supervise the litigation of such an action and any appeal of such an action in its own name by any of its attorneys designated by it for such purpose. In any action under this subparagraph, ; and\n**(2)**\nin section 504(a) ( 47 U.S.C. 504(a) )\u2014\n**(A)**\nby striking It shall be the duty and inserting Except as provided in the subsequent sentence, it shall be the duty ; and\n**(B)**\nby striking The costs and expenses of such prosecutions and inserting the following: If, during the 120-day period beginning on the date on which the Commission refers an unpaid forfeiture penalty imposed for a violation of section 227 (relating to restrictions on the use of telephone equipment) to the Attorney General for prosecution under this subsection, the Attorney General does not commence such a prosecution, the Commission may prosecute for the recovery of the forfeiture penalty. The costs and expenses of a prosecution under this subsection .\n##### (b) Priority\nIn carrying out the amendments made by subsection (a) of this section, the Federal Communications Commission shall prioritize enforcement of unpaid forfeiture penalties imposed for a violation of section 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ) (relating to restrictions on the use of telephone equipment) that are greater than $25,000,000.\n#### 3. Regulations for restrictions on use of automated telephone equipment\nSection 227(b)(2) of the Communications Act of 1934 ( 47 U.S.C. 227(b)(2) ) is amended, in the matter preceding subparagraph (A), by inserting before the period the following: as necessary in the judgment of the Commission to protect subscribers from unwanted calls .",
      "versionDate": "2025-03-13",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-14T16:47:17Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1025is.xml"
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
      "title": "FCC Legal Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FCC Legal Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Federal Communications Commission to enforce its own forfeiture penalties with respect to violations of restrictions on the use of telephone equipment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T04:18:19Z"
    }
  ]
}
```
