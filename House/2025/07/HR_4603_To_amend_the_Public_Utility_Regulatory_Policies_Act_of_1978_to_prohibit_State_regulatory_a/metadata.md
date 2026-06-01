# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4603?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4603
- Title: FAIR Act
- Congress: 119
- Bill type: HR
- Bill number: 4603
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2025-09-10T14:41:57Z
- Update date including text: 2025-09-10T14:41:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4603",
    "number": "4603",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John J. [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "FAIR Act",
    "type": "HR",
    "updateDate": "2025-09-10T14:41:57Z",
    "updateDateIncludingText": "2025-09-10T14:41:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
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
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:03:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4603ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4603\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Mr. McGuire introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to prohibit State regulatory authorities from approving rates charged by electric utilities that engage in certain diversity, equity, or inclusion practices, or that consider environmental, social, or governance factors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair, Affordable and Inclusive Rates Act or the FAIR Act .\n#### 2. Prohibition on approval of certain rates under PURPA\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621 ) is amended by adding at the end the following:\n(22) Diversity, Equity, or Inclusion (DEI) practice No State regulatory authority shall approve the rate of a State regulated electric utility if such State regulated electric utility engages in, or retains or employs a consultant or an advisor to promote or enforce, a diversity, equity, or inclusion practice, such as a practice\u2014 (A) discriminating for or against any person on the basis of race, color, ethnicity, religion, biological sex, or national origin; or (B) requiring, as a condition of employment, promotion, advancement, or the ability to speak, make presentations, or submit written materials, that an employee\u2014 (i) undergo training, education, coursework, or other pedagogy asserting that any particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged; or (ii) sign or assent to any statement, code of conduct, work program, plan, or similar device that asserts that any particular race, color, ethnicity, religion, biological sex, or national origin is inherently or systemically superior or inferior, oppressive or oppressed, or privileged or unprivileged. (23) Environmental, social, or governance (ESG) factors (A) In general Subject to subparagraph (B), no State regulatory authority shall approve the rate of a State regulated electric utility if such State regulated electric utility considers environmental, social, or governance factors in establishing rates or making operational decisions that affect rates. (B) Compliance Nothing in this paragraph shall be construed to prohibit a State regulated electric utility from complying with\u2014 (i) a Federal law or regulation requiring specific ESG factors if complying with such Federal law or regulation\u2014 (I) is limited to fulfilling the direct legal obligation of such Federal law or regulation; and (II) does not involve discretionary consideration of ESG factors beyond such direct legal obligation; or (ii) a State law or regulation that require such State regulated electric utility to purchase from certain types of generation sources if complying with such State law or regulation\u2014 (I) is limited to fulfilling the direct legal obligation; and (II) does not involve discretionary consideration of ESG factors beyond such obligation. (C) Environmental, social, or governance factor or ESG factor defined The term environmental, social, or governance factor or ESG factor means any factor relating to\u2014 (i) environmental considerations, including climate change policies, carbon emissions reductions, or environmental justice initiatives, unless directly tied to pecuniary impacts such as cost reduction, reliability enhancement, or compliance with Federal or State law or regulation; (ii) social considerations, including\u2014 (I) corporate board or workforce composition quotas based on race, color, ethnicity, sex, or national origin; or (II) supplier diversity programs that grant preferences based on race, color, ethnicity, sex, or national origin, unless such programs are required by applicable Federal or State law; or (iii) governance considerations, including the adoption of corporate governance policies primarily for the purpose of advancing political, ideological, or social objectives unrelated to pecuniary outcomes relevant to State regulated electric utility operations, customer service, or ratepayer cost impacts. .",
      "versionDate": "2025-07-22",
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
        "name": "Energy",
        "updateDate": "2025-09-10T14:41:57Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4603ih.xml"
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
      "title": "FAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair, Affordable and Inclusive Rates Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to prohibit State regulatory authorities from approving rates charged by electric utilities that engage in certain diversity, equity, or inclusion practices, or that consider environmental, social, or governance factors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:27Z"
    }
  ]
}
```
