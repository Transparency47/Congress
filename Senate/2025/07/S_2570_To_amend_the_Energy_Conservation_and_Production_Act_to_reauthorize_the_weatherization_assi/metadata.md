# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2570?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2570
- Title: Energy Savings and Weatherization Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2570
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2570",
    "number": "2570",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Energy Savings and Weatherization Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T15:06:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NH"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "ME"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "RI"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "AK"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2570is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2570\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Coons (for himself, Mrs. Shaheen , Ms. Collins , and Mr. Reed ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Energy Conservation and Production Act to reauthorize the weatherization assistance program.\n#### 1. Short title\nThis Act may be cited as the Energy Savings and Weatherization Reauthorization Act of 2025 .\n#### 2. Weatherization Assistance Program\n##### (a) Reauthorization\nSection 422(2) of the Energy Conservation and Production Act ( 42 U.S.C. 6872(2) ) is amended by striking 2025 and inserting 2030 .\n##### (b) Definition of fully weatherized\nSection 412 of the Energy Conservation and Production Act ( 42 U.S.C. 6862 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), (3), (8), and (9) as paragraphs (8), (1), (2), (9), and (10), respectively, and reordering accordingly; and\n**(2)**\nby inserting after paragraph (2) (as so redesignated) the following:\n(3) The term fully weatherized , with respect to a dwelling unit, means that\u2014 (A) the recommended measures from an energy audit tool approved by the Secretary or a priority list are installed in that dwelling unit; and (B) the dwelling unit has received a final quality control inspection. .\n##### (c) State average cost per unit\nSection 415(c) of the Energy Conservation and Production Act ( 42 U.S.C. 6865(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A)\u2014\n**(i)**\nin the first sentence, by striking $6,500 and inserting $15,000 ; and\n**(ii)**\nby striking (c)(1) Except as provided in paragraphs (3) and (4) and inserting the following:\n(c) Financial assistance (1) In general Except as provided in paragraphs (3), (4), and (6) ;\n**(B)**\nby conforming the margins of subparagraphs (A) through (D) to the margin of subparagraph (E);\n**(C)**\nin subparagraph (D), by striking , and and inserting ; and ; and\n**(D)**\nin subparagraph (E), by adding a period at the end;\n**(2)**\nin paragraph (2), in the first sentence, by striking weatherized (including dwelling units partially weatherized) and inserting fully weatherized ;\n**(3)**\nin paragraph (4), by striking $3,000 and inserting $6,000 ;\n**(4)**\nin paragraph (5)\u2014\n**(A)**\nin subparagraph (A)(i), by striking (6)(A)(ii) and inserting (7)(A)(ii) ; and\n**(B)**\nby striking (6)(A)(i)(I) each place it appears and inserting (7)(A)(i)(I) ;\n**(5)**\nby redesignating paragraph (6) as paragraph (7); and\n**(6)**\nby inserting after paragraph (5) the following:\n(6) Limit increase The Secretary may increase the amount of financial assistance provided per dwelling unit under this part beyond the limit specified in paragraph (1) if the Secretary determines that market conditions require such an increase to achieve the purposes of this part. .\n##### (d) Conforming Amendment\nSection 414D(b)(1)(C) of the Energy Conservation and Production Act ( 42 U.S.C. 6864d(b)(1)(C) ) is amended by striking 415(c)(6)(A) and inserting 415(c)(7)(A) .",
      "versionDate": "2025-07-31",
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
        "name": "Energy",
        "updateDate": "2025-09-18T18:21:23Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2570is.xml"
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
      "title": "Energy Savings and Weatherization Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Energy Savings and Weatherization Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy Conservation and Production Act to reauthorize the weatherization assistance program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:57Z"
    }
  ]
}
```
