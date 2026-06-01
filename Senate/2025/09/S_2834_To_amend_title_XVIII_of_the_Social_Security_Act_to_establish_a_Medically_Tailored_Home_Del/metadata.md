# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2834?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2834
- Title: Medically Tailored Home-Delivered Meals Program Pilot Act
- Congress: 119
- Bill type: S
- Bill number: 2834
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2025-12-05T22:48:18Z
- Update date including text: 2025-12-05T22:48:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2834",
    "number": "2834",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
    "type": "S",
    "updateDate": "2025-12-05T22:48:18Z",
    "updateDateIncludingText": "2025-12-05T22:48:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T17:14:34Z",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "KS"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "LA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2834is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2834\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Booker (for himself, Mr. Marshall , Mr. Cassidy , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to establish a Medically Tailored Home-Delivered Meals Program to test a payment and service delivery model under part A of Medicare to improve clinical health outcomes and reduce the rate of readmissions of certain individuals.\n#### 1. Short title\nThis Act may be cited as the Medically Tailored Home-Delivered Meals Program Pilot Act .\n#### 2. Medically tailored home-delivered meals program\nPart E of title XVIII of the Social Security Act is amended by inserting after section 1866G ( 42 U.S.C. 1395cc\u20137 ) the following new section:\n1866H. Medically tailored home-delivered meals program (a) Establishment For the 6-year period beginning not later than 30 months after the date of the enactment of this section, subject to subsection (f), the Secretary shall conduct, in accordance with the provisions of this section, a Medically Tailored Home-Delivered Meals Program (in this section referred to as the Program ) under which selected hospitals provide medically tailored home-delivered meals under part A of this title to qualified individuals to improve clinical health outcomes and reduce the rate of readmissions of such individuals. (b) Selection of hospitals To participate in program (1) Selected hospitals Under the Program, the Secretary shall, not later than June 30, 2027, select to participate in the Program at least, subject to subsection (f), 40 eligible hospitals that attest to the Secretary that they have the capacity to satisfy the requirements described in subsection (c). In this section, each such eligible hospital so selected shall be referred to as a selected hospital . (2) Eligible hospitals For purposes of this section, the term eligible hospital means a subsection (d) hospital (as defined in section 1886(d)(1)(B)) or a critical access hospital (as described in section 1820(c)(2)) that\u2014 (A) submits to the Secretary an application, at such time and in such form and manner as specified by the Secretary, that contains\u2014 (i) an attestation (in such form and manner as specified by the Secretary) that such hospital has the ability, or has an arrangement with providers of services or suppliers or other entities that have the ability, to furnish the services described in subsection (c); and (ii) such other information as the Secretary may require; (B) in the case of a subsection (d) hospital, has, for the 2 most recent fiscal years ending prior to the date of selection by the Secretary under paragraph (1), averaged at least 3 stars for the overall hospital quality star rating posted on the internet website of the Centers for Medicare & Medicaid Services (including Care Compare or a successor website); and (C) meets, as of the date of selection by the Secretary under paragraph (1), program integrity requirements, as determined by the Secretary. (c) Minimum program requirements Under the Program, a selected hospital shall comply with each of the following requirements: (1) Staffing The selected hospital shall provide (including through an arrangement described in subsection (b)(2)(A)(i)), for the duration of the participation of the hospital under the Program, a physician, registered dietitian or nutrition professional, or Advanced Practice Nursing Professional clinical social worker to carry out the screening and re-screening pursuant to paragraph (2) and medical nutrition therapy pursuant to paragraph (3)(B). (2) Screening and re-screening The selected hospital (including through arrangements described in subsection (b)(2)(A)(i)) shall\u2014 (A) as part of the discharge planning process described in section 1861(ee), screen individuals that are inpatients of such selected hospital with validated screening tools approved or deemed to be approved by the Secretary to determine whether such individuals are qualified individuals pursuant to subsection (g)(3); and (B) in the case of an individual that was an inpatient of such selected hospital and was screened pursuant to subparagraph (A) and determined to be a qualified individual, re-screen such individual with validated screening tools (as determined by the Secretary) every 12 weeks after such determination occurring during the participation of the hospital under the Program to determine whether such individual continues to be a qualified individual. (3) Providing medically tailored home-delivered meals and medical nutrition therapy In the case of an individual that is determined by the selected hospital pursuant to subsection (g)(3) to be a qualified individual, the selected hospital (including through arrangements described in subsection (b)(2)(A)(i)) shall, with respect to the period during which such hospital is participating in the Program\u2014 (A) provide, for each day during a period of at least 12 weeks following the screen pursuant to paragraph (2)(A) and for each subsequent 12-week period after the rescreen pursuant to paragraph (2)(B), for the duration of the Program, for the preparation and delivery to such individual of at least 2 medically tailored home-delivered meals (or a portioned equivalent) that meet at least two-thirds of the daily nutritional needs of the qualified individual and are responsive to the individual\u2019s medical and cultural needs (such as an allergy or dietary restrictions or other religious or cultural dietary needs); and (B) provide to such qualified individual, in connection with delivering such meals and for a period of at least 12 weeks and not more than 1 year, medical nutrition therapy. (4) Data submission The selected hospital shall submit to the Secretary data, in such form, manner, and frequency as designated by the Secretary, so that the Secretary may determine the effect of the Program with respect to the factors described in subsection (e)(2)(B). (d) Payment; cost-Sharing (1) Payment The Secretary shall determine the form, manner, and amount of payment to be provided to a selected hospital under the Program, taking into consideration payment amounts from other payers for similar food-related services. (2) Cost-sharing Items and services for which payment may be made under the Program shall be provided without application of deductibles, copayments, coinsurance, or other cost-sharing under this title. (e) Monitoring and evaluations (1) Program monitoring The Secretary shall monitor claims and other data submitted to the Secretary of each qualified individual receiving food under the Program for the purpose of determining whether the Program improves health outcomes for qualified individuals. (2) Intermediate and final evaluations and reports The Secretary shall conduct an intermediate and final evaluation of the Program. Each such evaluation shall\u2014 (A) with respect to individuals determined to be qualified individuals and receiving food and for the relevant periods, determine\u2014 (i) an analysis of inpatient admissions of such individuals after the initial inpatient admission, and the diagnosis-related groups for such admissions; (ii) the number of admissions to other post-acute care services of such individuals, and the reasons for such admissions; and (iii) the total expenditures under part A with respect to such individuals; (B) report the following, with a comparison to comparable beneficiaries not participating in the Program\u2014 (i) an assessment of clinical health outcomes, as defined by the Secretary; (ii) changes in the total cost of care under part A (including costs associated with readmission as defined in section 1886(q)(5)(E)); and (iii) patient and caregiving experience, including whether such individuals would have continued to receive the food if they were required to pay for it; (C) obtain information from hospitals about payments made under the Program, including whether such payments met or exceeded such hospitals\u2019 cost incurred in providing services under the Program; and (D) include an analysis of health outcomes of individuals receiving items and services under the Program compared to health outcomes of individuals not receiving items and services under the Program. (3) Reports The Secretary shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate\u2014 (A) not later than 3 years after the date of implementation of the Program, a report with respect to the intermediate evaluation under paragraph (2); and (B) not later than 8 years after such date of implementation, a report with respect to the final evaluation under such paragraph. (f) Funding (1) In general Payments for items and services furnished under the Program and funds necessary for the costs of carrying out the Program shall be made from the Federal Hospital Insurance Trust Fund under section 1817. (2) Budget neutrality The Secretary shall reduce payments made to subsection (d) hospitals under section 1886(d) in a manner such that the total amount of such reductions for a year are estimated to be equal to the total amount of payments made under the Program during such year. (g) Definitions In this section: (1) Medical nutrition therapy The term medical nutrition therapy has the meaning given such term in section 1861(vv)(1). (2) Medically tailored home-delivered meal The term medically tailored home-delivered meal means, with respect to a qualified individual, a meal that is designed by a registered dietitian or nutrition professional for the treatment plan of the qualified individual. (3) Qualified individual The term qualified individual means an individual, who\u2014 (A) is entitled to benefits under part A and is not receiving similar benefits from other State or Federal programs, as reported by the individual; (B) has a diet-impacted disease (such as kidney disease, congestive heart failure, diabetes, chronic obstructive pulmonary disease, or any other disease the Secretary determines appropriate); (C) at the time of discharge from a selected hospital or rescreening\u2014 (i) lives at home; (ii) is not eligible for or admitted to extended care services (as defined in section 1861(h)); (iii) has not made an election under section 1812(d)(1) to receive hospice care; (iv) is limited with respect to at least 2 of the activities of daily living (as described in section 7702B(c)(2)(B) of the Internal Revenue Code of 1986); and (v) meets any other criteria for high-risk of readmission (as determined by the Secretary). (4) Registered dietitian or nutrition professional The term registered dietitian or nutrition professional has the meaning given such term in section 1861(vv)(2). .",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-09-17",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5439",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
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
        "updateDate": "2025-11-17T18:34:10Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2834is.xml"
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
      "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medically Tailored Home-Delivered Meals Program Pilot Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to establish a Medically Tailored Home-Delivered Meals Program to test a payment and service delivery model under part A of Medicare to improve clinical health outcomes and reduce the rate of readmissions of certain individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:28Z"
    }
  ]
}
```
