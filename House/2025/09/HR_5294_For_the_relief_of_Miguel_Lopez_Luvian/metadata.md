# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5294?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5294
- Title: For the relief of Miguel Lopez Luvian.
- Congress: 119
- Bill type: HR
- Bill number: 5294
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-12-08T18:22:03Z
- Update date including text: 2025-12-08T18:22:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5294",
    "number": "5294",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001193",
        "district": "14",
        "firstName": "Eric",
        "fullName": "Rep. Swalwell, Eric [D-CA-14]",
        "lastName": "Swalwell",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "For the relief of Miguel Lopez Luvian.",
    "type": "HR",
    "updateDate": "2025-12-08T18:22:03Z",
    "updateDateIncludingText": "2025-12-08T18:22:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:04:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5294ih.xml",
      "text": "V\n119th CONGRESS\n1st Session\nH. R. 5294\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Swalwell introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nFor the relief of Miguel Lopez Luvian.\n#### 1. Naturalization of Miguel Lopez Luvian\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nMiguel Lopez Luvian has lived in the United States of America for 27 years, and has had immigration status petitions pending for most of that time;\n**(2)**\nhe is the husband of a United States Citizen, the father of three United States Citizens, and the grandfather to one United States Citizen;\n**(3)**\nMiguel Lopez Luvian has complied with the requirements provided by the Department of Homeland Security, and was arrested and detained at a routine immigration check-in and interned at the Golden State Annex in McFarland, California before being deported to Mexico;\n**(4)**\nthat deportation took place in direct contravention of a scheduled court hearing, during which a temporary restraining order was granted which would've prevented his removal from the United States of America; and\n**(5)**\nhis family, employer, and community would be better served if Miguel Lopez Luvian were to return to his home in Livermore, California.\n##### (b) Naturalization\nNotwithstanding section 337(a) or any other provision of title III of the Immigration and Nationality Act ( 8 U.S.C. 1401 et seq. ), Miguel Lopez Luvian shall be considered to be a naturalized citizen of the United States as of the date of the enactment of this Act and shall be furnished by the Attorney General with a certificate of naturalization.",
      "versionDate": "2025-09-10",
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
        "item": {
          "name": "Private Legislation",
          "updateDate": "2025-12-08T18:22:03Z"
        }
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-10",
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
          "measure-id": "id119hr5294",
          "measure-number": "5294",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-10",
          "originChamber": "HOUSE",
          "update-date": "2025-09-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5294v00",
            "update-date": "2025-09-12"
          },
          "action-date": "2025-09-10",
          "action-desc": "Introduced in House",
          "summary-text": "This bill provides for the relief of Miguel Lopez Luvian."
        },
        "title": "For the relief of Miguel Lopez Luvian."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5294.xml",
    "summary": {
      "actionDate": "2025-09-10",
      "actionDesc": "Introduced in House",
      "text": "This bill provides for the relief of Miguel Lopez Luvian.",
      "updateDate": "2025-09-12",
      "versionCode": "id119hr5294"
    },
    "title": "For the relief of Miguel Lopez Luvian."
  },
  "summaries": [
    {
      "actionDate": "2025-09-10",
      "actionDesc": "Introduced in House",
      "text": "This bill provides for the relief of Miguel Lopez Luvian.",
      "updateDate": "2025-09-12",
      "versionCode": "id119hr5294"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5294ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "For the relief of Miguel Lopez Luvian.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T02:18:23Z"
    },
    {
      "title": "For the relief of Miguel Lopez Luvian.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T08:06:31Z"
    }
  ]
}
```
