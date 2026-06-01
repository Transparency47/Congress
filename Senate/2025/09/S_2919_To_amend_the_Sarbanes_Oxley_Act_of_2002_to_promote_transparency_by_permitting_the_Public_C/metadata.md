# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2919?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2919
- Title: PCAOB Enforcement Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2919
- Origin chamber: Senate
- Introduced date: 2025-09-19
- Update date: 2025-12-16T18:48:58Z
- Update date including text: 2025-12-16T18:48:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in Senate
- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S6793)
- Latest action: 2025-09-19: Introduced in Senate

## Actions

- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S6793)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2919",
    "number": "2919",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
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
    "title": "PCAOB Enforcement Transparency Act of 2025",
    "type": "S",
    "updateDate": "2025-12-16T18:48:58Z",
    "updateDateIncludingText": "2025-12-16T18:48:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S6793)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T16:48:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2919is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2919\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Mr. Reed (for himself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Sarbanes-Oxley Act of 2002 to promote transparency by permitting the Public Company Accounting Oversight Board to allow its disciplinary proceedings to be open to the public, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PCAOB Enforcement Transparency Act of 2025 .\n#### 2. Open meetings authorized\nSection 105(c) of the Sarbanes-Oxley Act of 2002 ( 15 U.S.C. 7215(c) ) is amended by striking paragraph (2) and inserting the following:\n(2) Public hearings Hearings under this section shall be open to the public, unless the Board, on its own motion or after considering the motion of a party, orders otherwise. .\n#### 3. Publication of determinations\nSection 105(d)(1)(C) of the Sarbanes-Oxley Act of 2002 ( 15 U.S.C. 7215(d)(1)(C) ) is amended by striking (once any stay on the imposition of such sanction has been lifted) .",
      "versionDate": "2025-09-19",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-16T18:48:57Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2919is.xml"
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
      "title": "PCAOB Enforcement Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PCAOB Enforcement Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Sarbanes-Oxley Act of 2002 to promote transparency by permitting the Public Company Accounting Oversight Board to allow its disciplinary proceedings to be open to the public, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:20Z"
    }
  ]
}
```
