# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1060?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1060
- Title: Modern Authentication of Pharmaceuticals Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1060
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2026-04-08T17:28:33Z
- Update date including text: 2026-04-08T17:28:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H519)
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H519)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1060",
    "number": "1060",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Modern Authentication of Pharmaceuticals Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T17:28:33Z",
    "updateDateIncludingText": "2026-04-08T17:28:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H519)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1060ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1060\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. Davis of North Carolina (for himself, Mr. Rutherford , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to modernize the methods of authenticating controlled substances in the pharmaceutical distribution supply chain, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modern Authentication of Pharmaceuticals Act of 2025 .\n#### 2. Modernizing the authentication of controlled substances in the pharmaceutical distribution supply chain\n##### (a) In general\nSection 582(a)(9) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360eee\u20131(a)(9) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by striking and at the end;\n**(2)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(3)**\nby inserting after subparagraph (A) the following:\n(B) a physical chemical identifier shall be included in or on each dose of a product that is\u2014 (i) a controlled substance (as defined in section 102 of the Controlled Substances Act); (ii) in solid oral dosage form; and (iii) manufactured on or after the date that is five years after the date of enactment of the Modern Authentication of Pharmaceuticals Act of 2025 ; and .\n##### (b) Conforming changes\n**(1)**\nSection 581(14) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360eee(14) ) is amended to read as follows:\n(14) Product identifier The term product identifier means\u2014 (A) a standardized graphic that includes, in both human-readable form and on a machine-readable data carrier that conforms to the standards developed by a widely recognized international standards development organization, the standardized numerical identifier, lot number, and expiration date of the product; or (B) a physical chemical identifier, possessing a unique physical or chemical substance or combination of substances, that\u2014 (i) is in or on a product; (ii) is machine readable; and (iii) is intended to authenticate the product or a dosage form thereof. .\n**(2)**\nSection 581(28) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360eee(28) ) is amended to read as follows:\n(28) Verification or verify The term verification or verify means\u2014 (A) determining whether the product identifier affixed to, or imprinted upon, a package or homogeneous case corresponds to the standardized numerical identifier or lot number and expiration date assigned to the product by the manufacturer or the repackager, as applicable in accordance with section 582; or (B) determining whether a product or a dosage form thereof is authentic using a physical chemical identifier described in paragraph (14)(B). .",
      "versionDate": "2025-02-06",
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
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-04-14T14:33:46Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-04-14T14:33:46Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-14T14:33:46Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T17:28:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-11T13:18:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119hr1060",
          "measure-number": "1060",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2025-06-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1060v00",
            "update-date": "2025-06-06"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Modern Authentication of Pharmaceuticals Act of 2025</strong></p><p>This bill requires each dose of a pharmaceutical product that is a controlled substance and that is taken orally in solid form (i.e., pills) to include a physical chemical identifier.\u00a0(Physical chemical identifiers are substances that possess a unique physical or chemical property, such as inks, pigments, flavors, and molecular taggants, that unequivocally identify and authenticate a drug or dosage.) Under the bill, physical chemical identifiers must be included in or on the product and must be machine readable.\u00a0\u00a0</p><p>The bill applies to products manufactured beginning five years after the bill's enactment.</p>"
        },
        "title": "Modern Authentication of Pharmaceuticals Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1060.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Modern Authentication of Pharmaceuticals Act of 2025</strong></p><p>This bill requires each dose of a pharmaceutical product that is a controlled substance and that is taken orally in solid form (i.e., pills) to include a physical chemical identifier.\u00a0(Physical chemical identifiers are substances that possess a unique physical or chemical property, such as inks, pigments, flavors, and molecular taggants, that unequivocally identify and authenticate a drug or dosage.) Under the bill, physical chemical identifiers must be included in or on the product and must be machine readable.\u00a0\u00a0</p><p>The bill applies to products manufactured beginning five years after the bill's enactment.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119hr1060"
    },
    "title": "Modern Authentication of Pharmaceuticals Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Modern Authentication of Pharmaceuticals Act of 2025</strong></p><p>This bill requires each dose of a pharmaceutical product that is a controlled substance and that is taken orally in solid form (i.e., pills) to include a physical chemical identifier.\u00a0(Physical chemical identifiers are substances that possess a unique physical or chemical property, such as inks, pigments, flavors, and molecular taggants, that unequivocally identify and authenticate a drug or dosage.) Under the bill, physical chemical identifiers must be included in or on the product and must be machine readable.\u00a0\u00a0</p><p>The bill applies to products manufactured beginning five years after the bill's enactment.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119hr1060"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1060ih.xml"
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
      "title": "Modern Authentication of Pharmaceuticals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modern Authentication of Pharmaceuticals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to modernize the methods of authenticating controlled substances in the pharmaceutical distribution supply chain, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:19Z"
    }
  ]
}
```
