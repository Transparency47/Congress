# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7866?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7866
- Title: American Lending Fairness Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7866
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-05-08T08:06:03Z
- Update date including text: 2026-05-08T08:06:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7866",
    "number": "7866",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "American Lending Fairness Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:03Z",
    "updateDateIncludingText": "2026-05-08T08:06:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-03-09T17:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "KY"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7866ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7866\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Davidson (for himself and Mr. Barr ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo restore and clarify the intent of the Federal interest rate exportation parity for State-chartered banks by allowing States to opt out of preemption only with respect to loans made by their own chartered institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Lending Fairness Act of 2026 .\n#### 2. Interest rate applicable to out-of-State chartered financial institutions\n##### (a) Insured depository institutions\nSection 27 of the Federal Deposit Insurance Act ( 12 U.S.C. 1831d ) is amended by adding at the end the following:\n(c) If a State adopts a law or certifies that the voters of the State have voted in favor of any provision, constitutional or otherwise, that states explicitly and by its terms that the State does not want this subsection to apply with respect to loans made by institutions chartered by that State, subsection (a) shall not apply to loans made by (or for which a commitment to make such loan was entered into by) such institutions after the date on which that law is adopted or such certification is made. .\n##### (b) Insured credit unions\nSection 205(g) of the Federal Credit Union Act ( 12 U.S.C. 1785(g) ) is amended by adding at the end the following:\n(3) If a State adopts a law or certifies that the voters of the State have voted in favor of any provision, constitutional or otherwise, that states explicitly and by its terms that the State does not want this subsection to apply with respect to loans made by institutions chartered by that State, paragraph (1) shall not apply to loans made by (or for which a commitment to make such loan was entered into by) such institutions after the date on which that law is adopted or such certification is made. .\n##### (c) Repeal\n**(1) In general**\nSection 525 of the Depository Institutions Deregulation and Monetary Control Act of 1980 ( 12 U.S.C. 1730g note) is hereby repealed.\n**(2) Application**\nThe amendments made by subsections (a) and (b) shall apply with respect to, and govern the legal effect of, any State law adopted or certification made pursuant to section 525 of the Depository Institutions Deregulation and Monetary Control Act of 1980 ( 12 U.S.C. 1730g note) before the date of enactment of this Act.",
      "versionDate": "2026-03-09",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3889",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Lending Fairness Act of 2026",
      "type": "S"
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
        "updateDate": "2026-04-21T16:03:47Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7866ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2026-04-18T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Lending Fairness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T09:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restore and clarify the intent of the Federal interest rate exportation parity for State-chartered banks by allowing States to opt out of preemption only with respect to loans made by their own chartered institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T09:33:22Z"
    }
  ]
}
```
