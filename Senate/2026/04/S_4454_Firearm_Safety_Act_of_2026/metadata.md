# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4454
- Title: Firearm Safety Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4454
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-18T18:38:50Z
- Update date including text: 2026-05-18T18:38:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4454",
    "number": "4454",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Firearm Safety Act of 2026",
    "type": "S",
    "updateDate": "2026-05-18T18:38:50Z",
    "updateDateIncludingText": "2026-05-18T18:38:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T17:19:37Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "HI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "RI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4454is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4454\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Booker (for himself, Ms. Warren , Mr. Welch , Ms. Hirono , Mr. Reed , Mr. Durbin , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Consumer Product Safety Act to remove the exclusion of pistols, revolvers, and other firearms from the definition of consumer product in order to permit the issuance of safety standards for such articles by the Consumer Product Safety Commission.\n#### 1. Short title\nThis Act may be cited as the Firearm Safety Act of 2026 .\n#### 2. Removal of exclusion of firearms from the definition of consumer product\nSection 3(a)(5) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a)(5) ) is amended by striking subparagraph (E) and redesignating subparagraphs (F) through (I) as subparagraphs (E) through (H), respectively.",
      "versionDate": "2026-04-30",
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
        "name": "Commerce",
        "updateDate": "2026-05-11T21:26:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-30",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s4454",
          "measure-number": "4454",
          "measure-type": "s",
          "orig-publish-date": "2026-04-30",
          "originChamber": "SENATE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4454v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2026-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Firearm Safety Act of 2026</strong></p><p>This bill allows the Consumer Product Safety Commission (CPSC)\u00a0to issue safety standards for firearms and firearm components.</p><p>Under current law, firearms, shells, cartridges, and components\u00a0thereof are excluded from the CPSC's rulemaking authority.</p>"
        },
        "title": "Firearm Safety Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4454.xml",
    "summary": {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Firearm Safety Act of 2026</strong></p><p>This bill allows the Consumer Product Safety Commission (CPSC)\u00a0to issue safety standards for firearms and firearm components.</p><p>Under current law, firearms, shells, cartridges, and components\u00a0thereof are excluded from the CPSC's rulemaking authority.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119s4454"
    },
    "title": "Firearm Safety Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Firearm Safety Act of 2026</strong></p><p>This bill allows the Consumer Product Safety Commission (CPSC)\u00a0to issue safety standards for firearms and firearm components.</p><p>Under current law, firearms, shells, cartridges, and components\u00a0thereof are excluded from the CPSC's rulemaking authority.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119s4454"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4454is.xml"
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
      "title": "Firearm Safety Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Firearm Safety Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consumer Product Safety Act to remove the exclusion of pistols, revolvers, and other firearms from the definition of consumer product in order to permit the issuance for safety standards for such articles by the Consumer Product Safety Commission.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:38Z"
    }
  ]
}
```
