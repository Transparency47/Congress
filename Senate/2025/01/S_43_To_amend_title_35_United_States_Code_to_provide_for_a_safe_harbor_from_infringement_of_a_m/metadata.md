# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/43?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/43
- Title: Skinny Labels, Big Savings Act
- Congress: 119
- Bill type: S
- Bill number: 43
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-12-18T16:16:20Z
- Update date including text: 2025-12-18T16:16:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/43",
    "number": "43",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Skinny Labels, Big Savings Act",
    "type": "S",
    "updateDate": "2025-12-18T16:16:20Z",
    "updateDateIncludingText": "2025-12-18T16:16:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-01-09T19:38:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VT"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AR"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s43is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 43\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Hickenlooper (for himself, Mr. Welch , Mr. Cotton , and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 35, United States Code, to provide for a safe harbor from infringement of a method of use patent relating to drugs or biological products.\n#### 1. Short title\nThis Act may be cited as the Skinny Labels, Big Savings Act .\n#### 2. Safe harbor from infringement of a method of use patent\n##### (a) In general\nSection 271 of title 35, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (h) and (i) as subsections (k) and (l), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) (1) The following shall not be acts of direct, induced, or contributory infringement of a method of use claim in a patent included in the list described in section 505(j)(7) or section 512(n)(4) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(7) , 360b(n)(4)) in an action or counterclaim under this section: (A) Submitting or seeking approval of an application under section 505(j) or section 512(b)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j) , 360b(b)(2)), or submitting or seeking approval of an application described in section 505(b)(2) of such Act ( 21 U.S.C. 355(b)(2) ), provided that such application includes a statement under, as applicable, section 505(j)(2)(A)(viii), section 512(n)(1)(I), or section 505(b)(2)(B) of such Act ( 21 U.S.C. 355(j)(2)(A)(viii) , 360b(n)(1)(I), 355(b)(2)(B)) for the method of use claims in the patent with the labeling proposed in such application. (B) Promoting or commercially marketing a drug product with the labeling approved in an application described in subparagraph (A). (C) Describing a drug product approved in an application submitted under section 505(j) or section 512(b)(2) of such Act ( 21 U.S.C. 355(j) , 360b(b)(2)) or approved in an application described in section 505(b)(2) of such Act ( 21 U.S.C. 355(b)(2) ) as a generic of, or therapeutically equivalent to, the listed drug referenced in such application, as applicable. (2) Subparagraphs (A) through (C) of paragraph (1) shall apply only if the labeling, promotion, or commercial marketing does not reference the condition or conditions of use claimed in the patent that was identified by the patent owner or assignee to the Secretary under section 314.53 of title 21, Code of Federal Regulations (or a successor regulation) and that was subject to the statement under section 505(j)(2)(A)(viii), section 512(n)(1)(I), or section 505(b)(2)(B) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(2)(A)(viii) , 360b(n)(1)(I), 355(b)(2)(B)), as applicable. (i) (1) The following shall not be acts of direct, induced, or contributory infringement of a patent claim covering a method of using the reference product in an action or counterclaim under this section: (A) Submitting or seeking approval of an application under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ). (B) Describing a biological product approved in an application described in subparagraph (A) as biosimilar to, or interchangeable with, the reference product, as applicable, with the labeling approved in such application, when the biological product has not been approved for the patented condition or conditions of use. (C) Promoting or commercially marketing a biological product with the labeling approved in an application described in subparagraph (A). (2) Subparagraphs (A) through (C) of paragraph (1) shall apply only if the labeling, promotion, or commercial marketing does not reference the condition or conditions of use claimed in the patent and specifically reflected in the prescribing information. (j) As used in this section: (1) The terms biological product , biosimilar , interchangeable , and reference product have the meanings given such terms in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) ). (2) The term commercial marketing has the meaning given such term in section 314.3 of title 21, Code of Federal Regulations (or a successor regulation). (3) The term labeling has the meaning given such term in section 201(m) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(m) ). (4) The term promoting \u2014 (A) is within the meaning of the term used in section 202.1 of title 21, Code of Federal Regulations (or a successor regulation); and (B) includes the use of promotional labeling and advertising, as described in paragraphs (1) and (2) of section 202.1(l) of title 21, Code of Federal Regulations (or successor regulations). .\n##### (b) Application\nThis Act and the amendments made by this Act shall apply to\u2014\n**(1)**\nconduct that occurs before, on, or after the date of enactment of this Act; and\n**(2)**\nall judicial or other proceedings pending as of such date of enactment.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-05",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6485",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Skinny Labels, Big Savings Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-10T20:03:12Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s43",
          "measure-number": "43",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s43v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Skinny Labels, Big Savings Act</strong></p><p>This bill provides a statutory safe harbor from patent infringement claims for generic or\u00a0biosimilar manufacturers that seek or obtain approval for skinny labels of their drugs.</p><p>Under current law, the Food and Drug Administration (FDA) may approve generic and\u00a0biosimilar drugs through a process known as skinny labeling, which allows a generic manufacturer to seek approval only for approved uses of the drug that are no longer protected by patents. However, in <em>GlaxoSmithKline LLC v. Teva Pharmaceuticals USA, Inc.</em>, a court held that a generic manufacturer may sometimes be liable for patent infringement when it markets skinny label generics.</p><p>The bill specifically lists the following as actions that are not considered infringement of a method of use claim in a patent under the Federal Food, Drug, and Cosmetic Act:</p><ul><li>submitting or seeking approval of a skinny label for a generic or biosimilar drug;</li><li>promoting or commercially marketing a drug with skinny labeling approved by the FDA; or</li><li>describing a drug product approved by the FDA as a generic of, or therapeutically equivalent to, the branded drug.</li></ul><p>The bill also applies the safe harbor to similar actions under the Public Health Service Act.</p>"
        },
        "title": "Skinny Labels, Big Savings Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s43.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Skinny Labels, Big Savings Act</strong></p><p>This bill provides a statutory safe harbor from patent infringement claims for generic or\u00a0biosimilar manufacturers that seek or obtain approval for skinny labels of their drugs.</p><p>Under current law, the Food and Drug Administration (FDA) may approve generic and\u00a0biosimilar drugs through a process known as skinny labeling, which allows a generic manufacturer to seek approval only for approved uses of the drug that are no longer protected by patents. However, in <em>GlaxoSmithKline LLC v. Teva Pharmaceuticals USA, Inc.</em>, a court held that a generic manufacturer may sometimes be liable for patent infringement when it markets skinny label generics.</p><p>The bill specifically lists the following as actions that are not considered infringement of a method of use claim in a patent under the Federal Food, Drug, and Cosmetic Act:</p><ul><li>submitting or seeking approval of a skinny label for a generic or biosimilar drug;</li><li>promoting or commercially marketing a drug with skinny labeling approved by the FDA; or</li><li>describing a drug product approved by the FDA as a generic of, or therapeutically equivalent to, the branded drug.</li></ul><p>The bill also applies the safe harbor to similar actions under the Public Health Service Act.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s43"
    },
    "title": "Skinny Labels, Big Savings Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Skinny Labels, Big Savings Act</strong></p><p>This bill provides a statutory safe harbor from patent infringement claims for generic or\u00a0biosimilar manufacturers that seek or obtain approval for skinny labels of their drugs.</p><p>Under current law, the Food and Drug Administration (FDA) may approve generic and\u00a0biosimilar drugs through a process known as skinny labeling, which allows a generic manufacturer to seek approval only for approved uses of the drug that are no longer protected by patents. However, in <em>GlaxoSmithKline LLC v. Teva Pharmaceuticals USA, Inc.</em>, a court held that a generic manufacturer may sometimes be liable for patent infringement when it markets skinny label generics.</p><p>The bill specifically lists the following as actions that are not considered infringement of a method of use claim in a patent under the Federal Food, Drug, and Cosmetic Act:</p><ul><li>submitting or seeking approval of a skinny label for a generic or biosimilar drug;</li><li>promoting or commercially marketing a drug with skinny labeling approved by the FDA; or</li><li>describing a drug product approved by the FDA as a generic of, or therapeutically equivalent to, the branded drug.</li></ul><p>The bill also applies the safe harbor to similar actions under the Public Health Service Act.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s43"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s43is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-02-08T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Skinny Labels, Big Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 35, United States Code, to provide for a safe harbor from infringement of a method of use patent relating to drugs or biological products.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:27Z"
    }
  ]
}
```
