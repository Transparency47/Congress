# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/656?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/656
- Title: Fair Credit for American Hostages Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 656
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-05-27T14:12:52Z
- Update date including text: 2025-05-27T14:12:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/656",
    "number": "656",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
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
    "title": "Fair Credit for American Hostages Act of 2025",
    "type": "S",
    "updateDate": "2025-05-27T14:12:52Z",
    "updateDateIncludingText": "2025-05-27T14:12:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T18:32:49Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "NC"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "OR"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "WY"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "MD"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "SD"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s656is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 656\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Coons (for himself, Mr. Tillis , Mr. Wyden , Ms. Lummis , Mr. Van Hollen , and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Fair Credit Reporting Act to prohibit consumer reporting agencies from furnishing consumer reports containing adverse items of information about a consumer that resulted from that consumer being unlawfully or wrongfully detained abroad or held hostage abroad.\n#### 1. Short title\nThis Act may be cited as the Fair Credit for American Hostages Act of 2025 .\n#### 2. Adverse information about consumers unlawfully or wrongfully detained abroad or held hostage abroad\n##### (a) In general\nThe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ) is amended by inserting after section 605C the following:\n605D. Adverse information about consumers unlawfully or wrongfully detained abroad or held hostage abroad (a) Definitions In this section: (1) Covered consumer The term covered consumer means an individual who has been\u2014 (A) a United States national unlawfully or wrongfully detained abroad, as determined under section 302(a) of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741(a) ); or (B) a United States national taken hostage abroad, as determined by the Hostage Recovery Fusion Cell established by section 304 that Act ( 22 U.S.C. 1741b ). (2) Detention or hostage documentation The term detention or hostage documentation means documentation that\u2014 (A) certifies a consumer is a covered consumer under this section; (B) identifies the time period during which the covered consumer was unlawfully or wrongfully detained abroad or held hostage abroad; and (C) is authenticated by\u2014 (i) the Special Presidential Envoy for Hostage Affairs established by section 303 of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741a ); or (ii) the Hostage Recovery Fusion Cell established by section 304 of that Act ( 22 U.S.C. 1741b ). (b) Adverse information If a consumer reporting agency described in section 603(p) is able to authenticate detention or hostage documentation provided by a covered consumer, the consumer reporting agency may not furnish a consumer report containing any adverse item of information about the covered consumer dating during the time period the covered consumer was unlawfully or wrongfully detained abroad or held hostage abroad. .\n##### (b) Technical and conforming amendment\nThe table of contents of the Fair Credit Reporting Act is amended by inserting after the item relating to section 605C the following:\n605D. Adverse information about consumers unlawfully or wrongfully detained abroad or held hostage abroad. .",
      "versionDate": "2025-02-20",
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
        "updateDate": "2025-03-13T15:10:09Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s656is.xml"
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
      "title": "Fair Credit for American Hostages Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Credit for American Hostages Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Credit Reporting Act to prohibit consumer reporting agencies from furnishing consumer reports containing adverse items of information about a consumer that resulted from that consumer being unlawfully or wrongfully detained abroad or held hostage abroad.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:30Z"
    }
  ]
}
```
