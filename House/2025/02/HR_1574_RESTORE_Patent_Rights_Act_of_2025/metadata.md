# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1574?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1574
- Title: RESTORE Patent Rights Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1574
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:08:59Z
- Update date including text: 2025-12-05T22:08:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1574",
    "number": "1574",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001224",
        "district": "1",
        "firstName": "Nathaniel",
        "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
        "lastName": "Moran",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "RESTORE Patent Rights Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:08:59Z",
    "updateDateIncludingText": "2025-12-05T22:08:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:03:00Z",
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1574ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1574\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Moran (for himself, Ms. Dean of Pennsylvania , Mr. Roy , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 35, United States Code, to establish a rebuttable presumption that a permanent injunction should be granted in certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Realizing Engineering, Science, and Technology Opportunities by Restoring Exclusive Patent Rights Act of 2025 or the RESTORE Patent Rights Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSecuring effective and reliable patent protection for new technologies is critical to maintaining the competitive advantage of the United States in the global innovation economy.\n**(2)**\nThe Constitution of the United States empowers Congress to grant inventors the exclusive Right to their inventions in order to promote the Progress of Science and the useful Arts .\n**(3)**\nThe right to prevent others from making, using, offering to sell, selling, or importing a patented invention without authority from the inventor is the core of the patent right, ensuring that an inventor enjoys, for a limited time, the sole benefit of the inventor\u2019s invention or discovery.\n**(4)**\nCongress and the courts of the United States have long secured the constitutionally protected patent right through the traditional equitable remedy of an injunction.\n**(5)**\nGiven the irreparable harm that is caused by multiple acts of infringement or willful infringement of a patent, courts historically presumed that an injunction should be granted to prevent such acts, with a burden on defendants to rebut such a presumption with standard equitable defenses.\n**(6)**\nRecently, courts have ended the approach described in paragraph (5), which contradicts the traditional, historical practice governing the equitable remedy described in that paragraph.\n**(7)**\nEliminating the traditional, historical equitable practice of applying a rebuttable presumption of injunctive relief in the case of continuing acts of infringement or willful infringement of a patent has\u2014\n**(A)**\nsubstantially reduced the ability of patent owners to obtain injunctions to stop continuing or willful infringement of patents; and\n**(B)**\ncreated incentives for large, multinational companies to commit predatory acts of infringement, especially with respect to patents owned by undercapitalized entities, such as individual inventors, institutions of higher education, startups, and small or medium-sized enterprises.\n#### 3. Rebuttable presumption that injunctive relief is warranted\nSection 283 of title 35, United States Code, is amended\u2014\n**(1)**\nby striking The several and inserting the following:\n(a) In general The several ; and\n**(2)**\nby adding at the end the following:\n(b) Rebuttable presumption If, in a case under this title, the court enters a final judgment finding infringement of a right secured by patent, the patent owner shall be entitled to a rebuttable presumption that the court should grant a permanent injunction with respect to that infringing conduct. .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "708",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RESTORE Patent Rights Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-03-18T14:14:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119hr1574",
          "measure-number": "1574",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1574v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Realizing Engineering, Science, and Technology Opportunities by Restoring Exclusive Patent Rights Act of 2025 or the RESTORE Patent Rights Act of 2025</strong></p><p>This bill establishes a rebuttable presumption for injunctive relief in patent infringement cases. Specifically, if a court enters a final judgment finding infringement of a right secured by patent, the patent owner shall be entitled to a rebuttable presumption that the court should grant a permanent injunction with respect to that infringing conduct.</p><p>(In 2006, the U.S. Supreme Court held in\u00a0<em>eBay\u00a0v. MercExchange</em> that patent holders do not have an automatic right to a permanent injunction in a patent infringement case.)</p>"
        },
        "title": "RESTORE Patent Rights Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1574.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Realizing Engineering, Science, and Technology Opportunities by Restoring Exclusive Patent Rights Act of 2025 or the RESTORE Patent Rights Act of 2025</strong></p><p>This bill establishes a rebuttable presumption for injunctive relief in patent infringement cases. Specifically, if a court enters a final judgment finding infringement of a right secured by patent, the patent owner shall be entitled to a rebuttable presumption that the court should grant a permanent injunction with respect to that infringing conduct.</p><p>(In 2006, the U.S. Supreme Court held in\u00a0<em>eBay\u00a0v. MercExchange</em> that patent holders do not have an automatic right to a permanent injunction in a patent infringement case.)</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1574"
    },
    "title": "RESTORE Patent Rights Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Realizing Engineering, Science, and Technology Opportunities by Restoring Exclusive Patent Rights Act of 2025 or the RESTORE Patent Rights Act of 2025</strong></p><p>This bill establishes a rebuttable presumption for injunctive relief in patent infringement cases. Specifically, if a court enters a final judgment finding infringement of a right secured by patent, the patent owner shall be entitled to a rebuttable presumption that the court should grant a permanent injunction with respect to that infringing conduct.</p><p>(In 2006, the U.S. Supreme Court held in\u00a0<em>eBay\u00a0v. MercExchange</em> that patent holders do not have an automatic right to a permanent injunction in a patent infringement case.)</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1574"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1574ih.xml"
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
      "title": "RESTORE Patent Rights Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESTORE Patent Rights Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Realizing Engineering, Science, and Technology Opportunities by Restoring Exclusive Patent Rights Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 35, United States Code, to establish a rebuttable presumption that a permanent injunction should be granted in certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:47Z"
    }
  ]
}
```
