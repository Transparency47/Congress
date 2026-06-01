# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7953?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7953
- Title: FAIR ACT
- Congress: 119
- Bill type: HR
- Bill number: 7953
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-05-13T08:06:57Z
- Update date including text: 2026-05-13T08:06:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-17: Introduced in House

## Actions

- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7953",
    "number": "7953",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S000250",
        "district": "17",
        "firstName": "Pete",
        "fullName": "Rep. Sessions, Pete [R-TX-17]",
        "lastName": "Sessions",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FAIR ACT",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:57Z",
    "updateDateIncludingText": "2026-05-13T08:06:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T14:02:10Z",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7953ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7953\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Mr. Sessions (for himself and Mr. Peters ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo accelerate patient access to innovative medicines and clinical trials for life-threatening diseases by establishing a reciprocal approval mechanism with trusted international regulatory authorities.\n#### 1. Short title\nThis Act may be cited as the Fast-tracking Approval for Innovative Rare disease therapies Act or the FAIR ACT .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPatients in the United States often face significant delays in accessing innovative medicines compared to patients in other trusted nations.\n**(2)**\nThe lengthy regulatory process at the Food and Drug Administration contributes to the movement of clinical trials abroad, leading to fewer opportunities for United States patients to participate in cutting-edge research.\n**(3)**\nChina and other nations are rapidly expanding their clinical trial and biopharmaceutical development capacity, threatening United States leadership in biomedical innovation.\n**(4)**\nA reciprocal approval mechanism with trusted international regulatory authorities will accelerate access for United States patients to life-saving therapies and preserve the United States competitive position in biomedical research and innovation.\n#### 3. Reciprocal marketing approval for certain drugs\nThe Federal Food, Drug, and Cosmetic Act is amended by inserting after section 524B of such Act ( 21 U.S.C. 360n\u20132 ) the following:\n524C. Reciprocal marketing approval for certain drugs (a) In general A covered product with reciprocal marketing approval in effect under this section is deemed to be subject to an application or premarket notification for which an approval is in effect under section 505(c) or 510(k) of this Act or section 351(a) of the Public Health Service Act, as applicable. (b) Eligibility The Secretary shall, with respect to a covered product, grant reciprocal marketing approval if\u2014 (1) the sponsor of the covered product submits a request for reciprocal marketing approval; and (2) the request demonstrates to the Secretary\u2019s satisfaction that\u2014 (A) the covered product is lawfully marketed in a foreign country pursuant to an authorization from a trusted international regulatory authority of that country; (B) absent reciprocal marketing approval, the covered product is not approved for marketing, as described in subsection (a); (C) the Secretary has not, because of any concern relating to the safety or effectiveness of the covered product, rescinded or withdrawn any such approval; (D) the authorization to market the covered product in a foreign country pursuant to an authorization from a trusted international regulatory authority of that country has not, because of any concern relating to the safety or effectiveness of the covered product, been rescinded or withdrawn; and (E) the covered product is intended for use in the diagnosis, treatment, or mitigation of an immediately life-threatening disease or condition. (c) Request A request for reciprocal marketing approval shall\u2014 (1) be in such form, be submitted in such manner, and contain such information as the Secretary determines necessary to determine whether the criteria listed in subsection (b)(2) are met; and (2) include, with respect to each trusted international regulatory authority that authorized a covered product to be lawfully marketed in the foreign country involved, as described in subsection (b)(2)(A), an English translation (if necessary) of the dossier issued by such regulatory authority to authorize such marketing. (d) Timing The Secretary shall issue an order granting, or declining to grant, reciprocal marketing approval with respect to a covered product not later than 30 days after the Secretary\u2019s receipt of a request under subsection (b)(1) for the product. (e) Labeling; post-Market requirements During the 30-day period described in subsection (d), the Secretary shall finalize\u2014 (1) the form and content of the labeling for a covered product for which reciprocal marketing approval is to be granted; and (2) any postmarket studies the Secretary determines necessary to ensure the safety and effectiveness of such product. (f) Applicability of relevant provisions The provisions of this Act shall apply with respect to a covered product for which reciprocal marketing approval is in effect to the same extent and in the same manner as such provisions apply with respect to a product for which approval of an application or premarket notification under section 505(c) or 510(k) of this Act or section 351(a) of the Public Health Service Act, as applicable, is in effect. (g) Withdrawal of reciprocal marketing approval (1) In general The Secretary may, at any time, withdraw or suspend reciprocal marketing approval with respect to a covered product granted under this section if\u2014 (A) new clinical or real-world evidence demonstrates that the product presents an unreasonable risk of serious adverse events or mortality; or (B) the trusted international regulatory authority that originally authorized the covered product has rescinded or suspended its approval in the applicable foreign country. (2) Effect of withdrawal or suspension If the withdrawal or suspension under paragraph (1) is based on adverse event reports occurring within the first 30 days after reciprocal marketing approval, the Secretary shall provide public notice and may require immediate cessation of marketing and distribution. (3) Phase-out option The Secretary may implement a phase-out plan for withdrawal under paragraph (1), including patient transition measures, to protect public health while minimizing disruption to ongoing treatment. (h) Fees for request For purposes of imposing fees under chapter VII, a request for reciprocal marketing approval under this section shall be treated as an application or premarket notification for approval under section 505(c) or 510(k) or section 351(a) of the Public Health Service Act, as applicable. (i) Report Not later than 5 years after the date of enactment of this section, the Secretary shall submit to the Committee on Energy and Commerce and the Committee on Ways and Means of the House of Representatives and the Committee on Finance and the Committee on Health, Education, Labor, and Pensions of the Senate a comprehensive report on\u2014 (1) the effectiveness of the reciprocal marketing approval program under this section in accelerating access to innovative medicines in the United States; (2) the number of reciprocal marketing approvals of covered products granted or denied under this section; (3) the impact of the reciprocal marketing approval program under this section on patient safety and adverse event reporting; and (4) recommendations for the continuation, modification, or termination of the reciprocal marketing approval program under this section. (j) Definitions In this section: (1) Covered product The term covered product means a drug, including a biological product (as defined in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) )). (2) Immediately life-threatening disease or condition The term immediately life-threatening disease or condition has the meaning given such term in section 312.300(b)(1) of title 21, Code of Federal Regulations (or successor regulations). (3) Trusted international regulatory authority The term trusted international regulatory authority means\u2014 (A) the European Medicines Agency; (B) the Medicines and Healthcare Products Regulatory Agency of the United Kingdom; (C) Health Canada; and (D) any other international regulatory authority designated by the Secretary of Health and Human Services. .\n#### 4. Reciprocal allowance of clinical investigations authorized by trusted international regulatory authorities\nChapter V of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 351 et seq. ) is amended by inserting after section 569B ( 21 U.S.C. 360bbb\u20138b ) the following:\n569B\u20131. Reciprocal allowance of clinical investigations authorized by trusted international regulatory authorities (a) In general A manufacturer may seek reciprocal allowance to conduct a clinical trial under section 505(i) of this Act or section 351(a)(3) of the Public Health Service Act with respect to a qualified product by submitting an application for such allowance to the Secretary. (b) Application A manufacturer seeking reciprocal allowance under subsection (a) to conduct a clinical investigation as described in subsection (a) shall submit to the Secretary an application containing\u2014 (1) the authorization by a trusted international regulatory authority to conduct the same clinical investigation with respect to a qualified product in the applicable foreign country; and (2) any supporting documentation for such authorization. (c) Treatment The Secretary shall, for purposes of applying section 505(i) of this Act or section 351(a)(3) of the Public Health Service Act\u2014 (1) treat an application for reciprocal allowance with respect to a qualified product under this section as meeting the criteria applicable to a submission under section 505(i)(2) of this Act (or pursuant to section 351(a)(3) of the Public Health Service Act) with respect to beginning a clinical investigation of a new drug (or biological product); and (2) pursuant to that treatment, issue an order allowing, or declining to allow, a reciprocal allowance with respect to such qualified product not later than 30 days after the Secretary\u2019s receipt of a request under subsection (b) for the product. (d) Applicability of provisions The provisions of section 505(i) of this Act and section 351(a)(3) shall apply with respect to an application for reciprocal allowance under this section to the same extent and in the same manner as such provisions apply to an investigational new drug application under section 505(i) of this Act or section 351(a)(3) of the Public Health Service Act. (e) Protocol modifications The Secretary may request, before the end of the 30-day period specified in subsection (c)(2), that the manufacturer requesting a reciprocal allowance with respect to a clinical investigation under this section modify the protocols for such clinical investigation. The Secretary shall, notwithstanding a request for modification of protocols under this subsection, grant, or decline to grant such reciprocal allowance within such 30-day period. (f) Qualified product defined In this section, the term qualified product means a covered product (as defined in section 524B) that is intended for use in the diagnosis, treatment, or mitigation of an immediately life-threatening disease or condition. .",
      "versionDate": "2026-03-17",
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
        "updateDate": "2026-04-01T14:20:23Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7953ih.xml"
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
      "title": "FAIR ACT",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T12:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR ACT",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fast-tracking Approval for Innovative Rare disease therapies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To accelerate patient access to innovative medicines and clinical trials for life-threatening diseases by establishing a reciprocal approval mechanism with trusted international regulatory authorities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T12:18:23Z"
    }
  ]
}
```
