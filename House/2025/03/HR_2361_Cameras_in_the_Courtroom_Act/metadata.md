# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2361?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2361
- Title: Cameras in the Courtroom Act
- Congress: 119
- Bill type: HR
- Bill number: 2361
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-12-05T21:32:47Z
- Update date including text: 2025-12-05T21:32:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2361",
    "number": "2361",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001078",
        "district": "11",
        "firstName": "Gerald",
        "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
        "lastName": "Connolly",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Cameras in the Courtroom Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:32:47Z",
    "updateDateIncludingText": "2025-12-05T21:32:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:01:45Z",
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
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2361ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2361\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Connolly introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo permit the televising of Supreme Court proceedings.\n#### 1. Short title\nThis Act may be cited as the Cameras in the Courtroom Act .\n#### 2. Amendment to title 28\n##### (a) In general\nChapter 45 of title 28, United States Code, is amended by adding at the end the following:\n678. Televising Supreme Court proceedings The Supreme Court shall permit television coverage of all open sessions of the Court unless the Court decides, by a vote of the majority of justices, that allowing such coverage in a particular case would constitute a violation of the due process rights of one or more of the parties before the Court. .\n##### (b) Clerical amendment\nThe chapter analysis for chapter 45 of title 28, United States Code, is amended by adding at the end the following:\n678. Televising Supreme Court proceedings. .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-03-26",
        "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S1874)"
      },
      "number": "1146",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Cameras in the Courtroom Act",
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
        "name": "Law",
        "updateDate": "2025-04-04T15:41:49Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2361ih.xml"
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
      "title": "Cameras in the Courtroom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cameras in the Courtroom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit the televising of Supreme Court proceedings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T04:48:20Z"
    }
  ]
}
```
