# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/300?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/300
- Title: DLARA
- Congress: 119
- Bill type: S
- Bill number: 300
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-05-14T18:48:32Z
- Update date including text: 2026-05-14T18:48:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-20 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 22.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-20 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.
- 2025-03-04 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 22.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/300",
    "number": "300",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "DLARA",
    "type": "S",
    "updateDate": "2026-05-14T18:48:32Z",
    "updateDateIncludingText": "2026-05-14T18:48:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 22.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
            "date": "2025-03-04T22:06:46Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-21T00:57:59Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T18:01:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "IA"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SC"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "WV"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "ID"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NH"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s300is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 300\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Budd (for himself, Ms. Ernst , Mr. Scott of South Carolina , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo improve accountability in the disaster loan program of the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Loan Accountability and Reform Act or the DLARA .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nSec. 3. Definitions.\nSec. 4. Monthly disaster loan reports.\nSec. 5. Budget request relating to disaster loans.\nSec. 6. Limitations on loan forgiveness.\nSec. 7. Limits on disaster loans.\nSec. 8. Prohibition regarding SBA rules relating to disaster loans.\nSec. 9. GAO report on disaster loan changes.\nSec. 10. SBA Inspector General review.\nSec. 11. Budget and forecasting report regarding the cost of direct disaster loans.\n#### 3. Definitions\nIn this Act\u2014\n**(1)**\nthe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively; and\n**(2)**\nthe term appropriate committees of Congress means the Committee on Small Business and Entrepreneurship and the Committee on Appropriations of the Senate and the Committee on Small Business and the Committee on Appropriations of the House of Representatives.\n#### 4. Monthly disaster loan reports\nSection 12091(a) of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking during the applicable period for a major disaster ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (E), by striking how long the available funding for such loans will last and inserting the date at which available funding for such loans will reach 10 percent of the most recent appropriation and the date at which the funds will be depleted ;\n**(B)**\nin subparagraph (H), by striking and at the end;\n**(C)**\nin subparagraph (I), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(J) a summary detailing any changes to estimates or assumptions on obligations and expenditures, including data supporting these changes. ; and\n**(3)**\nby adding at the end the following:\n(3) Prohibition on official travel If the Administrator does not submit a report required to be submitted under paragraph (1) by the required date, no funds may be obligated for official travel by the Administrator until the Administrator submits the report. .\n#### 5. Budget request relating to disaster loans\nSection 1105 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(39) separate statements of\u2014 (A) the amount of appropriations requested for the fiscal year for which the budget is submitted for the cost of SBA disaster loans, the 10-year average of the cost of SBA disaster loans, and an explanation for any difference between the amount requested and the 10-year average cost; and (B) the amount of appropriations requested for the fiscal year for which the budget is submitted for the cost of COVID-EIDL loans, the 10-year average of the cost of COVID-EIDL loans, and an explanation for any difference between the amount requested and the 10-year average cost. (40) separate statements of\u2014 (A) the amount of appropriations requested for the fiscal year for which the budget is submitted for administrative costs relating to SBA disaster loans, the 10-year average of such administrative costs, and an explanation for any difference between the amount requested and the 10-year average costs; and (B) the amount of appropriations requested for the fiscal year for which the budget is submitted for administrative costs relating to COVID-EIDL loans, the 10-year average of such administrative costs, and an explanation for any difference between the amount requested and the 10-year average costs. ; and\n**(2)**\nby adding at the end the following:\n(j) In paragraphs (39) and (40) of subsection (a)\u2014 (1) the term COVID-EIDL loan means a direct loan under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) that was authorized under section 1110 of the CARES Act ( 15 U.S.C. 9009 ); and (2) the term SBA disaster loan means a direct loan authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ), other than a loan that was authorized under section 1110 of the CARES Act ( 15 U.S.C. 9009 ). .\n#### 6. Limitations on loan forgiveness\nSection 7 of the Small Business Act ( 15 U.S.C. 636 ) is amended by adding at the end the following:\n(o) Limitations on loan forgiveness (1) In general The Administrator may not\u2014 (A) forgive any loan under this section unless Congress has authorized such forgiveness; or (B) compromise on, suspend, or end collections on a debt owed to the Administration pursuant to paragraph (2) or (3) of section 3711(a) of title 31, United States Code. (2) Referral of debt If the Administrator seeks to discharge a debt and the discharge of such debt is limited under paragraph (1), the Administrator shall refer such debt to the Department of the Treasury for collection action, including a final determination regarding whether to suspend, end, or continue collection of the debt. .\n#### 7. Limits on disaster loans\n##### (a) Low funding\nSection 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) is amended\u2014\n**(1)**\nby redesignating the second paragraph designated as paragraph (16), relating to statute of limitations, as added by the COVID\u201319 EIDL Fraud Statute of Limitations Act of 2022 ( Public Law 117\u2013165 ; 136 Stat. 1363), as paragraph (18); and\n**(2)**\nby inserting after paragraph (16), relating to disaster declarations in rural areas, as added by the Disaster Assistance for Rural Communities Act ( Public Law 117\u2013249 ; 136 Stat. 2350), the following:\n(17) Requirements when funding is low (A) In general Not later than 24 hours after the unobligated balance of amounts available for the cost of direct loans authorized by this subsection is less than 10 percent of the most recent appropriation for such costs, the Administrator shall notify the Committee on Appropriations and the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Appropriations and the Committee on Small Business of the House of Representatives . (B) Limitation on obligating funds During the period beginning on the first business day occurring on or after the date by which the Administrator is required to notify Congress under subparagraph (A) and ending on the date on which additional amounts are appropriated for such costs, the Administrator may not obligate funds for a direct loan authorized under this subsection in an amount that is more than the amount of such a loan for which collateral is required. .\n##### (b) Repeal of authority To increase amount of loans for which collateral is not required\nSection 7(d)(6) of the Small Business Act is amended by striking (or such higher amount as the Administrator determines appropriate in the event of a major disaster) .\n#### 8. Prohibition regarding SBA rules relating to disaster loans\n##### (a) Definitions\nIn this section:\n**(1) Cost**\nThe term cost has the meaning given the term in section 502 of the Federal Credit Reform Act of 1990 ( 2 U.S.C. 661a ).\n**(2) Rule**\nThe term rule has the meaning given the term in section 551 of title 5, United States Code.\n##### (b) Prohibition\nNotwithstanding any other provision of law or regulation, beginning on the date of enactment of this Act, the Administrator of the Small Business Administration may not issue any rule that will result in any increased cost to the program carried out under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ).\n#### 9. GAO report on disaster loan changes\n##### (a) Definition\nIn this section, the term covered final rule means\u2014\n**(1)**\nthe final rule entitled Disaster Assistance Loan Program Changes to Maximum Loan Amounts and Miscellaneous Updates (88 Fed. Reg. 39335 (June 16, 2023); RIN 3245\u2013AH91); or\n**(2)**\nthe final rule entitled Disaster Assistance Loan Program Changes to Unsecured Loan Amounts and Credit Elsewhere Criteria (89 Fed. Reg. 59826 (July 24, 2024); RIN 3245\u2013AI08).\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Small Business and Entrepreneurship and the Committee on Appropriations of the Senate and the Committee on Small Business and the Committee on Appropriations of the House of Representatives a report on\u2014\n**(1)**\nthe cost (as defined in section 502 of the Federal Credit Reform Act of 1990 ( 2 U.S.C. 661a )) of the increase in the home loan lending limits for, the extension of the deferment period for, the expansion of mitigation options for, the modifications to the criteria for determining whether applicants can obtain credit elsewhere with respect to, the changes to collateral requirements for, and other changes to the terms and conditions of loans under section 7(b)(1) of the Small Business Act ( 15 U.S.C. 636(b)(1) ) made by the covered final rules; and\n**(2)**\nthe effect on the subsidy for such loans of the changes contained in the covered final rules.\n#### 10. SBA Inspector General review\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term covered amounts means amounts made available for the cost of direct loans authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ); and\n**(2)**\nthe term Inspector General means the Inspector General of the Administration.\n##### (b) Review\n**(1) In general**\nThe Inspector General shall conduct a review of the circumstances surrounding the funding shortfall with respect to covered amounts, as described in\u2014\n**(A)**\nthe letter from President Joseph R. Biden, Jr. entitled Letter to Congress on Disaster Needs , dated October 4, 2024; and\n**(B)**\nthe letter from the Administrator submitted to the Chair and Ranking Members of the Committees on Appropriations of the Senate and the House of Representatives, dated October 10, 2024.\n**(2) Contents**\nThe review required under paragraph (1) shall include the following with respect to the funding shortfall described in that paragraph:\n**(A)**\nThe identification of any reporting or notification requirements in statute that the Administration failed to provide to Congress with respect to the funding shortfall.\n**(B)**\nThe reason for any obligation or expenditure of covered amounts for a purpose that significantly diverged from the purpose for which the covered amounts were made available.\n**(C)**\nAn analysis of the accuracy of projections and estimates relevant to the divergences described in subparagraph (B).\n**(D)**\nThe identification and description of any internal controls in place to manage covered amounts.\n**(E)**\nAn analysis of the impact that any reorganization of the Administration, including the transfer of administrative authority for the program carried out under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) to the Office of Capital Access of the Administration, may have had with respect to the funding shortfall.\n**(F)**\nThe identification of actions that the Administration can take to\u2014\n**(i)**\nimprove the accuracy of information submitted by the President under section 1105(a) of title 31, United States Code, with respect to the Administration;\n**(ii)**\nprevent any future funding shortfall with respect to any account of the Administration; and\n**(iii)**\nimprove the report submitted to the appropriate committees of Congress under section 12091(a) of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k(a) ).\n**(G)**\nAny other matter determined relevant by the Inspector General.\n##### (c) Report\nNot later than 180 days after the date of enactment of this Act, the Inspector General shall submit to the appropriate committees of Congress a report that contains the findings of the review carried out under subsection (b).\n#### 11. Budget and forecasting report regarding the cost of direct disaster loans\n##### (a) Budget formulation and forecasting\nNot later than 30 days after the date of enactment of this Act, the Administrator shall submit to the appropriate committees of Congress a report detailing corrections the Administration will make to improve forecasting, data quality, and budget assumptions relating to budget submissions relating to amounts made available for the cost of direct loans authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ).\n##### (b) Updates\nNot later than 90 days after the date of enactment of this Act, and every 90 days thereafter until the date that is 90 days after the date on which all the corrections described in subsection (a) have been implemented, the Administrator shall submit to the appropriate committees of Congress a report\u2014\n**(1)**\ndetailing the actions the Administration has taken to implement the corrections described in subsection (a); and\n**(2)**\nexplaining how each action detailed under paragraph (1) is directly related to implementing 1 or more corrections described in subsection (a).",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s300rs.xml",
      "text": "II\nCalendar No. 22\n119th CONGRESS\n1st Session\nS. 300\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Budd (for himself, Ms. Ernst , Mr. Scott of South Carolina , Mr. Tillis , Mr. Husted , Mr. Justice , Mr. Young , Mr. Risch , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nMarch 4, 2025 Reported by Ms. Ernst , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo improve accountability in the disaster loan program of the Small Business Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disaster Loan Accountability and Reform Act or the DLARA .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nSec. 3. Definitions.\nSec. 4. Monthly disaster loan reports.\nSec. 5. Budget request relating to disaster loans.\nSec. 6. Limitations on loan forgiveness.\nSec. 7. Limits on disaster loans.\nSec. 8. Prohibition regarding SBA rules relating to disaster loans.\nSec. 9. GAO report on disaster loan changes.\nSec. 10. SBA Inspector General review.\nSec. 11. Budget and forecasting report regarding the cost of direct disaster loans.\n#### 3. Definitions\nIn this Act\u2014\n**(1)**\nthe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively; and\n**(2)**\nthe term appropriate committees of Congress means the Committee on Small Business and Entrepreneurship and the Committee on Appropriations of the Senate and the Committee on Small Business and the Committee on Appropriations of the House of Representatives.\n#### 4. Monthly disaster loan reports\nSection 12091(a) of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking during the applicable period for a major disaster ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (E), by striking how long the available funding for such loans will last and inserting the date at which available funding for such loans will reach 10 percent of the most recent appropriation and the date at which the funds will be depleted ;\n**(B)**\nin subparagraph (H), by striking and at the end;\n**(C)**\nin subparagraph (I), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(J) a summary detailing any changes to estimates or assumptions on obligations and expenditures, including data supporting these changes. ; and\n**(3)**\nby adding at the end the following:\n(3) Prohibition on official travel If the Administrator does not submit a report required to be submitted under paragraph (1) by the required date, no funds may be obligated for official travel by the Administrator until the Administrator submits the report. .\n#### 5. Budget request relating to disaster loans\nSection 1105 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(39) separate statements of\u2014 (A) the amount of appropriations requested for the fiscal year for which the budget is submitted for the cost of SBA disaster loans, the 10-year average of the cost of SBA disaster loans, and an explanation for any difference between the amount requested and the 10-year average cost; and (B) the amount of appropriations requested for the fiscal year for which the budget is submitted for the cost of COVID-EIDL loans, the 10-year average of the cost of COVID-EIDL loans, and an explanation for any difference between the amount requested and the 10-year average cost. (40) separate statements of\u2014 (A) the amount of appropriations requested for the fiscal year for which the budget is submitted for administrative costs relating to SBA disaster loans, the 10-year average of such administrative costs, and an explanation for any difference between the amount requested and the 10-year average costs; and (B) the amount of appropriations requested for the fiscal year for which the budget is submitted for administrative costs relating to COVID-EIDL loans, the 10-year average of such administrative costs, and an explanation for any difference between the amount requested and the 10-year average costs. ; and\n**(2)**\nby adding at the end the following:\n(j) In paragraphs (39) and (40) of subsection (a)\u2014 (1) the term COVID-EIDL loan means a direct loan under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) that was authorized under section 1110 of the CARES Act ( 15 U.S.C. 9009 ); and (2) the term SBA disaster loan means a direct loan authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ), other than a loan that was authorized under section 1110 of the CARES Act ( 15 U.S.C. 9009 ). .\n#### 6. Limitations on loan forgiveness\nSection 7 of the Small Business Act ( 15 U.S.C. 636 ) is amended by adding at the end the following:\n(o) Limitations on loan forgiveness (1) In general The Administrator may not\u2014 (A) forgive any loan under this section unless Congress has authorized such forgiveness; or (B) compromise on, suspend, or end collections on a debt owed to the Administration pursuant to paragraph (2) or (3) of section 3711(a) of title 31, United States Code. (2) Referral of debt If the Administrator seeks to discharge a debt and the discharge of such debt is limited under paragraph (1), the Administrator shall refer such debt to the Department of the Treasury for collection action, including a final determination regarding whether to suspend, end, or continue collection of the debt. .\n#### 7. Limits on disaster loans\n##### (a) Low funding\nSection 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) is amended\u2014\n**(1)**\nby redesignating the second paragraph designated as paragraph (16), relating to statute of limitations, as added by the COVID\u201319 EIDL Fraud Statute of Limitations Act of 2022 ( Public Law 117\u2013165 ; 136 Stat. 1363), as paragraph (18); and\n**(2)**\nby inserting after paragraph (16), relating to disaster declarations in rural areas, as added by the Disaster Assistance for Rural Communities Act ( Public Law 117\u2013249 ; 136 Stat. 2350), the following:\n(17) Requirements when funding is low (A) In general Not later than 24 hours after the unobligated balance of amounts available for the cost of direct loans authorized by this subsection is less than 10 percent of the most recent appropriation for such costs, the Administrator shall notify the Committee on Appropriations and the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Appropriations and the Committee on Small Business of the House of Representatives . (B) Limitation on obligating funds During the period beginning on the first business day occurring on or after the date by which the Administrator is required to notify Congress under subparagraph (A) and ending on the date on which additional amounts are appropriated for such costs, the Administrator may not obligate funds for a direct loan authorized under this subsection in an amount that is more than the amount of such a loan for which collateral is required. .\n##### (b) Repeal of authority To increase amount of loans for which collateral is not required\nSection 7(d)(6) of the Small Business Act is amended by striking (or such higher amount as the Administrator determines appropriate in the event of a major disaster) .\n#### 8. Prohibition regarding SBA rules relating to disaster loans\n##### (a) Definitions\nIn this section:\n**(1) Cost**\nThe term cost has the meaning given the term in section 502 of the Federal Credit Reform Act of 1990 ( 2 U.S.C. 661a ).\n**(2) Rule**\nThe term rule has the meaning given the term in section 551 of title 5, United States Code.\n##### (b) Prohibition\nNotwithstanding any other provision of law or regulation, beginning on the date of enactment of this Act, the Administrator of the Small Business Administration may not issue any rule that will result in any increased cost to the program carried out under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ).\n#### 9. GAO report on disaster loan changes\n##### (a) Definition\nIn this section, the term covered final rule means\u2014\n**(1)**\nthe final rule entitled Disaster Assistance Loan Program Changes to Maximum Loan Amounts and Miscellaneous Updates (88 Fed. Reg. 39335 (June 16, 2023); RIN 3245\u2013AH91); or\n**(2)**\nthe final rule entitled Disaster Assistance Loan Program Changes to Unsecured Loan Amounts and Credit Elsewhere Criteria (89 Fed. Reg. 59826 (July 24, 2024); RIN 3245\u2013AI08).\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Small Business and Entrepreneurship and the Committee on Appropriations of the Senate and the Committee on Small Business and the Committee on Appropriations of the House of Representatives a report on\u2014\n**(1)**\nthe cost (as defined in section 502 of the Federal Credit Reform Act of 1990 ( 2 U.S.C. 661a )) of the increase in the home loan lending limits for, the extension of the deferment period for, the expansion of mitigation options for, the modifications to the criteria for determining whether applicants can obtain credit elsewhere with respect to, the changes to collateral requirements for, and other changes to the terms and conditions of loans under section 7(b)(1) of the Small Business Act ( 15 U.S.C. 636(b)(1) ) made by the covered final rules; and\n**(2)**\nthe effect on the subsidy for such loans of the changes contained in the covered final rules.\n#### 10. SBA Inspector General review\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term covered amounts means amounts made available for the cost of direct loans authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ); and\n**(2)**\nthe term Inspector General means the Inspector General of the Administration.\n##### (b) Review\n**(1) In general**\nThe Inspector General shall conduct a review of the circumstances surrounding the funding shortfall with respect to covered amounts, as described in\u2014\n**(A)**\nthe letter from President Joseph R. Biden, Jr. entitled Letter to Congress on Disaster Needs , dated October 4, 2024; and\n**(B)**\nthe letter from the Administrator submitted to the Chair and Ranking Members of the Committees on Appropriations of the Senate and the House of Representatives, dated October 10, 2024.\n**(2) Contents**\nThe review required under paragraph (1) shall include the following with respect to the funding shortfall described in that paragraph:\n**(A)**\nThe identification of any reporting or notification requirements in statute that the Administration failed to provide to Congress with respect to the funding shortfall.\n**(B)**\nThe reason for any obligation or expenditure of covered amounts for a purpose that significantly diverged from the purpose for which the covered amounts were made available.\n**(C)**\nAn analysis of the accuracy of projections and estimates relevant to the divergences described in subparagraph (B).\n**(D)**\nThe identification and description of any internal controls in place to manage covered amounts.\n**(E)**\nAn analysis of the impact that any reorganization of the Administration, including the transfer of administrative authority for the program carried out under section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ) to the Office of Capital Access of the Administration, may have had with respect to the funding shortfall.\n**(F)**\nThe identification of actions that the Administration can take to\u2014\n**(i)**\nimprove the accuracy of information submitted by the President under section 1105(a) of title 31, United States Code, with respect to the Administration;\n**(ii)**\nprevent any future funding shortfall with respect to any account of the Administration; and\n**(iii)**\nimprove the report submitted to the appropriate committees of Congress under section 12091(a) of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636k(a) ).\n**(G)**\nAny other matter determined relevant by the Inspector General.\n##### (c) Report\nNot later than 180 days after the date of enactment of this Act, the Inspector General shall submit to the appropriate committees of Congress a report that contains the findings of the review carried out under subsection (b).\n#### 11. Budget and forecasting report regarding the cost of direct disaster loans\n##### (a) Budget formulation and forecasting\nNot later than 30 days after the date of enactment of this Act, the Administrator shall submit to the appropriate committees of Congress a report detailing corrections the Administration will make to improve forecasting, data quality, and budget assumptions relating to budget submissions relating to amounts made available for the cost of direct loans authorized by section 7(b) of the Small Business Act ( 15 U.S.C. 636(b) ).\n##### (b) Updates\nNot later than 90 days after the date of enactment of this Act, and every 90 days thereafter until the date that is 90 days after the date on which all the corrections described in subsection (a) have been implemented, the Administrator shall submit to the appropriate committees of Congress a report\u2014\n**(1)**\ndetailing the actions the Administration has taken to implement the corrections described in subsection (a); and\n**(2)**\nexplaining how each action detailed under paragraph (1) is directly related to implementing 1 or more corrections described in subsection (a).",
      "versionDate": "2025-03-04",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-06-27",
        "text": "Referred to the Committee on Small Business, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4238",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DLARA",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T13:51:08Z"
          },
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-03-19T13:50:25Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-19T13:53:41Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-03-19T13:50:49Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-19T13:53:32Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-03-19T14:04:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-03T12:22:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119s300",
          "measure-number": "300",
          "measure-type": "s",
          "orig-publish-date": "2025-03-04",
          "originChamber": "SENATE",
          "update-date": "2026-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s300v25",
            "update-date": "2026-05-14"
          },
          "action-date": "2025-03-04",
          "action-desc": "Reported to Senate",
          "summary-text": "<p><strong>Disaster Loan Accountability and Reform Act or the\u00a0DLARA</strong></p><p>This bill modifies the Small Business Administration (SBA) disaster loan program and requires external review of, and reporting on, the program.</p><p>First, the bill requires the SBA to report monthly on the operation of the disaster loan program. (Currently, the SBA must report only during the applicable period for a major disaster.) The report must estimate the date on which available funding for such loans will reach 10% of the most recent appropriation and the date on which the funds will be depleted.</p><p>Second, the President's annual budget\u00a0must include separate statements regarding the appropriations request for SBA disaster\u00a0loans and COVID-19 Economic Injury Disaster Loans (EIDL), including explanations for any difference between the amount requested and the 10-year average cost for such loans.</p><p>Third, for a period of four years, the SBA must notify Congress when the unobligated balance of amounts available for disaster\u00a0loans is less than 10% of the 10-year average annual cost provided in the most recent Presidential budget. At such point, the\u00a0SBA may\u00a0limit\u00a0disaster loans to collateralized amounts.</p><p>Finally, the bill requires additional oversight of the disaster loan program, including</p><ul><li>a Government Accountability Office report on the disbursement of disaster loans and the effect of specified SBA rules on home\u00a0lending limits,</li><li>an SBA Office of Inspector General review of recent\u00a0funding shortfalls for disaster loans, and</li><li>an SBA report on improvements for\u00a0forecasting the cost\u00a0of disaster loans.</li></ul>"
        },
        "title": "DLARA"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s300.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Disaster Loan Accountability and Reform Act or the\u00a0DLARA</strong></p><p>This bill modifies the Small Business Administration (SBA) disaster loan program and requires external review of, and reporting on, the program.</p><p>First, the bill requires the SBA to report monthly on the operation of the disaster loan program. (Currently, the SBA must report only during the applicable period for a major disaster.) The report must estimate the date on which available funding for such loans will reach 10% of the most recent appropriation and the date on which the funds will be depleted.</p><p>Second, the President's annual budget\u00a0must include separate statements regarding the appropriations request for SBA disaster\u00a0loans and COVID-19 Economic Injury Disaster Loans (EIDL), including explanations for any difference between the amount requested and the 10-year average cost for such loans.</p><p>Third, for a period of four years, the SBA must notify Congress when the unobligated balance of amounts available for disaster\u00a0loans is less than 10% of the 10-year average annual cost provided in the most recent Presidential budget. At such point, the\u00a0SBA may\u00a0limit\u00a0disaster loans to collateralized amounts.</p><p>Finally, the bill requires additional oversight of the disaster loan program, including</p><ul><li>a Government Accountability Office report on the disbursement of disaster loans and the effect of specified SBA rules on home\u00a0lending limits,</li><li>an SBA Office of Inspector General review of recent\u00a0funding shortfalls for disaster loans, and</li><li>an SBA report on improvements for\u00a0forecasting the cost\u00a0of disaster loans.</li></ul>",
      "updateDate": "2026-05-14",
      "versionCode": "id119s300"
    },
    "title": "DLARA"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Disaster Loan Accountability and Reform Act or the\u00a0DLARA</strong></p><p>This bill modifies the Small Business Administration (SBA) disaster loan program and requires external review of, and reporting on, the program.</p><p>First, the bill requires the SBA to report monthly on the operation of the disaster loan program. (Currently, the SBA must report only during the applicable period for a major disaster.) The report must estimate the date on which available funding for such loans will reach 10% of the most recent appropriation and the date on which the funds will be depleted.</p><p>Second, the President's annual budget\u00a0must include separate statements regarding the appropriations request for SBA disaster\u00a0loans and COVID-19 Economic Injury Disaster Loans (EIDL), including explanations for any difference between the amount requested and the 10-year average cost for such loans.</p><p>Third, for a period of four years, the SBA must notify Congress when the unobligated balance of amounts available for disaster\u00a0loans is less than 10% of the 10-year average annual cost provided in the most recent Presidential budget. At such point, the\u00a0SBA may\u00a0limit\u00a0disaster loans to collateralized amounts.</p><p>Finally, the bill requires additional oversight of the disaster loan program, including</p><ul><li>a Government Accountability Office report on the disbursement of disaster loans and the effect of specified SBA rules on home\u00a0lending limits,</li><li>an SBA Office of Inspector General review of recent\u00a0funding shortfalls for disaster loans, and</li><li>an SBA report on improvements for\u00a0forecasting the cost\u00a0of disaster loans.</li></ul>",
      "updateDate": "2026-05-14",
      "versionCode": "id119s300"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s300is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s300rs.xml"
        }
      ],
      "type": "Reported in Senate"
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
      "updateDate": "2025-04-10T11:03:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "DLARA",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Disaster Loan Accountability and Reform Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DLARA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T14:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Loan Accountability and Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T14:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve accountability in the disaster loan program of the Small Business Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T14:18:25Z"
    }
  ]
}
```
