# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2922
- Title: Hammers' Law
- Congress: 119
- Bill type: HR
- Bill number: 2922
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-12-05T21:41:18Z
- Update date including text: 2025-12-05T21:41:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2922",
    "number": "2922",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Hammers' Law",
    "type": "HR",
    "updateDate": "2025-12-05T21:41:18Z",
    "updateDateIncludingText": "2025-12-05T21:41:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
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
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:31:20Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "NJ"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2922ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2922\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Bacon (for himself, Mr. Van Drew , Ms. Matsui , and Ms. Scanlon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide authorization for nonpecuniary damages in an action resulting from a cruise ship voyage occurring on the high seas.\n#### 1. Short title\nThis Act may be cited as the Hammers' Law .\n#### 2. Limitations in certain cases\n##### (a) In general\nSection 30307 of title 46, United States Code, is amended\u2014\n**(1)**\nin the section heading, by striking Commercial aviation accidents and inserting Limitations in certain cases ;\n**(2)**\nby striking subsection (a) and inserting the following:\n(a) Definitions In this section: (1) Cruise ship The term cruise ship means a passenger vessel, other than a vessel of the United States operated by the Federal Government or a vessel owned and operated by a State, that\u2014 (A) is authorized to carry at least 250 passengers; (B) has onboard sleeping facilities for each passenger; (C) is on a voyage that embarks or disembarks passengers in the United States; and (D) is not engaged on a coastwise voyage. (2) Nonpecuniary damages The term nonpecuniary damages means damages for loss of care, comfort, and companionship. ;\n**(3)**\nin subsection (b), by inserting or cruise ship voyage after commercial aviation ; and\n**(4)**\nin subsection (c), by inserting or cruise ship voyage after commercial aviation .\n##### (b) Clerical amendment\nThe table of sections for chapter 303 of title 46, United States Code, is amended by striking the item relating to section 30307 and inserting the following:\n30307. Limitations in certain cases. .",
      "versionDate": "2025-04-17",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1423",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Hammers' Law",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-29T17:41:30Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2922ih.xml"
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
      "title": "Hammers' Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hammers' Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide authorization for nonpecuniary damages in an action resulting from a cruise ship voyage occurring on the high seas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T03:03:31Z"
    }
  ]
}
```
