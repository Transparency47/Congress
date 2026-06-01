# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5640?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5640
- Title: Northern Mariana Islands and American Samoa Criminal Justice Support Act
- Congress: 119
- Bill type: HR
- Bill number: 5640
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-04-06T16:34:02Z
- Update date including text: 2026-04-06T16:34:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5640",
    "number": "5640",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000404",
        "district": "",
        "firstName": "Kimberlyn",
        "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
        "lastName": "King-Hinds",
        "party": "R",
        "state": "MP"
      }
    ],
    "title": "Northern Mariana Islands and American Samoa Criminal Justice Support Act",
    "type": "HR",
    "updateDate": "2026-04-06T16:34:02Z",
    "updateDateIncludingText": "2026-04-06T16:34:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:05:35Z",
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
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5640ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5640\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Ms. King-Hinds (for herself and Mrs. Radewagen ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the definition of State in title I of the Omnibus Crime Control and Safe Streets Act of 1968, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Northern Mariana Islands and American Samoa Criminal Justice Support Act .\n#### 2. Definition of State\nSection 901(a)(2) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251(a)(2) ) is amended by striking Northern Mariana Islands and all that follows through Commonwealth of the Northern Mariana Islands. and inserting Northern Mariana Islands; .",
      "versionDate": "2025-09-30",
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
        "updateDate": "2025-12-17T16:50:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hr5640",
          "measure-number": "5640",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5640v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Northern Mariana Islands and American Samoa Criminal Justice Support Act</strong></p><p>This bill increases the amount of state formula grant funds allocated to American Samoa and the Northern Mariana Islands under the Edward Byrne Memorial Justice Assistance Grant (JAG) program.</p><p>Currently, American Samoa and the Northern Mariana Islands are considered to be one state, and they split one JAG allocation with 67% going to American Samoa and 33% going to the Northern Mariana Islands.</p><p>This bill considers American Samoa and the Northern Mariana Islands to be separate states, which entitles each of them to a full JAG allocation.</p>"
        },
        "title": "Northern Mariana Islands and American Samoa Criminal Justice Support Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5640.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Northern Mariana Islands and American Samoa Criminal Justice Support Act</strong></p><p>This bill increases the amount of state formula grant funds allocated to American Samoa and the Northern Mariana Islands under the Edward Byrne Memorial Justice Assistance Grant (JAG) program.</p><p>Currently, American Samoa and the Northern Mariana Islands are considered to be one state, and they split one JAG allocation with 67% going to American Samoa and 33% going to the Northern Mariana Islands.</p><p>This bill considers American Samoa and the Northern Mariana Islands to be separate states, which entitles each of them to a full JAG allocation.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr5640"
    },
    "title": "Northern Mariana Islands and American Samoa Criminal Justice Support Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Northern Mariana Islands and American Samoa Criminal Justice Support Act</strong></p><p>This bill increases the amount of state formula grant funds allocated to American Samoa and the Northern Mariana Islands under the Edward Byrne Memorial Justice Assistance Grant (JAG) program.</p><p>Currently, American Samoa and the Northern Mariana Islands are considered to be one state, and they split one JAG allocation with 67% going to American Samoa and 33% going to the Northern Mariana Islands.</p><p>This bill considers American Samoa and the Northern Mariana Islands to be separate states, which entitles each of them to a full JAG allocation.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr5640"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5640ih.xml"
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
      "title": "Northern Mariana Islands and American Samoa Criminal Justice Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Northern Mariana Islands and American Samoa Criminal Justice Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the definition of State in title I of the Omnibus Crime Control and Safe Streets Act of 1968, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:18Z"
    }
  ]
}
```
