# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/716?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/716
- Title: A bill for the relief of Vichai Sae Tung (also known as Chai Chaowasaree).
- Congress: 119
- Bill type: S
- Bill number: 716
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-09-02T19:54:16Z
- Update date including text: 2025-09-02T19:54:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/716",
    "number": "716",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A bill for the relief of Vichai Sae Tung (also known as Chai Chaowasaree).",
    "type": "S",
    "updateDate": "2025-09-02T19:54:16Z",
    "updateDateIncludingText": "2025-09-02T19:54:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T19:45:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s716is.xml",
      "text": "VI\n119th CONGRESS\n1st Session\nS. 716\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Ms. Hirono (for herself and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nFor the relief of Vichai Sae Tung (also known as Chai Chaowasaree).\n#### 1. Permanent residence status for Vichai Sae Tung\n##### (a) In general\nNotwithstanding any other provision of law, for purposes of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ), Vichai Sae Tung (also known as Chai Chaowasaree) shall be held and considered to have been lawfully admitted to the United States for permanent residence as of the date of the enactment of this Act upon payment of the required visa fees.\n##### (b) Reduction of number of available visas\nUpon the granting of permanent residence to Vichai Sae Tung (also known as Chai Chaowasaree) pursuant to subsection (a), the Secretary of State shall instruct the proper officer to reduce by one, during the current or subsequent fiscal year, the total number of immigrant visas available to natives of the country of the alien\u2019s birth under section 203(a) of the Immigration and Nationality Act ( 8 U.S.C. 1153(a) ).",
      "versionDate": "2025-02-25",
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
        "item": {
          "name": "Private Legislation",
          "updateDate": "2025-09-02T19:54:16Z"
        }
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s716is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill for the relief of Vichai Sae Tung (also known as Chai Chaowasaree).",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:18Z"
    },
    {
      "title": "A bill for the relief of Vichai Sae Tung (also known as Chai Chaowasaree).",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:56:19Z"
    }
  ]
}
```
