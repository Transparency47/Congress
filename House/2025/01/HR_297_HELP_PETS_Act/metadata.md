# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/297
- Title: HELP PETS Act
- Congress: 119
- Bill type: HR
- Bill number: 297
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-12-10T07:11:53Z
- Update date including text: 2025-12-10T07:11:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/297",
    "number": "297",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "HELP PETS Act",
    "type": "HR",
    "updateDate": "2025-12-10T07:11:53Z",
    "updateDateIncludingText": "2025-12-10T07:11:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:38:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr297ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 297\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo prohibit the availability of Federal funds to institutions of higher education that conduct painful biomedical research on dogs and cats.\n#### 1. Short title\nThis Act may be cited as the Higher Education Loses Payments for Painful Experiments, Tests and Studies Act or the HELP PETS Act .\n#### 2. Prohibition on availability of Federal Funds to Institutions of Higher Education that conduct painful research using dogs and cats\n##### (a) In general\nBeginning on the date that is 180 days after the date of the enactment of this Act, no Federal funds may be made available to any institution of higher education that conducts or funds, in whole or in part, painful research on dogs or cats.\n##### (b) Exceptions\nSubsection (a) shall not apply to\u2014\n**(1)**\nclinical veterinary research; or\n**(2)**\nany physical exam, training program, or study relating to service animals or military animals.\n##### (c) Definitions\nIn this section:\n**(1) Clinical veterinary research**\nThe term clinical veterinary research means research on a dog or cat with a naturally occurring disease or injury that is conducted\u2014\n**(A)**\nfor the benefit of the dog or cat; and\n**(B)**\nwith the intention of studying the effect of a procedure, device, or treatment protocol.\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(3) Military animal**\nThe term military animal has the meaning given the term in section 2583(i)(1) of title 10, United States Code.\n**(4) Painful research**\nThe term painful research includes any research, biomedical training, experimentation, or biological testing classified in pain category D or E by the Department of Agriculture.\n**(5) Service animal**\nThe term service animal has the meaning given the term in section 37.3 of title 49, Code of Federal Regulations.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-07",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "233",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "HELP PETS Act",
      "type": "HR"
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
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-02-28T15:22:02Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-02-28T15:22:02Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-02-28T15:22:02Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-02-28T15:22:02Z"
          },
          {
            "name": "Research ethics",
            "updateDate": "2025-02-28T15:22:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-13T21:20:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr297",
          "measure-number": "297",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr297v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Higher Education Loses Payments for Painful Experiments, Tests and Studies Act or the HELP PETS Act</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal funds if the IHE conducts or funds painful research on dogs or cats. <em>Painful research</em> refers to any research, biomedical training, experimentation, or biological testing classified in specified pain categories by the Department of Agriculture.</p>"
        },
        "title": "HELP PETS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr297.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Higher Education Loses Payments for Painful Experiments, Tests and Studies Act or the HELP PETS Act</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal funds if the IHE conducts or funds painful research on dogs or cats. <em>Painful research</em> refers to any research, biomedical training, experimentation, or biological testing classified in specified pain categories by the Department of Agriculture.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr297"
    },
    "title": "HELP PETS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Higher Education Loses Payments for Painful Experiments, Tests and Studies Act or the HELP PETS Act</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal funds if the IHE conducts or funds painful research on dogs or cats. <em>Painful research</em> refers to any research, biomedical training, experimentation, or biological testing classified in specified pain categories by the Department of Agriculture.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr297"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr297ih.xml"
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
      "title": "HELP PETS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HELP PETS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Higher Education Loses Payments for Painful Experiments, Tests and Studies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the availability of Federal funds to institutions of higher education that conduct painful biomedical research on dogs and cats.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:33Z"
    }
  ]
}
```
