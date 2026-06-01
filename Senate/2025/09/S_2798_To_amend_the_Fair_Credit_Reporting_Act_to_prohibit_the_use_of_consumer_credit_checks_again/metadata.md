# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2798?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2798
- Title: Equal Employment for All Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2798
- Origin chamber: Senate
- Introduced date: 2025-09-15
- Update date: 2025-12-05T21:41:28Z
- Update date including text: 2025-12-05T21:41:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in Senate
- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-15: Introduced in Senate

## Actions

- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2798",
    "number": "2798",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Equal Employment for All Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:41:28Z",
    "updateDateIncludingText": "2025-12-05T21:41:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-15",
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
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T19:27:49Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "PA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-15",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "HI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "OR"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "IL"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "OR"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2798is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2798\nIN THE SENATE OF THE UNITED STATES\nSeptember 15, 2025 Ms. Warren (for herself, Mr. Markey , Mr. Blumenthal , Mr. Fetterman , Mr. Booker , Mr. Sanders , Ms. Hirono , Mr. Murphy , Mr. Merkley , Mr. Durbin , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Fair Credit Reporting Act to prohibit the use of consumer credit checks against prospective and current employees for the purposes of making adverse employment decisions.\n#### 1. Short title\nThis Act may be cited as the Equal Employment for All Act of 2025 .\n#### 2. Use of credit checks prohibited for employment purposes\n##### (a) Prohibition for employment and adverse action\nSection 604 of the Fair Credit Reporting Act ( 15 U.S.C. 1681b ) is amended\u2014\n**(1)**\nin subsection (a)(3)(B), by inserting within the restrictions set forth in subsection (b) after purposes ;\n**(2)**\nby redesignating subsections (b) through (g) as subsections (c) through (h), respectively;\n**(3)**\nby inserting after subsection (a) the following new subsection:\n(b) Use of certain consumer report prohibited for employment purposes or adverse action (1) General prohibition Except as provided in paragraph (3), a person, including a prospective employer or current employer, may not use a consumer report or investigative consumer report, or cause a consumer report or investigative consumer report to be procured, with respect to any consumer where any information contained in the report bears on the creditworthiness, credit standing, or credit capacity of the consumer\u2014 (A) for employment purposes; or (B) for making an adverse action, as described in section 603(k)(1)(B)(ii). (2) Source of consumer report irrelevant The prohibition described in paragraph (1) shall apply even if the consumer consents or otherwise authorizes the procurement or use of a consumer report for employment purposes or in connection with an adverse action with respect to the consumer. (3) Exceptions Notwithstanding the prohibitions set forth in this subsection, and consistent with the other sections of this Act, an employer may use a consumer report with respect to a consumer in the following situations: (A) When the consumer applies for, or currently holds, employment that requires national security clearance. (B) When otherwise required by law. (4) Effect on disclosure and notification requirements The exceptions described in paragraph (3) shall have no effect upon the other requirements of this Act, including requirements in regards to disclosure and notification to a consumer when permissibly using a consumer report for employment purposes or for making an adverse action against the consumer. ; and\n**(4)**\nin subsection (c), as so redesignated\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby amending the paragraph heading to read as follows: Use of consumer reports for employment purposes ;\n**(ii)**\nin subparagraph (A), by redesignating clauses (i) and (ii) as subclauses (I) and (II), respectively, and by moving such subclauses two ems to the right;\n**(iii)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and by moving such clauses two ems to the right;\n**(iv)**\nby striking the period at the end of clause (ii) (as so redesignated) and inserting ; and ;\n**(v)**\nby striking agency may furnish and inserting\nagency\u2014 (A) may furnish ; and\n**(vi)**\nby adding at the end the following new subparagraph:\n(B) except as provided in paragraph (5), may not furnish a consumer report with respect to any consumer in which any information contained in the report bears on the consumer\u2019s creditworthiness, credit standing, or credit capacity to an employer if the employer seeks to use such information in a denial of employment or any other decision made for employment purposes. ; and\n**(B)**\nby adding at the end the following new paragraph:\n(5) Requirements for consumer reports bearing on the consumer\u2019s creditworthiness, credit standing, or credit capacity (A) Exceptions An employer may use a consumer report with respect to any consumer in which any information contained in the report bears on the consumer\u2019s creditworthiness, credit standing, or credit capacity in a decision made for employment purposes or before taking an adverse action for employment purposes only if the consumer authorizes the procurement of the report as described in paragraph (2)(A)(ii) and\u2014 (i) the consumer applies for, or currently holds, employment that requires the consumer to be eligible for access to classified information; or (ii) when otherwise required by law. (B) Limitation A person who seeks to obtain or use a consumer report with respect to any consumer in which any information contained in the report bears on the consumer\u2019s creditworthiness, credit standing, or credit capacity may not deny employment to the consumer or make any other decision for employment purposes with respect to the consumer because the consumer has not authorized the procurement of the report as described in paragraph (2)(A)(ii). .\n##### (b) Conforming amendments and cross references\nThe Fair Credit Reporting Act is further amended as follows:\n**(1)**\nIn section 603 ( 15 U.S.C. 1681a )\u2014\n**(A)**\nin subsection (d)(3), by striking 604(g)(3) and inserting 604(h)(3) ; and\n**(B)**\nin subsection (o), by striking A and inserting Subject to the restrictions set forth in subsection 604(b), a .\n**(2)**\nIn section 604 ( 15 U.S.C. 1681b )\u2014\n**(A)**\nin subsection (a), by striking subsection (c) and inserting subsection (d) ;\n**(B)**\nin subsection (c), as redesignated by subsection (a)(2) of this section\u2014\n**(i)**\nin paragraph (2)(A), by inserting and subject to the restrictions set forth in subsection (b) after subparagraph (B) ; and\n**(ii)**\nin paragraph (3)(A), by inserting and subject to the restrictions set forth in subsection (b) after subparagraph (B) ;\n**(C)**\nin subsection (d)(1), as redesignated by subsection (a)(2) of this section, by striking subsection (e) in both places that term appears and inserting subsection (f) ; and\n**(D)**\nin subsection (f), as redesignated by subsection (a)(2) of this section\u2014\n**(i)**\nin paragraph (1), by striking subsection (c)(1)(B) and inserting subsection (d)(1)(B) ; and\n**(ii)**\nin paragraph (5), by striking subsection (c)(1)(B) and inserting subsection (d)(1)(B) .\n**(3)**\nIn section 607(e)(3)(A) ( 15 U.S.C. 1681e(e)(3)(A) ), by striking 604(b)(4)(E)(i) and inserting 604(c)(4)(E)(i) .\n**(4)**\nIn section 609 ( 15 U.S.C. 1681g )\u2014\n**(A)**\nin subsection (a)(3)(C)(i), by striking 604(b)(4)(E)(i) and inserting 604(c)(4)(E)(i) ; and\n**(B)**\nin subsection (a)(3)(C)(ii), by striking 604(b)(4)(A) and inserting 604(c)(4)(A) .\n**(5)**\nIn section 613(b) ( 15 U.S.C. 1681k(b) ) by striking section 604(b)(4)(A) and inserting section 604(c)(4)(A) .\n**(6)**\nIn section 615 ( 15 U.S.C. 1681m )\u2014\n**(A)**\nin subsection (d)(1), by striking section 604(c)(1)(B) and inserting section 604(d)(1)(B) ;\n**(B)**\nin subsection (d)(1)(E), by striking section 604(e) and inserting section 604(f) ; and\n**(C)**\nin subsection (d)(2)(A), by striking section 604(e) and inserting section 604(f) .",
      "versionDate": "2025-09-15",
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
        "actionDate": "2025-09-15",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "5354",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Equal Employment for All Act of 2025",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-29T13:31:10Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2798is.xml"
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
      "title": "Equal Employment for All Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T11:03:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Equal Employment for All Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Credit Reporting Act to prohibit the use of consumer credit checks against prospective and current employees for the purposes of making adverse employment decisions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:22Z"
    }
  ]
}
```
