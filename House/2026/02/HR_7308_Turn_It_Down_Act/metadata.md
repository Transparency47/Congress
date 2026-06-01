# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7308
- Title: Turn It Down Act
- Congress: 119
- Bill type: HR
- Bill number: 7308
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-02-20T18:03:14Z
- Update date including text: 2026-02-20T18:03:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7308",
    "number": "7308",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Turn It Down Act",
    "type": "HR",
    "updateDate": "2026-02-20T18:03:14Z",
    "updateDateIncludingText": "2026-02-20T18:03:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7308ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7308\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mrs. Bice introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the CALM Act to establish requirements for video programming delivered using internet protocol, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Turn It Down Act .\n#### 2. Applicability of CALM Act to video programming delivered using internet protocol\nThe CALM Act ( 47 U.S.C. 621 ) is amended by adding at the end the following:\n3. Applicability to video programming delivered using internet protocol (a) In general Not later than 18 months after the date of the enactment of this section, the Federal Communications Commission shall prescribe pursuant to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) a regulation to ensure that commercial advertisements that accompany video programming delivered using internet protocol are subject to volume requirements that are substantially equivalent to the requirements applicable, pursuant to section 2, to commercial advertisements transmitted by a television broadcast station, cable operator, or other multichannel video programming distributor. (b) Video programming defined In this section, the term video programming \u2014 (1) means programming provided by, or generally considered comparable to programming provided by, a television broadcast station; and (2) does not include consumer-generated media. .",
      "versionDate": "2026-02-02",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-20T18:03:14Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7308ih.xml"
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
      "title": "Turn It Down Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Turn It Down Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the CALM Act to establish requirements for video programming delivered using internet protocol, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:26Z"
    }
  ]
}
```
