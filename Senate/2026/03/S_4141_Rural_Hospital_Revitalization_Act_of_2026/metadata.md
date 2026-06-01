# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4141
- Title: Rural Hospital Revitalization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4141
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-03-30T16:11:02Z
- Update date including text: 2026-03-30T16:11:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-19: Introduced in Senate

## Actions

- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4141",
    "number": "4141",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Rural Hospital Revitalization Act of 2026",
    "type": "S",
    "updateDate": "2026-03-30T16:11:02Z",
    "updateDateIncludingText": "2026-03-30T16:11:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T16:50:31Z",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4141is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4141\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Mr. Bennet (for himself and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to direct the Secretary of Agriculture to make temporary zero-percent interest loans under the community facilities direct loan program to construct or renovate certain rural hospitals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Hospital Revitalization Act of 2026 .\n#### 2. Rural hospital revitalization loans\nSubtitle A of the Consolidated Farm and Rural Development Act is amended by inserting after section 306A ( 7 U.S.C. 1926a ) the following:\n306B. Rural hospital revitalization loans (a) In general Under the community facilities direct loan program established under section 306(a)(1) (referred to in this section as the community facilities direct loan program ), the Secretary shall make temporary zero-percent interest loans to eligible rural hospitals described in subsection (b) for the construction of replacement hospital facilities or the improvement or renovation of existing hospital facilities in accordance with this section. (b) Eligible hospitals (1) In general An eligible rural hospital described in this subsection is a rural hospital\u2014 (A) the campus (as defined in section 413.65(a)(2) of title 42, Code of Federal Regulations (or successor regulations)) of which is in a county with a population of less than 20,000 inhabitants; (B) (i) the campus (as so defined) of which is not less than 35 miles from the nearest hospital; (ii) if the campus (as so defined) of which is in an area with mountainous terrain or only secondary roads, as determined by the Secretary, such campus is not less than 15 miles from the nearest hospital; (iii) that is a critical access hospital (as defined in section 1861(mm)(1) of the Social Security Act ( 42 U.S.C. 1395x(mm)(1) )); or (iv) that is a rural emergency hospital (as defined in section 1861(kkk)(2) of that Act ( 42 U.S.C. 1395x(kkk)(2) )); (C) that has been continuously licensed as a hospital in the community in which the hospital is located for not less than 30 years; (D) that submits to the Secretary an application at such time, in such manner, and containing such information to determine eligibility under this paragraph and priorities under paragraph (2) and such other information as the Secretary may require, including\u2014 (i) a statement demonstrating the need for the loan, which shall describe\u2014 (I) the age and condition of existing facilities to be replaced, improved, or renovated, including a certification that funds from a loan under this section will not be used for facilities that have been significantly improved during the 10-year period preceding the date of the application; and (II) the manner in which the use of the loan funds will address issues relating to the quality and viability of the facilities to preserve access to healthcare; (ii) a demonstration that the hospital has had a positive impact in the community served by the hospital, which shall include\u2014 (I) a positive impact on access to primary healthcare, emergency services, and services required under conditions of participation applicable under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ); and (II) a meaningful economic impact; and (iii) a statement of the anticipated health and economic impacts of the loan, including\u2014 (I) an impact on sustaining the provision of services that the hospital currently provides; (II) an impact on offering healthcare services that the hospital does not currently offer, as appropriate; (III) an impact on the provision of community-based services, including such services that influence social determinants of health; (IV) any other economic impacts; and (V) impacts compared to the impacts if the loan funds were not made available; and (E) that, subject to paragraph (3), is financially stable, as measured by having\u2014 (i) not less than 30 days cash on hand; and (ii) a projected debt-service coverage ratio of at least 1.2. (2) Priorities In making loans under this section, the Secretary shall give priority to an eligible rural hospital\u2014 (A) that serves an area in which there are fewer than 6 inhabitants per square mile, taking into consideration\u2014 (i) the distance from the hospital to a population center; (ii) the travel time from the hospital to reach a population center or specific health service; and (iii) seasonal variations in the need for access to healthcare services; (B) that requires replacement, improvement, or renovation that is not financially feasible at the rates and terms offered under the community facilities direct loan program; (C) for which not less than 50 percent of its inpatient days or discharges and outpatient visits during the most recent cost reporting period for which data are available were attributable to\u2014 (i) individuals entitled to, or enrolled for, benefits under part A or enrolled for benefits under part B of title XVIII of the Social Security Act, including individuals enrolled in a Medicare Advantage plan under part C of such title; (ii) individuals eligible for medical assistance under a State plan under title XIX of the Social Security Act (or a waiver of such a plan); or (iii) self-pay individuals; or (D) that meets 2 or more of the criteria described in subparagraphs (A) through (C). (3) Waiver The Secretary may waive the requirements described in paragraph (1)(D) in the case of a hospital that demonstrates sufficient community impacts described in paragraph (1)(C)(ii). (4) Eligibility For purposes of making loans under this section, the Secretary shall consider an eligible rural hospital described in paragraph (1) to be eligible for the community facilities direct loan program. (c) Loan interest and terms (1) Initial interest-free loan Except as otherwise provided in this subsection, a loan made under this section shall, for the first 5 years of the loan\u2014 (A) have a zero percent interest rate; and (B) require repayment of principal for a period of 5 years, amortized\u2014 (i) in accordance with the expected amortization schedule of a loan under the community facilities direct loan program; and (ii) over a period that is equal to the lesser of\u2014 (I) the expected life of the facility being constructed or renovated; and (II) a maximum term of 40 years. (2) Assessment At the end of the 5-year period of a loan described in paragraph (1), the Secretary shall conduct an assessment of the financial stability of the eligible rural hospital to determine whether the hospital has the financial strength for the loan to be refinanced at the prevailing rates offered under the community facilities direct loan program. (3) Refinancing If the Secretary determines through an assessment under paragraph (2) that an eligible rural hospital has sufficient financial strength to repay a loan under the community facilities direct loan program, subject to subsection (d)(2), the Secretary shall refinance the loan under this section into a loan under the community facilities direct loan program\u2014 (A) at the prevailing interest rate applicable to a loan under the community facilities direct loan program; (B) without a requirement of the payment of any interest on the amount of principal repaid during the period in which the interest rate of the loan was zero percent; (C) based on the unpaid principal balance; and (D) amortized in accordance with the community facilities direct loan program for the remaining term of the loan. (d) Renewals (1) Failure under assessment (A) In general If the Secretary determines through an assessment under subsection (c)(2) that an eligible rural hospital does not have sufficient financial strength to repay a loan under the community facilities direct loan program, the hospital may submit to the Secretary an application for a 1-time renewal of the zero-percent interest loan in accordance with the terms described in subsection (c)(1) for 1 additional term of not more than 5 years. (B) Requirements To be eligible for the renewal of a zero-percent interest loan under subparagraph (A), an eligible rural hospital shall demonstrate in the application submitted under that subparagraph that the hospital\u2014 (i) has first applied for and accepted any available Federal technical assistance for rural hospitals to support operational improvements and improve financial stability; and (ii) continues to meet all applicable community facilities direct loan program eligibility criteria. (C) Refinancing At the end of the period for which a zero-percent interest loan is renewed under subparagraph (A), the Secretary shall refinance the loan into a loan under the community facilities direct loan program in accordance with subsection (c)(3). (2) Interest rate protection (A) In general If the Secretary determines through an assessment under subsection (c)(2) that an eligible rural hospital has sufficient financial strength to repay a loan under the community facilities direct loan program, and the interest rate applicable to a loan under the community facilities direct loan program is more than 2.5 percent, the hospital may submit to the Secretary an application for a 1-time renewal of the zero-percent interest loan in accordance with the terms described in subsection (c)(1) for 1 additional term of 5 years. (B) Requirements To be eligible for the renewal of a zero-percent interest loan under subparagraph (A), an eligible rural hospital shall demonstrate in the application submitted under that subparagraph that the hospital\u2014 (i) has had a positive impact on access to primary healthcare, emergency services, and services required under conditions of participation applicable under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) in the community served by the hospital; and (ii) has had positive impacts in the community described in subsection (b)(1)(C)(ii). (C) Refinancing During the period of a zero-percent interest loan that has been renewed under subparagraph (A), at any time that the interest rate applicable to a loan under the community facilities direct loan program is 2.5 percent or less, the eligible rural hospital may elect to refinance the loan into a loan under the community facilities direct loan program in accordance with subsection (c)(3). (3) Disapproval If the Secretary disapproves an application to renew a zero-percent interest loan under paragraph (1)(A) or (2)(A), the Secretary shall resolve the applicable issues in accordance with the procedures that apply to the community facilities direct loan program. (e) Technical assistance grants (1) In general A hospital that receives a loan under this section shall be eligible for assistance through an award under a covered program to support operational improvements and improve financial stability during\u2014 (A) the 5-year period of a zero-percent interest loan described in subsection (c)(1); and (B) any renewal of a zero-percent interest loan for a lack of sufficient financial strength under subsection (d)(1). (2) Covered program defined In this subsection, the term covered program means\u2014 (A) the Targeted Technical Assistance for Rural Hospitals Program of the Health Resources and Services Administration; and (B) the Rural Hospital Technical Assistance Program carried out by the rural development mission area, in cooperation with the National Rural Health Association. .",
      "versionDate": "2026-03-19",
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
        "updateDate": "2026-03-30T16:11:01Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4141is.xml"
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
      "title": "Rural Hospital Revitalization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T02:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Hospital Revitalization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Farm and Rural Development Act to direct the Secretary of Agriculture to make temporary zero-percent interest loans under the community facilities direct loan program to construct or renovate certain rural hospitals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:21Z"
    }
  ]
}
```
