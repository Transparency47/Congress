# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/849?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/849
- Title: No Regulation Through Litigation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 849
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-09-09T12:34:32Z
- Update date including text: 2025-09-09T12:34:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/849",
    "number": "849",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "No Regulation Through Litigation Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-09T12:34:32Z",
    "updateDateIncludingText": "2025-09-09T12:34:32Z"
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
          "date": "2025-01-31T15:02:10Z",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "LA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "WI"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "PA"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "AL"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr849ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 849\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Cloud (for himself, Mr. Ogles , Mr. Higgins of Louisiana , Mr. Crane , Mr. Tiffany , and Mr. Perry ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide limitations for Federal agencies entering into settlement agreements and consent decrees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Regulation Through Litigation Act of 2025 .\n#### 2. Settlement agreements and consent decrees\n##### (a) Limitation on consent decrees\nThe head of a Federal agency may not enter into a consent decree that exceeds the authority of the court that enters the order related to such decree.\n##### (b) Limitation on attorneys\u2019 fees and litigation costs\nA settlement agreement or consent decree resulting in a regulation or guidance document with respect to which a Federal agency is a party may not include the payment of attorneys\u2019 fees or litigation costs.\n##### (c) Definitions\nIn this Act:\n**(1) Guidance document**\nThe term guidance document \u2014\n**(A)**\nmeans an agency statement of general applicability (other than a regulation that has the force and effect of law promulgated in accordance with the notice and public procedure under section 553 of title 5, United States Code) that\u2014\n**(i)**\ndoes not have the force and effect of law; and\n**(ii)**\nsets forth\u2014\n**(I)**\nan agency decision or a policy on a statutory, regulatory, or technical issue; or\n**(II)**\nan interpretation of a statutory or regulatory issue; and\n**(B)**\nmay include\u2014\n**(i)**\na memorandum;\n**(ii)**\na notice;\n**(iii)**\na bulletin;\n**(iv)**\na directive;\n**(v)**\na news release;\n**(vi)**\na letter;\n**(vii)**\na blog post;\n**(viii)**\na no-action letter;\n**(ix)**\na speech by an agency official;\n**(x)**\nan advisory;\n**(xi)**\na manual;\n**(xii)**\na circular; or\n**(xiii)**\nany combination of the items described in clauses (i) through (xii).\n**(2) Regulation**\nThe term regulation \u2014\n**(A)**\nmeans an agency statement of general applicability and future effect, which the agency intends to have the force and effect of law, that is designed to implement, interpret, or prescribe law or policy or to describe the procedure or practice requirements of an agency;\n**(B)**\nincludes regulations issued pursuant to\u2014\n**(i)**\nan informal rulemaking under section 553 of title 5, United States Code;\n**(ii)**\na formal rulemaking under sections 556 and 557 of title 5, United States Code; and\n**(iii)**\nany combination of the informal rulemaking described in clause (i) and the formal rulemaking described in clause (ii); and\n**(C)**\ndoes not include\u2014\n**(i)**\nregulations that pertain to a military or foreign affairs function of the United States, other than procurement regulations and regulations involving the import or export of non-defense articles and services;\n**(ii)**\nregulations or regulations that are limited to agency organization, management, or personnel matters; or\n**(iii)**\nany other category of regulations exempted by the Administrator of Office of Information and Regulatory Affairs.\n##### (d) Severability\nIf any provision of this Act or the application of any provision of this Act to any person or circumstance, is held invalid, the application of such provision to other persons or circumstances, and the remainder of this Act, shall not be affected thereby.",
      "versionDate": "2025-01-31",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-20T18:38:23Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-06-20T18:38:23Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-06-20T18:38:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-01T19:39:38Z"
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
          "measure-id": "id119hr849",
          "measure-number": "849",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr849v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Regulation Through Litigation Act of 2025</strong><strong></strong></p><p>This bill specifies that a federal agency may not enter into a consent decree that exceeds the authority of the court that enters the order related to the decree. It also limits the inclusion of attorney fees or litigation costs\u00a0in consent decrees or settlement agreements that result in a regulation or guidance document.\u00a0</p>"
        },
        "title": "No Regulation Through Litigation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr849.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Regulation Through Litigation Act of 2025</strong><strong></strong></p><p>This bill specifies that a federal agency may not enter into a consent decree that exceeds the authority of the court that enters the order related to the decree. It also limits the inclusion of attorney fees or litigation costs\u00a0in consent decrees or settlement agreements that result in a regulation or guidance document.\u00a0</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr849"
    },
    "title": "No Regulation Through Litigation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Regulation Through Litigation Act of 2025</strong><strong></strong></p><p>This bill specifies that a federal agency may not enter into a consent decree that exceeds the authority of the court that enters the order related to the decree. It also limits the inclusion of attorney fees or litigation costs\u00a0in consent decrees or settlement agreements that result in a regulation or guidance document.\u00a0</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr849"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr849ih.xml"
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
      "title": "No Regulation Through Litigation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Regulation Through Litigation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide limitations for Federal agencies entering into settlement agreements and consent decrees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:38Z"
    }
  ]
}
```
