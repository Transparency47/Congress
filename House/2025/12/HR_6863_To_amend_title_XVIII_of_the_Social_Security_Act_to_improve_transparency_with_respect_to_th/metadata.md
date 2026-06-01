# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6863?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6863
- Title: CAT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6863
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-22T15:07:05Z
- Update date including text: 2026-01-22T15:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6863",
    "number": "6863",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CAT Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-22T15:07:05Z",
    "updateDateIncludingText": "2026-01-22T15:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-18T14:02:30Z",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6863ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6863\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Harder of California (for himself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to improve transparency with respect to the suspension of Medicare payments pending an investigation into a credible allegation of fraud.\n#### 1. Short title\nThis Act may be cited as the Centers for Medicare & Medicaid Services Auditor Transparency Act of 2025 or the CAT Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2020, 139,000,000 individuals received health care coverage through the Medicare or Medicaid programs, costing the Federal Government approximately $1,500,000,000,000. Of these funds paid by United States taxpayers, $3,100,000,000 were discovered to have been fraudulent claims.\n**(2)**\nEnsuring the integrity of the Medicare and Medicaid programs is crucial to preventing fraud, waste, and abuse and safeguarding the financial sustainability of these important programs.\n**(3)**\nEven though the Centers for Medicare & Medicaid Services (CMS) utilization of Unified Program Integrity Contractors (UPICs) has shown to be effective at identifying bad actors defrauding the Federal Government through the Medicare and Medicaid programs, current Federal law and regulations have shown to be harmful to most providers who are submitting Medicare and Medicaid claims in good faith.\n**(4)**\nExisting law provides CMS and UPICs broad authority and discretion to suspend Medicare payments for up to a year pending the investigation of credible allegations of fraud .\n**(5)**\nHowever, current law does not require adequate transparency from CMS or UPICs into the nature of the alleged fraud before Medicare payments are suspended. Current law also does not require CMS or UPICs to provide adequate due process to providers whose payments have been suspended to challenge or cure the allegations of fraud prior to the suspension of Medicare payments.\n**(6)**\nIn addition, anecdotal reports have shown that some UPICs extend the suspension of Medicare payments on a routine basis so that they may have additional time to finish their audit despite not providing evidence that the continuation of a payment suspension is necessary to protect the integrity of the Medicare program.\n**(7)**\nThe broad authority to suspend Medicare payments pending the investigation of a credible allegation of fraud without adequate due process or transparency places the financial viability of many Medicare providers acting in good faith at risk.\n**(8)**\nIf Medicare providers acting in good faith close their doors as a result of the unnecessary suspension of payments by CMS or UPICs, Medicare beneficiaries and the American public could face additional barriers to access to necessary health care services as a direct result of unfair Federal law and regulations.\n#### 3. Improving transparency in suspension of payments pending investigation of credible allegations of fraud under Medicare\n##### (a) In general\nSection 1862(o) of the Social Security Act ( 42 U.S.C. 1395y(o) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking The Secretary may suspend and inserting Subject to paragraph (5), the Secretary may suspend ; and\n**(B)**\nby inserting An investigation of a credible allegation of fraud, and the suspension of payment pending such investigation under the preceding sentence, may only exceed 180 days if the Secretary determines there is good cause to extend such investigation and suspension. at the end;\n**(2)**\nin paragraph (4)\u2014\n**(A)**\nby striking a fraud hotline tip (as defined by the Secretary) and inserting the following items ; and\n**(B)**\nby striking credible allegation of fraud. and inserting\ncredible allegation of fraud: (A) A fraud hotline tip (as defined by the Secretary). (B) Mere error (as defined by the Secretary). (C) A billing error found during the course of an audit that is attributable to human error. .\n**(3)**\nby adding at the end the following new paragraphs:\n(5) Transparency in suspension of payments (A) In general The Secretary may only suspend payments to a provider of services or supplier under this title pursuant to paragraph (1) if\u2014 (i) subject to subparagraph (B) , not later than 30 days before the date on which the payment suspension begins, the Secretary provides such provider of services or supplier with information about each credible allegation of fraud that is the basis for the payment suspension, including\u2014 (I) the specific nature of each credible allegation of fraud; (II) the date of the alleged fraud; and (III) the basis of the credible allegation of fraud, such as whether the allegation is based upon\u2014 (aa) a fraud hotline complaint; (bb) data mining of data with respect to claims for payment under this title, title XIX, or title XXI; or (cc) a pattern identified through audits of providers of services or suppliers; and (ii) not less frequently than once every 30 days during such payment suspension, the Secretary provides such provider of services or supplier with\u2014 (I) a detailed, up-to-date list of the findings of the investigation; (II) an anticipated timeline for the completion of the investigation; and (III) an opportunity to ask the Centers for Medicare & Medicaid Services questions regarding the payment suspension and the investigation. (B) Exception The Secretary may elect not to provide a provider of services or supplier with the information described in subparagraph (A)(i) if the provision of such information would compromise the integrity of the investigation, as determined by the Secretary in consultation with the Inspector General of the Department of Health and Human Services and State auditors (as appropriate). (C) Failure to provide information If the requirements described in subparagraph (A) are not met with respect to the suspension of payment to a provider of services or a supplier under this title, the Secretary shall immediately resume such payment, and shall pay to the provider of services or supplier the amounts not paid due to such suspension and any interest accrued with respect to such amounts. (D) Annual report Not later than 180 days after the end of each fiscal year (beginning with fiscal year 2025), the Secretary shall submit to Congress a report that includes the following information with respect to such fiscal year: (i) The number of payment suspensions issued as the result of a pending investigation of a credible allegation of fraud under this subsection, section 1860D\u201312(b)(7) (including as applied pursuant to section 1857(f)(3)(D)), or section 1903(i)(2)(C). (ii) The basis of each such credible allegation of fraud. (iii) The average duration of a payment suspension described in clause (i) . (iv) The average duration of an investigation of a credible allegation of fraud described in clause (i) . (v) If applicable, the average time between the completion of an investigation into a credible allegation of fraud described in clause (i) and the reinstatement of payments to the relevant provider of services or supplier. (6) Appeals Not later than 180 days after the date of the enactment of the CAT Act of 2025 , the Secretary shall provide an independent process by which a provider of services or supplier under this title that has received notice of a payment suspension due to a pending investigation of a credible allegation of fraud pursuant to this subsection may appeal such suspension and receive a resolution of such appeal in a timely manner. .\n##### (b) Stakeholder consultation\nIn developing the appeals process required under section 1862(o)(6) of the Social Security Act, as added by subsection (a), the Secretary of Health and Human Services shall consult with relevant stakeholders, including providers of services and suppliers under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), title XIX of such Act ( 42 U.S.C. 1396 et seq. ), and title XXI of such Act ( 42 U.S.C. 1397aa et seq. ), as determined appropriate by the Secretary.\n##### (c) Applicability\nThe amendments made by this section shall apply with respect to any investigation of a credible allegation of fraud under section 1862(o) of the Social Security Act ( 42 U.S.C. 1395y(o) ), section 1860D\u201312(b)(7) of such Act ( 42 U.S.C. 1395w\u2013112(b)(7) ) (including as applied pursuant to section 1857(f)(3)(D) of such Act ( 42 U.S.C. 1395w\u201327(f)(3)(D) )), or section 1903(i)(2)(C) of such Act ( 42 U.S.C. 1396b(i)(2)(C) ) that is initiated after the date of enactment of this Act.",
      "versionDate": "2025-12-18",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-01-22T15:07:04Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6863ih.xml"
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
      "title": "CAT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CAT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Centers for Medicare & Medicaid Services Auditor Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to improve transparency with respect to the suspension of Medicare payments pending an investigation into a credible allegation of fraud.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:29Z"
    }
  ]
}
```
