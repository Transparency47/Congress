# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7490
- Title: Tribal Warrant Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 7490
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-05-01T08:08:49Z
- Update date including text: 2026-05-01T08:08:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7490",
    "number": "7490",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "C001053",
        "district": "4",
        "firstName": "Tom",
        "fullName": "Rep. Cole, Tom [R-OK-4]",
        "lastName": "Cole",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Tribal Warrant Fairness Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:49Z",
    "updateDateIncludingText": "2026-05-01T08:08:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:02:00Z",
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
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "WA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NM"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7490ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7490\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Cole (for himself, Mr. Larsen of Washington , Ms. Leger Fernandez , and Mr. Issa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo allow the U.S. Marshals Service to assist in certain Tribal criminal matters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tribal Warrant Fairness Act .\n#### 2. Amendments\n##### (a) U.S. Marshals Service\nSection 566(e)(1) of title 28, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B), by inserting including Tribal fugitive matters (on the request of an Indian Tribe, as applicable), after matters, ; and\n**(2)**\nin subparagraph (D), by inserting Tribal, after local, .\n##### (b) Presidential Threat Protection Act of 2000\nSection 6 of the Presidential Threat Protection Act of 2000 ( 34 U.S.C. 41503 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby inserting and Indian Tribes after components ; and\n**(B)**\nby striking and local and inserting local, and Tribal ; and\n**(2)**\nin subsection (c), by striking Federal or State law and inserting Federal, State, or Tribal law .",
      "versionDate": "2026-02-11",
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
        "actionDate": "2025-10-23",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3041",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tribal Warrant Fairness Act",
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
        "name": "Native Americans",
        "updateDate": "2026-02-23T23:38:39Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7490ih.xml"
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
      "title": "Tribal Warrant Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tribal Warrant Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow the U.S. Marshals Service to assist in certain Tribal criminal matters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:27Z"
    }
  ]
}
```
