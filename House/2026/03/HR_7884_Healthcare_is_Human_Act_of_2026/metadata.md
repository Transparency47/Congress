# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7884?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7884
- Title: Healthcare is Human Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7884
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-01T20:22:17Z
- Update date including text: 2026-04-01T20:22:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7884",
    "number": "7884",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Healthcare is Human Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-01T20:22:17Z",
    "updateDateIncludingText": "2026-04-01T20:22:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:01:15Z",
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
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7884ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7884\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Ms. Tenney (for herself and Mr. Horsford ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a tax credit to health care professionals that provide health care services in qualifying facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthcare is Human Act of 2026 .\n#### 2. Health care professional tax credit\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25F the following new section:\n25G. Health care professional tax credit (a) Allowance of credit In the case of a qualifying individual, there shall be allowed a credit against the tax imposed by this chapter for the taxable year in an amount equal to the sum of\u2014 (1) $300 multiplied by the number of calendar months during the taxable year in which such individual provides more than 80 but not more than 120 hours of qualifying health care services, (2) $400 multiplied by the number of calendar months during the taxable year in which such individual provides more than 120 but not more than 160 hours of qualifying health care services, plus (3) $500 multiplied by the number of calendar months during the taxable year in which such individual provides more than 160 hours of qualifying health care services. (b) Qualifying individual (1) In general For purposes of this section, the term qualifying individual means, with respect to a taxable year, an individual who is a licensed or certified health professional who provides qualifying health care services in a qualifying facility in good standing at any time during the taxable year. (2) Licensed or certified health professional For purposes of paragraph (1), the term licensed or certified health professional means an individual who is licensed, registered, or certified under Federal or State law or regulation to provide health care services. (c) Qualifying health care services (1) In general For purposes of this section the term qualifying health care services means\u2014 (A) any item or service for which payment may be made under title XVIII of the Social Security Act or under a State plan (or waiver of such plan) under title XIX of such Act, except for personal care services as defined under a State plan (or waiver of such plan) under title XIX of such Act, or (B) hospital care, medical services, or extended care services furnished directly to a veteran by\u2014 (i) a medical professional employed by the Department of Veterans Affairs, or (ii) a non-Department health care provider pursuant to an agreement with the Secretary of Veterans Affairs under chapter 17 of title 38, United States Code. (2) Exclusions Such term shall not include\u2014 (A) services provided by a supplier of durable medical equipment (as defined in section 1861(n) of the Social Security Act), (B) personal care services, consumer-directed or self-directed assistance programs, (C) fiscal intermediary services, or (D) home health or hospice care furnished by an individual is not a rendering or billing provider of record of title XVIII or XIX of the Social Security Act. (d) Qualifying facility in good standing For purposes of this section, the term qualifying facility in good standing means a facility or provider that\u2014 (1) is a medical facility of the Department of Veterans Affairs, as defined in section 8101 of title 38, United States Code, or (2) is\u2014 (A) located in a health professional shortage area (as defined in section 332(a)(1) of the Public Health Service Act), and (B) enrolled to furnish items and services under title XVIII of the Social Security Act or under a State plan (or waiver of such plan) under title XIX of such Act. (e) Income limitation and special rules (1) Income limitation No credit shall be allowed under subsection (a) to any individual in any taxable year in which the modified adjusted gross income of the taxpayer exceeds\u2014 (A) $400,000 in the case of a joint return or a surviving spouse, or (B) $200,000 in any other case. (2) Minimum number of qualifying months No credit shall be allowed with respect to qualifying health care services provided by an individual in any taxable year unless such individual provided 80 or more hours of qualifying health care services in each of 8 calendar months during such taxable year. (3) Modified adjusted gross income For purposes of paragraph (1), the term modified adjusted gross income means the adjusted gross income of the taxpayer for the taxable year increased by any amount excluded from gross income under section 911, 931, or 933. (f) Termination of credit No credit shall be allowed under subsection (a) for any taxable year beginning after December 31, 2030. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 25F the following new item:\nSec. 25G. Health care professional tax credit. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Evaluation and reports\n##### (a) Government Accountability Office study\nNot later than June 30, 2030, the Comptroller General of the United States shall submit to Congress a report on\u2014\n**(1)**\nthe overall impact of the credit allowed under section 25G of such Code on retention of health care professionals in health professional shortage areas;\n**(2)**\nthe effects of such credit on the quality and continuity of care furnished in Department of Veterans Affairs medical facilities, including Department of Veterans Affairs community-based outpatient clinics. and through non-Department medical providers pursuant to an agreement entered into with the Secretary of Veterans Affairs under chapter 17 of title 38, United States Code;\n**(3)**\nwhether the credit improved health care access or staffing stability in medical facilities of the Department of Veterans Affairs located in rural or underserved areas; and\n**(4)**\nany recommendations for improving the effectiveness or targeting of the credit.\n##### (b) Health professional shortage areas\nFor purposes of this section, the term health professional shortage areas has the meaning given such term in section 332(a)(1) of the Public Health Service Act.",
      "versionDate": "2026-03-09",
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
        "name": "Taxation",
        "updateDate": "2026-04-01T20:22:16Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7884ih.xml"
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
      "title": "Healthcare is Human Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare is Human Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a tax credit to health care professionals that provide health care services in qualifying facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:22Z"
    }
  ]
}
```
