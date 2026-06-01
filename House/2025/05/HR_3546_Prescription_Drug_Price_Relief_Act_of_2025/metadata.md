# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3546?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3546
- Title: Prescription Drug Price Relief Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3546
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2026-03-24T18:25:08Z
- Update date including text: 2026-03-24T18:25:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3546",
    "number": "3546",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Prescription Drug Price Relief Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-24T18:25:08Z",
    "updateDateIncludingText": "2026-03-24T18:25:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-21T14:02:25Z",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "WA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MN"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3546ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3546\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Khanna (for himself and Ms. Schakowsky ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo significantly lower prescription drug prices for patients in the United States by ending government-granted monopolies for manufacturers who charge drug prices that are higher than the median prices at which the drugs are available in other countries.\n#### 1. Short title\nThis Act may be cited as the Prescription Drug Price Relief Act of 2025 .\n#### 2. Identification of excessively priced drugs\n##### (a) In general\nNot later than 30 days after the date of enactment of this Act, the Secretary shall establish a process to conduct a review of all brand name drugs, not less frequently than once per calendar year, under which the Secretary determines under subsection (b) whether the price of each such drug is excessive.\n##### (b) Excessive price determinations\n**(1) International reference price**\n**(A) In general**\nThe Secretary shall determine that any brand name drug for which the domestic average manufacturing price exceeds the median price charged for such drug in the 5 reference countries to have an excessive price. In assessing the extent to which the price is excessive, the Secretary shall consider the factors described in paragraph (2).\n**(B) Reference Countries**\nIn this Act, the term reference countries means Canada, the United Kingdom, Germany, France, and Japan.\n**(C) Requirement with respect to drugs for which certain reference country information is not available**\nThe Secretary shall make a determination under paragraph (1) for every brand name drug for which pricing information is available for at least 3 of the 5 reference countries.\n**(2) Determinations based on other factors**\nWith respect to any brand name drug that is not determined to have an excessive price by operation of paragraph (1) (including any drug for which there is insufficient data to make such a determination under such paragraph), the Secretary shall determine that such drug has an excessive price if the price of the drug is higher than reasonable taking into account the following factors:\n**(A)**\nThe size of the affected patient population.\n**(B)**\nThe value of the drug to patients, including the impact of the price on access to the drug and the relationship of the price of the drug to its therapeutic health benefits.\n**(C)**\nThe risk adjusted value of Federal Government subsidies and investments related to the drug.\n**(D)**\nThe costs associated with development of the drug.\n**(E)**\nWhether the drug provided a significant improvement in health outcomes, compared to other therapies available at the time of its approval.\n**(F)**\nThe cumulative global revenues generated by the drug.\n**(G)**\nWhether the domestic average manufacturer price of the drug increased during any annual quarter by a percentage that is more than the percentage increase in the consumer price index for all urban consumers for the respective annual quarter.\n**(H)**\nOther factors the Secretary determines appropriate.\n##### (c) Petition for determination\n**(1) In general**\nAny person may petition the Secretary, in accordance with section 553(e) of title 5, United States Code, to make an excessive drug price determination for an applicable drug under subsection (b)(2). Not later than 90 days after the date of receipt of such a petition, subject to paragraph (2), the Secretary shall\u2014\n**(A)**\nmake a determination under subsection (b)(2) regarding such drug; or\n**(B)**\n**(i)**\ndecline to make such a determination; and\n**(ii)**\nmake public the reasons why the Secretary has declined to make such a determination.\n**(2) Exception**\nThe Secretary shall not make a determination under subsection (b)(2) for a drug in response to a petition under this section more frequently than once per calendar year.\n**(3) Public availability**\nThe Secretary shall make any petitions submitted under this subsection, together with any documentation related to the petitions and the Secretary's determinations on such petitions and rationale for such determinations, publicly available, including by posting such information on the database under section 5.\n#### 3. Ending government-granted monopolies for excessively priced drugs\n##### (a) Excessive drug price authority\nWith respect to any brand name drug, if the Secretary determines under section 2 that the price of the drug is excessive, the Secretary\u2014\n**(1)**\nshall waive or void any government-granted exclusivities with respect to such drug, effective on the date that the excessive price determination under section 2 is made for such drug; and\n**(2)**\nshall grant open, non-exclusive licenses allowing any person to make, use, offer to sell or sell, or import into the United States such drug, and to rely upon the regulatory test data of such drug, in accordance with section 4.\n##### (b) Expedited review\nThe Secretary shall prioritize the review of, and act within 8 months of the date of the submission of a generic drug application or a biosimilar biological product application if such application references a drug licensed under subsection (a)(2).\n##### (c) Civil actions\nIf the Secretary determines that the manufacturer of an excessively priced drug (as determined under section 2(a)) has increased the price of such drug during the period beginning on the date on which such price determination is made and ending on the date on which an entity begins manufacturing the drug under an open, non-exclusive license under subsection (a)(2), the Secretary may file a civil action in the United States district court for the district in which the manufacturer is located, or in the United States district court for the District of Columbia, to recover damages in an amount equal to not less than the total amount of revenue derived by the manufacturer as a result of any such price increase during such period. In actions brought under this subsection, the district courts shall have jurisdiction to grant all appropriate relief including injunctive relief and compensatory damages.\n#### 4. Excessive drug price license\n##### (a) Reasonable royalty\n**(1) In general**\nAn entity accepting an open, non-exclusive license under section 3(a)(2) shall pay a reasonable royalty to the holder of a patent that claims the drug or that claims a use of the drug or to the holder of an application approved under subsection 505(c) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(c) ) or section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) ) for which any government-granted exclusivity with respect to the drug was terminated under section 3(a)(1).\n**(2) Royalty rate**\nSuch royalty rate shall be\u2014\n**(A)**\na percentage of sales, where the percentage rate is no higher than the average royalty rate estimated from the data provided by the Internal Revenue Service for pharmaceutical manufacturer Federal income tax returns; or\n**(B)**\nan amount as determined by the Secretary, taking into account\u2014\n**(i)**\nthe value of the drug to patients;\n**(ii)**\nthe size of the affected patient population;\n**(iii)**\nthe risk adjusted value of the Federal Government subsidies and investments related to the drug;\n**(iv)**\nwhether the drug provided a significant improvement in health outcomes, compared to other therapies available at the time of the approval;\n**(v)**\nthe extent to which the brand name drug manufacturer has recovered risk adjusted investments related to the drug, including the investments related to the invention, regulatory test data, and any other relevant research and development costs; and\n**(vi)**\nany other information the Secretary determines appropriate.\n##### (b) Requirements\n**(1) In general**\nA royalty rate under subsection (a) shall be consistent with making drugs available to purchasers, including Federal, State, local, and nongovernmental purchasers and individuals, at prices that are affordable and reasonable. Under no condition shall a royalty be set at a rate that would cause a product for which an open, non-exclusive license was issued under section 3 to be sold at an excessive price, as determined under section 2.\n**(2) Multiple affected parties**\nIn the case that there is one or more holders or investors in the patented inventions related to the drug in addition to the brand name manufacturer, the royalty rate shall be divided among the holders or investors (including such manufacturer) in a manner agreed upon by the manufacturer and other holders or investors, or, in the absence of such an agreement, in a manner the Secretary determines to be appropriate.\n**(3) Price**\nAn entity accepting an open, non-exclusive license under section 3(a)(2) shall sell the drug at a price below the excessive price determined for that drug under section 2(b).\n#### 5. Public excessive drug price database\n##### (a) Excessive drug price database\n**(1) In general**\nThe Secretary shall establish and maintain a comprehensive, up-to-date database of brand name drugs and the excessive price determinations for such drugs under section 2.\n**(2) Contents**\nThe database shall include, at a minimum, for each brand name drug, for the applicable calendar year\u2014\n**(A)**\nthe name of the drug;\n**(B)**\nthe manufacturer;\n**(C)**\nwhether the drug was determined under section 2(b) to have an excessive price;\n**(D)**\nthe number of petitions the Secretary received under section 2(c) to make an excessive price determination for the drug, together with the information described in section 2(c)(3);\n**(E)**\nthe number of open, non-exclusive licenses the Secretary has granted under section 3(a)(2) for generic drug or biosimilar biological product versions of the drug; and\n**(F)**\nthe number of applications under subsection (b)(2) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ) submitted to the Secretary, pursuant to such a license granted under section 3(a)(2), and the number of such applications that have been approved.\n**(3) Certain determinations**\nWith respect to a determination made under section 2(b)(1), the Secretary shall publish on the database such determination in accordance with paragraph (1) within 30 days of receiving domestic and international pricing information from manufacturers under section 6.\n##### (b) Annual reports to Congress\nNot later than 60 days after the first excessive price review under section 2 is complete, and annually thereafter, the Secretary shall submit to Congress a report describing the excessive drug price review for the preceding year. The report shall contain summary data regarding\u2014\n**(1)**\nthe total number of drugs that were reviewed;\n**(2)**\nthe total number of drugs determined to be excessively priced under each of paragraphs (1) and (2) of section 2(b), and the name and manufacturer of each such drug;\n**(3)**\nthe total number of drugs determined to be excessively priced, listed by manufacturer;\n**(4)**\nthe extent to which the prices of the drugs identified under section 2 were higher than reasonable, on average;\n**(5)**\nthe total number of drugs for which an open, non-exclusive license has been granted under section 3(a)(2);\n**(6)**\nthe total number of generic drug or biosimilar biological product applications received and approved that reference a drug so licensed;\n**(7)**\nthe median approval time for generic drug or biosimilar biological product applications that reference a drug so licensed;\n**(8)**\nthe total number of petitions the Secretary received under section 2(c) to make excessive price determinations for drugs;\n**(9)**\na list of any manufacturers who failed to report information as required under section 6; and\n**(10)**\nother appropriate information, as the Secretary determines or as Congress requests.\n##### (c) Public availability\nThe Secretary shall make the information in the database described in subsection (a) and the report in subsection (b) publicly available, including on the website of the Food and Drug Administration, in a manner that is easy to find and understand.\n#### 6. Drug manufacturer reporting\n##### (a) In general\nEach manufacturer shall submit to the Secretary, in such format as the Secretary may require, an annual report that includes the following information for each brand name drug of the manufacturer, with respect to the previous calendar year:\n**(1)**\nThe average manufacturer price of the drug in the United States and in the reference countries, for the entire year, and broken down for each quarter of the year.\n**(2)**\nThe wholesale acquisition cost of the drug in the United States and in the reference countries, for the entire year, and broken down for each quarter of the year.\n**(3)**\nCumulative global revenues generated by the drug.\n**(4)**\nAnnual net sales revenue generated by the drug in the United States and in the reference countries, for the entire year, and broken down for each quarter of the year.\n**(5)**\nTotal expenditures on domestic and foreign drug research and development related to the drug, itemized by\u2014\n**(A)**\nbasic and preclinical research;\n**(B)**\nclinical research, reported separately for each clinical trial;\n**(C)**\ndevelopment of alternative dosage forms and strengths for the drug molecule or combinations, including the molecule;\n**(D)**\nother drug development activities, such as nonclinical laboratory studies and record and report maintenance;\n**(E)**\npursuing new or expanded indications for such drug through supplemental applications under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ); and\n**(F)**\ncarrying out postmarket requirements related to such drug, including under section 505(o)(3) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(o)(3) ).\n**(6)**\nTotal expenditures on domestic and foreign marketing and advertising related to the drug.\n**(7)**\nInvestments in human clinical trials related to the drug, by each trial and each year, including grants, research contracts, tax credits or deductions, and reimbursements from public or private health plans or insurance, and any other public sector subsidies or incentives, such as the fair market value or priority review vouchers or other considerations.\n**(8)**\nThe estimated size of the affected patient population.\n**(9)**\nAdditional information the manufacturer chooses to provide related to drug pricing decisions, such as information related to the methodology used to set the price of the drug.\n**(10)**\nAdditional information as the Secretary determines necessary to carry out this Act, including information for previous years.\n##### (b) Report due date\nApplicable manufacturers shall submit the reports described in subsection (a) not later than January 15 of the year following the date of enactment of this Act, and of each year thereafter.\n##### (c) Penalty for noncompliance\n**(1) In general**\nAny manufacturer that fails to submit information for a drug as required by this section on a timely basis or that knowingly provides false information shall be liable for a civil monetary penalty, as determined by the Secretary under paragraph (2), in addition to any other penalty under other applicable provisions of law.\n**(2) Amount of penalty**\nThe amount of a civil penalty under paragraph (1) shall be equal to the product of\u2014\n**(A)**\nan amount, as determined appropriate by the Secretary, which is\u2014\n**(i)**\nnot less than 0.5 percent of the gross revenues from sales for the previous calendar year of the drug for which the information was not submitted; and\n**(ii)**\nnot greater than 1 percent of the gross revenues from sales for the previous calendar year of such drug; and\n**(B)**\nthe number of days in the period between\u2014\n**(i)**\nthe report due date under subsection (b); and\n**(ii)**\nthe date on which the Secretary receives the information required to be reported by the manufacturer under this section.\n**(3) Use of civil penalty**\nThe Secretary shall collect the civil penalties under this subsection and shall use such funds to support competitive research grant programs of the National Institutes of Health.\n#### 7. Prohibition of anticompetitive behavior\nNo manufacturer may engage in anticompetitive behavior violating section 5(a) of the Federal Trade Commission Act ( 15 U.S.C. 45(a) ) with another manufacturer that may interfere with the issuance and implementation of open, non-exclusive licenses under this Act or otherwise run contrary to the public interest in the availability of affordable prescription drugs.\n#### 8. Definitions\nFor the purposes of this Act:\n**(1) Average manufacturer price**\n**(A) In general**\nThe term average manufacturer price , with respect to a drug, subject to subparagraph (B), has the meaning given such term in section 1927(k)(1) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(1) ); or with respect to a drug for which there is no average manufacturer price as so defined, such term shall mean the wholesale acquisition cost (as defined in section 1847A(c)(6)(B) of the Social Security Act (42 U.S.C. 1395w\u20133a(c)(6)(B))) of the drug.\n**(B) Application to reference countries**\nWith respect to reference countries, the term average manufacturer price , as defined in subparagraph (A), shall be determined based on the price of the drug in the applicable reference country.\n**(2) Biosimilar biological product**\nThe term biosimilar biological product means a biological product licensed pursuant to an application under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) ).\n**(3) Brand name drug**\nThe term brand name drug means a drug\u2014\n**(A)**\nthat is approved pursuant to an application under section (b)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b)(1) ) or that is licensed under section 351(a) of the Public Health Service Act ( 42 U.S.C. 262(a) );\n**(B)**\nthat is subject to section 503(b)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353(b)(1) ); and\n**(C)**\nthat is claimed in a patent, or a use of which is claimed in a patent.\n**(4) Generic drug**\nThe term generic drug means a drug approved pursuant to an application under section (b)(2) or (j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ).\n**(5) Government-granted exclusivity**\nThe term government-granted exclusivity means prohibitions on the submission or approval of drug applications granted under any of the following:\n**(A)**\nClauses (ii) through (v) of section 505(c)(3)(E) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(c)(3)(E) ).\n**(B)**\nSection 505(j)(5)(B)(iv) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(5)(B)(iv) ) or clause (ii), (iii), or (iv) of section 505(j)(5)(F) of such Act.\n**(C)**\nSection 505A of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355a ).\n**(D)**\nSection 505E of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355f ).\n**(E)**\nSection 527 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360cc ).\n**(F)**\nSection 351(k)(7) of the Public Health Service Act ( 42 U.S.C. 262(k)(7) ).\n**(G)**\nAny other provision of law that provides for exclusivity (or extension of exclusivity) with respect to a drug.\n**(6) Manufacturer**\nThe term manufacturer means the holder of an application approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or of a license issued under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ).\n**(7) Open, non-exclusive license**\nThe term open, non-exclusive license means a license that authorizes any person to use a patent held by a manufacturer that claims a brand name drug or a use of a brand name drug or rely upon regulatory test data for such drug, including patents held in common by the manufacturer and other entities, needed to produce, manufacture, import, export, distribute, offer in liquidation, sell, buy, or use such brand name drug.\n**(8) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-05-20",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1818",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Prescription Drug Price Relief Act of 2025",
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
        "updateDate": "2025-05-30T14:05:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
    "originChamber": "House",
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
          "measure-id": "id119hr3546",
          "measure-number": "3546",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-21",
          "originChamber": "HOUSE",
          "update-date": "2026-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3546v00",
            "update-date": "2026-03-24"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prescription Drug Price Relief Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to review brand-name drugs annually for excessive pricing and, if a drug is found to be priced excessively, to void any exclusivity granted to its sponsor.</p><p>Specifically, HHS must review all brand-name drug prices at least annually and upon petition. If any such drugs are found to be excessively priced, HHS must (1) void any government-granted exclusivity; (2) issue open, nonexclusive licenses for the drugs; and (3) expedite the review of corresponding applications for generic drugs and biosimilar biological products. HHS must also create a public database with its determinations for each drug.</p><p>An entity accepting an open, nonexclusive license under these provisions must pay a reasonable royalty to the holder of the relevant patent or approved new drug application, and must price the generic drug or\u00a0biosimilar below the excessive rate.</p><p>Under the bill, a price is considered excessive if the domestic average manufacturing price exceeds the median price for the drug in Canada, the United Kingdom, Germany, France, and Japan. If a price does not meet this criteria, or if pricing information is unavailable in at least three of these countries, the price is still considered excessive if it is higher than reasonable in light of specified factors, including development cost, revenue, and the size of the affected patient population.</p><p>The bill also requires drug manufacturers to report specified financial information for brand-name drugs, including research and advertising expenditures.</p>"
        },
        "title": "Prescription Drug Price Relief Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3546.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prescription Drug Price Relief Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to review brand-name drugs annually for excessive pricing and, if a drug is found to be priced excessively, to void any exclusivity granted to its sponsor.</p><p>Specifically, HHS must review all brand-name drug prices at least annually and upon petition. If any such drugs are found to be excessively priced, HHS must (1) void any government-granted exclusivity; (2) issue open, nonexclusive licenses for the drugs; and (3) expedite the review of corresponding applications for generic drugs and biosimilar biological products. HHS must also create a public database with its determinations for each drug.</p><p>An entity accepting an open, nonexclusive license under these provisions must pay a reasonable royalty to the holder of the relevant patent or approved new drug application, and must price the generic drug or\u00a0biosimilar below the excessive rate.</p><p>Under the bill, a price is considered excessive if the domestic average manufacturing price exceeds the median price for the drug in Canada, the United Kingdom, Germany, France, and Japan. If a price does not meet this criteria, or if pricing information is unavailable in at least three of these countries, the price is still considered excessive if it is higher than reasonable in light of specified factors, including development cost, revenue, and the size of the affected patient population.</p><p>The bill also requires drug manufacturers to report specified financial information for brand-name drugs, including research and advertising expenditures.</p>",
      "updateDate": "2026-03-24",
      "versionCode": "id119hr3546"
    },
    "title": "Prescription Drug Price Relief Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prescription Drug Price Relief Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to review brand-name drugs annually for excessive pricing and, if a drug is found to be priced excessively, to void any exclusivity granted to its sponsor.</p><p>Specifically, HHS must review all brand-name drug prices at least annually and upon petition. If any such drugs are found to be excessively priced, HHS must (1) void any government-granted exclusivity; (2) issue open, nonexclusive licenses for the drugs; and (3) expedite the review of corresponding applications for generic drugs and biosimilar biological products. HHS must also create a public database with its determinations for each drug.</p><p>An entity accepting an open, nonexclusive license under these provisions must pay a reasonable royalty to the holder of the relevant patent or approved new drug application, and must price the generic drug or\u00a0biosimilar below the excessive rate.</p><p>Under the bill, a price is considered excessive if the domestic average manufacturing price exceeds the median price for the drug in Canada, the United Kingdom, Germany, France, and Japan. If a price does not meet this criteria, or if pricing information is unavailable in at least three of these countries, the price is still considered excessive if it is higher than reasonable in light of specified factors, including development cost, revenue, and the size of the affected patient population.</p><p>The bill also requires drug manufacturers to report specified financial information for brand-name drugs, including research and advertising expenditures.</p>",
      "updateDate": "2026-03-24",
      "versionCode": "id119hr3546"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3546ih.xml"
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
      "title": "Prescription Drug Price Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prescription Drug Price Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To significantly lower prescription drug prices for patients in the United States by ending government-granted monopolies for manufacturers who charge drug prices that are higher than the median prices at which the drugs are available in other countries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T04:18:36Z"
    }
  ]
}
```
