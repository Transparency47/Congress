# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6735?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6735
- Title: Connecting Caregivers to Medicare Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6735
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-04-16T08:06:58Z
- Update date including text: 2026-04-16T08:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6735",
    "number": "6735",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Connecting Caregivers to Medicare Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:58Z",
    "updateDateIncludingText": "2026-04-16T08:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:03:50Z",
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
          "date": "2025-12-16T15:03:45Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
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
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6735ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6735\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Carey (for himself and Ms. Chu ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for outreach and education to Medicare beneficiaries to simplify access to information for family caregivers through 1\u2013800\u2013MEDICARE, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Connecting Caregivers to Medicare Act of 2025 .\n#### 2. Outreach and education to Medicare beneficiaries to simplify access to information for family caregivers through 1\u2013800-MEDICARE\nSection 1804 of the Social Security Act ( 42 U.S.C. 1395b\u20132 ) is amended by adding at the end the following new subsection:\n(e) (1) The Secretary shall provide for such outreach and education activities as are necessary, including as described in paragraph (2), to inform individuals entitled to benefits under part A or enrolled under part B and individuals applying for benefits under part A or enrolling under part B about the option to authorize a family caregiver (as defined in paragraph (8)(A)) of such an individual to access the personal health information of such individual through the toll-free 1\u2013800-MEDICARE telephone number maintained by the Secretary under subsection (b) if such individual completes and submits a specified family caregiver information access authorization form (as defined in paragraph (8)(B)) authorizing such access by such family caregiver to such information. (2) The outreach and education activities under paragraph (1) shall include the following: (A) Outreach and education efforts to provide information about the option described in paragraph (1) to individuals described in such paragraph, to providers of services and suppliers furnishing services to such individuals, to family caregivers, and to other appropriate entities specified by the Secretary. (B) Outreach and education efforts to inform such individuals, providers of services and suppliers, family caregivers, and other appropriate entities of best practices identified pursuant to paragraph (4) to protect such individuals from fraudulent practices described in such paragraph. (C) Outreach and education efforts to individuals described in paragraph (1) to inform such individuals of all existing reporting mechanisms for suspected Medicare fraud. (D) The inclusion of information about the option described in paragraph (1), and best practices identified pursuant to paragraph (4), in a manner that is prominent, easily accessible, and readily understandable\u2014 (i) in the notice under subsection (a); (ii) through the Medicare.gov website or a successor website; (iii) through other efforts specifically conducted for individuals enrolled in a Medicare Advantage plan under part C; and (iv) through other platforms or methods specified by the Secretary, such as social media. (E) The inclusion, in a manner that is prominent, easily accessible, and readily understandable, of the specified family caregiver information access authorization form in the notice under subsection (a), through\u2014 (i) the website described in subparagraph (D)(ii); and (ii) other efforts described in subparagraph (D)(iii). (F) Education efforts to train operators of 1\u2013800-MEDICARE on providing appropriate resources and information to family caregivers. (3) Information about the option described in paragraph (1) provided through efforts described in paragraph (2) shall include a notification clarifying that such option is available to all individuals described in paragraph (1) regardless of whether such individuals are enrolled for the original Medicare fee-for-service option under part A or B or enrolled in a Medicare Advantage plan. (4) Not later than 1 year after the date of enactment of this subsection, the Secretary, acting through the Office of the Inspector General of the Department of Health and Human Services, shall submit to Congress and make publicly available best practices to protect individuals described in paragraph (1) against fraud relating to inappropriately accessing or using the personal health information of such individuals, including best practices for educating beneficiaries on fraud reporting mechanisms, and recommendations to improve timely agency investigation of beneficiary fraud reports. The Secretary shall provide for, as the Secretary determines appropriate, separate best practices for individuals described in paragraph (1), family caregivers, providers of services and suppliers, and other entities specified by the Secretary. (5) The Secretary shall provide for opportunities (such as through surveys) for family caregivers to provide feedback to the Secretary on experiences accessing information through 1\u2013800-MEDICARE and on the outreach and education activities conducted under this subsection. (6) The outreach and education activities conducted under this subsection, and the specified family caregiver information access authorization form, shall be made available in non-English languages, as specified by the Secretary. (7) In conducting the outreach and education activities under this subsection, the Secretary shall, to the greatest extent practicable, coordinate such activities with activities carried out through State health insurance assistance programs or the Administration for Community Living. (8) For purposes of this subsection: (A) The term family caregiver has the meaning given such term in section 2 of the Recognize, Assist, Include, Support, and Engage Family Caregivers Act of 2017, and includes such other individuals as specified by the Secretary. (B) The term specified family caregiver information access authorization form means the CMS\u201310106 form or any successor form. .",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3439",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Connecting Caregivers to Medicare Act of 2025",
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
        "updateDate": "2026-03-11T14:08:50Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6735ih.xml"
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
      "title": "Connecting Caregivers to Medicare Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Connecting Caregivers to Medicare Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for outreach and education to Medicare beneficiaries to simplify access to information for family caregivers through 1-800-MEDICARE, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T05:18:21Z"
    }
  ]
}
```
