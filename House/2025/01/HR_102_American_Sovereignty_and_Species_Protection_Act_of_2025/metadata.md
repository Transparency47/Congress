# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/102?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/102
- Title: American Sovereignty and Species Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 102
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-01-14T16:37:07Z
- Update date including text: 2026-01-14T16:37:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/102",
    "number": "102",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "American Sovereignty and Species Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T16:37:07Z",
    "updateDateIncludingText": "2026-01-14T16:37:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr102ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 102\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to prevent a species that is not native to the United States from being listed as an endangered species or a threatened species, to prohibit certain types of financial assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Sovereignty and Species Protection Act of 2025 .\n#### 2. Limitation on listing of nonnative species and provision of certain financial assistance\n##### (a) Limitation on listing of nonnative species\nSection 4(a) of the Endangered Species Act of 1973 ( 16 U.S.C. 1533(a) ) is amended by adding at the end the following:\n(4) Nonnative species The Secretary may not determine that a species is an endangered species or a threatened species pursuant to this section if such species is not native to the United States. .\n##### (b) Limitation on provision of certain financial assistance\nSection 8(a) of the Endangered Species Act of 1973 ( 16 U.S.C. 1537(a) ) is amended\u2014\n**(1)**\nby striking As a demonstration of and inserting the following:\n(1) In general As a demonstration of ;\n**(2)**\nby striking (which includes, but is not limited to, the acquisition, by lease or otherwise, of lands, waters, or interests therein) ; and\n**(3)**\nby adding at the end the following:\n(2) Prohibition on purchasing land in a foreign country No financial assistance provided under paragraph (1) may be used to acquire, by lease or otherwise, lands, waters, or other interests in a foreign country. .",
      "versionDate": "2025-01-03",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-14T16:37:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr102",
          "measure-number": "102",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr102v00",
            "update-date": "2025-02-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Sovereignty and Species Protection Act of 2025</strong></p><p>This bill limits the protection of endangered or threatened species to species that are native to the United States. In addition, the bill prohibits certain funding for endangered or threatened species from being used to acquire lands, waters, or other interests in foreign countries.</p>"
        },
        "title": "American Sovereignty and Species Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr102.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Sovereignty and Species Protection Act of 2025</strong></p><p>This bill limits the protection of endangered or threatened species to species that are native to the United States. In addition, the bill prohibits certain funding for endangered or threatened species from being used to acquire lands, waters, or other interests in foreign countries.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr102"
    },
    "title": "American Sovereignty and Species Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Sovereignty and Species Protection Act of 2025</strong></p><p>This bill limits the protection of endangered or threatened species to species that are native to the United States. In addition, the bill prohibits certain funding for endangered or threatened species from being used to acquire lands, waters, or other interests in foreign countries.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr102"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr102ih.xml"
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
      "title": "American Sovereignty and Species Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Sovereignty and Species Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to prevent a species that is not native to the United States from being listed as an endangered species or a threatened species, to prohibit certain types of financial assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:23Z"
    }
  ]
}
```
