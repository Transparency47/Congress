# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1416?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1416
- Title: Parental Oversight and Educational Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 1416
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-02-11T14:57:19Z
- Update date including text: 2026-02-11T14:57:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1416",
    "number": "1416",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Parental Oversight and Educational Transparency Act",
    "type": "HR",
    "updateDate": "2026-02-11T14:57:19Z",
    "updateDateIncludingText": "2026-02-11T14:57:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1416ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1416\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Ms. Hageman (for herself and Mrs. Miller of Illinois ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the General Education Provisions Act to require parental notification and consent with respect to certain activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Parental Oversight and Educational Transparency Act .\n#### 2. Protection of pupil rights\nSection 445(c)(2)(B) of the General Education Provisions Act ( 20 U.S.C. 1232h ) is amended\u2014\n**(1)**\nby striking The local educational agency and inserting the following:\n(i) In general The local educational agency ; and\n**(2)**\nby adding at the end the following:\n(ii) Written consent required In addition to the notification required under clause (i), not later than 14 days before the specific date during the school year on which an activity described in subparagraph (C) will occur, the local educational agency shall directly notify the parent of a student of such date and receive written consent from such parent in order for such student to participate in such activity. .",
      "versionDate": "2025-02-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-02-11T14:57:09Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2026-02-11T14:57:19Z"
          },
          {
            "name": "School administration",
            "updateDate": "2026-02-11T14:57:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-05-14T17:58:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1416",
          "measure-number": "1416",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1416v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Parental Oversight and Educational Transparency Act</strong></p><p>This bill requires local educational agencies (LEAs) to provide additional notification to, and receive written consent from, parents of students regarding certain school activities that relate to students' privacy.\u00a0</p><p>Under current law, an LEA must annually notify parents of the specific or approximate dates during the school year when specified activities involving information collection, surveys, and screenings are scheduled or expected to be scheduled.</p><p>In addition to this required notification, the bill requires an LEA to directly notify a student's parent 14 days before the scheduled activity and receive written consent from the parent in order for the student to participate in the activity.</p>"
        },
        "title": "Parental Oversight and Educational Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1416.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parental Oversight and Educational Transparency Act</strong></p><p>This bill requires local educational agencies (LEAs) to provide additional notification to, and receive written consent from, parents of students regarding certain school activities that relate to students' privacy.\u00a0</p><p>Under current law, an LEA must annually notify parents of the specific or approximate dates during the school year when specified activities involving information collection, surveys, and screenings are scheduled or expected to be scheduled.</p><p>In addition to this required notification, the bill requires an LEA to directly notify a student's parent 14 days before the scheduled activity and receive written consent from the parent in order for the student to participate in the activity.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1416"
    },
    "title": "Parental Oversight and Educational Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parental Oversight and Educational Transparency Act</strong></p><p>This bill requires local educational agencies (LEAs) to provide additional notification to, and receive written consent from, parents of students regarding certain school activities that relate to students' privacy.\u00a0</p><p>Under current law, an LEA must annually notify parents of the specific or approximate dates during the school year when specified activities involving information collection, surveys, and screenings are scheduled or expected to be scheduled.</p><p>In addition to this required notification, the bill requires an LEA to directly notify a student's parent 14 days before the scheduled activity and receive written consent from the parent in order for the student to participate in the activity.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119hr1416"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1416ih.xml"
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
      "title": "Parental Oversight and Educational Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parental Oversight and Educational Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the General Education Provisions Act to require parental notification and consent with respect to certain activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:22Z"
    }
  ]
}
```
