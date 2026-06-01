# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1342?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1342
- Title: Weatherization Assistance Program Improvements Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1342
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S2477-2478)
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S2477-2478)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1342",
    "number": "1342",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Weatherization Assistance Program Improvements Act of 2025",
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
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: CR S2477-2478)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T19:36:00Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "DE"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1342is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1342\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Reed (for himself, Ms. Collins , Mrs. Shaheen , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Energy Conservation and Production Act to improve the weatherization assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Weatherization Assistance Program Improvements Act of 2025 .\n#### 2. Weatherization Assistance Program\n##### (a) Weatherization Readiness Fund\nSection 414 of the Energy Conservation and Production Act ( 42 U.S.C. 6864 ) is amended by adding at the end the following:\n(d) Weatherization Readiness Fund (1) In general The Secretary shall establish a fund, to be known as the Weatherization Readiness Fund , from which the Secretary shall distribute funds to States receiving financial assistance under this part, in accordance with subsection (a). (2) Use of funds (A) In general A State receiving funds under paragraph (1) shall use the funds for repairs to dwelling units described in subparagraph (B) that will remediate the applicable structural defects or hazards of the dwelling unit so that weatherization measures may be installed. (B) Dwelling unit A dwelling unit referred to in subparagraph (A) is a dwelling unit occupied by a low-income person that, on inspection pursuant to the program under this part, was found to have significant defects or hazards that prevented the installation of weatherization measures under the program. (3) Authorization of appropriations In addition to amounts authorized to be appropriated under section 422, there is authorized to be appropriated to the Secretary to carry out this subsection $30,000,000 for each of fiscal years 2026 through 2030. .\n##### (b) State average cost per unit\n**(1) In general**\nSection 415(c) of the Energy Conservation and Production Act ( 42 U.S.C. 6865(c) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A)\u2014\n**(I)**\nin the first sentence, by striking $6,500 and inserting $15,000 ; and\n**(II)**\nby striking (c)(1) Except as provided in paragraphs (3) and (4) and inserting the following:\n(c) Financial assistance (1) In general Except as provided in paragraphs (3), (4), and (6) ;\n**(ii)**\nby conforming the margins of subparagraphs (A) through (D) to the margin of subparagraph (E);\n**(iii)**\nin subparagraph (D), by striking , and and inserting ; and ; and\n**(iv)**\nin subparagraph (E), by adding a period at the end;\n**(B)**\nin paragraph (2), in the first sentence, by striking weatherized (including dwelling units partially weatherized) and inserting fully weatherized ;\n**(C)**\nin paragraph (4), by striking $3,000 and inserting $6,000 ;\n**(D)**\nin paragraph (5)\u2014\n**(i)**\nin subparagraph (A)(i), by striking (6)(A)(ii) and inserting (7)(A)(ii) ; and\n**(ii)**\nby striking (6)(A)(i)(I) each place it appears and inserting (7)(A)(i)(I) ;\n**(E)**\nby redesignating paragraph (6) as paragraph (7); and\n**(F)**\nby inserting after paragraph (5) the following:\n(6) Limit increase The Secretary may increase the amount of financial assistance provided per dwelling unit under this part beyond the limit specified in paragraph (1) if the Secretary determines that market conditions require such an increase to achieve the purposes of this part. .\n**(2) Conforming amendment**\nSection 414D(b)(1)(C) of the Energy Conservation and Production Act ( 42 U.S.C. 6864d(b)(1)(C) ) is amended by striking 415(c)(6)(A) and inserting 415(c)(7) .",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-19T12:24:14Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1342is.xml"
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
      "title": "Weatherization Assistance Program Improvements Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Weatherization Assistance Program Improvements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy Conservation and Production Act to improve the weatherization assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:20Z"
    }
  ]
}
```
