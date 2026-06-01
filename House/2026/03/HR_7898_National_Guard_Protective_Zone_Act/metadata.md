# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7898?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7898
- Title: National Guard Protective Zone Act
- Congress: 119
- Bill type: HR
- Bill number: 7898
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-06T13:09:42Z
- Update date including text: 2026-04-06T13:09:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7898",
    "number": "7898",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001325",
        "district": "3",
        "firstName": "Sheri",
        "fullName": "Rep. Biggs, Sheri [R-SC-3]",
        "lastName": "Biggs",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "National Guard Protective Zone Act",
    "type": "HR",
    "updateDate": "2026-04-06T13:09:42Z",
    "updateDateIncludingText": "2026-04-06T13:09:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:35:30Z",
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
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TN"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "LA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "AL"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7898ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7898\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mrs. Biggs of South Carolina (for herself, Mr. DesJarlais , Mr. Higgins of Louisiana , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish criminal penalties for interfering with National Guard protective zones.\n#### 1. Short title\nThis Act may be cited as the National Guard Protective Zone Act .\n#### 2. Interference with National Guard protective zone\n##### (a) In general\nChapter 67 of title 18, United States Code, is amended by adding at the end the following:\n1390. Interference with National Guard protective zone (a) Definition In this section, the term posted protective zone means an area around a member of the National Guard\u2014 (1) the perimeter of which is not more than 15 feet from the member; and (2) that is marked by a verbal warning, visible signage, barricade tape, or other reasonable means. (b) Offense It shall be unlawful, during a deployment authorized under chapter 15 of title 10 or under title 32, for any person to knowingly enter or remain within a posted protective zone with the intent to impede, intimidate, or interfere with the official duties of a member of the National Guard who is within the posted protective zone. (c) Penalties (1) In general Except as provided in paragraph (2), any person who violates subsection (b) shall be fined under this title, imprisoned not more than 1 year, or both. (2) Aggravated penalty If, in the course of committing a violation of subsection (b), a person makes physical contact with, throws an object at, or spits on the member of the National Guard, the maximum term of imprisonment under paragraph (1) shall be 5 years. (d) Rule of construction Nothing in this section shall be construed to prohibit activity protected by the First Amendment to the Constitution of the United States that is conducted outside a posted protective zone. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 67 of title 18, United States Code, is amended by adding at the end the following:\n1390. Interference with National Guard protective zone. .",
      "versionDate": "2026-03-12",
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
        "actionDate": "2025-12-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3558",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "National Guard Protective Zone Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-06T13:09:42Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7898ih.xml"
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
      "title": "National Guard Protective Zone Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Guard Protective Zone Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to establish criminal penalties for interfering with National Guard protective zones.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:33Z"
    }
  ]
}
```
