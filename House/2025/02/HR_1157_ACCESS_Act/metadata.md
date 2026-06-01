# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1157
- Title: ACCESS Act
- Congress: 119
- Bill type: HR
- Bill number: 1157
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2026-02-12T09:06:30Z
- Update date including text: 2026-02-12T09:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1157",
    "number": "1157",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "ACCESS Act",
    "type": "HR",
    "updateDate": "2026-02-12T09:06:30Z",
    "updateDateIncludingText": "2026-02-12T09:06:30Z"
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
          "date": "2025-02-10T17:02:15Z",
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
          "date": "2025-02-10T17:02:10Z",
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
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "UT"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1157ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1157\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Steube (for himself and Mrs. Cammack ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo allow individuals to elect to receive contributions to a health savings account in lieu of reduced cost-sharing under health insurance obtained through a health insurance Exchange.\n#### 1. Short title\nThis Act may be cited as the Affordable Care and Comprehensive Economic Support through Savings Act or the ACCESS Act .\n#### 2. Health savings account contributions in lieu of reduced cost-sharing\n##### (a) In general\nSection 223 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(i) Health savings account contributions in lieu of reduced cost-Sharing for Exchange-Provided plans (1) In general In the case of any eligible insured who is enrolled in an Exchange-provided high deductible health plan for any month and who elects (at such time and in such manner as the Secretary may provide) the application of this subsection\u2014 (A) section 1402 of the Patient Protection and Affordable Care Act shall not apply to such individual for such month, (B) the health insurance issuer offering such plan shall make a payment to a health savings account of such individual for such month in an amount equal to 1/12 of the annual reduced cost-sharing actuarial equivalent amount, and (C) the Secretary shall make payments to such health insurance issuer in amounts which are equal to the payments made by such issuer under subparagraph (B). (2) Annual reduced cost-sharing actuarial equivalent amount For purposes of this section, the term annual reduced cost-sharing actuarial equivalent amount means, with respect to any Exchange-provided high deductible health plan enrolled in by an eligible insured, an amount that would produce an actuarial value equal to the actuarial value of the reduction in cost-sharing (as determined under section 1402 of the Patient Protection and Affordable Care Act and without regard to any election under this subsection) for the plan year determined by taking into account the household income of the eligible insured. (3) Restriction on distributions (A) In general Any trust which receives a payment described in paragraph (1)(B) shall not be treated as a health savings account for purposes of this section unless the terms of such trust require that, during any month during which such a payment is received, no distribution may be made from such trust unless such distribution is made to satisfy a charge properly made to a qualified medical debit card. (B) Qualified medical debit card For purposes of this paragraph, the term qualified medical debit card means a debit card which\u2014 (i) is issued by a bank (as defined in section 408(n)), (ii) is provided by the trustee of the health savings account to the designated beneficiary, and (iii) is encoded in such a manner that the only expenses which may charged with such card are amounts paid for medical care (as defined in section 213(d)). (4) Recapture of excess payments For purposes of applying the recapture rules of section 36B(f)(2)\u2014 (A) payments made to the health savings account of an individual under paragraph (1)(B) shall be treated as an advance payment of the credit allowed under section 36B, and (B) the credit allowed under section 36B shall be treated as having been increased by the payments which would have been made to the health savings account of such individual under paragraph (1)(B) if such payments had been determined using the household income of such individual for the taxable year referred to in such section. (5) Other definitions and special rules For purposes of this section\u2014 (A) Exchange-provided high deductible health plan The term Exchange-provided high deductible health plan means, with respect to any eligible insured, any high deductible health plan enrolled in by such eligible insured through an Exchange established under the Patient Protection and Affordable Care Act. (B) Eligible insured The term eligible insured has the meaning given such term in section 1402(b) of the Patient Protection and Affordable Care Act. (C) Coordination with contribution limits; etc The payments described in paragraph (1)(B) shall not fail to be taken into account under this section as contributions to the health savings account to which paid and such payments shall not be required to be made to the extent that the eligible insured does not have a health savings account or such account is prohibited from accepting such payment by reason of subsection (d)(1)(A)(ii). .\n##### (b) Requirements related to Exchange-Provided high deductible health plans\nSection 1301(a) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18021(a) ) is amended by adding at the end the following new paragraph:\n(5) Requirements related to high deductible health plans (A) Requirement to offer high deductible health plan as alternative A health plan in the silver level of coverage in the individual market which is not a high deductible health plan shall not be treated as a qualified health plan unless the health insurance issuer offering such plan offers a high deductible health plan which is actuarially equivalent to such plan to any individual who would be an eligible insured (as defined in section 1402(b)) if such individual were enrolled in such plan. (B) Requirement to make health savings account contributions upon election of eligible insured A high deductible health plan shall not be treated as a qualified health plan unless the health insurance issuer offering such plan complies with the requirement of section 223(i)(1)(B) of such Code with respect to such plan. (C) Determination of actuarial value For purposes of this Act, the actuarial value of a high deductible health plan shall take into account payments made by the issuer to a health savings account of the enrollee pursuant to such plan. (D) High deductible health plan For purposes of this paragraph, the term high deductible health plan has the meaning given such term by section 223 of the Internal Revenue Code of 1986. .\n##### (c) Public education\nBeginning on January 1, 2026, each health insurance issuer offering coverage through an Exchange established under the Patient Protection and Affordable Care Act, and each such Exchange, shall provide all prospective enrollees\u2014\n**(1)**\ninformation regarding the availability of insurer-provided health savings account contributions in lieu of reduced cost-sharing for silver level high deductible health plans selected in the Exchange, and\n**(2)**\ninformation regarding how to establish and use a health savings account.\n##### (d) Permanent appropriation for cost-Sharing reduction payments and HSA contributions made in lieu of such payments\nNecessary amounts are appropriated to the Secretary of the Treasury for making payments described in section 1402(d)(3) of the Patient Protection and Affordable Care Act, and payments described in section 223(i)(1)(C) of the Internal Revenue Code of 1986 (as added by this section), for months beginning after December 31, 2025.\n##### (e) Effective date\nThe amendments made by this section shall apply to months beginning after December 31, 2025.",
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-04-24T16:19:28Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-24T16:19:28Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-24T16:19:28Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-04-24T16:19:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-14T14:33:27Z"
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
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1157ih.xml"
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
      "title": "ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Care and Comprehensive Economic Support through Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow individuals to elect to receive contributions to a health savings account in lieu of reduced cost-sharing under health insurance obtained through a health insurance Exchange.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:23Z"
    }
  ]
}
```
