# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/871?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/871
- Title: RULES Act
- Congress: 119
- Bill type: HR
- Bill number: 871
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-01-10T07:32:46Z
- Update date including text: 2026-01-10T07:32:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/871",
    "number": "871",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "RULES Act",
    "type": "HR",
    "updateDate": "2026-01-10T07:32:46Z",
    "updateDateIncludingText": "2026-01-10T07:32:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:04:30Z",
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "UT"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr871ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 871\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mrs. Luna (for herself, Mr. Ogles , Mr. Weber of Texas , and Mr. Rulli ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to modify the eligibility requirements for asylum.\n#### 1. Short title\nThis Act may be cited as the Refugees Using Legal Entry Safely Act or RULES Act .\n#### 2. Modification of asylum eligibility\nSection 208(a) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a) ) is amended\u2014\n**(1)**\nby amending paragraph (1) to read as follows:\n(1) Application at ports of entry (A) In general Any alien who arrives at a port of entry of the United States, irrespective of such alien's status, may, only at such a port of entry, apply for asylum in accordance with this section or, as applicable, section 235(b). (B) Prohibition on parole or release into the United States Notwithstanding section 236(a)(2), an alien applying for asylum at a port of entry may not be paroled or released into the United States. ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking subparagraph (B);\n**(B)**\nin subparagraph (C), by striking Subject to subparagraph (D), paragraph and inserting Paragraph ;\n**(C)**\nby striking subparagraph (D);\n**(D)**\nin subparagraph (E), by striking Subparagraphs (A) and (B) and inserting Subparagraph (A) ;\n**(E)**\nby redesignating subparagraphs (C) and (E) as subparagraphs (B) and (C), respectively; and\n**(F)**\nby adding at the end the following:\n(D) Effect of apprehension in the United States Paragraph (1) shall not apply to any alien who is apprehended by or referred to the Secretary of Homeland Security as an alien who has entered the United States without inspection and admission or who has remained in the United States beyond the alien's period of authorized stay. ; and\n**(3)**\nby striking Attorney General each place it appears and inserting Attorney General or the Secretary of Homeland Security, as applicable, .",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "200",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RULES Act",
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
        "name": "Immigration",
        "updateDate": "2025-03-04T16:47:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr871",
          "measure-number": "871",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr871v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Refugees Using Legal Entry Safely Act or RULES Act</strong></p><p>This bill requires\u00a0non-U.S. nationals (<em>aliens</em> under federal law) applying for asylum to arrive and apply at a U.S. port of entry. Applicants are prohibited from being paroled into the U.S. pending approval of such application. Further, individuals apprehended in the U.S. without legal immigration status are ineligible for asylum. Applicants rejected for asylum are barred from applying for asylum in the future. Under current law, an applicant may reapply in changed or extraordinary circumstances.</p>"
        },
        "title": "RULES Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr871.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Refugees Using Legal Entry Safely Act or RULES Act</strong></p><p>This bill requires\u00a0non-U.S. nationals (<em>aliens</em> under federal law) applying for asylum to arrive and apply at a U.S. port of entry. Applicants are prohibited from being paroled into the U.S. pending approval of such application. Further, individuals apprehended in the U.S. without legal immigration status are ineligible for asylum. Applicants rejected for asylum are barred from applying for asylum in the future. Under current law, an applicant may reapply in changed or extraordinary circumstances.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr871"
    },
    "title": "RULES Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Refugees Using Legal Entry Safely Act or RULES Act</strong></p><p>This bill requires\u00a0non-U.S. nationals (<em>aliens</em> under federal law) applying for asylum to arrive and apply at a U.S. port of entry. Applicants are prohibited from being paroled into the U.S. pending approval of such application. Further, individuals apprehended in the U.S. without legal immigration status are ineligible for asylum. Applicants rejected for asylum are barred from applying for asylum in the future. Under current law, an applicant may reapply in changed or extraordinary circumstances.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119hr871"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr871ih.xml"
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
      "title": "RULES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RULES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Refugees Using Legal Entry Safely Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to modify the eligibility requirements for asylum.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T05:48:40Z"
    }
  ]
}
```
