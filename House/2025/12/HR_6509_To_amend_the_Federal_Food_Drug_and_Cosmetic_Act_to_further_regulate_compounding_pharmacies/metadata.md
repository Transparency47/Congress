# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6509?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6509
- Title: SAFE Drugs Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6509
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-05-21T08:08:30Z
- Update date including text: 2026-05-21T08:08:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6509",
    "number": "6509",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "SAFE Drugs Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:30Z",
    "updateDateIncludingText": "2026-05-21T08:08:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:06:15Z",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "VA"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "WV"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "FL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "IN"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "IN"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "IN"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6509ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6509\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Yakym (for himself and Mr. Carson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to further regulate compounding pharmacies and outsourcing facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Americans from Fraudulent and Experimental Drugs Act of 2025 or the SAFE Drugs Act of 2025 .\n#### 2. Definitions relating to compounding of drug products\nSection 503A(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353a(b) ) is amended\u2014\n**(1)**\nby amending paragraph (1)(D) to read as follows:\n(D) does not, more than 20 times in a single month, compound any drug product that is essentially a copy of a commercially available drug product. ; and\n**(2)**\nby amending paragraph (2) to read as follows:\n(2) Definitions (A) For purposes of paragraph (1)(D), the term essentially a copy of a commercially available drug product means any drug product\u2014 (i) that contains any active ingredient found in a commercially available drug product; and (ii) in which there is no change, made for an identified individual patient, which produces for that patient a significant difference, as determined by the prescribing practitioner, between the compounded drug product and the comparable commercially available drug product. (B) For purposes of subparagraph (A), the term commercially available drug product includes any drug product that\u2014 (i) is sold in the commercial marketplace in the United States and manufactured in one or more facilities required to comply with section 501(a)(2)(B); and (ii) is not included in the discontinued section of the list of products described in section 505(j)(7)(A). .\n#### 3. Reporting requirement\nSection 503A of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353a ) is amended\u2014\n**(1)**\nby redesignating subsections (d) and (e) as subsections (e) and (f), respectively; and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Reporting requirement (1) In general For calendar year 2025 and each calendar year thereafter, if a pharmacy, facility, or physician compounds, more than 20 times in a single month for patients who reside outside the State in which the compounding occurs, any drug product that contains any active ingredient found in a commercially available drug product (as defined in subsection (b)(2)(B)), such pharmacy, facility, or physician shall submit a report to the Secretary. (2) Contents Each report under paragraph (1) shall identify\u2014 (A) each type of drug product described in paragraph (1) that is compounded for a patient described in such paragraph; and (B) for each month, the total number of times each such type is so compounded. (3) Timing For any calendar year for which paragraph (1) applies, the pharmacy, facility, or physician shall submit the report under such paragraph not later than the end of such calendar year. (4) Form and manner A pharmacy, facility, or physician shall submit each report under paragraph (1) in such form and manner as the Secretary may prescribe. (5) Hospital pharmacy exclusion This subsection does not apply to the compounding of any drug products for hospital patients by a pharmacy located on the premises of the hospital. .\n#### 4. Large-scale outsourcing facilities\n##### (a) Inspections\nSection 503B(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353b(b) ) is amended by adding at the end the following:\n(6) Inspections of large-scale outsourcing facilities (A) In general In the case of a large-scale outsourcing facility, the risk-based inspections under paragraph (4) shall include\u2014 (i) an inspection prior to such facility compounding any drug product for the first time; and (ii) the reinspection of such facility not less than biennially. (B) Large-scale outsourcing facility defined For purposes of this paragraph, the term large-scale outsourcing facility means any outsourcing facility that compounds, more than 100 times in a single calendar year, any drug product. .\n##### (b) Registration and reporting requirement\nSection 510(g)(1) of such Act ( 21 U.S.C. 360(g)(1) ) is amended by inserting before the semicolon at the end the following: , except that the exemption in this paragraph shall not apply to any outsourcing facility (as defined in section 503B(d)(4)) .\n##### (c) Delayed applicability\nThe amendments made by subsections (a) and (b) apply beginning 6 months after the date of enactment of this Act.\n#### 5. Base establishment fee\nSection 744K(c)(1)(A)(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201362(c)(1)(A)(i) ) is amended by striking $15,000 and inserting a base amount deemed appropriate by the Secretary to fund activities to ensure the safety of compounded drug products .",
      "versionDate": "2025-12-09",
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
        "actionDate": "2026-02-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3794",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAFE Drugs Act of 2026",
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
        "name": "Health",
        "updateDate": "2026-01-06T15:46:18Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6509ih.xml"
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
      "title": "SAFE Drugs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Drugs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Americans from Fraudulent and Experimental Drugs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to further regulate compounding pharmacies and outsourcing facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:14Z"
    }
  ]
}
```
