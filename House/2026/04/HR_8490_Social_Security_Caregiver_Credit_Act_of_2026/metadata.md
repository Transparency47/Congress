# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8490
- Title: Social Security Caregiver Credit Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8490
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-22T08:08:11Z
- Update date including text: 2026-05-22T08:08:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8490",
    "number": "8490",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001190",
        "district": "10",
        "firstName": "Bradley",
        "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
        "lastName": "Schneider",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Social Security Caregiver Credit Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:11Z",
    "updateDateIncludingText": "2026-05-22T08:08:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:00:20Z",
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
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "DC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8490ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8490\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Schneider (for himself, Ms. Meng , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to credit individuals serving as caregivers of dependent relatives with deemed wages for up to five years of such service.\n#### 1. Short title\nThis Act may be cited as the Social Security Caregiver Credit Act of 2026 .\n#### 2. Findings and sense of Congress\n##### (a) Findings\nCongress finds that:\n**(1)**\nCaregiving is an essential element of family life and a vital service for children, the ill, the disabled, and the elderly.\n**(2)**\nThe establishment of a caregiver credit would bolster the economic prospects of unpaid caregivers and would provide them with vital retirement security.\n**(3)**\nThe 2025 Annual Report of the Board of Trustees of the Federal Old-Age and Survivors Insurance and Federal Disability Insurance Trust Funds concluded that the combined Trust Funds will be able to pay scheduled benefits in full until 2034.\n##### (b) Sense of congress\nIt is the sense of Congress that Congress should address the unfair exclusion of professional and hardworking home care providers who are not eligible to receive Social Security or Medicare because they provide paid care to a family member with a disability under programs operated at the State and local level for general health and welfare protection.\n#### 3. Deemed wages for caregivers of dependent relatives\n##### (a) In general\nTitle II of the Social Security Act is amended by adding after section 234 ( 42 U.S.C. 434 ) the following new section:\n235. Deemed wages for caregivers of dependent relatives (a) Definitions For purposes of this section\u2014 (1) (A) Subject to subparagraph (B), the term qualifying month means, in connection with an individual, any month during which such individual was engaged for not less than 80 hours in providing care to a dependent relative without monetary compensation. (B) The term qualifying month does not include any month ending after the date on which such individual attains retirement age (as defined in section 216(l)). (C) For purposes of subparagraph (A), assistance provided to a family caregiver of an eligible veteran under section 1720G of title 38, United States Code, shall not be considered monetary compensation for providing care to such eligible veteran. (2) The term dependent relative means, in connection with an individual\u2014 (A) a child, grandchild, niece, or nephew (of such individual or such individual\u2019s spouse or domestic partner), or a child to which the individual or the individual\u2019s spouse or domestic partner is standing in loco parentis, who is under the age of 12; or (B) a child, grandchild, niece, or nephew (of such individual or such individual\u2019s spouse or domestic partner), a child to which the individual or the individual\u2019s spouse or domestic partner is standing in loco parentis, a parent, grandparent, sibling, aunt, or uncle (of such individual or his or her spouse or domestic partner), or such individual\u2019s spouse or domestic partner, if such child, grandchild, niece, nephew, parent, grandparent, sibling, aunt, uncle, spouse, or domestic partner is a chronically dependent individual. (3) (A) The term chronically dependent individual means an individual who\u2014 (i) is dependent on a daily basis on verbal reminding, physical cueing, supervision, or other assistance provided to the individual by another person in the performance of at least two of the activities of daily living (described in subparagraph (B)) or instrumental activities of daily living (described in subparagraph (C)); and (ii) without the assistance described in clause (i), could not perform such activities of daily living or instrumental activities of daily living. (B) The activities of daily living referred to in subparagraph (A) means basic personal everyday activities, including\u2014 (i) eating; (ii) bathing; (iii) dressing; (iv) toileting; and (v) transferring in and out of a bed or in and out of a chair. (C) The instrumental activities of daily living referred to in subparagraph (A) means activities related to living independently in the community, including\u2014 (i) meal planning and preparation; (ii) managing finances; (iii) shopping for food, clothing, or other essential items; (iv) performing essential household chores; (v) communicating by phone or other form of media; and (vi) traveling around and participating in the community. (b) Deemed Wages of Caregiver (1) (A) For purposes of determining entitlement to and the amount of any monthly benefit for any month after December 2026, or entitlement to and the amount of any lump-sum death payment in the case of a death after such month, payable under this title on the basis of the wages and self-employment income of any individual, and for purposes of section 216(i)(3), such individual shall be deemed to have been paid during each qualifying month (in addition to wages or self-employment income actually paid to or derived by such individual during such month) at an amount per month equal to\u2014 (i) in the case of a qualifying month during which no wages or self-employment income were actually paid to or derived by such individual, 50 percent of the national average wage index (as defined in section 209(k)(1)) for the second calendar year preceding the calendar year in which such month occurs; and (ii) in the case of any other qualifying month, the excess of the amount determined under clause (i) over 1/2 of the wages or self-employment income actually paid to or derived by such individual during such month. (B) In any case in which there are more than 60 qualifying months for an individual, only the last 60 of such months shall be taken into account for purposes of this section. (2) Paragraph (1) shall not be applicable in the case of any monthly benefit or lump-sum death payment if a larger such benefit or payment, as the case may be, would be payable without its application. (c) Rules and regulations (1) Not later than 1 year after the date of the enactment of this section, the Commissioner of Social Security shall promulgate such regulations as are necessary to carry out this section and to prevent fraud and abuse with respect to the benefits under this section, including regulations establishing procedures for the application and certification requirements described in paragraph (2). (2) A qualifying month shall not be taken into account under this section with respect to an individual unless\u2014 (A) the individual submits to the Commissioner of Social Security an application for benefits under this section that includes\u2014 (i) the name and identifying information of the dependent relative with respect to whom the individual was engaged in providing care during such month; (ii) if the dependent relative is not a child under the age of 12, documentation from the physician of the dependent relative explaining why the dependent relative is a chronically dependent individual; and (iii) such other information as the Commissioner may require to verify the status of the dependent relative; and (B) for every qualifying month or period of up to 12 consecutive qualifying months that occurs after the first period of 12 consecutive qualifying months, the individual certifies, in such form and manner as the Commissioner shall require, that the information provided in the individual\u2019s application for benefits under this section has not changed. .\n##### (b) Conforming amendment\nSection 209(k)(1) of such Act ( 42 U.S.C. 409(k)(1) ) is amended\u2014\n**(1)**\nby striking and before 230(b)(2) the first time it appears; and\n**(2)**\nby inserting and 235(b)(1)(A)(i), after 1977), .",
      "versionDate": "2026-04-23",
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
        "actionDate": "2026-04-27",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4396",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Social Security Caregiver Credit Act of 2026",
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
        "name": "Social Welfare",
        "updateDate": "2026-05-07T17:44:09Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8490ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Social Security Caregiver Credit Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "title": "Social Security Caregiver Credit Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to credit individuals serving as caregivers of dependent relatives with deemed wages for up to five years of such service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T05:48:27Z"
    }
  ]
}
```
