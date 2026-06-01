# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8026?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8026
- Title: CLEAR Act
- Congress: 119
- Bill type: HR
- Bill number: 8026
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-09T14:46:23Z
- Update date including text: 2026-04-09T14:46:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8026",
    "number": "8026",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "CLEAR Act",
    "type": "HR",
    "updateDate": "2026-04-09T14:46:23Z",
    "updateDateIncludingText": "2026-04-09T14:46:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TN"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "NC"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "CO"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "FL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8026ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8026\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Steube (for himself, Mr. Burchett , Mr. Harrigan , Mr. DesJarlais , Ms. Boebert , and Mr. Fine ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 111 of title 18, United States Code, to establish an offense relating to obstructing certain law enforcement vehicle.\n#### 1. Short title\nThis Act may be cited as the Criminalizing Law Enforcement Access Restriction Act or the CLEAR Act .\n#### 2. Offense relating to obstructing certain law enforcement vehicle\nSection 111 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (e); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Enhanced penalty for use of a vehicle Whoever uses a vehicle to forcibly assault, resist, intimidate, or interfere with a Federal law enforcement officer of the Department of Homeland Security or the Department of Justice, while engaged in or on account of the performance of official duties, shall be fined under this title or imprisoned not more than 20 years, or both. (d) Enhanced penalty for obstructing a Federal law enforcement vehicle Whoever forcibly assaults, resists, opposes, impedes, intimidates, or interferes with a Federal law enforcement officer of the Department of Homeland Security or the Department of Justice, while engaged in or on account of the performance of official duties in a Federal law enforcement vehicle, shall be fined under this title or imprisoned not more than 20 years, or both. .",
      "versionDate": "2026-03-19",
      "versionType": "Introduced in House"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-09T14:46:23Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8026ih.xml"
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
      "title": "CLEAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-06T16:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-06T16:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Criminalizing Law Enforcement Access Restriction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-06T16:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 111 of title 18, United States Code, to establish an offense relating to obstructing certain law enforcement vehicle.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-06T16:33:29Z"
    }
  ]
}
```
