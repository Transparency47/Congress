# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3794?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3794
- Title: SAFE Drugs Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3794
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-02-26T14:55:50Z
- Update date including text: 2026-02-26T14:55:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3794",
    "number": "3794",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "SAFE Drugs Act of 2026",
    "type": "S",
    "updateDate": "2026-02-26T14:55:50Z",
    "updateDateIncludingText": "2026-02-26T14:55:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T19:43:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3794is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3794\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Banks (for himself and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to further regulate compounding pharmacies and outsourcing facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Americans from Fraudulent and Experimental Drugs Act of 2026 or the SAFE Drugs Act of 2026 .\n#### 2. Definitions relating to compounding of drug products\nSection 503A(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353a(b) ) is amended\u2014\n**(1)**\nby amending paragraph (1)(D) to read as follows:\n(D) does not, more than 20 times in a single month, compound any drug product that is essentially a copy of a commercially available drug product. ; and\n**(2)**\nby amending paragraph (2) to read as follows:\n(2) Definitions (A) For purposes of paragraph (1)(D), the term essentially a copy of a commercially available drug product means any drug product\u2014 (i) that contains any active ingredient found in a commercially available drug product; and (ii) in which there is no change, made for an identified individual patient, which produces for that patient a significant difference, as determined by the prescribing practitioner, between the compounded drug product and the comparable commercially available drug product. (B) For purposes of subparagraph (A), the term commercially available drug product includes any drug product that\u2014 (i) is sold in the commercial marketplace in the United States and manufactured in one or more facilities required to comply with section 501(a)(2)(B); and (ii) is not included in the discontinued section of the list of products described in section 505(j)(7)(A). .\n#### 3. Reporting requirement\nSection 503A of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353a ) is amended\u2014\n**(1)**\nby redesignating subsections (d) and (e) as subsections (e) and (f), respectively; and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Reporting requirement (1) In general For calendar year 2025 and each calendar year thereafter, if a pharmacy, facility, or physician compounds, more than 20 times in a single month for patients who reside outside the State in which the compounding occurs, any drug product that contains any active ingredient found in a commercially available drug product (as defined in subsection (b)(2)(B)), such pharmacy, facility, or physician shall submit a report to the Secretary. (2) Contents Each report under paragraph (1) shall identify\u2014 (A) each type of drug product described in paragraph (1) that is compounded for a patient described in such paragraph; and (B) for each month, the total number of times each such type is so compounded. (3) Timing For any calendar year for which paragraph (1) applies, the pharmacy, facility, or physician shall submit the report under such paragraph not later than the end of such calendar year. (4) Form and manner A pharmacy, facility, or physician shall submit each report under paragraph (1) in such form and manner as the Secretary may prescribe. (5) Hospital pharmacy exclusion This subsection does not apply to the compounding of any drug products for hospital patients by a pharmacy located on the premises of the hospital. .\n#### 4. Large-scale outsourcing facilities\n##### (a) Inspections\nSection 503B(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353b(b) ) is amended by adding at the end the following:\n(6) Inspections of large-scale outsourcing facilities (A) In general In the case of a large-scale outsourcing facility, the risk-based inspections under paragraph (4) shall include\u2014 (i) an inspection prior to such facility compounding any drug product for the first time; and (ii) the reinspection of such facility not less than biennially. (B) Large-scale outsourcing facility defined For purposes of this paragraph, the term large-scale outsourcing facility means any outsourcing facility that compounds, more than 100 times in a single calendar year, any drug product. .\n##### (b) Registration and reporting requirement\nSection 510(g)(1) of such Act ( 21 U.S.C. 360(g)(1) ) is amended by inserting before the semicolon at the end the following: , except that the exemption in this paragraph shall not apply to any outsourcing facility (as defined in section 503B(d)(4)) .\n##### (c) Delayed applicability\nThe amendments made by subsections (a) and (b) apply beginning 6 months after the date of enactment of this Act.\n#### 5. Base establishment fee\nSection 744K(c)(1)(A)(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201362(c)(1)(A)(i) ) is amended by striking $15,000 and inserting a base amount deemed appropriate by the Secretary to fund activities to ensure the safety of compounded drug products .",
      "versionDate": "2026-02-05",
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
        "actionDate": "2025-12-09",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6509",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAFE Drugs Act of 2025",
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
        "updateDate": "2026-02-26T14:55:50Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3794is.xml"
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
      "title": "SAFE Drugs Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Drugs Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safeguarding Americans from Fraudulent and Experimental Drugs Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to further regulate compounding pharmacies and outsourcing facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:33Z"
    }
  ]
}
```
