# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1139?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1139
- Title: Passport Sanity Act
- Congress: 119
- Bill type: HR
- Bill number: 1139
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-02-26T16:37:44Z
- Update date including text: 2026-02-26T16:37:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1139",
    "number": "1139",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Passport Sanity Act",
    "type": "HR",
    "updateDate": "2026-02-26T16:37:44Z",
    "updateDateIncludingText": "2026-02-26T16:37:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1139ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1139\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Roy introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the Secretary of State from issuing a passport, passport card, or Consular Report of Birth Abroad that includes the unspecified (X) gender designation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Passport Sanity Act .\n#### 2. Prohibition regarding certain gender designation on passports, passport cards, and Consular Reports of Birth Abroad issued by Department of State\n##### (a) In general\nThe Secretary of State shall\u2014\n**(1)**\nensure each application for a covered document includes only the gender designations male and female; and\n**(2)**\nprohibit the issuing of a covered document that includes the unspecified (X) gender designation.\n##### (b) Covered document defined\nIn this section, the term covered document means a passport, passport card, or Consular Report of Birth Abroad issued by the Department of State.",
      "versionDate": "2025-02-07",
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
        "name": "Immigration",
        "updateDate": "2025-03-11T18:30:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1139",
          "measure-number": "1139",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2026-02-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1139v00",
            "update-date": "2026-02-26"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Passport Sanity Act</strong></p> <p>This bill prohibits the Department of State from issuing a passport, passport card, or Consular Report of Birth Abroad with an unspecified (X) gender designation. The State Department must also ensure that applications for such documents include only male and female gender designations.</p>"
        },
        "title": "Passport Sanity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1139.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Passport Sanity Act</strong></p> <p>This bill prohibits the Department of State from issuing a passport, passport card, or Consular Report of Birth Abroad with an unspecified (X) gender designation. The State Department must also ensure that applications for such documents include only male and female gender designations.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119hr1139"
    },
    "title": "Passport Sanity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Passport Sanity Act</strong></p> <p>This bill prohibits the Department of State from issuing a passport, passport card, or Consular Report of Birth Abroad with an unspecified (X) gender designation. The State Department must also ensure that applications for such documents include only male and female gender designations.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119hr1139"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1139ih.xml"
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
      "title": "Passport Sanity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Passport Sanity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of State from issuing a passport, passport card, or Consular Report of Birth Abroad that includes the unspecified (X) gender designation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:35Z"
    }
  ]
}
```
