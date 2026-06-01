# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5439?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5439
- Title: Medically Tailored Home-Delivered Meals Program Pilot Act
- Congress: 119
- Bill type: HR
- Bill number: 5439
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2026-04-28T08:06:39Z
- Update date including text: 2026-04-28T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-09-17 - IntroReferral: Sponsor introductory remarks on measure. (CR H4374-4375)
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-09-17 - IntroReferral: Sponsor introductory remarks on measure. (CR H4374-4375)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5439",
    "number": "5439",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000312",
        "district": "2",
        "firstName": "James",
        "fullName": "Rep. McGovern, James P. [D-MA-2]",
        "lastName": "McGovern",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:39Z",
    "updateDateIncludingText": "2026-04-28T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H4374-4375)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "ME"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "AL"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "WI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "WA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NJ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "IN"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "MN"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "MD"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "TN"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5439ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5439\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. McGovern (for himself, Ms. Malliotakis , Ms. Pingree , Mr. Fitzpatrick , and Mr. Evans of Pennsylvania ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to establish a Medically Tailored Home-Delivered Meals Program to test a payment and service delivery model under part A of Medicare to improve clinical health outcomes and reduce the rate of readmissions of certain individuals.\n#### 1. Short title\nThis Act may be cited as the Medically Tailored Home-Delivered Meals Program Pilot Act .\n#### 2. Medically tailored home-delivered meals program\nPart E of title XVIII of the Social Security Act is amended by inserting after section 1866G ( 42 U.S.C. 1395cc\u20137 ) the following new section:\n1866H. Medically tailored home-delivered meals program (a) Establishment For the 6-year period beginning not later than 30 months after the date of the enactment of this section, subject to subsection (f), the Secretary shall conduct, in accordance with the provisions of this section, a Medically Tailored Home-Delivered Meals Program (in this section referred to as the Program ) under which selected hospitals provide medically tailored home-delivered meals under part A of this title to qualified individuals to improve clinical health outcomes and reduce the rate of readmissions of such individuals. (b) Selection of hospitals To participate in program (1) Selected hospitals Under the Program, the Secretary shall, not later than June 30, 2027, select to participate in the Program at least, subject to subsection (f), 40 eligible hospitals that attest to the Secretary that they have the capacity to satisfy the requirements described in subsection (c). In this section, each such eligible hospital so selected shall be referred to as a selected hospital . (2) Eligible hospitals For purposes of this section, the term eligible hospital means a subsection (d) hospital (as defined in section 1886(d)(1)(B)) or a critical access hospital (as described in section 1820(c)(2)) that\u2014 (A) submits to the Secretary an application, at such time and in such form and manner as specified by the Secretary, that contains\u2014 (i) an attestation (in such form and manner as specified by the Secretary) that such hospital has the ability, or has an arrangement with providers of services or suppliers or other entities that have the ability, to furnish the services described in subsection (c); and (ii) such other information as the Secretary may require; (B) in the case of a subsection (d) hospital, has, for the 2 most recent fiscal years ending prior to the date of selection by the Secretary under paragraph (1), averaged at least 3 stars for the overall hospital quality star rating posted on the internet website of the Centers for Medicare & Medicaid Services (including Care Compare or a successor website); and (C) meets, as of the date of selection by the Secretary under paragraph (1), program integrity requirements, as determined by the Secretary. (c) Minimum program requirements Under the Program, a selected hospital shall comply with each of the following requirements: (1) Staffing The selected hospital shall provide (including through an arrangement described in subsection (b)(2)(A)(i)), for the duration of the participation of the hospital under the Program, a physician, registered dietitian or nutrition professional, Advanced Practice Nursing Professional, or clinical social worker to carry out the screening and re-screening pursuant to paragraph (2), medical nutrition therapy pursuant to paragraph (3)(B). (2) Screening and re-screening The selected hospital (including through arrangements described in subsection (b)(2)(A)(i)) shall\u2014 (A) as part of the discharge planning process described in section 1861(ee), screen individuals that are inpatients of such selected hospital with validated screening tools approved or deemed to be approved by the Secretary to determine whether such individuals are qualified individuals pursuant to subsection (h)(3); and (B) in the case of an individual that was an inpatient of such selected hospital and was screened pursuant to subparagraph (A) and determined to be a qualified individual, re-screen such individual with validated screening tools (as determined by the Secretary) every 12 weeks after such determination occurring during the participation of the hospital under the Program to determine whether such individual continues to be a qualified individual. (3) Providing medically tailored home-delivered meals and medical nutrition therapy In the case of an individual that is determined by the selected hospital pursuant to subsection (h)(3) to be a qualified individual, the selected hospital (including through arrangements described in subsection (b)(2)(A)(i)) shall, with respect to the period during which such hospital is participating in the Program\u2014 (A) provide, for each day during a period of at least 12 weeks following the screen pursuant to paragraph (2)(A) and for each subsequent 12-week period after the rescreen pursuant to paragraph (2)(B), for the duration of the Program, for the preparation and delivery to such individual of at least 2 medically tailored home-delivered meals (or a portioned equivalent) that meet at least two-thirds of the daily nutritional needs of the qualified individual and are responsive to the individual\u2019s medical and cultural needs (such as an allergy or dietary restrictions or other religious or cultural dietary needs); and (B) provide to such qualified individual, in connection with delivering such meals and for a period of at least 12 weeks and not more than 1 year, medical nutrition therapy. (4) Data submission The selected hospital shall submit to the Secretary data, in such form, manner, and frequency as designated by the Secretary, so that the Secretary may determine the effect of the Program with respect to the factors described in subsection (e)(2)(B). (d) Payment; cost-Sharing (1) Payment The Secretary shall determine the form, manner, and amount of payment to be provided to a selected hospital under the Program, taking into consideration payment amounts from other payers for similar food-related services. (2) Cost-sharing Items and services for which payment may be made under the Program shall be provided without application of deductibles, copayments, coinsurance, or other cost-sharing under this title. (e) Monitoring and evaluations (1) Program monitoring The Secretary shall monitor claims and other data submitted to the Secretary of each qualified individual receiving food under the Program for the purpose of determining whether the Program improves health outcomes for qualified individuals. (2) Intermediate and final evaluations and reports The Secretary shall conduct an intermediate and final evaluation of the Program. Each such evaluation shall\u2014 (A) with respect to individuals determined to be qualified individuals and receiving food and for the relevant periods, determine\u2014 (i) an analysis of inpatient admissions of such individuals after the initial inpatient admission, and the diagnosis-related groups for such admissions; (ii) the number of admissions to other post-acute care services of such individuals, and the reasons for such admissions; and (iii) the total expenditures under part A with respect to such individuals; (B) report the following, with a comparison to comparable beneficiaries not participating in the Program\u2014 (i) an assessment of clinical health outcomes, as defined by the Secretary; (ii) changes in the total cost of care under part A (including costs associated with readmission as defined in section 1866(q)(5)(E)); and (iii) patient and caregiving experience, including whether such individuals would have continued to receive the food if they were required to pay for it; (C) obtain information from hospitals about payments made under the Program, including whether such payments met or exceeded such hospitals\u2019 cost incurred in providing services under the Program; and (D) an analysis of health outcomes of individuals receiving items and services under the Program compared to health outcomes of individuals not receiving items and services in the Program. (3) Reports The Secretary shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate\u2014 (A) not later than 3 years after the date of implementation of the Program, a report with respect to the intermediate evaluation under paragraph (2); and (B) not later than 8 years after such date of implementation, a report with respect to the final evaluation under such paragraph. (f) Funding (1) In general Payments for items and services furnished under the Program and funds necessary for the costs of carrying out the Program shall be made from the Hospital Insurance Trust Fund under section 1817. (2) Budget neutrality The Secretary shall reduce payments made to subsection (d) hospitals under section 1886(d) in a manner such that the total amount of such reductions for a year are estimated to be equal to the total amount of payments made under the Program during such year. (g) Definitions In this section: (1) Medical nutrition therapy The term medical nutrition therapy has the meaning given such term in section 1861(vv)(1). (2) Medically tailored home-delivered meal The term medically tailored home-delivered meal means, with respect to a qualified individual, a meal that is designed by a registered dietitian or nutrition professional for the treatment plan of the qualified individual. (3) Qualified individual The term qualified individual means an individual, who\u2014 (A) is entitled to benefits under part A and is not receiving similar benefits from other state or Federal programs, as reported by the individual; (B) has a diet-impacted disease (such as kidney disease, congestive heart failure, diabetes, chronic obstructive pulmonary disease, or any other disease the Secretary determines appropriate); (C) at the time of discharge from a selected hospital or rescreening\u2014 (i) lives at home; (ii) is not eligible for or admitted to extended care services (as defined in section 1861(h)); (iii) has not made an election under section 1812(d)(1) to receive hospice care; (iv) is limited with respect to at least 2 of the activities of daily living (as described in section 7702B(c)(2)(B) of the Internal Revenue Code of 1986); and (v) meets any other criteria for high-risk of readmission (as determined by the Secretary). (4) Registered dietitian or nutrition professional The term registered dietitian or nutrition professional has the meaning given such term in section 1861(vv)(2). .",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2834",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
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
        "updateDate": "2025-11-17T18:33:06Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5439ih.xml"
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
      "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to establish a Medically Tailored Home-Delivered Meals Program to test a payment and service delivery model under part A of Medicare to improve clinical health outcomes and reduce the rate of readmissions of certain individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:16Z"
    }
  ]
}
```
