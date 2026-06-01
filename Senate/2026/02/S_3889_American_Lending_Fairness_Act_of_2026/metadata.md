# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3889?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3889
- Title: American Lending Fairness Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3889
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-04-21T16:03:41Z
- Update date including text: 2026-04-21T16:03:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3889",
    "number": "3889",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "American Lending Fairness Act of 2026",
    "type": "S",
    "updateDate": "2026-04-21T16:03:41Z",
    "updateDateIncludingText": "2026-04-21T16:03:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T20:40:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3889is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3889\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo restore and clarify the intent of the Federal interest rate exportation parity for State-chartered banks by allowing States to opt out of preemption only with respect to loans made by their own chartered institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Lending Fairness Act of 2026 .\n#### 2. Interest rate applicable to out-of-State chartered financial institutions\n##### (a) Insured depository institutions\nSection 27 of the Federal Deposit Insurance Act ( 12 U.S.C. 1831d ) is amended by adding at the end the following:\n(c) If a State adopts a law or certifies that the voters of the State have voted in favor of any provision, constitutional or otherwise, that states explicitly and by its terms that the State does not want this subsection to apply with respect to loans made by institutions chartered by that State, subsection (a) shall not apply to loans made by (or for which a commitment to make such loan was entered into by) such institutions after the date on which that law is adopted or such certification is made. .\n##### (b) Insured credit unions\nSection 205(g) of the Federal Credit Union Act ( 12 U.S.C. 1785(g) ) is amended by adding at the end the following:\n(3) If a State adopts a law or certifies that the voters of the State have voted in favor of any provision, constitutional or otherwise, that states explicitly and by its terms that the State does not want this subsection to apply with respect to loans made by institutions chartered by that State, paragraph (1) shall not apply to loans made by (or for which a commitment to make such loan was entered into by) such institutions after the date on which that law is adopted or such certification is made. .\n##### (c) Repeal\n**(1) In general**\nSection 525 of the Depository Institutions Deregulation and Monetary Control Act of 1980 ( 12 U.S.C. 1730g note) is hereby repealed.\n**(2) Application**\nThe amendments made by subsections (a) and (b) shall apply with respect to, and govern the legal effect of, any State law adopted or certification made pursuant to section 525 of the Depository Institutions Deregulation and Monetary Control Act of 1980 ( 12 U.S.C. 1730g note) before the date of enactment of this Act.",
      "versionDate": "2026-02-12",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-09",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "7866",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Lending Fairness Act of 2026",
      "type": "HR"
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
        "updateDate": "2026-03-02T15:25:15Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3889is.xml"
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
      "title": "American Lending Fairness Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Lending Fairness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restore and clarify the intent of the Federal interest rate exportation parity for State-chartered banks by allowing States to opt out of preemption only with respect to loans made by their own chartered institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T03:48:22Z"
    }
  ]
}
```
