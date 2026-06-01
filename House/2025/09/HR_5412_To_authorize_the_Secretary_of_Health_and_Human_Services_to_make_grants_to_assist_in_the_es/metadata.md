# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5412?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5412
- Title: Food Farmacy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5412
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2026-01-09T09:06:41Z
- Update date including text: 2026-01-09T09:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5412",
    "number": "5412",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Food Farmacy Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:41Z",
    "updateDateIncludingText": "2026-01-09T09:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:05:20Z",
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
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5412ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5412\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mrs. Sykes (for herself, Ms. De La Cruz , and Ms. Bynum ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize the Secretary of Health and Human Services to make grants to assist in the establishment and operation of healthy food pharmacies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Food Farmacy Act of 2025 .\n#### 2. Finding\nCongress finds that the goal of healthy food pharmacies (also known as food farmacies ) is to improve the health outcomes of their patrons by expanding access to nutritious foods and providing nutritional guidance.\n#### 3. Grants for healthy food pharmacies\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by adding at the end the following:\n320C. Grants for healthy food pharmacies (a) Authority To make grants The Secretary, in consultation with the Secretary of Agriculture, may make grants to eligible entities to assist in the establishment and operation of healthy food pharmacies. (b) Use of grants A grant received by an eligible entity under this section shall be used for costs related to\u2014 (1) construction, conversion, or renovation of a healthy food pharmacy; (2) the acquisition of equipment for a healthy food pharmacy, including for a mobile food pharmacy; (3) staffing to operate a healthy food pharmacy and help connect patients to other programs that support health outcomes and combat food insecurity; and (4) the acquisition of food and materials necessary for food distribution by a healthy food pharmacy. (c) Eligibility (1) Eligible entities The following entities shall be eligible to receive a grant under this section: (A) A non-profit qualified health care provider. (B) A State or local government entity. (C) A Tribal organization. (2) Eligible healthy food pharmacies The Secretary may make a grant under this section with respect to a healthy food pharmacy if the healthy food pharmacy\u2014 (A) offers a range of services to its patrons, including access to healthy foods and nutritional guidance from a qualified health care professional; (B) is operated in a manner that prioritizes the provision of services to communities that are low income, rural, or facing food insecurity (as such terms may be defined by the Secretary); (C) provides food and nutritional guidance free of charge to individuals receiving benefits under Medicaid or the Supplemental Nutrition Assistance Program; and (D) is operated in a manner that supports the Food is Medicine initiative of the Department of Health and Human Services. (d) Application (1) In general To receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (2) Plan for continuation of grant activities As part of such an application, the Secretary shall require an eligible entity to submit a plan for continuing to carry out activities described in subsection (b) after the eligible entity is no longer receiving grant funds under this section, including a plan to retain staff hired using the grant funds. (e) Partnerships An eligible entity that receives a grant under this section may carry out activities using the amounts of the grant in partnership with other organizations seeking to reduce food insecurity and improve health outcomes. (f) Limitation on grant amounts The Secretary may not award to an eligible entity more than $500,000 in grants under this section for a fiscal year. (g) Authority To waive certain requirements The Secretary may waive requirements of title XI of the Social Security Act as may be necessary solely for the purposes of carrying out a program under this section. (h) Reporting requirements (1) Reports to Secretary The Secretary may make a grant to an eligible entity under this section with respect to a healthy food pharmacy only if the eligible entity agrees to submit to the Secretary, on an annual basis for such period as the Secretary may prescribe, a report on the effectiveness of the activities funded with the amounts of the grant, including a description of\u2014 (A) the number of patrons served by the healthy food pharmacy; (B) the health needs of such patrons; (C) the repeated use of the healthy food pharmacy by such patrons; (D) the reported health outcomes of such patrons; (E) the types of food acquired by such patrons from the healthy food pharmacy; and (F) the assistance provided by the healthy food pharmacy to connect such patrons with other programs that address food insecurity and improve health outcomes. (2) Reports to Congress Not later than 2 years after the date of enactment of this section, and biennially thereafter during the term of the grant program under this section, the Secretary shall submit to Congress a report that summarizes the reports received by the Secretary under paragraph (1). (i) Definitions In this Act: (1) Eligible entity The term eligible entity means an entity described in subsection (c)(1). (2) Healthy food pharmacy The term healthy food pharmacy means an organization that provides to its patrons services that include\u2014 (A) access to nutritious foods that are representative of foods for a healthy diet, based on the Dietary Guidelines of the Department of Agriculture and guidance from the Secretary; and (B) nutritional guidance from a qualified health care professional. (3) Qualified health care professional The term qualified health care professional means\u2014 (A) a registered dietitian or nutrition professional, as defined by section 1861(vv)(2) of the Social Security Act ( 42 U.S.C. 1395x(vv)(2) ); (B) a physician, as defined by section 1861(r) of the Social Security Act ( 42 U.S.C. 1395x(r) ); and (C) a nurse practitioner, clinical nurse specialist, physician assistant, or other professional, as determined appropriate by the Secretary. (4) Qualified health care provider The term qualified health care provider means\u2014 (A) a provider of services, as defined by section 1861(u) of the Social Security Act ( 42 U.S.C. 1395x(u) ); (B) a physician organization, as defined by section 411.351 of title 42, Code of Federal Regulations (or successor regulations); (C) a rural health clinic, as defined by section 1861(aa)(2) of the Social Security Act ( 42 U.S.C. 1395x(aa)(2) ); (D) a Federally qualified health center, as defined by section 1887(aa)(4) of the Social Security Act ( 42 U.S.C. 1395x(aa)(4) ); or (E) another provider, as determined appropriate by the Secretary. (5) Secretary The term Secretary means the Secretary of Health and Human Services, acting through the Assistant Secretary for Health. (j) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $10,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-09-16",
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
        "updateDate": "2025-09-29T13:22:30Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5412ih.xml"
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
      "title": "Food Farmacy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Food Farmacy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Health and Human Services to make grants to assist in the establishment and operation of healthy food pharmacies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T05:33:23Z"
    }
  ]
}
```
