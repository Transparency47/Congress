# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4236
- Title: American Seafood Competitiveness Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4236
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-15T01:25:25Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4236",
    "number": "4236",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "American Seafood Competitiveness Act of 2026",
    "type": "S",
    "updateDate": "2026-04-15T01:25:25Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T18:39:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-26",
      "state": "ME"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "AK"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4236is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4236\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Ms. Murkowski (for herself, Mr. King , Mr. Sullivan , Mr. Merkley , and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to expand eligibility of Department of Agriculture loans and grants for fishing and mariculture businesses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Seafood Competitiveness Act of 2026 .\n#### 2. Department of Agriculture loans and grants for fishing and mariculture businesses\n##### (a) Definitions of farmer and farming\nSection 343(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking farming. and inserting farming, commercial fishing, or fish processing. ;\n**(2)**\nin paragraph (2), by striking farming. and inserting farming, commercial fishing, and fish processing. ; and\n**(3)**\nby adding at the end the following:\n(14) Commercial fishing The term commercial fishing means fishing (as defined in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 )) in which the fish harvested, either in whole or in part, are intended to enter commerce or enter commerce through sale, barter, or trade. (15) Commercial fishing vessel The term commercial fishing vessel means a fishing vessel and a fish processing vessel (as those terms are defined in section 2101 of title 46, United States Code). (16) Fish The term fish has the meaning given the term in section 2101 of title 46, United States Code. (17) Fish processing The term fish processing means the processing of fish for commercial use or consumption. (18) Fish processing facility The term fish processing facility means a facility or vessel, boat, ship, or other craft used or equipped for fish processing. .\n##### (b) Farm ownership loans\n**(1) Eligibility**\nSection 302(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1922(a) ) is amended by adding at the end the following:\n(3) Eligibility of wild-caught fish and shellfish Notwithstanding any other provision of this Act, for purposes of direct and guaranteed farm loans under this subtitle\u2014 (A) the terms farmer and rancher shall include an individual or entity engaged in commercial fishing or fish processing; and (B) the terms farm and ranch shall include\u2014 (i) a commercial fishing vessel; and (ii) a fish processing facility. .\n**(2) Purposes**\nSection 303(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1923(a) ) is amended by adding at the end the following:\n(3) Commercial fishery participants; fish processors (A) Commercial fishery participants An individual or entity engaged in commercial fishing may only use a direct or guaranteed loan under this subtitle for\u2014 (i) acquiring a commercial fishing permit; (ii) acquiring a commercial fishing vessel; and (iii) making capital improvements to a commercial fishing vessel. (B) Fish processors An individual or entity engaged in fish processing may use a direct or guaranteed loan under this subtitle for acquiring or making capital improvements to a fish processing facility. .\n##### (c) Farm operating loans\n**(1) Eligibility**\nSection 311(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1941(a) ) is amended by adding at the end the following:\n(3) Eligibility of wild-caught fish and shellfish Notwithstanding any other provision of this Act, for purposes of direct and guaranteed farm loans under this subtitle\u2014 (A) the terms farmer and rancher shall include an individual or entity engaged in commercial fishing or fish processing; and (B) the terms farm and ranch shall include\u2014 (i) a commercial fishing vessel; and (ii) a fish processing facility. .\n**(2) Purposes**\nSection 312 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1942 ) is amended by adding at the end the following:\n(f) Commercial fishery participants; fish processors (1) Commercial fishery participants An individual or entity engaged in commercial fishing may only use a direct or guaranteed loan under this subtitle for the costs associated with operating and maintaining a commercial fishing vessel. (2) Fish processors An individual or entity engaged in fish processing may use a direct or guaranteed loan under this subtitle for the costs associated with operating and maintaining a fish processing facility. .\n##### (d) Local agriculture market program\n**(1) Farmers\u2019 markets and local food promotion program**\nSection 210A(d)(6) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c(d)(6) ) is amended by adding at the end the following:\n(F) Eligibility of wild-caught fish and shellfish For purposes of this paragraph\u2014 (i) an agricultural commodity or product described in subsection (a)(12) shall include fish (as defined in section 2101 of title 46, United States Code) that is caught, taken, or harvested from the wild; and (ii) the eligible activities described in paragraph (2) shall include domestic seafood marketing. .\n**(2) Waiver of matching funds requirements**\nSection 210A(i) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c(i) ) is amended by adding at the end the following:\n(4) Waiver of matching funds requirements The Secretary may waive a requirement for a recipient of a grant under this section to provide matching funds, or reduce the amount of matching funds required to be provided, if the recipient is engaged in commercial fishing or fish processing (as those terms are defined in section 343(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a) )). .\n##### (e) Implementation and coordination\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture shall take such actions as are necessary to ensure the successful and effective integration of individuals and entities in the commercial fishing industry, including those engaged in commercial fishing or fish processing (as those terms are defined in section 343(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a) )), into each program of the Department of Agriculture for which those individuals and entities are made eligible under the amendments made by this section.\n**(2) Technical assistance and guidance**\nIn carrying out paragraph (1), the Secretary of Agriculture shall\u2014\n**(A)**\nprovide outreach and technical assistance to participants in the commercial fishing industry, including through cooperative agreements and public-private and other partnerships, to promote awareness of and access to relevant programs;\n**(B)**\nprovide guidance and training to relevant agency personnel of the Department of Agriculture, including through cooperative agreements and public-private and other partnerships, to ensure program services are effectively delivered to the commercial fishing industry; and\n**(C)**\ncoordinate, as appropriate, with the National Oceanic and Atmospheric Administration and other relevant Federal and State agencies to implement the amendments made by this section.\n#### 3. Extension of credit to businesses providing services to producers or harvesters of aquatic products\n##### (a) Farm credit banks\n**(1) Eligibility for credit and financial services**\nSection 1.9 of the Farm Credit Act of 1971 ( 12 U.S.C. 2017 ) is amended\u2014\n**(A)**\nin paragraph (2), by striking or at the end;\n**(B)**\nby redesignating paragraph (3) as paragraph (4); and\n**(C)**\nby inserting after paragraph (2) the following:\n(3) persons furnishing to producers or harvesters of aquatic products services directly related to their operating needs; or .\n**(2) Purposes for extensions of credit**\nSection 1.11(c)(1) of the Farm Credit Act of 1971 ( 12 U.S.C. 2019(c)(1) ) is amended by inserting and to persons furnishing services directly related to the operating needs of producers or harvesters of aquatic products after needs .\n##### (b) Production credit associations\nSection 2.4(a) of the Farm Credit Act of 1971 ( 12 U.S.C. 2075(a) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(4) persons furnishing to producers or harvesters of aquatic products services directly related to their operating needs. .",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-15T01:25:25Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4236is.xml"
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
      "title": "American Seafood Competitiveness Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Seafood Competitiveness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Farm and Rural Development Act to expand eligibility of Department of Agriculture loans and grants for fishing and mariculture businesses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:25Z"
    }
  ]
}
```
