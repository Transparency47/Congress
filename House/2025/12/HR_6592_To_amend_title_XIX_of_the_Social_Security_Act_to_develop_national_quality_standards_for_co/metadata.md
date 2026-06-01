# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6592
- Title: Continuous Skilled Nursing Quality Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6592
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-02-04T09:07:04Z
- Update date including text: 2026-02-04T09:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6592",
    "number": "6592",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000619",
        "district": "6",
        "firstName": "Michael",
        "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
        "lastName": "Rulli",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Continuous Skilled Nursing Quality Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T09:07:04Z",
    "updateDateIncludingText": "2026-02-04T09:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:00:10Z",
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
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "AZ"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NJ"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6592ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6592\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Rulli (for himself, Mr. Stanton , and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to develop national quality standards for continuous skilled nursing services provided through Medicaid, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Continuous Skilled Nursing Quality Improvement Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Full-benefit dual eligible individual**\nThe term full-benefit dual eligible individual means an individual who is entitled to, or enrolled for, benefits under part A of title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), or enrolled for benefits under part B of title XVIII of such Act, and is eligible for medical assistance under the Medicaid program for full benefits under section 1902(a)(10)(A) of such Act ( 42 U.S.C. 1396a(a)(10)(A) ) or 1902(a)(10)(C) of such Act ( 42 U.S.C. 1396a(a)(10)(C) ), by reason of section 1902(f) of such Act ( 42 U.S.C. 1396a(f) ), or under any other category of eligibility for medical assistance for full benefits, as determined by the Secretary.\n**(2) Medicaid beneficiary**\nThe term Medicaid beneficiary means an individual who is eligible for, and enrolled in, a State Medicaid program.\n**(3) Medicaid program**\nThe term Medicaid program means, with respect to a State, the State program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) (including any waiver or demonstration under such title or under section 1115 of such Act ( 42 U.S.C. 1315 ) relating to such title).\n**(4) Private duty nursing services**\nThe term private duty nursing services has the meaning given that term for purposes of section 1905(a)(8) of the Social Security Act ( 42 U.S.C. 1396d(a)(8) ) (as in effect on the date of enactment of this Act).\n**(5) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(6) State**\nThe term State has the meaning given such term in section 1101(a) of the Social Security Act ( 42 U.S.C. 1301(a) ) for purposes of title XIX of such Act ( 42 U.S.C. 1396 et seq. ).\n#### 3. Redefining private duty nursing services provided through Medicaid\n##### (a) Definition of medical assistance\n**(1) In general**\nSection 1905(a)(8) of the Social Security Act (42 U.S. 1396d(a)(8)) is amended by striking private duty nursing services; and inserting continuous skilled nursing services; .\n**(2) Effective date**\nThe amendment made by paragraph (1) takes effect on the date that is 18 months after the date of enactment of this Act.\n##### (b) Definition of continuous skilled nursing services\nNot later than 18 months after the date of enactment of this Act, the Secretary, through notice and comment rulemaking, shall\u2014\n**(1)**\nrevise the definition of private duty nursing services in section 440.80 of title 42, Code of Federal Regulations, to be continuous skilled nursing services ; and\n**(2)**\nrequire that such services under the Medicaid program provided to complex-care patients who require multiple hours of continuous nursing services per day, as determined by the State, are provided by a licensed nurse, including a registered nurse or a licensed practical nurse.\n#### 4. Development of national quality standards for continuous skilled nursing services provided through Medicaid\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary shall convene a working group that includes representatives of independent and national providers of private duty nursing services under the Medicaid program, other private duty nursing agencies, associations representing providers of continuous skilled nursing services, full-benefit dual eligible individuals, Medicaid beneficiaries, patient advocacy groups, officials of State Medicaid programs, private duty nursing accrediting bodies, and other relevant stakeholders, to develop and establish national quality standards for the purposes of improving the standard of care for private duty nursing services provided by States under the Medicaid program.\n##### (b) Ensuring clinically appropriate standards\nThe Secretary shall issue a letter to State Medicaid Directors stating that providers of private duty nursing services under the Medicaid program are not required to adhere to conditions of participation for home health agencies under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n##### (c) Publication of national standards\nNot later than 1 year after the date on which the working group described in subsection (a) is first convened, the Secretary, after providing a period of public notice and opportunity for comment, shall publish the national quality standards developed by the working group for use by State Medicaid programs, managed care entities that enter into contracts with such programs, and providers of items and services under such programs.\n#### 5. Maintaining up-to-date continuous skilled nursing standards\n##### (a) Updating home and community-Based waiver services\nNot later than 18 months after the date of enactment of this Act, the Secretary, through notice and comment rulemaking, shall revise the list of services that are included as home and community-based waiver services under section 440.180(b) of title 42, Code of Federal Regulations, to include continuous skilled nursing care services, as defined for purposes of section 1905(a)(8) of the Social Security Act (as amended by section 3(a)) under section 440.80 of title 42, Code of Federal Regulations (as revised after the application of section 3(b)).\n##### (b) Updating the home and community-Based services quality measure set\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall update and publish the HCBS Quality Measure Set, described in the State Medicaid Director Letter #22\u2013003 issued on July 21, 2022, to include core and supplemental quality measures for continuous skilled nursing services for use by State Medicaid programs, managed care entities that enter into contracts with such programs, and providers of items and services under such programs.\n**(2) Regular reviews and updates**\nThe Secretary shall review and update the core set and supplemental set of continuous skilled nursing services quality measures published under paragraph (1) not less frequently than every 8 years. Any such update shall include a period of public notice and opportunity for comment.",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1920",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Continuous Skilled Nursing Quality Improvement Act of 2025",
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
        "updateDate": "2025-12-12T16:32:29Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6592ih.xml"
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
      "title": "Continuous Skilled Nursing Quality Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T14:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Continuous Skilled Nursing Quality Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T14:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to develop national quality standards for continuous skilled nursing services provided through Medicaid, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T14:05:39Z"
    }
  ]
}
```
