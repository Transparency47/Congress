# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1702?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1702
- Title: Access to Prescription Digital Therapeutics Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1702
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-12-11T12:03:16Z
- Update date including text: 2025-12-11T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1702",
    "number": "1702",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Access to Prescription Digital Therapeutics Act of 2025",
    "type": "S",
    "updateDate": "2025-12-11T12:03:16Z",
    "updateDateIncludingText": "2025-12-11T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T19:42:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NH"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NJ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1702is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1702\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mrs. Capito (for herself and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to provide for coverage of prescription digital therapeutics under such titles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Prescription Digital Therapeutics Act of 2025 .\n#### 2. Coverage and payment of prescription digital therapeutics under the Medicare program\n##### (a) Prescription digital therapeutic defined\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Prescription digital therapeutic The term prescription digital therapeutic means a product, device, internet application, or other technology that\u2014 (1) is cleared or approved under section 510(k), 513(f)(2), or 515 of the Federal Food, Drug, and Cosmetic Act; (2) has a cleared or approved indication for the prevention, management, or treatment of a medical disease, condition, or disorder; (3) primarily uses software to achieve its intended result; and (4) is a device that is exempt from section 502(f)(1) of the Federal Food, Drug, and Cosmetic Act under section 801.109 of title 21 of the Code of Federal Regulations (or any successor regulation). .\n##### (b) Coverage as medical and other health service\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(1)**\nin subparagraph (II), by striking and at the end;\n**(2)**\nin subparagraph (JJ), by adding and at the end; and\n**(3)**\nby adding at the end the following new subparagraph:\n(KK) prescription digital therapeutics furnished on or after January 1, 2026; .\n##### (c) Requirements for prescription digital therapeutics under Medicare\nPart B of the Social Security Act ( 42 U.S.C. 1395j et seq. ) is amended by inserting after section 1834A the following new section:\n1834B. Requirements for prescription digital therapeutics (a) Payment (1) In general Not later than 1 year after the date of enactment of this section, the Secretary shall establish a payment methodology for manufacturers of prescription digital therapeutics, which may consist of a one-time payment or periodic payments, as determined appropriate by the Secretary. (2) Considerations for payment methodology For purposes of establishing the payment methodology under paragraph (1), the Secretary shall consider\u2014 (A) the actual list charge of such prescription digital therapeutic; (B) the weighted median (calculated by arraying the distribution of all payment rates reported for the most recent period for which such rates were reported under subsection (c)(1) for each prescription digital therapeutic weighted by volume for each payor and each manufacturer) for such prescription digital therapeutic; (C) in the case of a prescription digital therapeutic that requires ongoing use, the amount for such ongoing use; and (D) other factors as determined by the Secretary. (b) Coding (1) In general Not later than 2 years after the date of enactment of this section, the Secretary shall establish product-specific HCPCS codes for prescription digital therapeutic covered under this title. (2) Temporary code The Secretary shall adopt temporary product-specific HCPCS codes for purposes of providing payment under this title until a permanent product-specific HCPCS code has been established under paragraph (1). (c) Manufacturer reporting (1) In general Beginning on January 1, 2026, each manufacturer of a prescription digital therapeutic covered under this title shall submit to the Secretary, at such time and in such manner as specified by the Secretary, and annually thereafter, a report describing\u2014 (A) the payment rate that was paid by each private payor for each prescription digital therapeutic during the period specified by the Secretary; (B) the volume of such prescription digital therapeutic distributed to each such payor for such period; and (C) the number of individual users of such prescription digital therapeutic for such period. (2) Treatment of discounts The payment rate reported by a manufacturer in accordance with paragraph (1)(A) shall reflect all discounts, rebates, coupons, and other price concessions, including those described in section 1847A(c)(3). (3) Civil monetary penalty (A) In general If the Secretary determines that a manufacturer has failed to report, or made a misrepresentation or omission in reporting, information under this subsection with respect to a prescription digital therapeutic, the Secretary may apply a civil money penalty in an amount of up to $10,000 per day for each failure to report or each such misrepresentation or omission. (B) Application The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil money penalty under this paragraph in the same manner as they apply to a civil money penalty or proceeding under section 1128A(a). (4) Confidentiality Information reported under this subsection shall be treated in the same manner in which information disclosed by a manufacturer or a wholesaler of a covered outpatient drug is treated under section 1927(b)(3)(D). (d) Definitions For purposes of this section: (1) Actual list charge The term actual list charge means the publicly available payment rate for a prescription digital therapeutic on the first day that such prescription digital therapeutic is available for purchase by a private payor. (2) HCPCS The term HCPCS means, with respect to an item, the code under the Healthcare Common Procedure Coding System (HCPCS) (or a successor code) for such item. (3) Manufacturer The term manufacturer has the meaning given such term by section 820.3(o) of title 21, Code of Federal Regulations (or any successor regulation). (4) Prescription digital therapeutic The term prescription digital therapeutic has the meaning given such term in section 1861(nnn). (5) Private payor The term private payor has the meaning given such term in section 1834A(a)(8). .\n#### 3. Coverage of prescription digital therapeutics under the Medicaid program\nSection 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) is amended\u2014\n**(1)**\nin paragraph (31), by striking ; and and inserting a semicolon;\n**(2)**\nby redesignating paragraph (32) as paragraph (33); and\n**(3)**\nby inserting the following paragraph after paragraph (31):\n(32) prescription digital therapeutics (as defined in section 1861(nnn)); and .",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3288",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Access to Prescription Digital Therapeutics Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-05-29T15:41:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119s1702",
          "measure-number": "1702",
          "measure-type": "s",
          "orig-publish-date": "2025-05-08",
          "originChamber": "SENATE",
          "update-date": "2025-06-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1702v00",
            "update-date": "2025-06-06"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Access to Prescription Digital Therapeutics Act of </strong><strong>2025</strong></p><p>This bill provides for Medicare and Medicaid coverage of prescription digital therapeutics (i.e., software applications that are used to prevent, manage, or treat medical conditions). The Centers for Medicare & Medicaid Services must establish a Medicare payment methodology for payments to manufacturers that takes into account certain factors (e.g., ongoing use); manufacturers must report specified information about private payors, subject to civil penalties.</p>"
        },
        "title": "Access to Prescription Digital Therapeutics Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1702.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Access to Prescription Digital Therapeutics Act of </strong><strong>2025</strong></p><p>This bill provides for Medicare and Medicaid coverage of prescription digital therapeutics (i.e., software applications that are used to prevent, manage, or treat medical conditions). The Centers for Medicare & Medicaid Services must establish a Medicare payment methodology for payments to manufacturers that takes into account certain factors (e.g., ongoing use); manufacturers must report specified information about private payors, subject to civil penalties.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119s1702"
    },
    "title": "Access to Prescription Digital Therapeutics Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Access to Prescription Digital Therapeutics Act of </strong><strong>2025</strong></p><p>This bill provides for Medicare and Medicaid coverage of prescription digital therapeutics (i.e., software applications that are used to prevent, manage, or treat medical conditions). The Centers for Medicare & Medicaid Services must establish a Medicare payment methodology for payments to manufacturers that takes into account certain factors (e.g., ongoing use); manufacturers must report specified information about private payors, subject to civil penalties.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119s1702"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1702is.xml"
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
      "title": "Access to Prescription Digital Therapeutics Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Prescription Digital Therapeutics Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XVIII and XIX of the Social Security Act to provide for coverage of prescription digital therapeutics under such titles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:46Z"
    }
  ]
}
```
