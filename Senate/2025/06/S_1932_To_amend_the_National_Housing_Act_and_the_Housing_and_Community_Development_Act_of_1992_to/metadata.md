# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1932?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1932
- Title: VALID Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1932
- Origin chamber: Senate
- Introduced date: 2025-06-03
- Update date: 2026-03-06T12:03:20Z
- Update date including text: 2026-03-06T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in Senate
- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-03: Introduced in Senate

## Actions

- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1932",
    "number": "1932",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "VALID Act of 2025",
    "type": "S",
    "updateDate": "2026-03-06T12:03:20Z",
    "updateDateIncludingText": "2026-03-06T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-03",
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
        "item": [
          {
            "date": "2025-06-03T18:47:26Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-03T18:47:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "DE"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "NE"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "WY"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "VA"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "AK"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "HI"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CO"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "KS"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1932is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1932\nIN THE SENATE OF THE UNITED STATES\nJune 3, 2025 Mr. Van Hollen (for himself and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the National Housing Act and the Housing and Community Development Act of 1992 to include information regarding VA home loans in the Informed Consumer Choice Disclosure required to be provided to prospective FHA borrowers and to require a military service question on the Uniform Residential Loan Application, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Loan Informed Disclosure Act of 2025 or VALID Act of 2025 .\n#### 2. FHA informed consumer choice disclosure\n##### (a) Inclusion of information relating to vA loans\nSubparagraph (A) of section 203(f)(2) of the National Housing Act ( 12 U.S.C. 1709(f)(2)(A) ) is amended\u2014\n**(1)**\nby inserting (i) after loan-to-value ratio ; and\n**(2)**\nby inserting before the semicolon the following: , and (ii) in connection with a loan guaranteed or insured under chapter 37 of title 38, United States Code, assuming prevailing interest rates .\n##### (b) Rule of construction\nNothing in the amendments made by subsection (a) shall be construed to require an original lender to determine whether a prospective borrower is eligible for any loan included in the notice required under section 203(f) of the National Housing Act ( 12 U.S.C. 1709(f) ).\n#### 3. Military service question\n##### (a) In general\nSubpart A of part 2 of subtitle A of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4541 et seq. ) is amended by adding at the end the following:\n1329. Uniform residential loan application Not later than 6 months after the date of enactment of this section, the Director shall require each enterprise to\u2014 (1) include a military service question on the form known as the Uniform Residential Loan Application; and (2) position the question described in paragraph (1) above the signature line of the Uniform Residential Loan Application. .\n##### (b) Rulemaking\nNot later than 6 months after the date of enactment of this Act, the Director of the Federal Housing Finance Agency shall issue a rule to carry out the amendment made by this section.",
      "versionDate": "2025-06-03",
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
        "actionDate": "2025-06-03",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "3694",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "VALID Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-06-18T14:16:57Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1932is.xml"
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
      "title": "VALID Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VALID Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VA Loan Informed Disclosure Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Housing Act and the Housing and Community Development Act of 1992 to include information regarding VA home loans in the Informed Consumer Choice Disclosure required to be provided to prospective FHA borrowers and to require a military service question on the Uniform Residential Loan Application, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:18:15Z"
    }
  ]
}
```
