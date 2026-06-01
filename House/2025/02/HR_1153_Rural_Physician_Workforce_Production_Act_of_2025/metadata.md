# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1153
- Title: Rural Physician Workforce Production Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1153
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2025-10-22T08:05:23Z
- Update date including text: 2025-10-22T08:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-10 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1153",
    "number": "1153",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Rural Physician Workforce Production Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-22T08:05:23Z",
    "updateDateIncludingText": "2025-10-22T08:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-10T17:00:20Z",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "NE"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "HI"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "NM"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NM"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1153ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1153\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mrs. Harshbarger (for herself, Ms. Schrier , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to support rural residency training funding that is equitable for all States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Physician Workforce Production Act of 2025 .\n#### 2. Elective rural sustainability per resident payment for residents training in rural training locations\n##### (a) In general\nSection 1886 of the Social Security Act ( 42 U.S.C. 1395ww ) is amended by adding at the end the following new subsection:\n(u) Elective rural sustainability per resident payment amount for residents training in rural training locations (1) Determination of elective rural sustainability per resident payment amount (A) In general The elective rural sustainability per resident payment amount determined under this subsection for an applicable hospital (as defined in paragraph (7)(A)) that makes an election under paragraph (2), with respect to each full-time-equivalent resident in an approved medical residency training program that receives training in a rural training location (as defined in paragraph (7)(C)), is an amount equal to the difference between\u2014 (i) the total elective rural sustainability amount determined under subparagraph (B) (or, in the case of an applicable hospital not located in a rural area, the total elective rural sustainability amount or urban total elective rural sustainability amount, as applicable, determined under such subparagraph); and (ii) the amount (if any) the applicable hospital otherwise receives for direct graduate medical education costs under subsection (h) or section 1814(l), as applicable, with respect to each such resident. (B) Total elective rural sustainability amount (i) Establishment for initial cost reporting periods (I) In general Subject to subclause (II), for cost reporting periods beginning during the first year beginning on or after the date of the enactment of this subsection, the Secretary shall establish a total elective rural sustainability amount for time spent by each full-time-equivalent resident in an approved medical residency training program that receives training in a rural training location. Such amount shall be the amount that the Secretary determines is equal to the median national direct GME training costs per full-time-equivalent resident for 2015 described in table 9 on page 33 of the March 2018 GAO report on Physician Workforce (GAO\u201318\u2013240), updated for each subsequent year through the first year beginning on or after the date of the enactment of this subsection, by the annual percentage increase in the consumer price index for all urban consumers (all items; United States city average). (II) Application to urban hospitals For cost reporting periods beginning during the first year beginning on or after the date of the enactment of this subsection, in the case of an applicable hospital that is not located in a rural area\u2014 (aa) with respect to such residents that receive training in a rural track or an integrated rural track, the total elective rural sustainability amount per resident shall be equal to the amount established under subclause (I); and (bb) with respect to such residents that receive training in a rural training location and who are not participating in a rural track or an integrated rural track, the total elective rural sustainability amount per resident shall be equal to 50 percent of the amount established under subclause (I) (referred to in this subsection as the urban total elective rural sustainability amount ). (ii) Updating for subsequent cost reporting periods For each subsequent cost reporting period, the total elective rural sustainability amount under clause (i)(I) and clause (i)(II)(aa) and the urban total elective rural sustainability amount under clause (i)(II)(bb), respectively, are equal to such amounts determined under such clause for the previous cost reporting period updated, through the midpoint of the period, by projecting the estimated percentage change in the consumer price index for all urban consumers (all items; United States city average) during the 12-month period ending at that midpoint, with appropriate adjustments to reflect previous under- or over-estimations under this clause in the projected percentage change in the consumer price index for medical care services. (C) Clarification The total elective rural sustainability amount, the urban total elective rural sustainability amount, and the elective rural sustainability per resident payment amount determined under this paragraph shall not be discounted or otherwise adjusted based on the Medicare patient load (as defined in subsection (h)(3)(C)) of an applicable hospital or discharges in a diagnosis-related group. (2) Election For cost reporting periods beginning on or after the date that is 1 year after the date of the enactment of this subsection, an applicable hospital may elect to receive the elective rural sustainability per resident payment amount for each full-time-equivalent resident in an approved medical residency training program that receives training in a rural training location in accordance with this subsection. An applicable hospital may make an election under the preceding sentence regardless of whether the applicable hospital is otherwise eligible for a payment or adjustment for indirect and direct graduate medical education costs under subsections (d)(5)(B) and (h) or section 1814(l), as applicable, with respect to such residents. (3) Application The provisions of this subsection, or the application of such provisions to an applicable hospital\u2014 (A) shall not result in\u2014 (i) the establishment of a limitation on the number of residents in allopathic or osteopathic medicine for purposes of subsections (d)(5)(B) and (h) with respect to an approved medical residency training program of an applicable hospital (or be taken into account in determining such a limitation during the cap building period of an applicable hospital); or (ii) the counting of any resident with respect to which the applicable hospital receives an elective rural sustainability per resident payment amount under this subsection towards the application of the limitation described in clause (i) for purposes of subsections (d)(5)(B) and (h); and (B) shall not have any effect on the determination of\u2014 (i) the additional payment amount under subsection (d)(5)(B); or (ii) hospital-specific approved FTE resident amounts under subsection (h). (4) Allocation of payments In providing for payments under this subsection, the Secretary shall provide for an allocation of such payments between parts A and part B (and the trust funds established under the respective parts) as reasonably reflects the proportion of such costs associated with the provision of services under each respective part. (5) Eligibility for payment (A) In general An applicable hospital shall be eligible for payment of the elective rural sustainability per resident payment amount under this subsection for time spent by a resident training in a rural training location if the following requirements are met: (i) The resident spends the equivalent of at least 8 weeks over the course of their training in a rural training location. (ii) The hospital pays the salary and benefits of the resident for the time spent training in a rural training location. (B) Treatment of time spent in rural tracks or integrated rural tracks An applicable hospital shall be eligible for payment of the elective rural sustainability per resident payment amount under this subsection for all time spent by residents in an approved medical residency program (or separately defined track within a program) that provides more than 50 percent of the total residency training time in rural training locations, regardless of where the training occurs and regardless of specialty. (6) Determination of full-time-equivalent residents The determination of full-time-equivalent residents for purposes of this subsection shall be made in the same manner as the determination of full-time-equivalent residents under subsection (h)(4), but not taking into account the limitation under subparagraph (F) of such subsection. (7) Definitions In this subsection: (A) Applicable hospital The term applicable hospital means a hospital, critical access hospital, sole community hospital (as defined in subsection (d)(5)(D)(iii)), or rural emergency hospital (as defined in section 1861(kkk)(2)). (B) Approved medical residency training program; direct graduate medical education costs; resident The terms approved medical residency training program , direct graduate medical education costs , and resident have the meanings given those terms in subsection (h)(5). (C) Rural training location The term rural training location means a location in which training occurs that, based on the 2010 census or any subsequent census adjustment, meets one or more of the following criteria: (i) The training occurs in a location that is a rural area (as defined in section 1886(d)(2)(D)), not including any hospital treated as being located in a rural area pursuant to section 1886(d)(8)(E). (ii) The training occurs in a location that has a rural-urban commuting area code equal to or greater than 4.0. (iii) The training occurs in a sole community hospital (as defined in subsection (d)(5)(D)(iii)) or in a location that is within 10 miles of a sole community hospital. (8) Budget neutrality requirement The Secretary shall ensure that aggregate payments for direct medical education costs and indirect medical education costs under this title, including any payments under this subsection, for each year (effective beginning on or after the date that is 1 year after the date of enactment of this subsection) are not greater than the aggregate payments for such costs that would have been made under this title for the year without the application of this subsection. For purposes of carrying out the budget neutrality requirement under the preceding sentence, the Secretary may make appropriate adjustments to the amount of such payments for direct graduate medical education costs and indirect medical education costs under subsections (h) and (d)(5)(B), respectively. .\n##### (b) Treatment of critical access hospitals and sole community hospitals\n**(1) Critical access hospitals**\nSection 1814(l) of the Social Security Act ( 42 U.S.C. 1395f(l) ) is amended by adding at the end the following new paragraph:\n(6) For cost reporting periods beginning on or after the date that is 1 year after the date of enactment of this paragraph, the following shall apply: (A) A critical access hospital may elect to be treated as a hospital or as a non-provider setting for purposes of counting resident time for indirect medical education costs and direct graduate medical education costs for the time spent by the resident in that setting under subsections (d)(5)(B) and (h), respectively, of section 1886. (B) Direct medical education costs shall not be considered reasonable costs of a critical access hospital for purposes of payment under paragraph (1), to the extent that the critical access hospital is treated as a non-provider setting of another hospital or another hospital receives payment for such costs for the time spent by the resident in that setting pursuant to subsection (d)(5)(B), subsection (h), or subsection (u) of section 1886. .\n**(2) Sole community hospitals**\nSection 1886(d)(5)(D) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(D) ) is amended by adding at the end the following new clause:\n(vi) For cost reporting periods beginning on or after the date that is 1 year after the date of enactment of this paragraph, the hospital-specific payment amount determined under clause (i)(I) with respect to a sole community hospital shall not include direct medical education costs, to the extent that the sole community hospital receives payment for such costs for the time spent by the resident in that setting pursuant to subsection (u). .\n##### (c) Conforming amendments\n**(1)**\nSection 1886 of the Social Security Act ( 42 U.S.C. 1395ww ) is amended\u2014\n**(A)**\nin subsection (d)(5)(B), in the matter preceding clause (i), by striking The Secretary and inserting Subject to subsection (u), the Secretary ; and\n**(B)**\nin subsection (h)\u2014\n**(i)**\nin paragraph (1), by inserting subject to subsection (u) after 1861(v), ; and\n**(ii)**\nin paragraph (3), in the flush matter following subparagraph (B), by striking subsection (k) and inserting subsection (k) or subsection (u) .\n#### 3. Supporting new, expanding, and existing rural training tracks\n##### (a) Direct graduate medical education\nSection 1886(h) of the Social Security Act ( 42 U.S.C. 1395ww(h) ) is amended\u2014\n**(1)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (F)(i)\u2014\n**(i)**\nby striking 130 percent and inserting for cost reporting periods beginning on or after October 1, 1997, and before the date that is 1 year after the date of enactment of the Rural Physician Workforce Production Act of 2025 , 130 percent ; and\n**(ii)**\nby adding at the end the following: For cost reporting periods beginning on or after the date that is 1 year after the date of enactment of the Rural Physician Workforce Production Act of 2025 , such rules shall provide that any full-time-equivalent resident in an approved medical residency program (or separately defined track within a program) that provides more than 50 percent of the total residency training time in rural training locations (as defined in subsection (u)(6)(C)), regardless of where the training occurs and regardless of specialty, shall not be taken into account for purposes of applying the limitation under this subparagraph. ; and\n**(B)**\nin subparagraph (H)\u2014\n**(i)**\nin clause (i), in the second sentence, by inserting the following before the period: , in accordance with the second sentence of clause (i) of such subparagraph ; and\n**(ii)**\nin clause (iv), by inserting the following before the period: , in accordance with the second sentence of clause (i) of such subparagraph ; and\n**(2)**\nin paragraph (5), by adding at the end the following new subparagraph:\n(L) Special rules regarding application of elective rural sustainability per resident payment amount For special rules regarding application of the elective rural sustainability per resident payment amount under subsection (u), see paragraph (3) of such subsection. .\n##### (b) Indirect medical education\nSection 1886(d)(5)(B)(v) is amended\u2014\n**(1)**\nby striking 130 percent and inserting for cost reporting periods beginning on or after October 1, 1997, and before the date that is 1 year after the date of enactment of the Rural Physician Workforce Production Act of 2025 , 130 percent ; and\n**(2)**\nby adding at the end the following: For cost reporting periods beginning on or after the date that is 1 year after the date of enactment of the Rural Physician Workforce Production Act of 2025 , such rules shall provide that any full-time-equivalent resident in an approved medical residency program (or separately defined track within a program) that provides more than 50 percent of the total residency training time in rural training locations (as defined in subsection (u)(6)(C)), regardless of where the training occurs and regardless of specialty, shall not be taken into account for purposes of applying the limitation under this subparagraph. For special rules regarding application of the elective rural sustainability per resident payment amount under subsection (u), see paragraph (3) of such subsection. .",
      "versionDate": "2025-02-10",
      "versionType": "Introduced in House"
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
            "name": "Education programs funding",
            "updateDate": "2025-06-13T18:48:45Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-06-13T18:48:45Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-13T18:48:45Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-06-13T18:48:45Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-06-13T18:48:45Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-06-13T18:48:45Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-06-13T18:48:45Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-06-13T18:48:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-02T14:54:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1153",
          "measure-number": "1153",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1153v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural Physician Workforce Production Act of </strong><strong>2025</strong></p><p>This bill allows certain hospitals to receive additional payment under Medicare for full-time equivalent residents who receive training in rural areas.</p><p>Specifically, hospitals, critical access hospitals, sole community hospitals, and rural emergency hospitals may elect to receive payment for time spent by a resident in a rural training location if the resident trains for at least eight weeks in the location and the hospital pays the salary and benefits of the resident during this time. Additionally, hospitals may receive payment for all time spent by residents in a residency program in which 50% of all training is in rural locations, regardless of where the training occurs or specialty.</p><p>Payments are based on the difference between the total amount of eligible payments (as determined by the Centers for Medicare & Medicaid Services) and the amount of graduate medical education payments received (if applicable).</p>"
        },
        "title": "Rural Physician Workforce Production Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1153.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Physician Workforce Production Act of </strong><strong>2025</strong></p><p>This bill allows certain hospitals to receive additional payment under Medicare for full-time equivalent residents who receive training in rural areas.</p><p>Specifically, hospitals, critical access hospitals, sole community hospitals, and rural emergency hospitals may elect to receive payment for time spent by a resident in a rural training location if the resident trains for at least eight weeks in the location and the hospital pays the salary and benefits of the resident during this time. Additionally, hospitals may receive payment for all time spent by residents in a residency program in which 50% of all training is in rural locations, regardless of where the training occurs or specialty.</p><p>Payments are based on the difference between the total amount of eligible payments (as determined by the Centers for Medicare & Medicaid Services) and the amount of graduate medical education payments received (if applicable).</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1153"
    },
    "title": "Rural Physician Workforce Production Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Physician Workforce Production Act of </strong><strong>2025</strong></p><p>This bill allows certain hospitals to receive additional payment under Medicare for full-time equivalent residents who receive training in rural areas.</p><p>Specifically, hospitals, critical access hospitals, sole community hospitals, and rural emergency hospitals may elect to receive payment for time spent by a resident in a rural training location if the resident trains for at least eight weeks in the location and the hospital pays the salary and benefits of the resident during this time. Additionally, hospitals may receive payment for all time spent by residents in a residency program in which 50% of all training is in rural locations, regardless of where the training occurs or specialty.</p><p>Payments are based on the difference between the total amount of eligible payments (as determined by the Centers for Medicare & Medicaid Services) and the amount of graduate medical education payments received (if applicable).</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hr1153"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1153ih.xml"
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
      "title": "Rural Physician Workforce Production Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Physician Workforce Production Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to support rural residency training funding that is equitable for all States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T09:03:24Z"
    }
  ]
}
```
