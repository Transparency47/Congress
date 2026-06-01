# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1458
- Title: Adoption Tax Credit Refundability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1458
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-05T21:37:46Z
- Update date including text: 2025-12-05T21:37:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1458",
    "number": "1458",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Adoption Tax Credit Refundability Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:37:46Z",
    "updateDateIncludingText": "2025-12-05T21:37:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T20:11:14Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NM"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MO"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-10",
      "state": "ME"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "OK"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "SC"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "WV"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1458is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1458\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Cramer (for himself, Ms. Klobuchar , Mrs. Blackburn , Mr. Luj\u00e1n , Mr. Hawley , Mr. King , Mr. Lankford , Mr. Fetterman , Mr. Scott of South Carolina , Mr. Merkley , Mr. Van Hollen , Ms. Warren , Mr. Warner , Mr. Kaine , Ms. Duckworth , Ms. Rosen , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for a refundable adoption tax credit.\n#### 1. Short title\nThis Act may be cited as the Adoption Tax Credit Refundability Act of 2025 .\n#### 2. Refundable adoption tax credit\n##### (a) Credit made refundable\n**(1) Credit moved to subpart relating to refundable credits**\nThe Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby redesignating section 23 as section 36C, and\n**(B)**\nby moving section 36C (as so redesignated) from subpart A of part IV of subchapter A of chapter 1 to the location immediately before section 37 in subpart C of part IV of subchapter A of chapter 1.\n**(2) Conforming Amendments**\n**(A)**\nSection 25(e)(1)(C) of such Code is amended by striking sections 23 and 25D and inserting section 25D .\n**(B)**\nSection 36C of such Code, as so redesignated, is amended\u2014\n**(i)**\nin subsection (b)(2)(A), by striking (determined without regard to subsection (c)) ,\n**(ii)**\nby striking subsection (c), and\n**(iii)**\nby redesignating subsections (d) through (i) as subsections (c) through (h), respectively.\n**(C)**\nSection 137 of such Code is amended\u2014\n**(i)**\nin subsection (d), by striking section 23(d) and inserting section 36C(c) , and\n**(ii)**\nin subsection (e), by striking subsections (e), (f), and (g) of section 23 and inserting subsections (d), (e), and (f) of section 36C .\n**(D)**\nSection 1016(a)(26) of such Code is amended by striking 23(g) and inserting 36C(f) .\n**(E)**\nSection 6211(b)(4)(A) of such Code is amended by inserting 36C, after 36B, .\n**(F)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by striking the item relating to section 23.\n**(G)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n**(H)**\nParagraph (33) of section 471(a) of the Social Security Act ( 42 U.S.C. 671(a) ) is amended by striking section 23 and inserting section 36C .\n**(I)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Adoption expenses.\n##### (b) Third-Party affidavits\nSection 36C(h) of the Internal Revenue Code of 1986, as redesignated and moved by subsection (a), is amended\u2014\n**(1)**\nby striking such regulations and inserting such regulations and guidance ,\n**(2)**\nby striking including regulations which treat and inserting\nincluding regulations and guidance which\u2014 (1) treat ,\n**(3)**\nby striking the period at the end and inserting , and , and\n**(4)**\nby adding at the end the following:\n(2) provide for a standardized third-party affidavit for purposes of verifying a legal adoption\u2014 (A) of a type with respect to which qualified adoption expenses may be paid or incurred, or (B) involving a child with special needs for purposes of subsection (a)(3). .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n##### (d) Transitional rule To treat carryforward as refundable credit\nIn the case of any excess described in section 23(c) of the Internal Revenue Code of 1986 with respect to any taxpayer for the taxable year which precedes the first taxable year to which the amendments made by this section apply, such excess shall be added to the credit allowable under section 36C(a) of such Code with respect to such taxpayer for such first taxable year.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2833",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Adoption Tax Credit Refundability Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-12T20:00:44Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1458is.xml"
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
      "title": "Adoption Tax Credit Refundability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Adoption Tax Credit Refundability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide for a refundable adoption tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:40Z"
    }
  ]
}
```
