# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2761?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2761
- Title: RESULTS Act
- Congress: 119
- Bill type: S
- Bill number: 2761
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2026-05-12T11:03:32Z
- Update date including text: 2026-05-12T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2761",
    "number": "2761",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "RESULTS Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:32Z",
    "updateDateIncludingText": "2026-05-12T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
            "date": "2025-09-10T20:20:57Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-10T20:20:57Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "GA"
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
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "VT"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "KS"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "IN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "UT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NH"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "TN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "MT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2761is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2761\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Tillis (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide long-term stability for Medicare beneficiary access to clinical diagnostic laboratory tests by improving the accuracy of, and feasibility of data collection for, the private payor-based fee schedule payment rates applied under the Medicare program for such tests, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reforming and Enhancing Sustainable Updates to Laboratory Testing Services Act of 2025 or the RESULTS Act .\n#### 2. Improving the accuracy and data collection feasibility of the private payor-based Medicare payment rates for clinical diagnostic laboratory tests\n##### (a) Acquiring data for widely available non-Advanced diagnostic laboratory tests from a qualifying comprehensive claims database of an independent national nonprofit entity\nSection 1834A(a) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking requirements .\u2014Subject to subparagraph (B) and inserting\nrequirements .\u2014 (i) In general Subject to subparagraph (B) and except as provided for in clause (ii) ;\n**(ii)**\nin clause (i), as added by clause (i) of this subparagraph\u2014\n**(I)**\nby striking paragraph (2) and inserting paragraph (2)(A) ;\n**(II)**\nby inserting , in accordance with the provisions of this section, before report to the Secretary ;\n**(III)**\nby striking applicable information (as defined in paragraph (3)) for a data collection period (as defined in paragraph (4)) and inserting\napplicable information (as defined in paragraph (3))\u2014 (I) for a data collection period (as defined in paragraph (4)) beginning before January 1, 2027, ;\n**(IV)**\nby striking the period at the end and inserting ; and ; and\n**(V)**\nby adding at the end the following new subclause:\n(II) for a data collection period beginning on or after January 1, 2027, for each clinical diagnostic laboratory test for which final payment is made under this part to the laboratory during such period. ; and\n**(iii)**\nby adding at the end the following new clause;\n(ii) Collection and submission of data (I) In general With respect to data collection periods for reporting periods beginning on or after January 1, 2028, and for purposes of this section, in the case of a widely available non-ADLT clinical diagnostic laboratory test (as defined in paragraph (2)(E)), the Secretary shall collect and use applicable information from a qualifying comprehensive claims database (as defined in paragraph (2)(C)) of a qualifying independent claims data entity (as defined in paragraph (2)(D)) with which the Secretary has in effect a contract under subclause (II) for each such test furnished during the respective data collection period and for which final payment is made under this part during the year in which such data collection period occurs. (II) Contract with qualifying independent claims data entity for access to applicable information As soon as practicable after the date of enactment of this clause, the Secretary shall identify and enter into a contract with a qualifying independent claims data entity for the purpose of, with respect to widely available non-ADLT clinical diagnostic laboratory tests furnished during a data collection period, such entity reporting to the Secretary applicable information from a qualifying comprehensive claims database of the entity for such tests for which final payment is made under this part during the year in which such data collection period occurs and for which there is applicable information within such database for such period. .\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking 2025 and inserting 2027 ;\n**(ii)**\nin clause (ii), by striking beginning January 1, 2026, and ending March 31, 2026 and inserting beginning January 1, 2028, and ending March 31, 2028 ; and\n**(iii)**\nin clause (iii), by striking three years and inserting 4 years ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking Definition of applicable laboratory .\u2014In this section, the term applicable laboratory means and inserting Definitions .\u2014In this section:\n(A) Applicable laboratory (i) Reporting periods before 2028 With respect to reporting periods beginning before January 1, 2028, the term applicable laboratory means ;\n**(B)**\nin subparagraph (A), as inserted by subparagraph (A) of this paragraph\u2014\n**(i)**\nin clause (i), in the second sentence, by striking paragraph and inserting clause ; and\n**(ii)**\nby adding at the end the following new clause:\n(ii) Reporting periods beginning during 2028 and subsequent years With respect to reporting periods beginning on or after January 1, 2028, the term applicable laboratory shall have the meaning given such term in section 414.502 of title 42, Code of Federal Regulations, as in effect on May 1, 2025, except without application of paragraph (3) of such section. ; and\n**(C)**\nby adding at the end the following new subparagraphs:\n(B) Non-widely available non-ADLT clinical diagnostic laboratory test The term non-widely available non-ADLT clinical diagnostic laboratory test means, with respect to a reporting period, a clinical diagnostic laboratory test that is not an advanced diagnostic laboratory test and that is not described in subparagraph (E). (C) Qualifying independent claims data entity The term qualifying independent claims data entity means an entity that satisfies each of the following criteria: (i) The entity is a national nonprofit organization that is not affiliated with any Government agency, insurance issuer, group health plan, provider of services or supplier, or other organization in the health care sector. (ii) The entity collects data and maintains a qualifying comprehensive claims database (as defined in subparagraph (D)). (iii) The entity is certified by the Secretary to be a qualified entity (as defined in paragraph (2) of section 1874(e)) with respect to having access to data described in paragraph (3) of such section. (iv) The entity, with respect to all data included in the qualifying comprehensive claims database of the entity, complies with all applicable Federal and State privacy and security requirements, including HIPAA privacy and security law (as defined in section 3009 of the Public Health Service Act). (v) The entity applies quality assurance processes to validate all data that is included in the qualifying comprehensive claims database of the entity, including comprehensive statistical testing. (D) Qualifying comprehensive claims database The term qualifying comprehensive claims database means an independent database of private payor claims data, which\u2014 (i) includes at least 50,000,000,000 claims from more than 50 private payors and claims administrators; (ii) is a statistically significant repository of claims data that is representative for all 50 States and the District of Columbia; (iii) includes only data that is validated by quality assurance processes, including comprehensive statistical testing; (iv) complies with all applicable Federal and State privacy and security requirements, as described in subparagraph (C)(iv); (v) provides for version control of claims to enable the collation and submission, for purposes of this section, of only claims representative of final payment amounts; and (vi) includes claims data with respect to widely available non-ADLT clinical diagnostic laboratory tests. (E) Widely available non-ADLT clinical diagnostic laboratory test The term widely available non-ADLT clinical diagnostic laboratory test means, with respect to a reporting period, a clinical diagnostic laboratory test that is not an advanced diagnostic laboratory test and for which, during the first 6 months of the year immediately preceding the data collection period for such reporting period, the number of providers of services and suppliers receiving payments under this section (as determined by the Secretary using the national provider identifier of the provider of services or supplier on the claim submitted for payment under this part for such test) exceeds 100. ;\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nby inserting final after The ; and\n**(B)**\nby inserting or from a qualifying comprehensive claims database pursuant to paragraph (1)(A)(ii) after reported by a laboratory under this subsection ;\n**(4)**\nin paragraph (6)\u2014\n**(A)**\nby inserting (or, with respect to a widely available non-ADLT clinical diagnostic laboratory test, the qualifying comprehensive claims database of the qualifying independent claims data entity with a contract under paragraph (1)(A)(ii)) after In the case where an applicable laboratory ;\n**(B)**\nby striking payment rate each place it appears and inserting final payment rate ;\n**(C)**\nby inserting (and such different payment rates do not relate to the same claim) after for the same payor for the same test ; and\n**(D)**\nby inserting or qualifying independent claims data entity, as applicable, after the applicable laboratory ;\n**(5)**\nin paragraph (9)(A), by inserting required to be reported by such laboratory after in reporting information ;\n**(6)**\nin paragraph (10)\u2014\n**(A)**\nby striking by a laboratory after information disclosed ; and\n**(B)**\nby inserting by a laboratory or the qualifying independent claims data entity with a contract under paragraph (1)(A)(ii) after under this subsection ; and\n**(7)**\nin paragraph (12)\u2014\n**(A)**\nby striking Regulations .\u2014Not later than June 30, 2015, and inserting\nRegulations .\u2014 (A) For data collection periods before 2027 Not later than June 30, 2015, for data collection periods beginning before January 1, 2027, ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B) For data collection periods beginning with 2027 Not later than December 31, 2026, the Secretary shall establish through notice and comment rulemaking parameters for data collection periods beginning on or after January 1, 2027. .\n##### (b) Incorporating data collection improvements into private payor-Based Medicare payment rates for clinical diagnostic laboratory tests that are not advanced diagnostic laboratory tests\n**(1) Calculation of weighted median of private payor-based rates**\nSection 1834A(b)(2) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b)(2) ) is amended\u2014\n**(A)**\nby inserting and, in the case of widely available non-ADLT clinical diagnostic laboratory tests, with respect to data collection periods for reporting periods beginning on or after January 1, 2028, for each such test furnished by an applicable laboratory with respect to which there is applicable information made available to the Secretary pursuant to paragraph (1)(A)(ii) of such subsection after under subsection (a) for a data collection period ; and\n**(B)**\nby inserting final before payment rates reported .\n**(2) Default adjustment in cases of widely available non-ADLT clinical diagnostic laboratory tests for periods for which there is no contract with a qualifying independent claims entity or no applicable information in the qualifying comprehensive claims database**\nSection 1834A(b) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by striking paragraph (3) and inserting paragraphs (3) and (6) ; and\n**(B)**\nby adding at the end the following new paragraph:\n(6) Default payment for widely available non-ADLT clinical diagnostic laboratory tests for periods for which there is no contract with an independent entity or with respect to which there is no data (A) In general With respect to data collection periods for reporting periods beginning on or after January 1, 2028, in the case of a widely available non-ADLT clinical diagnostic laboratory test with respect to which subsection (c) does not apply, if a circumstance described in subparagraph (B) applies with respect to such a reporting period and such a clinical diagnostic laboratory test, payment for such test under this section for a year beginning during the qualified rate period described in subparagraph (C), shall be equal to the amount of payment for such clinical diagnostic laboratory test under this section for the previous year, increased by the percentage increase in the Consumer Price Index for all urban consumers (all items; United States city average) over the previous year. (B) Circumstances described For purposes of subparagraph (A), with respect to a data collection period and a widely available non-ADLT clinical diagnostic laboratory test, the circumstances described in this subparagraph are if the Secretary\u2014 (i) is not able to enter into a contract under subsection (a)(1)(A)(ii) with a qualifying independent claims data entity with respect to such data collection period; or (ii) determines that there is no applicable information with respect to such clinical diagnostic laboratory test and data collection period in the qualifying comprehensive claims database of such qualifying independent claims data entity. (C) Qualified rate period described For purposes of subparagraph (A), the qualified rate period, with respect to a data collection period and a widely available non-ADLT clinical diagnostic test to which a circumstance described in subparagraph (B) applies, is the period\u2014 (i) beginning on the first day of the second year following the first data collection period with respect to which such circumstance applies with respect to such test; and (ii) ending with the last day of the year following the first data collection period with respect to which such circumstance no longer applies with respect to such test. .\n**(3) Payment in cases in which there is no reported applicable information for non-widely available non-ADLTs**\nSection 1834A of the Social Security Act ( 42 U.S.C. 1395m\u20131 ), is amended\u2014\n**(A)**\nin subsection (b), as amended by paragraph (2)\u2014\n**(i)**\nin paragraph (1)(A), by striking paragraphs (3) and (6) and inserting paragraphs (3), (6), and (7) ; and\n**(ii)**\nby adding at the end the following new paragraph:\n(7) Payment for non-widely available non-ADLT clinical diagnostic laboratory tests for which there is no applicable information (A) In general For determining payment under this subsection for a year in the case of a non-widely available non-ADLT clinical diagnostic laboratory test with respect to which subsection (c) does not apply, if the Secretary determines that no applicable information has been reported under subsection (a)(1)(A)(i) by any applicable laboratory for such test with respect to the most recent data collection period (beginning with data collection periods for reporting periods beginning on or after January 1, 2028), payment for such test under this section for such year shall be determined as follows: (i) In the case that a process described in subparagraph (B) was not applied pursuant to this subparagraph for determining payment for such test for a previous year with respect to such data collection period, payment for such test and year shall be determined using such a process. (ii) In the case that a process described in subparagraph (B) was applied pursuant to this subparagraph for determining payment for such test for a previous year with respect to such data collection period, payment for such test and year shall be equal to the amount of payment for such test under this section for the previous year. (B) Process described For purposes of subparagraph (A), a process described in this subparagraph, with respect to a non-widely available non-ADLT clinical diagnostic laboratory test for which there is no reported data (as described in such subparagraph) with respect to a data collection period, is\u2014 (i) cross-walking (as described in section 414.508(a) of title 42, Code of Federal Regulations, or any successor regulation) to the most appropriate clinical diagnostic laboratory test under the fee schedule under this section during that period; or (ii) if no other clinical diagnostic laboratory test is comparable to the test for which there is no reported applicable information, according to the gapfilling process described in subsection (c)(2). ; and\n**(B)**\nin subsection (c)(3), by inserting or subsection (b)(7) after under this subsection .\n**(4) Publicly available explanation of payment rates**\nSection 1834A(b) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b) ), as amended by paragraphs (2) and (3)(A), is amended by adding at the end the following new paragraph:\n(8) Explanation of payment rates In the case of a clinical diagnostic laboratory test for which payment is made under this subsection, the Secretary shall make available to the public an explanation of the payment rate for such test, including any supporting data as may be necessary for a laboratory to assess the accuracy of the calculations. .\n**(5) Technical correction clarifying period of application of market rates**\nSection 1834A(b)(4)(A) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b)(4)(A) ) is amended by striking until the year following and inserting through the year following .\n##### (c) Additional improvements To ensure updated, accurate market-Based data for clinical diagnostic laboratory tests\n**(1) Updates to applicable information to better reflect final payment rates**\nSection 1834A(a)(3) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a)(3) ) is amended\u2014\n**(A)**\nin the heading, by inserting and final payment rate after information ;\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nin the heading, by striking In general and inserting Data collection periods before January 1, 2027 ; and\n**(ii)**\nin the matter preceding clause (i)\u2014\n**(I)**\nby striking subparagraph (B) and inserting subparagraph (C) ; and\n**(II)**\nby inserting beginning before January 1, 2027 after for a data collection period ;\n**(C)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(D)**\nby inserting after subparagraph (A) the following new subparagraph:\n(B) Subsequent data collection periods In this section, subject to subparagraph (C), for a data collection period beginning on or after January 1, 2027, the term applicable information means\u2014 (i) with respect to a widely available non-ADLT clinical diagnostic laboratory test furnished during such period\u2014 (I) the final payment rate (as determined in accordance with paragraph (5) and defined in subparagraph (D)) that was paid by each private payor for the test during the year in which such period occurs; and (II) the volume, for each such payor, of such test for which final payment was made during such year; and (ii) with respect to a non-widely available non-ADLT clinical diagnostic laboratory test or an advanced diagnostic laboratory test\u2014 (I) the final payment rate (as determined in accordance with paragraph (5) and defined in subparagraph (D)) that was paid by each private payor for the test during the data collection period; and (II) the volume, for each such payor, of such test for which final payment was made during such period. ; and\n**(E)**\nby inserting after subparagraph (C), the following new subparagraph:\n(D) Final payment rate In this section, for a data collection period beginning on or after January 1, 2027, the term final payment rate \u2014 (i) means\u2014 (I) with respect to a widely available non-ADLT clinical diagnostic laboratory test furnished during a data collection period, the last payment made for a test during the year in which the data collection period occurs; and (II) with respect to a non-widely available non-ADLT clinical diagnostic laboratory test or an advanced diagnostic laboratory test paid during a data collection period, the last payment made during the data collection period; and (ii) does not include\u2014 (I) denied payments; (II) payments under appeal or under review by the private payor; (III) payments made in error; or (IV) payments that are recouped by the private payor. .\n**(2) Updating data collection periods**\nSection 1834A(a)(4)(B) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a)(4)(B) ) is amended\u2014\n**(A)**\nby striking January 1, 2019 and inserting January 1, 2027 ;\n**(B)**\nby striking June 30, 2019 and inserting June 30, 2027 ; and\n**(C)**\nby adding at the end the following new sentence: In the case of the reporting period after the reporting period described in paragraph (1)(B)(ii) and each subsequent reporting period with respect to clinical diagnostic laboratory tests that are not advanced diagnostic laboratory tests, the term data collection period means the 6-month period beginning January 1st of the year preceding the year during which such reporting period begins. .\n**(3) Ensuring data is market-based by excluding rates of Medicaid managed care organizations**\nSection 1834A(a)(8)(C) of the Social Security Act ( 42 U.S.C. 1395m\u20131(a)(8)(C) ) is amended by striking A medicaid managed care organization and inserting With respect to data collection periods for reporting periods beginning before January 1, 2028, a medicaid managed care organization. .\n**(4) Modifications to limits on payment reductions**\nSection 1834A(b)(3) of the Social Security Act ( 42 U.S.C. 1395m\u20131(b)(3) ) is amended\u2014\n**(A)**\nin subparagraph (A), by striking each of 2017 through 2028 and inserting 2017 and each subsequent year ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (ii), by striking 2025 and inserting 2028 ; and\n**(ii)**\nin clause (iii), by striking for each of 2026 through 2028, 15 percent and inserting for 2029 and each subsequent year, 5 percent ; and\n**(C)**\nin subparagraph (C)(ii), by inserting laboratory after advanced diagnostic .\n**(5) Sunsetting review limitations**\nSection 1834A(h)(1) of the Social Security Act ( 42 U.S.C. 1395m\u20131(h)(1) ) is amended by inserting before January 1, 2029 before the period at the end.",
      "versionDate": "2025-09-10",
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
        "actionDate": "2025-09-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5269",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RESULTS Act",
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
        "updateDate": "2025-09-23T16:55:12Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2761is.xml"
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
      "title": "RESULTS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RESULTS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reforming and Enhancing Sustainable Updates to Laboratory Testing Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide long-term stability for Medicare beneficiary access to clinical diagnostic laboratory tests by improving the accuracy of, and feasibility of data collection for, the private payor-based fee schedule payment rates applied under the Medicare program for such tests, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T06:03:24Z"
    }
  ]
}
```
