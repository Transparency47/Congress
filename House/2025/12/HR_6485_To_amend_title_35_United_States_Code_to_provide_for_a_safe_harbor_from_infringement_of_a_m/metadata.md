# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6485?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6485
- Title: Skinny Labels, Big Savings Act
- Congress: 119
- Bill type: HR
- Bill number: 6485
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2026-05-20T08:06:17Z
- Update date including text: 2026-05-20T08:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6485",
    "number": "6485",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Skinny Labels, Big Savings Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:06:17Z",
    "updateDateIncludingText": "2026-05-20T08:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
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
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:01:05Z",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "VA"
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
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6485ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6485\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Mr. Cline (for himself and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 35, United States Code, to provide for a safe harbor from infringement of a method of use patent relating to drugs or biological products.\n#### 1. Short title\nThis Act may be cited as the Skinny Labels, Big Savings Act .\n#### 2. Safe harbor from infringement of a method of use patent\n##### (a) In general\nSection 271 of title 35, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (h) and (i) as subsections (k) and (l), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) (1) The following shall not be acts of direct, induced, or contributory infringement of a method of use claim in a patent included in the list described in section 505(j)(7) or section 512(n)(4) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(7) , 360b(n)(4)) in an action or counterclaim under this section: (A) Submitting or seeking approval of an application under section 505(j) or section 512(b)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j) , 360b(b)(2)), or submitting or seeking approval of an application described in section 505(b)(2) of such Act ( 21 U.S.C. 355(b)(2) ), provided that such application includes a statement under, as applicable, section 505(j)(2)(A)(viii), section 512(n)(1)(I), or section 505(b)(2)(B) of such Act ( 21 U.S.C. 355(j)(2)(A)(viii) , 360b(n)(1)(I), 355(b)(2)(B)) for the method of use claims in the patent with the labeling proposed in such application. (B) Promoting or commercially marketing a drug product with the labeling approved in an application described in subparagraph (A). (C) Describing a drug product approved in an application submitted under section 505(j) or section 512(b)(2) of such Act ( 21 U.S.C. 355(j) , 360b(b)(2)) or approved in an application described in section 505(b)(2) of such Act ( 21 U.S.C. 355(b)(2) ) as a generic of, or therapeutically equivalent to, the listed drug referenced in such application, as applicable. (2) Subparagraphs (A) through (C) of paragraph (1) shall apply only if the labeling, promotion, or commercial marketing does not reference the condition or conditions of use claimed in the patent that was identified by the patent owner or assignee to the Secretary under section 314.53 of title 21, Code of Federal Regulations (or a successor regulation) and that was subject to the statement under section 505(j)(2)(A)(viii), section 512(n)(1)(I), or section 505(b)(2)(B) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(2)(A)(viii) , 360b(n)(1)(I), 355(b)(2)(B)), as applicable. (i) (1) The following shall not be acts of direct, induced, or contributory infringement of a patent claim covering a method of using the reference product in an action or counterclaim under this section: (A) Submitting or seeking approval of an application under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (B) Describing a biological product approved in an application described in subparagraph (A) as biosimilar to, or interchangeable with, the reference product, as applicable, with the labeling approved in such application, when the biological product has not been approved for the patented condition or conditions of use. (C) Promoting or commercially marketing a biological product with the labeling approved in an application described in subparagraph (A). (2) Subparagraphs (A) through (C) of paragraph (1) shall apply only if the labeling, promotion, or commercial marketing does not reference the condition or conditions of use claimed in the patent and specifically reflected in the prescribing information. (j) As used in this section: (1) The terms biological product , biosimilar , interchangeable , and reference product have the meanings given such terms in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ). (2) The term commercial marketing has the meaning given such term in section 314.3 of title 21, Code of Federal Regulations (or a successor regulation). (3) The term labeling has the meaning given such term in section 201(m) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(m) ). (4) The term promoting \u2014 (A) is within the meaning of the term used in section 202.1 of title 21, Code of Federal Regulations (or a successor regulation); and (B) includes the use of promotional labeling and advertising, as described in paragraphs (1) and (2) of section 202.1(l) of title 21, Code of Federal Regulations (or successor regulations). .\n##### (b) Application\nThis Act and the amendments made by this Act shall apply to\u2014\n**(1)**\nconduct that occurs before, on, or after the date of enactment of this Act; and\n**(2)**\nall judicial or other proceedings pending as of such date of enactment.",
      "versionDate": "2025-12-05",
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
        "actionDate": "2025-01-09",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "43",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Skinny Labels, Big Savings Act",
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
        "updateDate": "2025-12-18T16:16:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-05",
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
          "measure-id": "id119hr6485",
          "measure-number": "6485",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-05",
          "originChamber": "HOUSE",
          "update-date": "2026-02-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6485v00",
            "update-date": "2026-02-23"
          },
          "action-date": "2025-12-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Skinny Labels, Big Savings Act</strong></p><p>This bill provides a statutory safe harbor from patent infringement claims for generic or\u00a0biosimilar manufacturers that seek or obtain approval for skinny labels of their drugs.</p><p>Under current law, the Food and Drug Administration (FDA) may approve generic and\u00a0biosimilar drugs through a process known as skinny labeling, which allows a generic manufacturer to seek approval only for approved uses of the drug that are no longer protected by patents. However, in <em>GlaxoSmithKline LLC v. Teva Pharmaceuticals USA, Inc.</em>, a court held that a generic manufacturer may sometimes be liable for patent infringement when it markets skinny label generics.</p><p>The bill specifically lists the following as actions that are not considered infringement of a method of use claim in a patent under the Federal Food, Drug, and Cosmetic Act:</p><ul><li>submitting or seeking approval of a skinny label for a generic or biosimilar drug;</li><li>promoting or commercially marketing a drug with skinny labeling approved by the FDA; or</li><li>describing a drug product approved by the FDA as a generic of, or therapeutically equivalent to, the branded drug.</li></ul><p>The bill also applies the safe harbor to similar actions under the Public Health Service Act.</p>"
        },
        "title": "Skinny Labels, Big Savings Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6485.xml",
    "summary": {
      "actionDate": "2025-12-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Skinny Labels, Big Savings Act</strong></p><p>This bill provides a statutory safe harbor from patent infringement claims for generic or\u00a0biosimilar manufacturers that seek or obtain approval for skinny labels of their drugs.</p><p>Under current law, the Food and Drug Administration (FDA) may approve generic and\u00a0biosimilar drugs through a process known as skinny labeling, which allows a generic manufacturer to seek approval only for approved uses of the drug that are no longer protected by patents. However, in <em>GlaxoSmithKline LLC v. Teva Pharmaceuticals USA, Inc.</em>, a court held that a generic manufacturer may sometimes be liable for patent infringement when it markets skinny label generics.</p><p>The bill specifically lists the following as actions that are not considered infringement of a method of use claim in a patent under the Federal Food, Drug, and Cosmetic Act:</p><ul><li>submitting or seeking approval of a skinny label for a generic or biosimilar drug;</li><li>promoting or commercially marketing a drug with skinny labeling approved by the FDA; or</li><li>describing a drug product approved by the FDA as a generic of, or therapeutically equivalent to, the branded drug.</li></ul><p>The bill also applies the safe harbor to similar actions under the Public Health Service Act.</p>",
      "updateDate": "2026-02-23",
      "versionCode": "id119hr6485"
    },
    "title": "Skinny Labels, Big Savings Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Skinny Labels, Big Savings Act</strong></p><p>This bill provides a statutory safe harbor from patent infringement claims for generic or\u00a0biosimilar manufacturers that seek or obtain approval for skinny labels of their drugs.</p><p>Under current law, the Food and Drug Administration (FDA) may approve generic and\u00a0biosimilar drugs through a process known as skinny labeling, which allows a generic manufacturer to seek approval only for approved uses of the drug that are no longer protected by patents. However, in <em>GlaxoSmithKline LLC v. Teva Pharmaceuticals USA, Inc.</em>, a court held that a generic manufacturer may sometimes be liable for patent infringement when it markets skinny label generics.</p><p>The bill specifically lists the following as actions that are not considered infringement of a method of use claim in a patent under the Federal Food, Drug, and Cosmetic Act:</p><ul><li>submitting or seeking approval of a skinny label for a generic or biosimilar drug;</li><li>promoting or commercially marketing a drug with skinny labeling approved by the FDA; or</li><li>describing a drug product approved by the FDA as a generic of, or therapeutically equivalent to, the branded drug.</li></ul><p>The bill also applies the safe harbor to similar actions under the Public Health Service Act.</p>",
      "updateDate": "2026-02-23",
      "versionCode": "id119hr6485"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6485ih.xml"
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
      "title": "Skinny Labels, Big Savings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Skinny Labels, Big Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 35, United States Code, to provide for a safe harbor from infringement of a method of use patent relating to drugs or biological products.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:17Z"
    }
  ]
}
```
