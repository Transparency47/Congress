# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4238
- Title: DLARA
- Congress: 119
- Bill type: HR
- Bill number: 4238
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-05-21T08:07:42Z
- Update date including text: 2026-05-21T08:07:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-27 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 23 - 0.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-27 - IntroReferral: Referred to the Committee on Small Business, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 23 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4238",
    "number": "4238",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "DLARA",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:42Z",
    "updateDateIncludingText": "2026-05-21T08:07:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 23 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Small Business, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Small Business, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
        "item": [
          {
            "date": "2026-05-20T21:42:36Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-27T13:01:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-27T13:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NC"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "NC"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "MP"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "NC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "SC"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "AZ"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "NC"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "SC"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "OH"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "NC"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NE"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "AK"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "IN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4238ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4238\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Moore of North Carolina (for himself, Mr. Davis of North Carolina , Mr. Edwards , Ms. King-Hinds , Mr. Gimenez , Mr. Murphy , Mr. Donalds , Mr. Fry , Mr. Ciscomani , Mr. Rouzer , and Mr. Wilson of South Carolina ) introduced the following bill; which was referred to the Committee on Small Business , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo improve accountability in the disaster loan program of the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Loan Accountability and Reform Act or the DLARA .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nSec. 3. Definitions.\nSec. 4. Monthly disaster loan reports.\nSec. 5. Budget request relating to disaster loans.\nSec. 6. Limitations on disaster loans.\nSec. 7. GAO report on SBA disaster loan account.\nSec. 8. GAO report on disaster loan changes.\nSec. 9. SBA Inspector General review.\nSec. 10. Budget and forecasting report regarding the cost of direct disaster loans.\n#### 3. Definitions\nIn this Act\u2014\n**(1)**\nthe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively;\n**(2)**\nthe term appropriate committees of Congress means the Committee on Small Business and Entrepreneurship and the Committee on Appropriations of the Senate and the Committee on Small Business and the Committee on Appropriations of the House of Representatives; and\n**(3)**\nthe term SBA disaster loan means a direct loan authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ), other than a loan that was authorized under section 1110 of the CARES Act ( 15 U.S.C. 9009 ).\n#### 4. Monthly disaster loan reports\nSection 12091(a) of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking during the applicable period for a major disaster ; and\n**(B)**\nby striking for that major disaster ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (E), by striking how long the available funding for such loans will last and inserting the date at which available funding for such loans will reach 10 percent of the most recent appropriation and the date at which the funds will be depleted ;\n**(B)**\nin subparagraph (H), by striking and at the end;\n**(C)**\nin subparagraph (I), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(J) a summary detailing any changes to estimates or assumptions on obligations and expenditures, including data supporting these changes. ; and\n**(3)**\nby adding at the end the following:\n(3) Prohibition on official travel If the Administrator does not submit a report required to be submitted under paragraph (1) by the required date, no funds may be obligated for official travel by the Administrator until the Administrator submits the report. .\n#### 5. Budget request relating to disaster loans\nSection 1105 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(39) separate statements of\u2014 (A) the amount of appropriations requested for the fiscal year for which the budget is submitted for the cost of SBA disaster loans, the 10-year average of the cost of SBA disaster loans, and an explanation for any difference between the amount requested and the 10-year average cost; and (B) the amount of appropriations requested for the fiscal year for which the budget is submitted for the cost of COVID-EIDL loans, the 10-year average of the cost of COVID-EIDL loans, and an explanation for any difference between the amount requested and the 10-year average cost. (40) separate statements of\u2014 (A) the amount of appropriations requested for the fiscal year for which the budget is submitted for administrative costs relating to SBA disaster loans, the 10-year average of such administrative costs, and an explanation for any difference between the amount requested and the 10-year average costs; and (B) the amount of appropriations requested for the fiscal year for which the budget is submitted for administrative costs relating to COVID-EIDL loans, the 10-year average of such administrative costs, and an explanation for any difference between the amount requested and the 10-year average costs. ; and\n**(2)**\nby adding at the end the following:\n(j) In paragraphs (39) and (40) of subsection (a)\u2014 (1) the term COVID-EIDL loan means a direct loan under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) that was authorized under section 1110 of the CARES Act ( 15 U.S.C. 9009 ); and (2) the term SBA disaster loan means a direct loan authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ), other than a loan that was authorized under section 1110 of the CARES Act ( 15 U.S.C. 9009 ). .\n#### 6. Limitations on disaster loans\n##### (a) Low funding\nSection 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) is amended\u2014\n**(1)**\nby redesignating the second paragraph designated as paragraph (16), relating to statute of limitations, as added by the COVID\u201319 EIDL Fraud Statute of Limitations Act of 2022 ( Public Law 117\u2013165 ; 136 Stat. 1363), as paragraph (18); and\n**(2)**\nby inserting after paragraph (16), relating to disaster declarations in rural areas, as added by the Disaster Assistance for Rural Communities Act ( Public Law 117\u2013249 ; 136 Stat. 2350), the following:\n(17) Requirements when funding is low (A) In general Not later than 24 hours after the unobligated balance of amounts available for the cost of direct loans authorized by this subsection is less than 10 percent of the 10-year average annual cost provided in the most recent Presidential budget request required under section 1105(a)(39)(A) of title 31, United States Code, or, if unavailable, the 10-year average annual cost for the immediately preceding 10-year period of SBA disaster loans (as defined in section 1105(j) of such title), the Administrator shall notify the Committee on Appropriations and the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Appropriations and the Committee on Small Business of the House of Representatives . (B) Limitation on obligating funds During the period beginning on the first business day occurring on or after the date by which the Administrator is required to notify Congress under subparagraph (A) and ending on the date on which additional amounts are appropriated for such costs, the Administrator may limit the obligation of funds for a direct loan authorized under this subsection to the amount of such a loan for which collateral is required. (C) Authority to limit obligation of funds In carrying out the authority to enact a limitation under (B), the Administrator shall apply that limitation with respect to amounts obligated for all direct loans authorized under this subsection during the period described in subparagraph (B). (D) Requirement to disburse within 14 days If the Administrator exercises the authority under (B), the Administrator shall, not later than 14 days after the date on which additional amounts are appropriated under subparagraph (B), obligate and disburse on a regular schedule any remaining amount outstanding on a direct loan authorized under this subsection. .\n##### (b) Sunset\nEffective on the date that is 4 years after the date of enactment of this Act, section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) is amended\u2014\n**(1)**\nby striking paragraph (17); and\n**(2)**\nby redesignating paragraph (18) as paragraph (17).\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, in the event that the Administrator exercises the authority described in paragraph (17)(B) of section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ), as added by subsection (a), the Comptroller General of the United States shall submit to the appropriate committees of Congress a report assessing the actual and potential impact of the amendments made by subsection (a) during the period covered by the report.\n#### 7. GAO report on SBA disaster loan account\n##### (a) Report\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Administrator and the appropriate committees of Congress a report on\u2014\n**(1)**\nthe average weekly rate at which the Administration obligates the unobligated balance of amounts available for the cost of SBA disaster loans;\n**(2)**\nthe average amount, during the periods beginning on October 1, 2015, and ending on July 31, 2023, and beginning on July 31, 2023, and ending on the date of enactment of this Act, respectively, disbursed to a borrower each week, during the initial 12-week period in which a borrower receives amounts from an SBA disaster loan, beginning the day after the borrower accepts their loan, separated by home SBA disaster loan borrowers, business SBA disaster loan borrowers, and economic injury disaster loan borrowers; and\n**(3)**\nthe average amount of fully disbursed SBA disaster loans, originated during the period beginning on July 31, 2023, and ending on the date of enactment of this Act, with separate averages for SBA disaster loans delineated by home, business, and economic injury disaster loans.\n##### (b) Response\nNot later than 90 days after the date on which the Comptroller General of the United States submits the report under subsection (a), the Administrator shall submit to the appropriate committees of Congress a response to the report, including an implementation plan for any recommendations in the report.\n#### 8. GAO report on disaster loan changes\n##### (a) Definition\nIn this section, the term covered final rule means\u2014\n**(1)**\nthe final rule entitled Disaster Assistance Loan Program Changes to Maximum Loan Amounts and Miscellaneous Updates (88 Fed. Reg. 39335 (June 16, 2023); RIN 3245\u2013AH91); or\n**(2)**\nthe final rule entitled Disaster Assistance Loan Program Changes to Unsecured Loan Amounts and Credit Elsewhere Criteria (89 Fed. Reg. 59826 (July 24, 2024); RIN 3245\u2013AI08).\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to the appropriate committees of Congress a report on\u2014\n**(1)**\nthe cost (as defined in section 502 of the Federal Credit Reform Act of 1990 ( 2 U.S.C. 661a )) of the increase in the home loan lending limits for, the extension of the deferment period for, the expansion of mitigation options for, the modifications to the criteria for determining whether applicants can obtain credit elsewhere with respect to, the changes to collateral requirements for, and other changes to the terms and conditions of loans under section 7(b)(1) of the Small Business Act ( 15 U.S.C. 636(b)(1) ) made by the covered final rules; and\n**(2)**\nthe effect on the subsidy for such loans of the changes contained in the covered final rules.\n#### 9. SBA Inspector General review\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term covered amounts means amounts made available for the cost of direct loans authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ); and\n**(2)**\nthe term Inspector General means the Inspector General of the Administration.\n##### (b) Review\n**(1) In general**\nThe Inspector General shall conduct a review of the circumstances surrounding the funding shortfall with respect to covered amounts, as described in\u2014\n**(A)**\nthe letter from President Joseph R. Biden, Jr. entitled Letter to Congress on Disaster Needs , dated October 4, 2024; and\n**(B)**\nthe letter from the Administrator submitted to the Chair and Ranking Members of the Committees on Appropriations of the Senate and the House of Representatives, dated October 10, 2024.\n**(2) Contents**\nThe review required under paragraph (1) shall include the following with respect to the funding shortfall described in that paragraph:\n**(A)**\nThe identification of any report or notification required by statute that the Administration failed to provide to Congress with respect to the funding shortfall.\n**(B)**\nThe reason for any obligation or expenditure of covered amounts for a purpose that significantly diverged from the purpose for which the covered amounts were made available.\n**(C)**\nAn analysis of the accuracy of projections and estimates relevant to the divergences described in subparagraph (B).\n**(D)**\nThe identification and description of any internal controls in place to manage covered amounts.\n**(E)**\nAn analysis of the impact that any reorganization of the Administration, including the transfer of administrative authority for the program carried out under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) to the Office of Capital Access of the Administration, may have had with respect to the funding shortfall.\n**(F)**\nThe identification of actions that the Administration can take to\u2014\n**(i)**\nimprove the accuracy of information submitted by the President under section 1105(a) of title 31, United States Code, with respect to the Administration;\n**(ii)**\nprevent any future funding shortfall with respect to any account of the Administration; and\n**(iii)**\nimprove the reports submitted to the appropriate committees of Congress under section 12091(a) of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k(a) ).\n**(G)**\nAny other matter determined relevant by the Inspector General.\n##### (c) Report\nNot later than 180 days after the date of enactment of this Act, the Inspector General shall submit to the appropriate committees of Congress a report that contains the findings of the review carried out under subsection (b).\n#### 10. Budget and forecasting report regarding the cost of direct disaster loans\n##### (a) Budget formulation and forecasting\nNot later than 30 days after the date of enactment of this Act, the Administrator shall submit to the appropriate committees of Congress a report detailing corrections the Administration will make to improve forecasting, data quality, and budget assumptions relating to budget submissions relating to amounts made available for the cost of SBA disaster loans.\n##### (b) Updates\nNot later than 90 days after the date of enactment of this Act, and every 90 days thereafter until the date that is 90 days after the date on which all the corrections described in subsection (a) have been implemented, the Administrator shall submit to the appropriate committees of Congress a report\u2014\n**(1)**\ndetailing the actions the Administration has taken to implement the corrections described in subsection (a); and\n**(2)**\nexplaining how each action detailed under paragraph (1) is directly related to implementing 1 or more corrections described in subsection (a).",
      "versionDate": "2025-06-27",
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
        "actionDate": "2025-03-04",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 22."
      },
      "number": "300",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DLARA",
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
        "updateDate": "2025-09-17T14:53:58Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4238ih.xml"
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
      "title": "DLARA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DLARA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Loan Accountability and Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-15T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve accountability in the disaster loan program of the Small Business Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-15T04:18:32Z"
    }
  ]
}
```
