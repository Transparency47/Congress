# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4350?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4350
- Title: Southeast New England Program Authorization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4350
- Origin chamber: Senate
- Introduced date: 2026-04-21
- Update date: 2026-05-14T16:47:40Z
- Update date including text: 2026-05-14T16:47:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in Senate
- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S1859)
- Latest action: 2026-04-21: Introduced in Senate

## Actions

- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S1859)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4350",
    "number": "4350",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
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
    "title": "Southeast New England Program Authorization Act of 2026",
    "type": "S",
    "updateDate": "2026-05-14T16:47:40Z",
    "updateDateIncludingText": "2026-05-14T16:47:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S1859)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:51:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "RI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4350is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4350\nIN THE SENATE OF THE UNITED STATES\nApril 21, 2026 Mr. Reed (for himself, Mr. Whitehouse , Mr. Markey , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Federal Water Pollution Control Act to establish the Southeast New England Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Southeast New England Program Authorization Act of 2026 .\n#### 2. Southeast New England Program\nTitle I of the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ) is amended by adding at the end the following:\n127. Southeast New England Program (a) Definition of coastal watersheds of southeast New England In this section, the term coastal watersheds of southeast New England means all of the watersheds of Rhode Island and southeastern Massachusetts that drain into coastal waters between Long Island Sound and the Gulf of Maine. (b) Establishment There is established in the Environmental Protection Agency a program, to be known as the Southeast New England Program (referred to in this section as the Program ). (c) Purpose The purpose of the Program shall be to protect, enhance, and restore the coastal watersheds of southeast New England by developing, funding, and advancing implementation of protection and restoration projects in collaboration with partners across the southeast New England region. (d) Grant program (1) In general In carrying out the Program, the Administrator may award grants to support and carry out projects in the coastal watersheds of southeast New England that assist in\u2014 (A) eliminating or reducing pollution; (B) restoring contaminated sites; (C) protecting or restoring ecosystems or habitat; (D) improving water quality; (E) monitoring watersheds to evaluate trends; (F) reducing stormwater runoff; (G) promoting resilience of the coastal watersheds; (H) supporting workforce development, training, or education initiatives that contribute to the health of the coastal watersheds of southeast New England; or (I) providing technical assistance in carrying out projects described in subparagraphs (A) through (H). (2) Eligible recipients An entity eligible for a grant under this subsection is\u2014 (A) a State; (B) a county or local government, or a subdivision of such a government; (C) a federally recognized Indian tribe; (D) a regional planning organization; (E) a nonprofit organization; and (F) an institution of higher education. (3) Cost-share The Federal share of an activity carried out using a grant under this subsection shall not exceed 75 percent. (e) Coordination The Administrator shall coordinate the actions of Federal agencies that affect water quality and the living resources of the coastal watersheds of southeast New England to improve those resources and enhance efficiency. (f) Authorities and duties of Administrator (1) In general In carrying out this section, the Administrator may\u2014 (A) enter into interagency agreements; (B) establish interagency working groups; and (C) contract for services to carry out the purposes of this section. (2) Staffing The Administrator shall provide adequate staff to carry out this section. (g) Authorization of appropriations (1) In general There is authorized to be appropriated to the Administrator to carry out this section $30,000,000 for each of fiscal years 2027 through 2031, to remain available until expended. (2) Technical assistance Of the amounts made available to award grants under subsection (d) in a fiscal year, not more than 10 percent may be used to award grants the primary purpose of which is providing technical assistance pursuant to paragraph (1)(I) of that subsection. (3) Administrative expenses Of the amounts made available under paragraph (1) in a fiscal year, not more than 5 percent may be used for administrative expenses. .",
      "versionDate": "2026-04-21",
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
        "name": "Environmental Protection",
        "updateDate": "2026-05-14T16:47:40Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4350is.xml"
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
      "title": "Southeast New England Program Authorization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T06:53:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Southeast New England Program Authorization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T06:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Water Pollution Control Act to establish the Southeast New England Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T06:48:31Z"
    }
  ]
}
```
